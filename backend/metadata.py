import io
import streamlit as st
import msal
import requests
import pyarrow as pa


def get_metadata_token():

    TENANT_ID = st.secrets["POWERBI_TENANT_ID"]
    CLIENT_ID = st.secrets["POWERBI_CLIENT_ID"]
    CLIENT_SECRET = st.secrets["POWERBI_CLIENT_SECRET"]

    app = msal.ConfidentialClientApplication(
        CLIENT_ID,
        authority=f"https://login.microsoftonline.com/{TENANT_ID}",
        client_credential=CLIENT_SECRET
    )

    result = app.acquire_token_for_client(
        scopes=["https://analysis.windows.net/powerbi/api/.default"]
    )

    if "access_token" not in result:
        raise Exception(
            result.get("error_description", "Authentication failed")
        )

    return result["access_token"]


def execute_metadata_dax(query):

    DATASET_ID = st.secrets["DATASET_ID"]

    url = (
        f"https://api.powerbi.com/v1.0/myorg/"
        f"datasets/{DATASET_ID}/executeDaxQueries"
    )

    token = get_metadata_token()

    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }

    payload = {
        "query": query,
        "queryTimeout": 120
    }

    response = requests.post(
        url,
        headers=headers,
        json=payload,
        timeout=150
    )

    if not response.ok:
        raise Exception(
            f"Power BI API error {response.status_code}: "
            f"{response.text[:3000]}"
        )

    # Convert Apache Arrow response into pandas DataFrame
    stream = io.BytesIO(response.content)

    reader = pa.ipc.open_stream(stream)

    # Check for query errors even when HTTP status is 200
    metadata = reader.schema.metadata or {}

    if metadata.get(b"IsError") == b"true":
        raise Exception(
            metadata.get(b"FaultString", b"Metadata query failed").decode()
        )

    return reader.read_all().to_pandas()



def get_tables():
    return execute_metadata_dax("""
        EVALUATE
        INFO.VIEW.TABLES()
    """)


def get_columns():
    return execute_metadata_dax("""
        EVALUATE
        INFO.VIEW.COLUMNS()
    """)


def get_measures():
    return execute_metadata_dax("""
        EVALUATE
        INFO.VIEW.MEASURES()
    """)


def get_relationships():
    return execute_metadata_dax("""
        EVALUATE
        INFO.VIEW.RELATIONSHIPS()
    """)
