
import os
import streamlit as st
import requests
import msal
import pandas as pd

# =====================================================
# POWER BI CONFIGURATION
# =====================================================

TENANT_ID = st.secrets.get("TENANT_ID") or os.getenv("TENANT_ID")
CLIENT_ID = st.secrets.get("CLIENT_ID") or os.getenv("CLIENT_ID")
CLIENT_SECRET = st.secrets.get("CLIENT_SECRET") or os.getenv("CLIENT_SECRET")

WORKSPACE_ID = st.secrets.get("WORKSPACE_ID") or os.getenv("WORKSPACE_ID")
DATASET_ID = st.secrets.get("DATASET_ID") or os.getenv("DATASET_ID")



AUTHORITY = f"https://login.microsoftonline.com/{TENANT_ID}"

SCOPES = [
    "https://analysis.windows.net/powerbi/api/.default"
]

EXECUTE_URL = (
    f"https://api.powerbi.com/v1.0/myorg/groups/"
    f"{WORKSPACE_ID}/datasets/{DATASET_ID}/executeQueries"
)

_msal_app = msal.ConfidentialClientApplication(
    CLIENT_ID,
    authority=AUTHORITY,
    client_credential=CLIENT_SECRET
)

_access_token = None


def get_access_token():
    global _access_token

    result = _msal_app.acquire_token_for_client(
        scopes=SCOPES
    )

    if "access_token" not in result:
        raise Exception(
            "Power BI authentication failed: "
            + result.get("error_description", str(result))
        )

    _access_token = result["access_token"]
    return _access_token


def execute_dax(query):

    if not query or not query.strip():
        raise ValueError("DAX query cannot be empty.")

    token = get_access_token()

    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }

    payload = {
        "queries": [{"query": query}],
        "serializerSettings": {"includeNulls": True}
    }

    response = requests.post(
        EXECUTE_URL,
        headers=headers,
        json=payload,
        timeout=120
    )

    if response.status_code == 401:
        token = get_access_token()
        headers["Authorization"] = f"Bearer {token}"

        response = requests.post(
            EXECUTE_URL,
            headers=headers,
            json=payload,
            timeout=120
        )

    if not response.ok:
        raise Exception(
            f"Power BI API Error: "
            f"{response.status_code}\n{response.text}"
        )

    data = response.json()

    try:
        rows = data["results"][0]["tables"][0]["rows"]
        return pd.DataFrame(rows)

    except (KeyError, IndexError, TypeError) as e:
        raise Exception(
            f"Unable to parse Power BI response: {data}"
        ) from e
