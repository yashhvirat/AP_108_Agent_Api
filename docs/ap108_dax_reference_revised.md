# AP108 AI Analyst — Complete DAX Reference

> Generated from the supplied Power BI metadata exports on 2026-11-20.
> Purpose: provide the DAX generator with AP108 business rules and the exact semantic-model schema, measures, and relationships.
> Scope is limited to information useful for generating DAX. This file does not document application UI, deployment, credentials, or infrastructure.

## 1. Source-of-truth and precedence

- The live semantic-model metadata supplied to the application is authoritative for table, column, measure, and relationship names.
- This document records the metadata snapshot exported in the four supplied CSV files. Refresh this document when the semantic model changes.
- If this document and current live metadata disagree, use current live metadata for model objects and relationships.
- Use the approved AP108 business definitions in this document for operational meaning. Do not silently redefine a KPI.
- Planner output supplies the interpreted metric, grouping, filters, and date range; verify all referenced objects against metadata.
- Never invent columns, measures, relationships, values, or business definitions.

## 2. Model overview

- Tables in export: **31**
- Columns in export: **547**
- Relationships in export: **33**
- Measures in export: **513**
- Main operational fact table: `ERR`.
- Calendar table: `Calender`.
- Other tables must be used only where the metadata confirms their fields and relationship paths.

### 2.1 Tables

| Table | Hidden | Storage mode | Data category | Description |
| --- | --- | --- | --- | --- |
| ERR | False | Import | Regular |  |
| Calender | False | Import | Time |  |
| Refresh_time | True | Import | Regular |  |
| Locality | False | Import | Regular |  |
| Missed dispatches | False | Import | Regular |  |
| Vehicles Master Database | False | Import | Regular |  |
| Month Slicer | False | Import | Regular |  |
| ODO Reading MDT | False | Import | Regular |  |
| Off Road | False | Import | Regular |  |
| Fuel Filling | False | Import | Regular |  |
| Segments | False | Import | Regular |  |
| Districts & Regions | False | Import | Regular |  |
| GH Bins | False | Import | Regular |  |
| ODO Reading Manual | False | Import | Regular |  |
| ODO Reading GPS | False | Import | Regular |  |
| Vehicles & Segments | False | Import | Regular |  |
| Combined ODO | False | Import | Regular |  |
| IFT Summary Table | False | Import | Regular |  |
| ODO Manual Pivot | False | Import | Regular |  |
| Hospital Mapping | False | Import | Regular |  |
| Private Hospital Mapping | False | Import | Regular |  |
| ART & GH Summary | False | Import | Regular |  |
| FRS Attendance | False | Import | Regular |  |
| FRS Master | False | Import | Regular |  |
| FRS EMT & PILOT | False | Import | Regular |  |
| Case Delay Reasons | False | Import | Regular |  |
| Accept Time Threshold | False | Import | Regular |  |
| Deviation % Slicer | False | Import | Regular |  |
| Deviated Cases Slicer | False | Import | Regular |  |
| Delay Type Slicer | False | Import | Regular |  |
| Abandoned Summary | False | Import | Regular |  |

## 3. Complete column schema

Use the exact table and column spelling below. The `Hidden` flag is included for reference; hidden columns should not normally be selected for user-facing grouping unless the DAX task or existing measure requires them.

### 3.1 `ERR`

| Column | Data type | Hidden | Key | Unique | Nullable | Summarize by | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| RowNumber-2662979B-1795-4F74-8F37-6A1BA8059B61 | Integer | True | True | True | False | Default |  |
| Source.Name | Text | False | False | False | True |  |  |
| SI No. | Number | False | False | False | True | Sum |  |
| Vehicle Id | Text | False | False | False | True |  |  |
| Event Id | Text | False | False | True | False |  |  |
| Calltime | Date | False | False | False | True |  |  |
| Caller Number | Text | False | False | False | True |  |  |
| Caller Name | Text | False | False | False | True |  |  |
| Patient First Name | Text | False | False | False | True |  |  |
| Patient Last Name | Text | False | False | False | True |  |  |
| DIstress Contact NO | Text | False | False | False | True |  |  |
| Caller Address | Text | False | False | False | True |  |  |
| EMS Narrative | Text | False | False | False | True |  |  |
| SUB Event Marked By DO | Text | False | False | False | True |  |  |
| SUB Event Marked By MDT | Text | False | False | False | True |  |  |
| DO Marked Address | Text | False | False | False | True |  |  |
| Drop Address(MDT) | Text | False | False | False | True |  |  |
| DO NAME | Text | False | False | False | True |  |  |
| Ambulance Base Location | Text | False | False | False | True |  |  |
| Delivery Status | Text | False | False | False | True |  |  |
| Hospital To Hospital Transfer | True/False | False | False | False | True |  |  |
| Vehicle Callsign | Text | False | False | False | True |  |  |
| Vehicle Eta | Text | False | False | False | True |  |  |
| Routed Time | Date | False | False | False | True |  |  |
| Assign Time | Date | False | False | False | True |  |  |
| Accepted Time | Date | False | False | False | True |  |  |
| On Action Time | Date | False | False | False | True |  |  |
| At Scene Tme | Date | False | False | False | True |  |  |
| Enroute Time | Date | False | False | False | True |  |  |
| Hospital Reached Time | Date | False | False | False | True |  |  |
| Hospital Handoverd Time | Date | False | False | False | True |  |  |
| Mdt Abandoned Time | Date | False | False | False | True |  |  |
| Dispatch Over Time | Text | False | False | False | True |  |  |
| Vehicle Actual Duration Reach | Text | False | False | False | True |  |  |
| Total Time To Complete | Text | False | False | False | True |  |  |
| ATR Remarks | Text | False | False | False | True |  |  |
| District Name | Text | False | False | False | True |  |  |
| Mandal Name | Text | False | False | False | True |  |  |
| Village Name | Text | False | False | False | True |  |  |
| Distress Age | Text | False | False | False | True |  |  |
| Gender Name | Text | False | False | False | True |  |  |
| MDT Abandoned Reason | Text | False | False | False | True |  |  |
| PNA Reason | Text | False | False | False | True |  |  |
| Ambulance/Feeder vehicle | Text | False | False | False | True |  |  |
| DO remarks trimmed | Text | False | False | False | True |  |  |
| GH secs. | Integer | False | False | False | True | Sum |  |
| GH mins. | Number | False | False | False | True | Sum |  |
| Event GH (hrs) | Number | False | False | False | True |  |  |
| GH grouping | Text | False | False | False | True |  |  |
| ART Eligible | Text | False | False | False | True |  |  |
| ART secs. | Integer | False | False | False | True | Sum |  |
| ART mins. | Number | False | False | False | True | Sum |  |
| At Scene to Hosp Reach (sec) | Integer | False | False | False | True | Sum |  |
| At Scene to Hosp Reach (mins) | Number | False | False | False | True | Sum |  |
| Hosp reach cases | Integer | False | False | False | True | Sum |  |
| At Scene to Hosp eligible | Integer | False | False | False | True | Sum |  |
| Actionable calls | Integer | False | False | False | True | Sum |  |
| Ambulance Assigned | Integer | False | False | False | True | Sum |  |
| DO Remarks grouping | Text | False | False | False | True |  |  |
| Ambulance not assigned | Integer | False | False | False | True | Sum |  |
| Mobile & Date | Text | False | False | False | True |  |  |
| Event result (ERR) | Text | False | False | False | True |  |  |
| Event stages | Text | False | False | False | True |  |  |
| GH Eligible | Text | False | False | False | True |  |  |
| Addressed actionable calls | Integer | False | False | False | True | Sum |  |
| Call Hour (12-hour) | Text | False | False | False | True |  |  |
| Hour | Integer | False | False | False | True | Sum |  |
| Locality (BL) | Text | False | False | False | True |  |  |
| ART honored | Integer | False | False | False | True | Sum |  |
| IFT Label | Text | False | False | False | True |  |  |
| Indirect successful assignments | Integer | False | False | False | True | Sum |  |
| Disptaches direct & indirect | Integer | False | False | False | True | Sum |  |
| Ambulance Already assigned (c) | Integer | False | False | False | True | Sum |  |
| Failed dispatch of ambulance | Integer | False | False | False | True | Sum |  |
| Assign number | Text | False | False | False | True |  |  |
| Caller Base Location | Text | False | False | False | True |  |  |
| Match Base Locations | Integer | False | False | False | True | Sum |  |
| IFT Analaysis | Text | False | False | False | True |  |  |
| IFT_Index | Integer | False | False | False | True | Sum |  |
| IFT_Boundary | Integer | False | False | False | True | Sum |  |
| IFT_CallDate | Date | False | False | False | True |  |  |
| Missed Cases Due to IFT | Integer | False | False | False | True | Sum |  |
| Accepted Flag | Integer | False | False | False | True | Sum |  |
| Assigned Flag | Integer | False | False | False | True | Sum |  |
| On Action Flag | Integer | False | False | False | True | Sum |  |
| Enroute Flag | Integer | False | False | False | True | Sum |  |
| At Scene Flag | Integer | False | False | False | True | Sum |  |
| Hospital Reached Flag | Integer | False | False | False | True | Sum |  |
| Calltime Flag | Integer | False | False | False | True | Sum |  |
| MDT Available Flag | Integer | False | False | False | True | Sum |  |
| GH group sorting | Integer | False | False | False | True | Sum |  |
| At Scene Closure | Integer | False | False | False | True | Sum |  |
| MDT AVBL Flag | Integer | False | False | False | True | Sum |  |
| MDT Used Flag | Integer | False | False | False | True | Sum |  |
| SUB Event Marked By CO | Text | False | False | False | True |  |  |
| Drop Address(DO) | Text | False | False | False | True |  |  |
| GH hh:mm:ss | Date | False | False | False | True |  |  |
| ART Shortfall | Text | False | False | False | True |  |  |
| GH Shortfall | Text | False | False | False | True |  |  |
| Not Addressed actionable calls | Integer | False | False | False | True | Sum |  |
| District Final | Text | False | False | False | True |  |  |
| Ambulance Base Location (null) | Text | False | False | False | True |  |  |
| PNA Reason grouping | Text | False | False | False | True |  |  |
| Hospital Handover Flag | Integer | False | False | False | True | Sum |  |
| MDT Partially Used Flag | Integer | False | False | False | True | Sum |  |
| Abandoned After Dispatch | Integer | False | False | False | True | Sum |  |
| MDT Abandoned Reason new | Text | False | False | False | True |  |  |
| Accepted/OnAction/MDTAbdTime Flag | Integer | False | False | False | True | Sum |  |
| ATR Remarks Trimmed | Text | False | False | False | True |  |  |
| GH grouping 2 | Text | False | False | False | True |  |  |
| GH group 2 sorting | Integer | False | False | False | True | Sum |  |
| Special Base Locations Flag | Integer | False | False | False | True | Sum |  |
| Incorrect MDT Stamp Flag | Integer | False | False | False | True | Sum |  |
| Assign to At Scene (mins) | Number | False | False | False | True | Sum |  |
| KMS Bucket | Text | False | False | False | True |  |  |
| KMS Bucket Sort | Integer | False | False | False | True | Sum |  |
| GH (Hours) | Number | False | False | False | True | Sum |  |
| Time Bucket | Text | False | False | False | True |  |  |
| Time Bucket Sort | Integer | False | False | False | True | Sum |  |
| Speed (kmph) | Number | False | False | False | True | Sum |  |
| Speed Bucket | Text | False | False | False | True |  |  |
| Speed Bucket Sort | Integer | False | False | False | True | Sum |  |
| 1. On Action ODO | Number | False | False | False | True | Sum |  |
| 3. Hospital Reached ODO | Number | False | False | False | True | Sum |  |
| Fuel Amount - One Way (Approx) | Number | False | False | False | True | Sum |  |
| Range of KMS | Text | False | False | False | True |  |  |
| Range of KMS Sort | Integer | False | False | False | True | Sum |  |
| IFT cases KMs availability | Integer | False | False | False | True | Sum |  |
| Call Hour Bin | Text | False | False | False | True |  |  |
| Hour group | Text | False | False | False | True |  |  |
| 2. At Scene ODO | Number | False | False | False | True | Sum |  |
| 4. Back to Base ODO | Number | False | False | False | True | Sum |  |
| Valid ODO Flag | Integer | False | False | False | True | Sum |  |
| Govt - Pvt | Text | False | False | False | True |  |  |
| MDT ODO Completeness | Text | False | False | False | True |  |  |
| KMS Travelled (MDT) Two Way | Number | False | False | False | True | Sum |  |
| ERO Remarks | Text | False | False | False | True |  |  |
| ERO Marked Address | Text | False | False | False | True |  |  |
| ERO NAME | Text | False | False | False | True |  |  |
| Date | Date | False | False | False | True |  |  |
| Date Modified | Date | False | False | False | True |  |  |
| UID (ODO) | Text | False | False | False | True |  |  |
| EMT Flag | Integer | False | False | False | True | Sum |  |
| Vehicle Assigned Number | Number | False | False | False | True | Sum |  |
| Pick Facility Type | Text | False | False | False | True |  |  |
| Drop Facility Type | Text | False | False | False | True |  |  |
| Assigned order | Integer | False | False | False | True | Sum |  |
| KMS Eligibility | Text | False | False | False | True |  |  |
| 5. Max Closing ODO Two Way | Number | False | False | False | True | Sum |  |
| Region Lookup | Text | False | False | False | True |  |  |
| District (Caller) | Text | False | False | False | True |  |  |
| Range of KMS till At Scene | Text | False | False | False | True |  |  |
| Range of KMS till At Scene Sort | Integer | False | False | False | True | Sum |  |
| KMS Travelled (MDT) Raw Two Way | Number | False | False | False | True | Sum |  |
| Range of KMS Scene to Hosp | Text | False | False | False | True |  |  |
| Range of KMS Scene to Hosp Sort | Integer | False | False | False | True | Sum |  |
| Range of KMS Hosp to Base | Text | False | False | False | True |  |  |
| Range of KMS Hosp to Base Sort | Integer | False | False | False | True | Sum |  |
| Abandoned Status | Text | False | False | False | True |  |  |
| Drop Facility final | Text | False | False | False | True |  |  |
| Hospital pick type | Text | False | False | False | True |  |  |
| Hospital drop type | Text | False | False | False | True |  |  |
| Drop Type Hierarchy | Text | False | False | False | True |  |  |
| Hospital Reach KMs >30 Flag | Integer | False | False | False | True | Sum |  |
| Neonatal Flag | Text | False | False | False | True |  |  |
| GH Shortfall sort | Integer | False | False | False | True | Sum |  |
| Drop Type Lookup | Text | False | False | False | True |  |  |
| Pick Type Lookup | Text | False | False | False | True |  |  |
| Range of KMS (Abandoned) | Text | False | False | False | True |  |  |
| Range of KMS (Abandoned) sort | Integer | False | False | False | True | Sum |  |
| 5. Max Closing ODO One Way | Number | False | False | False | True | Sum |  |
| KMS Travelled (MDT) One Way | Number | False | False | False | True | Sum |  |
| Range of KMS - IFT Scene to Hosp One Way | Text | False | False | False | True |  |  |
| Hospital pick ranking | Integer | False | False | False | True | Sum |  |
| Hospital drop ranking | Integer | False | False | False | True | Sum |  |
| Fuel Amount - Two Way (Approx) | Number | False | False | False | True | Sum |  |
| One Way vs Return KMs MDT Diff Flag (10% buffer) | Number | False | False | False | True | Sum |  |
| KMS Travelled Return (MDT) | Number | False | False | False | True | Sum |  |
| PNA Reason New | Text | False | False | False | True |  |  |
| GH mins. Delay | Number | False | False | False | True | Sum |  |
| GH Crossed due to Accepted Time >2min & On Action Time >2min Flag | Integer | False | False | False | True | Sum |  |
| ART mins. Delay | Number | False | False | False | True | Sum |  |
| ART Crossed due to Accepted Time >2min & On Action Time >2min Flag | Integer | False | False | False | True | Sum |  |
| Date Shift | Text | False | False | False | True |  |  |
| GH Delay due to Accepted/On Action/Enroute Time Delay Improve Flag | Integer | False | False | False | True | Sum |  |
| EMT EMP Id | Text | False | False | False | True |  |  |
| PILOT EMP Id | Text | False | False | False | True |  |  |
| EMT Name | Text | False | False | False | True |  |  |
| PILOT Name | Text | False | False | False | True |  |  |
| GH mins. Delay (61 min) | Number | False | False | False | True | Sum |  |
| GH Delay due to Accepted/On Action/Enroute Time Delay Improve Flag (61 min) | Integer | False | False | False | True | Sum |  |
| Accept Time Bin | Text | False | False | False | True |  |  |
| On Action Time Bin | Text | False | False | False | True |  |  |
| Enroute Time Bin | Text | False | False | False | True |  |  |
| MDT_REMARKS | Text | False | False | False | True |  |  |
| Delayed Reasons | Text | False | False | False | True |  |  |
| GH Achieved | Text | False | False | False | True |  |  |
| ART Honored Yes/No | Text | False | False | False | True |  |  |
| ART hh:mm:ss | Date | False | False | False | True |  |  |
| Accept Time Bin 2 | Text | False | False | False | True |  |  |
| On Action Time Bin 2 | Text | False | False | False | True |  |  |
| Enroute Time Bin 2 | Text | False | False | False | True |  |  |
| ART Crossed due to Accepted Time >2 min Flag | Integer | False | False | False | True | Sum |  |
| GH Crossed due to Accepted Time >2 min Flag | Integer | False | False | False | True | Sum |  |
| ART Crossed due to On Action Time >2 min Flag | Integer | False | False | False | True | Sum |  |
| GH Crossed due to On Action Time >2 min Flag | Integer | False | False | False | True | Sum |  |
| GH Crossed due to Enroute Time >10 min Flag | Integer | False | False | False | True | Sum |  |
| acknowldge_read_start | Text | False | False | False | True |  |  |
| acknowldge_read_end | Text | False | False | False | True |  |  |
| atscene_odo_start | Text | False | False | False | True |  |  |
| atscene_odo_end | Text | False | False | False | True |  |  |
| reached_to_hospital_read_start | Text | False | False | False | True |  |  |
| reached_to_hospital_read_end | Text | False | False | False | True |  |  |
| back_to_base_read_start | Text | False | False | False | True |  |  |
| back_to_base_read_end | Text | False | False | False | True |  |  |
| MDT ODO Stamp Completeness | Text | False | False | False | True |  |  |
| AHT Eligible | Text | False | False | False | True |  |  |
| Private Hospital Location | Text | False | False | False | True |  |  |
| Selected Private Hospitals | Integer | False | False | False | True | Sum |  |
| Accept Time Bin sort | Integer | False | False | False | True | Sum |  |
| On Action Time Bin sort | Integer | False | False | False | True | Sum |  |
| Enroute Time Bin sort | Integer | False | False | False | True | Sum |  |
| Next Assign Time | Date | False | False | False | True |  |  |
| Current Assign - Next Assign Diff (mins) | Number | False | False | False | True | Sum |  |
| Back to Base Stamp Missed IFT Flag | Integer | False | False | False | True | Sum |  |
| Hopital Reach - Next Assign Diff (hh:mm:ss) | Text | False | False | False | True |  |  |
| Private Hospital District | Text | False | False | False | True |  |  |

### 3.2 `Calender`

| Column | Data type | Hidden | Key | Unique | Nullable | Summarize by | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| RowNumber-2662979B-1795-4F74-8F37-6A1BA8059B61 | Integer | True | False | True | False | Default |  |
| Date | Date | False | True | True | False |  |  |
| Year | Integer | False | False | False | True | Sum |  |
| Quarter | Text | False | False | False | True |  |  |
| Month Number | Integer | False | False | False | True | Sum |  |
| Week Number | Integer | False | False | False | True | Sum |  |
| Year-Week | Text | False | False | False | True |  |  |
| Week Start | Date | False | False | False | True |  |  |
| Week End | Date | False | False | False | True |  |  |
| Day | Integer | False | False | False | True | Sum |  |
| Week Sort | Integer | False | False | False | True | Sum |  |
| Formatted Date | Text | False | False | False | True |  |  |
| Week in Month | Text | False | False | False | True |  |  |
| Month Sort | Integer | False | False | False | True | Sum |  |
| Formatted Date 2 | Text | False | False | False | True |  |  |
| Month Full | Text | False | False | False | True |  |  |
| Day name | Text | False | False | False | True |  |  |
| Day Sort | Integer | False | False | False | True | Sum |  |
| Month & Year Full | Date | False | False | False | True |  |  |
| Date Availability (ODO) | Integer | False | False | False | True | Sum |  |
| Month & Year | Text | False | False | False | True |  |  |
| Month | Text | False | False | False | True |  |  |
| Month Start | Date | False | False | False | True |  |  |

### 3.3 `Refresh_time`

| Column | Data type | Hidden | Key | Unique | Nullable | Summarize by | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| RowNumber-2662979B-1795-4F74-8F37-6A1BA8059B61 | Integer | True | True | True | False | Default |  |
| Refresh_IST | Text | True | False | False | True |  |  |

### 3.4 `Locality`

| Column | Data type | Hidden | Key | Unique | Nullable | Summarize by | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| RowNumber-2662979B-1795-4F74-8F37-6A1BA8059B61 | Integer | True | True | True | False | Default |  |
| Locality | Text | False | False | True | False |  |  |
| SortOrder | Integer | False | False | False | True |  |  |
| BenchMark | Integer | False | False | False | True |  |  |

### 3.5 `Missed dispatches`

| Column | Data type | Hidden | Key | Unique | Nullable | Summarize by | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| RowNumber-2662979B-1795-4F74-8F37-6A1BA8059B61 | Integer | True | True | True | False | Default |  |
| Mobile & Date | Text | False | False | True | False |  |  |
| Date | Date | False | False | False | True |  |  |
| Total | Integer | False | False | False | True |  |  |
| Success | Integer | False | False | False | True |  |  |
| Failure | Integer | False | False | False | True |  |  |
| Event result | Text | False | False | False | True |  |  |

### 3.6 `Vehicles Master Database`

| Column | Data type | Hidden | Key | Unique | Nullable | Summarize by | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| RowNumber-2662979B-1795-4F74-8F37-6A1BA8059B61 | Integer | True | True | True | False | Default |  |
| Sl No. | Number | False | False | False | True | Sum |  |
| Project Name | Text | False | False | False | True |  |  |
| Region | Text | False | False | False | True |  |  |
| District Code | Text | False | False | False | True |  |  |
| District Name | Text | False | False | False | True |  |  |
| Mandal Name | Text | False | False | False | True |  |  |
| Base Location | Text | False | False | False | True |  |  |
| OE Name | Text | False | False | False | True |  |  |
| Contact Number | Text | False | False | False | True |  |  |
| District Manager | Text | False | False | False | True |  |  |
| Contact Number2 | Text | False | False | False | True |  |  |
| Vehicle Number | Text | False | False | True | False |  |  |
| New/Old | Text | False | False | False | True |  |  |
| Vehicle Year | Number | False | False | False | True | Sum |  |
| Vehicle Model | Text | False | False | False | True |  |  |
| Regular/Backup | Text | False | False | False | True |  |  |
| Locality | Text | False | False | False | True |  |  |
| ALS/BLS | Text | False | False | False | True |  |  |
| Segment Code | Text | False | False | False | True |  |  |
| Service Code | Text | False | False | False | True |  |  |
| Special Base Locations Flag | Integer | False | False | False | True | Sum |  |
| Chassis number | Text | False | False | False | True |  |  |
| Engine Number | Text | False | False | False | True |  |  |
| Group | Text | False | False | False | True |  |  |
| Source.Name | Text | False | False | False | True |  |  |
| Date Modified | Date | False | False | False | True |  |  |
| Vehicle Type | Text | False | False | False | True |  |  |
| Divisions | Text | False | False | False | True |  |  |

### 3.7 `Month Slicer`

| Column | Data type | Hidden | Key | Unique | Nullable | Summarize by | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| RowNumber-2662979B-1795-4F74-8F37-6A1BA8059B61 | Integer | True | True | True | False | Default |  |
| Date | Date | False | False | False | True |  |  |
| Year-Month | Text | False | False | False | True |  |  |
| Month Sort | Integer | False | False | False | True | Sum |  |
| Month & Year | Text | False | False | False | True |  |  |

### 3.8 `ODO Reading MDT`

| Column | Data type | Hidden | Key | Unique | Nullable | Summarize by | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| RowNumber-2662979B-1795-4F74-8F37-6A1BA8059B61 | Integer | True | True | True | False | Default |  |
| Source.Name | Text | False | False | False | True |  |  |
| VEHICLE_ID | Text | False | False | False | True |  |  |
| EVENT_ID | Text | False | False | False | True |  |  |
| On Action ODO | Number | False | False | False | True | Sum |  |
| Scene ODO | Number | False | False | False | True | Sum |  |
| Hospital Reached ODO | Number | False | False | False | True | Sum |  |
| back_to_base_ODO | Number | False | False | False | True | Sum |  |
| lmei.UPDATED_TIME | Date | False | False | False | True |  |  |
| Date | Date | False | False | False | True |  |  |
| MIN ODO | Number | False | False | False | True | Sum |  |
| MAX ODO | Number | False | False | False | True | Sum |  |
| KMS | Number | False | False | False | True | Sum |  |
| UID | Text | False | False | False | True |  |  |
| How Many Stamps | Integer | False | False | False | True | Sum |  |
| Date Modified | Date | False | False | False | True |  |  |
| acknowldge_read_start | Text | False | False | False | True |  |  |
| atscene_odo_start | Text | False | False | False | True |  |  |
| reached_to_hospital_read_start | Text | False | False | False | True |  |  |
| back_to_base_read_start | Text | False | False | False | True |  |  |

### 3.9 `Off Road`

| Column | Data type | Hidden | Key | Unique | Nullable | Summarize by | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| RowNumber-2662979B-1795-4F74-8F37-6A1BA8059B61 | Integer | True | True | True | False | Default |  |
| Source.Name | Text | False | False | False | True |  |  |
| Sl. No. | Number | False | False | False | True | Sum |  |
| Vehicle Id | Text | False | False | False | True |  |  |
| District Name | Text | False | False | False | True |  |  |
| Mandal Name | Text | False | False | False | True |  |  |
| Base Location | Text | False | False | False | True |  |  |
| Maintenance Type | Text | False | False | False | True |  |  |
| Off Road Reason | Text | False | False | False | True |  |  |
| Offroad Remarks | Text | False | False | False | True |  |  |
| Off Road DateTime | Date | False | False | False | True |  |  |
| On Road Date Time | Date | False | False | False | True |  |  |
| Offroad Duration | Text | False | False | False | True |  |  |
| Date | Date | False | False | False | True |  |  |
| Off Road Diff | Integer | False | False | False | True | Sum |  |
| Duration Bucket | Text | False | False | False | True |  |  |
| Duration Bucket Sort | Integer | False | False | False | True | Sum |  |
| Off Road Date | Date | False | False | False | True |  |  |
| On Road Date | Date | False | False | False | True |  |  |
| Date Modified | Date | False | False | False | True |  |  |
| Callsign | Text | False | False | False | True |  |  |
| Vehicle Sub Status | Text | False | False | False | True |  |  |
| Updated By | Text | False | False | False | True |  |  |

### 3.10 `Fuel Filling`

| Column | Data type | Hidden | Key | Unique | Nullable | Summarize by | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| RowNumber-2662979B-1795-4F74-8F37-6A1BA8059B61 | Integer | True | True | True | False | Default |  |
| S.No | Number | False | False | False | True | Sum |  |
| VehicleNo | Text | False | False | False | True |  |  |
| District | Text | False | False | False | True |  |  |
| Division | Text | False | False | False | True |  |  |
| Location/ Mandal | Text | False | False | False | True |  |  |
| Petro Card Number | Text | False | False | False | True |  |  |
| Distance from Base location to Filling Station | Text | False | False | False | True |  |  |
| Name of the Filling station | Text | False | False | False | True |  |  |
| Name of the Filling Location/ Dealer code | Text | False | False | False | True |  |  |
| DEO/EMT/OE Name | Text | False | False | False | True |  |  |
| Pilot /Driver Name | Text | False | False | False | True |  |  |
| Contact No | Text | False | False | False | True |  |  |
| Fuel Filling Date (DD-MMM-YY) | Date | False | False | False | True |  |  |
| Fuel Previous filling Odometer Reading | Number | False | False | False | True | Sum |  |
| Fuel Current filling Odometer Reading | Number | False | False | False | True | Sum |  |
| KMS running | Number | False | False | False | True | Sum |  |
| Fuel Quantity | Number | False | False | False | True | Sum |  |
| Fuel Amount | Number | False | False | False | True | Sum |  |
| Cost / Lit. | Number | False | False | False | True | Sum |  |
| KMPL | Number | False | False | False | True | Sum |  |
| Base Location | Text | False | False | False | True |  |  |
| Transection ID (On Bill) | Text | False | False | False | True |  |  |
| Card Swipe Status Swiped /Pending | Text | False | False | False | True |  |  |
| Project Name | Text | False | False | False | True |  |  |
| Name | Text | False | False | False | True |  |  |
| Source.Name | Text | False | False | False | True |  |  |
| Date Modified | Date | False | False | False | True |  |  |
| District (BL) | Text | False | False | False | True |  |  |

### 3.11 `Segments`

| Column | Data type | Hidden | Key | Unique | Nullable | Summarize by | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| RowNumber-2662979B-1795-4F74-8F37-6A1BA8059B61 | Integer | True | True | True | False | Default |  |
| District Name | Text | False | False | False | True |  |  |
| Mandal Name | Text | False | False | False | True |  |  |
| Base Location | Text | False | False | True | False |  |  |
| Locality | Text | False | False | False | True |  |  |
| Special Base Locations Flag | Integer | False | False | False | True | Sum |  |

### 3.12 `Districts & Regions`

| Column | Data type | Hidden | Key | Unique | Nullable | Summarize by | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| RowNumber-2662979B-1795-4F74-8F37-6A1BA8059B61 | Integer | True | True | True | False | Default |  |
| District | Text | False | False | True | False |  |  |
| Region | Text | False | False | False | True |  |  |

### 3.13 `GH Bins`

| Column | Data type | Hidden | Key | Unique | Nullable | Summarize by | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| RowNumber-2662979B-1795-4F74-8F37-6A1BA8059B61 | Integer | True | True | True | False | Default |  |
| Bin | Text | False | False | False | True |  |  |
| Min | Number | False | False | False | True | Sum |  |
| Max | Number | False | False | False | True | Sum |  |
| Sort | Integer | False | False | False | True | Sum |  |

### 3.14 `ODO Reading Manual`

| Column | Data type | Hidden | Key | Unique | Nullable | Summarize by | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| RowNumber-2662979B-1795-4F74-8F37-6A1BA8059B61 | Integer | True | True | True | False | Default |  |
| Source.Name | Text | False | False | False | True |  |  |
| UID | Text | False | False | False | True |  |  |
| S No | Number | False | False | False | True | Sum |  |
| Project | Text | False | False | False | True |  |  |
| Date | Date | False | False | False | True |  |  |
| District | Text | False | False | False | True |  |  |
| Division | Text | False | False | False | True |  |  |
| Mandal | Text | False | False | False | True |  |  |
| Vehicle no. | Text | False | False | False | True |  |  |
| Vehicle Type | Text | False | False | False | True |  |  |
| Opening ODO | Number | False | False | False | True | Sum |  |
| Closing ODO | Number | False | False | False | True | Sum |  |
| KMS | Number | False | False | False | True | Sum |  |
| Date Modified | Date | False | False | False | True |  |  |
| KMs range | Text | False | False | False | True |  |  |
| KMs range sort | Integer | False | False | False | True | Sum |  |
| Segment | Text | False | False | False | True |  |  |

### 3.15 `ODO Reading GPS`

| Column | Data type | Hidden | Key | Unique | Nullable | Summarize by | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| RowNumber-2662979B-1795-4F74-8F37-6A1BA8059B61 | Integer | True | True | True | False | Default |  |
| Source.Name | Text | False | False | False | True |  |  |
| Project | Text | False | False | False | True |  |  |
| Vehicle | Text | False | False | False | True |  |  |
| Device ID | Text | False | False | False | True |  |  |
| Kms travelled | Number | False | False | False | True | Sum |  |
| Pings | Number | False | False | False | True | Sum |  |
| First ping (IST) | Date | False | False | False | True |  |  |
| Last ping (IST) | Date | False | False | False | True |  |  |
| Date Modified | Date | False | False | False | True |  |  |

### 3.16 `Vehicles & Segments`

| Column | Data type | Hidden | Key | Unique | Nullable | Summarize by | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| RowNumber-2662979B-1795-4F74-8F37-6A1BA8059B61 | Integer | True | True | True | False | Default |  |
| UID (ODO) | Text | False | False | False | True |  |  |
| Segment | Text | False | False | False | True |  |  |

### 3.17 `Combined ODO`

| Column | Data type | Hidden | Key | Unique | Nullable | Summarize by | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| RowNumber-2662979B-1795-4F74-8F37-6A1BA8059B61 | Integer | True | True | True | False | Default |  |
| Vehicle Id | Text | False | False | False | True |  |  |
| District | Text | False | False | False | True |  |  |
| Date | Date | False | False | False | True |  |  |
| Manual Opening ODO | Number | False | False | False | True | Sum |  |
| Manual Closing ODO | Number | False | False | False | True | Sum |  |
| Manual KMS | Number | False | False | False | True | Sum |  |
| MDT KMS | Number | False | False | False | True | Sum |  |
| GPS KMS | Number | False | False | False | True | Sum |  |
| Base Location | Text | False | False | False | True |  |  |
| District (BL) | Text | False | False | False | True |  |  |
| MDT Opening ODO | Number | False | False | False | True | Sum |  |
| MDT Closing ODO | Number | False | False | False | True | Sum |  |
| MDT O-O KMS | Number | False | False | False | True | Sum |  |
| MDT C-O KMS | Number | False | False | False | True | Sum |  |
| MDT Non Ops KMs | Number | False | False | False | True | Sum |  |

### 3.18 `IFT Summary Table`

| Column | Data type | Hidden | Key | Unique | Nullable | Summarize by | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| RowNumber-2662979B-1795-4F74-8F37-6A1BA8059B61 | Integer | True | True | True | False | Default |  |
| Date | Date | False | False | False | True |  |  |
| Vehicle Id | Text | False | False | False | True |  |  |
| Ambulance Base Location | Text | False | False | False | True |  |  |
| IFT Cases | Integer | False | False | False | True | Sum |  |
| Total KMS | Number | False | False | False | True | Sum |  |

### 3.19 `ODO Manual Pivot`

| Column | Data type | Hidden | Key | Unique | Nullable | Summarize by | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| RowNumber-2662979B-1795-4F74-8F37-6A1BA8059B61 | Integer | True | True | True | False | Default |  |
| Vehicle no. | Text | False | False | False | True |  |  |
| Avg KM/month | Number | False | False | False | True | Sum |  |
| Kms travelled | Number | False | False | False | True | Sum |  |
| ODO pivot district | Text | False | False | False | True |  |  |
| ODO pivot KM range bucket | Text | False | False | False | True |  |  |
| ODO pivot KM range bucket Sort | Integer | False | False | False | True | Sum |  |
| Month & Year Full | Date | False | False | False | True |  |  |

### 3.20 `Hospital Mapping`

| Column | Data type | Hidden | Key | Unique | Nullable | Summarize by | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| RowNumber-2662979B-1795-4F74-8F37-6A1BA8059B61 | Integer | True | True | True | False | Default |  |
| HOSPITAL_ID | Number | False | False | False | True | Count |  |
| HOSPITAL_NAME | Text | False | False | False | True |  |  |
| HOSPITAL_TYPE | Text | False | False | False | True |  |  |
| Source.Name | Text | False | False | False | True |  |  |
| Date Modified | Date | False | False | False | True |  |  |

### 3.21 `Private Hospital Mapping`

| Column | Data type | Hidden | Key | Unique | Nullable | Summarize by | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| RowNumber-2662979B-1795-4F74-8F37-6A1BA8059B61 | Integer | True | True | True | False | Default |  |
| Slno | Text | False | False | False | True |  |  |
| District | Text | False | False | False | True |  |  |
| Location | Text | False | False | False | True |  |  |
| Hospital Name | Text | False | False | False | True |  |  |
| Hospital ID in ERC | Text | False | False | False | True |  |  |
| Hospital Type | Text | False | False | False | True |  |  |

### 3.22 `ART & GH Summary`

| Column | Data type | Hidden | Key | Unique | Nullable | Summarize by | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| RowNumber-2662979B-1795-4F74-8F37-6A1BA8059B61 | Integer | True | True | True | False | Default |  |
| Ambulance Base Location | Text | False | False | False | True |  |  |
| Locality (BL) | Text | False | False | False | True |  |  |
| Avg ART | Number | False | False | False | True | Sum |  |
| Avg GH | Number | False | False | False | True | Sum |  |
| Month Start | Date | False | False | False | True |  |  |
| ART Achieved | Text | False | False | False | True |  |  |
| GH Achieved | Text | False | False | False | True |  |  |
| ART No & GH Yes | Integer | False | False | False | True | Sum |  |
| Month & Year | Text | False | False | False | True |  |  |
| District Final | Text | False | False | False | True |  |  |
| Total Dispatches | Integer | False | False | False | True | Sum |  |
| ART Eligible | Integer | False | False | False | True | Sum |  |
| GH Eligible | Integer | False | False | False | True | Sum |  |
| GH Ontime | Integer | False | False | False | True | Sum |  |
| GH Ontime % | Number | False | False | False | True | Sum |  |
| ART No but GH Yes | Integer | False | False | False | True | Sum |  |
| ART Yes but GH No | Integer | False | False | False | True | Sum |  |

### 3.23 `FRS Attendance`

| Column | Data type | Hidden | Key | Unique | Nullable | Summarize by | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| RowNumber-2662979B-1795-4F74-8F37-6A1BA8059B61 | Integer | True | True | True | False | Default |  |
| Source.Name | Text | False | False | False | True |  |  |
| Date | Date | False | False | False | True |  |  |
| District | Text | False | False | False | True |  |  |
| Segment (served) | Text | False | False | False | True |  |  |
| Base Location | Text | False | False | False | True |  |  |
| Vehicle Number | Text | False | False | False | True |  |  |
| Name | Text | False | False | False | True |  |  |
| Employee ID | Integer | False | False | False | True | Count |  |
| Role | Text | False | False | False | True |  |  |
| Shift slot | Text | False | False | False | True |  |  |
| Early (min) | Integer | False | False | False | True | Sum |  |
| Check-in | Date | False | False | False | True |  |  |
| Check-out | Date | False | False | False | True |  |  |
| Hours | Number | False | False | False | True | Sum |  |
| Method | Text | False | False | False | True |  |  |
| Date Shift | Text | False | False | False | True |  |  |
| Attendance Status | Text | False | False | False | True |  |  |
| Leave Reason | Text | False | False | False | True |  |  |
| Approved By | Text | False | False | False | True |  |  |
| Hazaru in | Text | False | False | False | True |  |  |
| Hazaru out | Text | False | False | False | True |  |  |
| Date Modified | Date | False | False | False | True |  |  |

### 3.24 `FRS Master`

| Column | Data type | Hidden | Key | Unique | Nullable | Summarize by | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| RowNumber-2662979B-1795-4F74-8F37-6A1BA8059B61 | Integer | True | True | True | False | Default |  |
| District | Text | False | False | False | True |  |  |
| Division Name | Text | False | False | False | True |  |  |
| Segment Code | Text | False | False | False | True |  |  |
| Segment Name | Text | False | False | False | True |  |  |
| EMP ID | Text | False | False | False | True |  |  |
| EMP Name | Text | False | False | False | True |  |  |
| Designation | Text | False | False | False | True |  |  |
| Posting | Text | False | False | False | True |  |  |
| Date of OPS Added | Text | False | False | False | True |  |  |
| Number of Transfers | Text | False | False | False | True |  |  |
| Current Working Status | Text | False | False | False | True |  |  |
| Aadhaar No | Text | False | False | False | True |  |  |
| Date of Exit | Text | False | False | False | True |  |  |
| Last working day | Text | False | False | False | True |  |  |
| Exit reason | Text | False | False | False | True |  |  |
| Status last changed | Text | False | False | False | True |  |  |
| Status changed by | Text | False | False | False | True |  |  |
| Status changed at | Text | False | False | False | True |  |  |
| Source.Name | Text | False | False | False | True |  |  |
| Date Modified | Text | False | False | False | True |  |  |
| Date of Joining (HRMS) | Text | False | False | False | True |  |  |

### 3.25 `FRS EMT & PILOT`

| Column | Data type | Hidden | Key | Unique | Nullable | Summarize by | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| RowNumber-2662979B-1795-4F74-8F37-6A1BA8059B61 | Integer | True | True | True | False | Default |  |
| EMP ID | Text | False | False | False | True |  |  |
| EMP Name | Text | False | False | False | True |  |  |
| Designation | Text | False | False | False | True |  |  |
| Current Working Status | Text | False | False | False | True |  |  |
| Segment Name | Text | False | False | False | True |  |  |

### 3.26 `Case Delay Reasons`

| Column | Data type | Hidden | Key | Unique | Nullable | Summarize by | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| RowNumber-2662979B-1795-4F74-8F37-6A1BA8059B61 | Integer | True | True | True | False | Default |  |
| Source.Name | Text | False | False | False | True |  |  |
| Date Modified | Date | False | False | False | True |  |  |
| EVENT_ID | Text | False | False | True | False |  |  |
| Calltime | Date | False | False | False | True |  |  |
| VEHICLE_ID | Text | False | False | False | True |  |  |
| DELAYED_REASONS | Text | False | False | False | True |  |  |

### 3.27 `Accept Time Threshold`

| Column | Data type | Hidden | Key | Unique | Nullable | Summarize by | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| RowNumber-2662979B-1795-4F74-8F37-6A1BA8059B61 | Integer | True | True | True | False | Default |  |
| Threshold Minutes | Integer | False | False | False | True | Sum |  |
| Threshold Range | Text | False | False | False | True |  |  |

### 3.28 `Deviation % Slicer`

| Column | Data type | Hidden | Key | Unique | Nullable | Summarize by | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| RowNumber-2662979B-1795-4F74-8F37-6A1BA8059B61 | Integer | True | True | True | False | Default |  |
| Deviation % | Integer | False | False | False | True | Sum |  |
| Deviation Range | Text | False | False | False | True |  |  |

### 3.29 `Deviated Cases Slicer`

| Column | Data type | Hidden | Key | Unique | Nullable | Summarize by | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| RowNumber-2662979B-1795-4F74-8F37-6A1BA8059B61 | Integer | True | True | True | False | Default |  |
| Deviated Cases Range | Text | False | False | False | True |  |  |
| Deviated Cases Threshold | Integer | False | False | False | True | Sum |  |

### 3.30 `Delay Type Slicer`

| Column | Data type | Hidden | Key | Unique | Nullable | Summarize by | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| RowNumber-2662979B-1795-4F74-8F37-6A1BA8059B61 | Integer | True | True | True | False | Default |  |
| Delay Type | Text | False | False | False | True |  |  |

### 3.31 `Abandoned Summary`

| Column | Data type | Hidden | Key | Unique | Nullable | Summarize by | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| RowNumber-2662979B-1795-4F74-8F37-6A1BA8059B61 | Integer | True | True | True | False | Default |  |
| Abandoned Type | Text | False | False | False | True |  |  |
| Sort Order | Integer | False | False | False | True | Sum |  |

## 4. Complete relationship map

Relationship direction is shown exactly as exported. `From` and `To` columns, cardinality, active state, and cross-filter behaviour must be respected. Do not infer an alternate relationship.

| From table | From column | From cardinality | To table | To column | To cardinality | Active | Cross-filter | State | Security filter |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ERR | Locality (BL) | Many | Locality | Locality | One | True | OneDirection | Ready | Single |
| ERR | Vehicle Id | Many | Vehicles Master Database | Vehicle Number | One | True | OneDirection | Ready | Single |
| ERR | District Final | Many | Districts & Regions | District | One | True | OneDirection | Ready | Single |
| ERR | Ambulance Base Location | Many | Segments | Base Location | One | True | OneDirection | Ready | Single |
| ERR | Event Id | One | Case Delay Reasons | EVENT_ID | One | True | BothDirections | Ready | Single |
| ERR | Mobile & Date | Many | Missed dispatches | Mobile & Date | One | True | OneDirection | Ready | Single |
| ERR | Date | Many | Calender | Date | One | True | OneDirection | Ready | Single |
| Vehicles Master Database | Base Location | Many | Segments | Base Location | One | False | OneDirection | Ready | Single |
| Vehicles Master Database | District Name | Many | Districts & Regions | District | One | False | OneDirection | Ready | Single |
| ODO Reading MDT | EVENT_ID | Many | ERR | Event Id | One | True | OneDirection | Ready | Single |
| Off Road | Vehicle Id | Many | Vehicles Master Database | Vehicle Number | One | True | OneDirection | Ready | Single |
| Off Road | Base Location | Many | Segments | Base Location | One | True | OneDirection | Ready | Single |
| Off Road | Off Road Date | Many | Calender | Date | One | True | OneDirection | Ready | Single |
| Fuel Filling | VehicleNo | Many | Vehicles Master Database | Vehicle Number | One | True | OneDirection | Ready | Single |
| Fuel Filling | Base Location | Many | Segments | Base Location | One | True | OneDirection | Ready | Single |
| Fuel Filling | District (BL) | Many | Districts & Regions | District | One | True | OneDirection | Ready | Single |
| Fuel Filling | Fuel Filling Date (DD-MMM-YY) | Many | Calender | Date | One | True | OneDirection | Ready | Single |
| Segments | District Name | Many | Districts & Regions | District | One | False | OneDirection | Ready | Single |
| ODO Reading Manual | District | Many | Districts & Regions | District | One | True | OneDirection | Ready | Single |
| ODO Reading Manual | Vehicle no. | Many | Vehicles Master Database | Vehicle Number | One | True | OneDirection | Ready | Single |
| ODO Reading Manual | Segment | Many | Segments | Base Location | One | True | OneDirection | Ready | Single |
| ODO Reading Manual | Date | Many | Calender | Date | One | True | OneDirection | Ready | Single |
| ODO Reading GPS | Vehicle | Many | Vehicles Master Database | Vehicle Number | One | True | OneDirection | Ready | Single |
| Combined ODO | Base Location | Many | Segments | Base Location | One | True | OneDirection | Ready | Single |
| Combined ODO | Vehicle Id | Many | Vehicles Master Database | Vehicle Number | One | True | OneDirection | Ready | Single |
| Combined ODO | District (BL) | Many | Districts & Regions | District | One | True | OneDirection | Ready | Single |
| Combined ODO | Date | Many | Calender | Date | One | True | OneDirection | Ready | Single |
| ODO Manual Pivot | ODO pivot district | Many | Districts & Regions | District | One | True | OneDirection | Ready | Single |
| ODO Manual Pivot | Month & Year Full | Many | Calender | Date | One | True | OneDirection | Ready | Single |
| ART & GH Summary | District Final | Many | Districts & Regions | District | One | True | OneDirection | Ready | Single |
| ART & GH Summary | Month Start | Many | Calender | Date | One | True | OneDirection | Ready | Single |
| FRS Attendance | Vehicle number | Many | Vehicles Master Database | Vehicle Number | One | True | OneDirection | Ready | Single |
| Case Delay Reasons | EVENT_ID | One | ERR | Event Id | One | True | BothDirections | Ready | Single |

### 4.1 Relationship usage rules

- Prefer dimension-table columns for grouping when a valid relationship exists.
- Use only active relationship paths unless an inactive relationship is explicitly required and supported by the task.
- Respect relationship cardinality and cross-filter direction.
- Do not invent `TREATAS`, `USERELATIONSHIP`, `CROSSFILTER`, or manual join logic to compensate for an unverified relationship.
- If more than one plausible relationship path exists, inspect metadata and clarify if ambiguity remains.

## 5. Complete measure catalogue

All measures exported in the supplied metadata are listed below with their home table, data type, visibility, and state.

**Expression availability:** the supplied `measures.csv` contains an `[Expression]` column, but all 513 expression values are empty. Therefore this document can catalogue measure names but cannot establish their formulas or dependencies. The generator must retrieve measure expressions from live metadata when it needs to verify a measure's business meaning. Do not infer formulas from measure names.

### Measures — `ERR`

| Measure | Data type | Hidden | State | Description | Display folder |
| --- | --- | --- | --- | --- | --- |
| ART avg (sec) | Number | False | Valid |  |  |
| ART hh:mm:ss (m) | Text | False | Valid |  | ART |
| EMT accepted | Integer | False | Valid |  |  |
| ART cases | Integer | False | Valid |  |  |
| % cases for ART cal | Number | False | Valid |  |  |
| GH Ontime % | Number | False | Valid |  |  |
| GH Eligible (m) | Integer | False | Valid |  | GH |
| GH Ontime | Integer | False | Valid |  | GH |
| % cases assigned ambulances | Number | False | Valid |  |  |
| % vehicles accepted | Number | False | Valid |  |  |
| Ambulance already assigned | Integer | False | Valid |  |  |
| % calls addressed | Number | False | Valid |  |  |
| ART Eligible (m) | Integer | False | Valid |  | ART |
| % ART honoured | Number | False | Valid |  |  |
| Unique vehicles | Integer | False | Valid |  |  |
| GH mins (m) | Number | False | Valid |  | GH |
| GH penality | Text | False | Valid |  |  |
| GH penalty cases | Integer | False | Valid |  |  |
| GH Penality amount | Integer | False | Valid |  |  |
| Vehicle within GH time new | Integer | False | Valid |  |  |
| % IFT cases | Number | False | Valid |  |  |
| IFT Case Requests | Integer | False | Valid |  |  |
| IFT Cases/Day | Number | False | Valid |  |  |
| Private Hosp Dispatches | Integer | False | Valid |  |  |
| % Private Hosp Dispatches | Number | False | Valid |  |  |
| Pvt sector drops/day | Number | False | Valid |  |  |
| IFT Served | Integer | False | Valid |  |  |
| IFT Served % | Number | False | Valid |  |  |
| Unsuccessful Actionable calls | Integer | False | Valid |  |  |
| Dist selection | Text | False | Valid |  |  |
| Total events (ERR) | Integer | False | Valid |  |  |
| % Total events (Dist) | Number | False | Valid |  |  |
| Same_Mandal_Missed_Cases | Integer | False | Valid |  |  |
| Penalty | Number | False | Valid |  |  |
| penali | Integer | False | Valid |  |  |
| urban art diff | Number | False | Valid |  |  |
| % Abnadoned Dispatches | Number | False | Valid |  |  |
| % Abandoned after dispatch | Number | False | Valid |  |  |
| IFT_Missed_Count | Integer | False | Valid |  |  |
| % missed cases due to IFT | Number | False | Valid |  |  |
| % missed cases / Total cases | Number | False | Valid |  |  |
| Ambulance Assigned Count(G) | Integer | False | Valid |  |  |
| Accepted Count(G) | Integer | False | Valid |  |  |
| Assigned Count(G) | Integer | False | Valid |  |  |
| On Action Count(G) | Integer | False | Valid |  |  |
| Enroute Count | Integer | False | Valid |  |  |
| At Scene Count | Integer | False | Valid |  |  |
| Hospital Reached Count | Integer | False | Valid |  |  |
| Assigned → Accepted % (G) | Number | False | Valid |  |  |
| Accepted → On Action % | Number | False | Valid |  |  |
| At Scene → Enroute % (G) | Number | False | Valid |  |  |
| Enroute → Hospital % | Number | False | Valid |  |  |
| Calltime Count(G) | Integer | False | Valid |  |  |
| Total EROs | Integer | False | Valid |  |  |
| MDT Not Available Vehicles | Integer | False | Valid |  |  |
| MDT Not Available % | Number | False | Valid |  |  |
| MDT Available % | Number | False | Valid |  |  |
| ART Rural | Number | False | Valid |  | ART |
| ART Tribal | Number | False | Valid |  | ART |
| Dispatches | Integer | False | Valid |  |  |
| Dispatch % | Number | False | Valid |  |  |
| Missed Dispatches | Integer | False | Valid |  |  |
| Missed Dispatch % | Number | False | Valid |  |  |
| ART Shortfall Measure | Text | False | Valid |  |  |
| ART formatting | Text | False | Valid |  |  |
| ART Urban | Number | False | Valid |  | ART |
| MDT Not Available veh % | Number | False | Valid |  |  |
| MDT AVBL Segments | Integer | False | Valid |  |  |
| MDT Used Segments | Integer | False | Valid |  |  |
| MDT Usage/Cases % | Number | False | Valid |  |  |
| MDT Used Segement % | Number | False | Valid |  |  |
| MDT Not Used Segments | Integer | False | Valid |  |  |
| GH Shortfall Measure | Text | False | Valid |  |  |
| MDT Selected Date | Date | False | Valid |  |  |
| Total Segments Served | Integer | False | Valid |  |  |
| GH Not Ontime | Integer | False | Valid |  | GH |
| % Not completed in GH | Number | False | Valid |  |  |
| At Scene Closure % | Number | False | Valid |  |  |
| MDT Uptime % | Number | False | Valid |  |  |
| ART Urban formatting | Text | False | Valid |  |  |
| GH hh:mm:ss (m) | Date | False | Valid |  | GH |
| ART New Measure | Text | False | Valid |  |  |
| MDT Not Used Cases | Integer | False | Valid |  |  |
| MDT Used Cases | Integer | False | Valid |  |  |
| MDT Not Used/Cases % | Number | False | Valid |  |  |
| Delivered Emergencies | Integer | False | Valid |  |  |
| Failed Emergencies | Integer | False | Valid |  |  |
| ART Font formatting | Text | False | Valid |  |  |
| % calls not addressed | Number | False | Valid |  |  |
| % GH Exceeded | Number | False | Valid |  |  |
| MDT AVBL Cases | Integer | False | Valid |  |  |
| Segments Not Served | Integer | False | Valid |  |  |
| Missing Locations Flag | Integer | False | Valid |  |  |
| Dispatch Target | Number | False | Valid |  |  |
| Abandoned Cases Valid | Integer | False | Valid |  |  |
| Abandoned Cases % Valid | Number | False | Valid |  |  |
| Segments within GH SLA (95%) | Integer | False | Valid |  |  |
| Segments within GH SLA % | Number | False | Valid |  |  |
| MDT Partially Used/Case % | Number | False | Valid |  |  |
| Segment with most Abandoned cases | Text | False | Valid |  |  |
| District with most Abandoned cases | Text | False | Valid |  |  |
| Total Segments Served % | Number | False | Valid |  |  |
| Top District with GH Achieved Segments | Text | False | Valid |  |  |
| Top District with GH Achieved Segments % | Number | False | Valid |  |  |
| Within SLA (top 5) | Integer | False | Valid |  |  |
| Within SLA (bottom 5) | Integer | False | Valid |  |  |
| Vehicle IDs by Segment | Text | False | Valid |  |  |
| Segment Days in Selected Month | Integer | False | Valid |  |  |
| Segment Uptime % | Number | False | Valid |  |  |
| 1 | Integer | False | Valid |  |  |
| Dynamic GH Title | Text | False | Valid |  |  |
| GH% Current Month | Number | False | Valid |  |  |
| GH% 3 Month ago | Number | False | Valid |  |  |
| Segments not within GH SLA (95%) | Integer | False | Valid |  |  |
| Segments not within GH SLA % | Number | False | Valid |  |  |
| GH Current Month | Integer | False | Valid |  |  |
| GH% 2 Month ago | Number | False | Valid |  |  |
| GH% 1 Month ago | Number | False | Valid |  |  |
| Improvement Flag | Text | False | Valid |  |  |
| Last 3 Months Filter | Integer | False | Valid |  |  |
| Current Month & Year | Text | False | Valid |  |  |
| Prev Month & Year | Text | False | Valid |  |  |
| Prev2 Month & Year | Text | False | Valid |  |  |
| Total Segments Served Last Month | Integer | False | Valid |  |  |
| Segments within GH SLA (96%) Last Month | Integer | False | Valid |  |  |
| Segments not within GH SLA (95%) Last Month | Integer | False | Valid |  |  |
| Penalty Cases Last Month | Integer | False | Valid |  |  |
| Segments within GH SLA % Last Month | Number | False | Valid |  |  |
| Segments not within GH SLA % Last Month | Number | False | Valid |  |  |
| Time Taken Last Month | Date | False | Valid |  |  |
| GH Last Month | Number | False | Valid |  |  |
| GH Last 2nd Month | Number | False | Valid |  |  |
| GH Last 3rd Month | Number | False | Valid |  |  |
| Improvement Flag 2 | Text | False | Valid |  |  |
| Current Month & Year Achieved | Text | False | Valid |  |  |
| Ontime Last Month | Integer | False | Valid |  |  |
| Current Month & Year Total | Text | False | Valid |  |  |
| GH Segements Last Month | Integer | False | Valid |  |  |
| GH Segements Last 2nd Month | Number | False | Valid |  |  |
| GH Segements Last 3rd Month | Number | False | Valid |  |  |
| GH Segements Last Month % | Number | False | Valid |  |  |
| Selected Segment | Text | False | Valid |  |  |
| Locality of Selected Segment | Text | False | Valid |  |  |
| Segment ART Font formatting | Text | False | Valid |  |  |
| GH Font formatting | Text | False | Valid |  |  |
| Avg Assign to Accepted (min) | Number | False | Valid |  |  |
| Avg Accepted to On Action (min) | Number | False | Valid |  |  |
| Avg On Action At Scene (min) | Number | False | Valid |  |  |
| Avg At Scene to Enroute (min) | Number | False | Valid |  |  |
| Avg Enroute to Hospital Reached (min) | Number | False | Valid |  |  |
| Avg Hospital Reached to Handover (min) | Number | False | Valid |  |  |
| Selected Vehicle | Text | False | Valid |  |  |
| Locality of Selected Vehicle | Text | False | Valid |  |  |
| KMS (m) | Variant | False | Valid |  |  |
| Speed (m) | Variant | False | Valid |  |  |
| Penalty Events Last Month | Integer | False | Valid |  |  |
| KMS Last Month | Variant | False | Valid |  |  |
| GH (Hours) Last Month | Number | False | Valid |  |  |
| Speed Last Month | Variant | False | Valid |  |  |
| % completed in GH 2 | Number | False | Valid |  |  |
| Vehicle ART Font formatting | Text | False | Valid |  |  |
| Avg Assign to Accept Formatting | Text | False | Valid |  |  |
| Avg Accept to OnAction Formatting | Text | False | Valid |  |  |
| Avg OnAction to At Scene Formatting | Text | False | Valid |  |  |
| Avg At Scene to Enroute Formatting | Text | False | Valid |  |  |
| Avg Enroute to Hosp Reach Formatting | Text | False | Valid |  |  |
| Avg Hosp Reach to Handover Formatting | Text | False | Valid |  |  |
| ELC Accepted to Action % | Text | False | Valid |  |  |
| ELC Action to At Scene % | Text | False | Valid |  |  |
| ELC At Scene to Enroute % | Text | False | Valid |  |  |
| ELC Enroute to Hosp Reached % | Text | False | Valid |  |  |
| ELC Hosp Reached to Handover % | Text | False | Valid |  |  |
| Count of DO Remarks | Integer | False | Valid |  |  |
| ART temp | Text | False | Valid |  |  |
| GH Temp | Date | False | Valid |  |  |
| Opening ODO 2 (m) | Number | False | Valid |  |  |
| Closing ODO 2 (m) | Number | False | Valid |  |  |
| Fuel Amount Both Ways | Number | False | Valid |  |  |
| % IFT KM available cases | Number | False | Valid |  |  |
| Avg Events Per Active Hour | Number | False | Valid |  |  |
| ODO Eligible IFT Cases | Integer | False | Valid |  | ODO Reading MDT |
| ODO Eligible IFT Cases % | Number | False | Valid |  | ODO Reading MDT |
| % IFT Served (All Subevent) | Number | False | Valid |  |  |
| Caller District Match | Integer | False | Valid |  |  |
| Govt to Pvt % | Number | False | Valid |  |  |
| Pvt to Govt % | Number | False | Valid |  |  |
| Govt to Govt % | Number | False | Valid |  |  |
| Pvt to Pvt % | Number | False | Valid |  |  |
| Total Complete IFT ODO % | Number | False | Valid |  | ODO Reading MDT |
| Complete IFT ODO % | Number | False | Valid |  | ODO Reading MDT |
| Partial Complete IFT ODO % | Number | False | Valid |  | ODO Reading MDT |
| Incomplete IFT ODO % | Number | False | Valid |  | ODO Reading MDT |
| Govt to Govt IFT Cases | Integer | False | Valid |  |  |
| Lower to Higher IFT % | Number | False | Valid |  |  |
| Higher to Lower IFT % | Number | False | Valid |  |  |
| Transparent Color Code | Text | False | Valid |  |  |
| ODO Eligible Cases | Integer | False | Valid |  | ODO Reading MDT |
| ODO Eligible Cases % | Number | False | Valid |  | ODO Reading MDT |
| Caller Segment Match | Integer | False | Valid |  |  |
| Total Complete ODO % | Number | False | Valid |  | ODO Reading MDT |
| Partially Complete ODO % | Number | False | Valid |  | ODO Reading MDT |
| Incomplete ODO % | Number | False | Valid |  | ODO Reading MDT |
| Temp Zero | Number | False | Valid |  |  |
| Total Complete ODO | Integer | False | Valid |  | ODO Reading MDT |
| Partially Complete ODO | Integer | False | Valid |  | ODO Reading MDT |
| Incomplete ODO | Integer | False | Valid |  | ODO Reading MDT |
| Closing ODO (MDT) | Number | False | Valid |  | ODO Reading MDT |
| Opening ODO (MDT) | Number | False | Valid |  | ODO Reading MDT |
| Emergencies Addressed | Integer | False | Valid |  |  |
| Emergencies Not Addressed | Integer | False | Valid |  |  |
| Same Level IFT % | Number | False | Valid |  |  |
| IFT KMS | Number | False | Valid |  |  |
| Non IFT KMS | Number | False | Valid |  |  |
| Non IFT cases assigned ambulance | Integer | False | Valid |  |  |
| Higher to Lower | Integer | False | Valid |  |  |
| Higher to Lower % | Number | False | Valid |  |  |
| Neonatal Served | Integer | False | Valid |  | Neonatal |
| Neonatal Served % | Number | False | Valid |  | Neonatal |
| IFT Neonatal Served % | Number | False | Valid |  | Neonatal |
| Non IFT Neonatal Served % | Number | False | Valid |  | Neonatal |
| Neonatal Segments Uptime % (CM) | Number | False | Valid |  | Neonatal |
| Neonatal Segments Uptime % (PM) | Number | False | Valid |  | Neonatal |
| Neonatal Served (CM) | Integer | False | Valid |  | Neonatal |
| Neonatal Served (PM) | Integer | False | Valid |  | Neonatal |
| IFT Neonatal Served % (CM) | Number | False | Valid |  | Neonatal |
| IFT Neonatal Served % (PM) | Number | False | Valid |  | Neonatal |
| Non IFT Neonatal Served % (CM) | Number | False | Valid |  | Neonatal |
| Non IFT Neonatal Served % (PM) | Number | False | Valid |  | Neonatal |
| Neonatal KMS Travelled (CM) | Number | False | Valid |  | Neonatal |
| Neonatal KMS Travelled (PM) | Number | False | Valid |  | Neonatal |
| Neonatal IFT KMS Travelled (CM) | Number | False | Valid |  | Neonatal |
| Neonatal IFT KMS Travelled (PM) | Number | False | Valid |  | Neonatal |
| Neonatal Non IFT KMS Travelled (CM) | Number | False | Valid |  | Neonatal |
| Neonatal Non IFT KMS Travelled (PM) | Number | False | Valid |  | Neonatal |
| Neonatal Served (CQ) | Integer | False | Valid |  | Neonatal |
| Neonatal Served (PQ) | Integer | False | Valid |  | Neonatal |
| Neonatal Segments Uptime % (CQ) | Number | False | Valid |  | Neonatal |
| Neonatal Segments Uptime % (PQ) | Number | False | Valid |  | Neonatal |
| IFT Neonatal Served % (CQ) | Number | False | Valid |  | Neonatal |
| IFT Neonatal Served % (PQ) | Number | False | Valid |  | Neonatal |
| Non IFT Neonatal Served % (CQ) | Number | False | Valid |  | Neonatal |
| Non IFT Neonatal Served % (PQ) | Number | False | Valid |  | Neonatal |
| Neonatal KMS Travelled (CQ) | Number | False | Valid |  | Neonatal |
| Neonatal KMS Travelled (PQ) | Number | False | Valid |  | Neonatal |
| Neonatal IFT KMS Travelled (CQ) | Number | False | Valid |  | Neonatal |
| Neonatal IFT KMS Travelled (PQ) | Number | False | Valid |  | Neonatal |
| Neonatal Non IFT KMS Travelled (CQ) | Number | False | Valid |  | Neonatal |
| Neonatal Non IFT KMS Travelled (PQ) | Number | False | Valid |  | Neonatal |
| Neonatal Served (CW) | Integer | False | Valid |  | Neonatal |
| Neonatal Served (PW) | Integer | False | Valid |  | Neonatal |
| Neonatal Segments Uptime % (CW) | Number | False | Valid |  | Neonatal |
| Neonatal Segments Uptime % (PW) | Number | False | Valid |  | Neonatal |
| IFT Neonatal Served % (CW) | Number | False | Valid |  | Neonatal |
| IFT Neonatal Served % (PW) | Number | False | Valid |  | Neonatal |
| Non IFT Neonatal Served % (CW) | Number | False | Valid |  | Neonatal |
| Non IFT Neonatal Served % (PW) | Number | False | Valid |  | Neonatal |
| Neonatal KMS Travelled (CW) | Number | False | Valid |  | Neonatal |
| Neonatal KMS Travelled (PW) | Number | False | Valid |  | Neonatal |
| Neonatal IFT KMS Travelled (CW) | Number | False | Valid |  | Neonatal |
| Neonatal IFT KMS Travelled (PW) | Number | False | Valid |  | Neonatal |
| Neonatal Non IFT KMS Travelled (CW) | Number | False | Valid |  | Neonatal |
| Neonatal Non IFT KMS Travelled (PW) | Number | False | Valid |  | Neonatal |
| Neonatal Served % (Out of all) | Number | False | Valid |  | Neonatal |
| IFT Dispatches/Requests % | Number | False | Valid |  |  |
| IFT Discard | Integer | False | Valid |  |  |
| % base location ODOs | Number | False | Valid |  |  |
| O-O Difference Case wise | Number | False | Valid |  |  |
| Abandoned Cases | Integer | False | Valid |  |  |
| KMS Travelled (MDT) (On Action to At Scene) | Number | False | Valid |  | ODO Reading MDT |
| KMS Travelled (MDT) (At Scene to Hosp Reached) | Number | False | Valid |  | ODO Reading MDT |
| KMS Travelled (MDT) (Hosp Reached to Back to Base) | Number | False | Valid |  | ODO Reading MDT |
| Abandoned Cases KMs % | Number | False | Valid |  | ODO Reading MDT |
| At Scene >30 KMs % | Number | False | Valid |  | ODO Reading MDT |
| At Scene <30 KMs % | Number | False | Valid |  | ODO Reading MDT |
| On Action to Scene KMs % | Number | False | Valid |  | ODO Reading MDT |
| At Scene to Hosp KMs % | Number | False | Valid |  | ODO Reading MDT |
| Hosp to Base KMs % | Number | False | Valid |  | ODO Reading MDT |
| KMS Travelled (MDT) (On Action to At Scene) >30 KMs | Number | False | Valid |  | ODO Reading MDT |
| Abandoned Cases KMs | Number | False | Valid |  | ODO Reading MDT |
| size | Integer | False | Valid |  |  |
| % KMs Travelled - IFT | Number | False | Valid |  | ODO Reading MDT |
| % KMs Travelled - Non IFT | Number | False | Valid |  | ODO Reading MDT |
| Abandoned Cases ODO | Integer | False | Valid |  |  |
| At Scene ODO Stamps % | Number | False | Valid |  | ODO Reading MDT |
| On Action ODO Stamps % | Number | False | Valid |  | ODO Reading MDT |
| Hospital Reached ODO Stamps % | Number | False | Valid |  | ODO Reading MDT |
| Back to Base ODO Stamps % | Number | False | Valid |  | ODO Reading MDT |
| Hospital Reached <100 KMs % | Number | False | Valid |  | ODO Reading MDT |
| Hospital Reached >500 KMs % | Number | False | Valid |  | ODO Reading MDT |
| Back to Base <30 KMs % | Number | False | Valid |  | ODO Reading MDT |
| Back to Base >30 KMs % | Number | False | Valid |  | ODO Reading MDT |
| At Scene <30 KMs Cases % | Number | False | Valid |  | ODO Reading MDT |
| At Scene >30 KMs Cases % | Number | False | Valid |  | ODO Reading MDT |
| Hosp Reach >100 KMs Cases % | Number | False | Valid |  | ODO Reading MDT |
| Hosp Reach <100 KMs Cases % | Number | False | Valid |  | ODO Reading MDT |
| Back to Base >30 KMs Cases % | Number | False | Valid |  | ODO Reading MDT |
| Back to Base <30 KMs Cases % | Number | False | Valid |  | ODO Reading MDT |
| At Scene Wrong ODO Cases % | Number | False | Valid |  | ODO Reading MDT |
| At Scene No KMS Cases % | Number | False | Valid |  | ODO Reading MDT |
| Hosp Reach Wrong ODO Cases % | Number | False | Valid |  | ODO Reading MDT |
| Hosp Reach No KMS Cases % | Number | False | Valid |  | ODO Reading MDT |
| Back to Base Wrong ODO Cases % | Number | False | Valid |  | ODO Reading MDT |
| Back to Base No KMS Cases % | Number | False | Valid |  | ODO Reading MDT |
| Avg MDT KMS per Day | Number | False | Valid |  | ODO Reading MDT |
| Daily MDT KMS Change | Number | False | Valid |  | ODO Reading MDT |
| Daily MDT KMS Change % | Number | False | Valid |  | ODO Reading MDT |
| Previous Day MDT KMS Travelled | Number | False | Valid |  | ODO Reading MDT |
| Previous Day Dispatches | Integer | False | Valid |  |  |
| Current Day Dispatches | Integer | False | Valid |  |  |
| Avg MDT KMS per Trip | Number | False | Valid |  | ODO Reading MDT |
| MDT KMS Decreasing Reason | Text | False | Valid |  | ODO Reading MDT |
| % IFT cases assigned prev day | Number | False | Valid |  |  |
| Monthly MDT KMS Change | Number | False | Valid |  | ODO Reading MDT |
| Previous Month MDT KMS Travelled | Number | False | Valid |  | ODO Reading MDT |
| Monthly MDT KMS Change % | Number | False | Valid |  | ODO Reading MDT |
| Previous Month Dispatches | Integer | False | Valid |  |  |
| Previous Week MDT KMS Travelled | Number | False | Valid |  | ODO Reading MDT |
| Weekly MDT KMS Change | Number | False | Valid |  | ODO Reading MDT |
| Current Week MDT KMS Travelled | Number | False | Valid |  | ODO Reading MDT |
| Weekly MDT KMS Change % | Number | False | Valid |  | ODO Reading MDT |
| Previous Week Dispatches | Integer | False | Valid |  |  |
| Avg Cases/Segment | Number | False | Valid |  |  |
| Avg Cases/Month | Number | False | Valid |  |  |
| Current Month & Year # | Text | False | Valid |  |  |
| 1st Ambulance Assigned % | Number | False | Valid |  |  |
| Missed IFT Dispatch/Requests % | Number | False | Valid |  |  |
| Missed IFT Dispatches | Integer | False | Valid |  |  |
| Least Month Missed/Request % | Number | False | Valid |  |  |
| Latest Month Missed/Requests % | Number | False | Valid |  |  |
| Latest - Least Month diff % | Number | False | Valid |  |  |
| Avg KM/Day MDT | Number | False | Valid |  | ODO Reading MDT |
| Diff from Avg KMs per Day | Number | False | Valid |  | ODO Reading MDT |
| Avg KM/Dispatch MDT | Number | False | Valid |  | ODO Reading MDT |
| Diff from Avg KMs per Dispatch | Number | False | Valid |  | ODO Reading MDT |
| IFT Dispatches % Change % | Number | False | Valid |  | ODO Reading MDT |
| Wrong MDT ODO % | Number | False | Valid |  | ODO Reading MDT |
| KMS Travelled (MDT) Text | Text | False | Valid |  |  |
| Non IFT Dispatches | Integer | False | Valid |  |  |
| KMS Travelled (MDT) in Lakhs Text | Text | False | Valid |  |  |
| KMS Travelled Raw (MDT) in Lakhs Text | Text | False | Valid |  |  |
| Year Filter Active | Text | False | Valid |  | Slicer Active |
| Month Filter Active | Text | False | Valid |  | Slicer Active |
| Week Filter Active | Text | False | Valid |  | Slicer Active |
| Date Filter Active | Text | False | Valid |  | Slicer Active |
| Region Filter Active | Text | False | Valid |  | Slicer Active |
| District Filter Active | Text | False | Valid |  | Slicer Active |
| Segment Filter Active | Text | False | Valid |  | Slicer Active |
| Locality Filter Active | Text | False | Valid |  | Slicer Active |
| Vehicle Filter Active | Text | False | Valid |  | Slicer Active |
| IFT Label Filter Active | Text | False | Valid |  | Slicer Active |
| Neonatal Filter Active | Text | False | Valid |  | Slicer Active |
| Previous Day IFT Dispatches | Integer | False | Valid |  |  |
| Previous Day IFT KMS Travelled | Number | False | Valid |  |  |
| Avg KMs per Dispatch - At Scene to Hosp One Way | Number | False | Valid |  | ODO Reading MDT |
| Avg KMs per Dispatch One Way | Number | False | Valid |  | ODO Reading MDT |
| KMS Travelled (MDT) Projected | Number | False | Valid |  | ODO Reading MDT |
| Private Hosp Served | Integer | False | Valid |  |  |
| % Private Hosp Served | Number | False | Valid |  |  |
| Total Cases Served | Integer | False | Valid |  |  |
| IFT Dispatches | Integer | False | Valid |  |  |
| IFT Abandoned % | Number | False | Valid |  |  |
| IFT Dispatches % | Number | False | Valid |  |  |
| IFT Served out of Total Diapatches % | Number | False | Valid |  |  |
| Total Cases Served % | Number | False | Valid |  |  |
| Non IFT Dispatches % | Number | False | Valid |  |  |
| Non IFT Served | Integer | False | Valid |  |  |
| Non IFT Served % | Number | False | Valid |  |  |
| IFT KMS Travelled % | Number | False | Valid |  |  |
| Non-IFT KMS Travelled % | Number | False | Valid |  |  |
| Avg KM/District Served MDT | Number | False | Valid |  | ODO Reading MDT |
| Avg KM/Vehicle MDT (Served) | Number | False | Valid |  | ODO Reading MDT |
| Avg KM/Served MDT | Number | False | Valid |  | ODO Reading MDT |
| Avg KM/IFT Served MDT | Number | False | Valid |  | ODO Reading MDT |
| Avg KM/Non IFT Served MDT | Number | False | Valid |  | ODO Reading MDT |
| Avg KM/Case - ART MDT | Number | False | Valid |  | ODO Reading MDT |
| On Action to At Scene KMs Asigned Order > 2 | Number | False | Valid |  | ODO Reading MDT |
| At Scene to Hospital KMs Asigned Order > 2 | Number | False | Valid |  | ODO Reading MDT |
| Hopsital to Base KMs Asigned Order > 2 | Number | False | Valid |  | ODO Reading MDT |
| Cases without On Action ODO | Integer | False | Valid |  |  |
| Neonatal KMS Travelled (MDT) Two Way | Number | False | Valid |  | Neonatal |
| Neonatal IFT KMS Travelled (MDT) Two Way | Number | False | Valid |  | Neonatal |
| Neonatal Non IFT KMS Travelled (MDT) Two Way | Number | False | Valid |  | Neonatal |
| Non IFT Abandoned | Integer | False | Valid |  |  |
| Abandoned Cases (Before + After At Scene) | Integer | False | Valid |  |  |
| IFT Abandoned (Before + After At Scene) | Integer | False | Valid |  |  |
| Non IFT Abandoned (Before + After At Scene) | Integer | False | Valid |  |  |
| Neonatal Abandoned (Before + After At Scene) | Integer | False | Valid |  |  |
| Non Neonatal Abandoned (Before + After At Scene) | Integer | False | Valid |  |  |
| Abandoned KMs (Before + After At Scene) | Number | False | Valid |  |  |
| IFT Abandoned KMs (Before + After At Scene) | Number | False | Valid |  |  |
| Non IFT Abandoned KMs (Before + After At Scene) | Number | False | Valid |  |  |
| Neonatal Abandoned KMs (Before + After At Scene) | Number | False | Valid |  |  |
| Non Neonatal Abandoned KMs (Before + After At Scene) | Number | False | Valid |  |  |
| Saved KMs by IFT Abandoned Cases | Number | False | Valid |  |  |
| Saved KMs by Non IFT Abandoned Cases | Number | False | Valid |  |  |
| Avg KM/Neonatal Served MDT | Number | False | Valid |  | ODO Reading MDT |
| Saved KMs by Neonatal Abandoned Cases | Number | False | Valid |  |  |
| Saved KMs Total | Number | False | Valid |  |  |
| KMS Travelled (MDT) IFT in Lakhs Text | Text | False | Valid |  |  |
| KMS Travelled (MDT) Non IFT in Lakhs Text | Text | False | Valid |  |  |
| Avg KM/Vehicle/Day MDT | Number | False | Valid |  | ODO Reading MDT |
| ART Delay Cases % | Number | False | Valid |  |  |
| Temp Delay | Number | False | Valid |  |  |
| ART Honored Label | Text | False | Valid |  | ART |
| GH Achieved Label | Text | False | Valid |  | GH |
| ART | Number | False | Valid |  |  |
| GH | Number | False | Valid |  | GH |
| Accept Time >2 min | Integer | False | Valid |  |  |
| On Action Time >2 min | Integer | False | Valid |  |  |
| Enroute Time >10 min | Integer | False | Valid |  |  |
| Accept Time >2 min % | Number | False | Valid |  |  |
| On Action Time >2 min % | Number | False | Valid |  |  |
| Enroute Time >10 min % | Number | False | Valid |  |  |
| Total Time Delay Exceeded Cases | Integer | False | Valid |  |  |
| Enroute Time Available Cases (Non IFT) | Integer | False | Valid |  |  |
| Complete ODO Stamps | Integer | False | Valid |  |  |
| Incomplete ODO Stamps | Integer | False | Valid |  |  |
| Complete ODO Stamps % | Number | False | Valid |  |  |
| Inomplete ODO Stamps % | Number | False | Valid |  |  |
| Incomplete ODO Stamps % | Number | False | Valid |  |  |
| Avg Call to Assign (min) | Number | False | Valid |  |  |
| Accident Cases Shifted | Integer | False | Valid |  |  |
| Pregnancy Cases Shifted | Integer | False | Valid |  |  |
| Private Hospital Location (m) | Text | False | Valid |  |  |
| Accept Time Available Cases | Integer | False | Valid |  |  |
| On Action Time Available Cases | Integer | False | Valid |  |  |
| Month Slicer Filter Active | Text | False | Valid |  | Slicer Active |
| Non IFT Case Requests | Integer | False | Valid |  |  |
| At Scene Closures | Integer | False | Valid |  |  |
| ART honoured | Integer | False | Valid |  | ART |
| MDT KMS | Number | False | Valid |  |  |
| MDT KMS One Way | Number | False | Valid |  |  |
| Total Cases Last Month | Integer | False | Valid |  |  |

### Measures — `Calender`

| Measure | Data type | Hidden | State | Description | Display folder |
| --- | --- | --- | --- | --- | --- |
| Date selection | Text | False | Valid |  |  |
| Max & Min Date | Text | False | Valid |  |  |
| Max Date | Text | False | Valid |  |  |

### Measures — `Refresh_time`

| Measure | Data type | Hidden | State | Description | Display folder |
| --- | --- | --- | --- | --- | --- |
| Last Refresh (IST) | Text | True | Valid |  |  |

### Measures — `Vehicles Master Database`

| Measure | Data type | Hidden | State | Description | Display folder |
| --- | --- | --- | --- | --- | --- |
| Vehicle Days in Selected Month | Integer | False | Valid |  |  |
| Vehicle Uptime Days (This Month) | Integer | False | Valid |  |  |
| Vehicle Uptime Title | Text | False | Valid |  |  |
| Vehicle Uptime % | Number | False | Valid |  |  |
| Total Days of all Vehicles in this month | Integer | False | Valid |  |  |
| Off Road Reason (m) | Text | False | Valid |  |  |
| Off Road Vehicles | Integer | False | Valid |  |  |
| No Cases Vehicles | Integer | False | Valid |  |  |
| 0% Uptime Vehicles | Integer | False | Valid |  |  |
| District Match (DistrictRegions & Vehicle Master) | Integer | False | Valid |  |  |
| Total Vehicles | Integer | False | Valid |  |  |
| Segment Match (Segment & Vehicle Master) | Integer | False | Valid |  |  |
| Segment Lookup | Text | False | Valid |  |  |
| Vehicle Uptime | Number | False | Valid |  |  |

### Measures — `ODO Reading MDT`

| Measure | Data type | Hidden | State | Description | Display folder |
| --- | --- | --- | --- | --- | --- |
| MDT Opening ODO (m) | Number | False | Valid |  |  |
| MDT Closing ODO (m) | Number | False | Valid |  |  |
| ODO Diff (m) | Number | False | Valid |  |  |
| MDT ODO Diff | Number | False | Valid |  |  |

### Measures — `Off Road`

| Measure | Data type | Hidden | State | Description | Display folder |
| --- | --- | --- | --- | --- | --- |
| Off Road Count | Integer | False | Valid |  |  |
| Off Road Latest Date | Text | False | Valid |  |  |

### Measures — `Fuel Filling`

| Measure | Data type | Hidden | State | Description | Display folder |
| --- | --- | --- | --- | --- | --- |
| Total KMS | Number | False | Valid |  |  |
| Fuel Amount in Lakhs Text | Text | False | Valid |  |  |

### Measures — `Segments`

| Measure | Data type | Hidden | State | Description | Display folder |
| --- | --- | --- | --- | --- | --- |
| Segments Uptime | Number | False | Valid |  |  |
| Days in Selected Month | Integer | False | Valid |  |  |
| No. of Days Served in this Month | Integer | False | Valid |  |  |
| Segment Uptime Days (This Month) | Integer | False | Valid |  |  |
| Segments Uptime % | Number | False | Valid |  |  |
| Segments Uptime Title | Text | False | Valid |  |  |
| Segments with 0% Uptime | Text | False | Valid |  |  |
| Segments with 0% Uptime count | Integer | False | Valid |  |  |
| Segments with 100% Uptime | Integer | False | Valid |  |  |
| Segments with 100% Uptime % | Number | False | Valid |  |  |
| Selected Date | Text | False | Valid |  |  |
| Total Days of all Segments in this month | Integer | False | Valid |  |  |
| Segments with 0% Uptime % | Number | False | Valid |  |  |
| District Match (CallBL & DistrictRegions) | Integer | False | Valid |  |  |
| Is Not Reported | Integer | False | Valid |  |  |
| Selected District | Integer | False | Valid |  |  |
| Neonatal Segments Uptime | Number | False | Valid |  |  |
| Total Days of Neonatal Segments in this month | Integer | False | Valid |  |  |
| Neonatal Segments | Integer | False | Valid |  |  |
| Neonatal Segment % | Number | False | Valid |  |  |
| Total Segments | Integer | False | Valid |  |  |
| Segment Served Flag | Integer | False | Valid |  |  |
| Segment Served Flag KPI | Integer | False | Valid |  |  |

### Measures — `GH Bins`

| Measure | Data type | Hidden | State | Description | Display folder |
| --- | --- | --- | --- | --- | --- |
| GH Segments in Bin | Integer | False | Valid |  |  |

### Measures — `ODO Reading Manual`

| Measure | Data type | Hidden | State | Description | Display folder |
| --- | --- | --- | --- | --- | --- |
| Diff Manual | Number | False | Valid |  |  |
| KMs travelled current month | Number | False | Valid |  |  |
| KMs travelled diff CM  vs PM | Number | False | Valid |  |  |
| KMs travelled Previous Month | Number | False | Valid |  |  |
| Vehicle working days | Integer | False | Valid |  |  |
| Vehicles in Use/KMS Run | Integer | False | Valid |  |  |
| Avg KM/Vehicle/Day Manual | Number | False | Valid |  |  |
| Avg KM/District Manual | Number | False | Valid |  |  |

### Measures — `Combined ODO`

| Measure | Data type | Hidden | State | Description | Display folder |
| --- | --- | --- | --- | --- | --- |
| Manual & MDT KMS Diff | Number | False | Valid |  |  |
| Manual & MDT Diff Match | Text | False | Valid |  |  |
| MDT O-O vs Manual KMS Diff | Number | False | Valid |  |  |
| MDT Manual Difference % | Number | False | Valid |  |  |
| Actual vs Logbook KMS | Number | False | Valid |  |  |
| Actual vs Logbook KMS % | Number | False | Valid |  |  |
| MDT Vehicles in Use/KMS Run | Integer | False | Valid |  |  |
| Avg KM/Vehicle/Day MDT (Combined ODO) | Number | False | Valid |  |  |
| KMS Travelled (Manual) in Lakhs Text | Text | False | Valid |  |  |
| Vehicles Travelled >500 KMs in a Day | Integer | False | Valid |  |  |

### Measures — `Accept Time Threshold`

| Measure | Data type | Hidden | State | Description | Display folder |
| --- | --- | --- | --- | --- | --- |
| Available Cases Dynamic | Integer | False | Valid |  |  |
| Deviated Cases Dynamic | Integer | False | Valid |  |  |
| Deviation % Dynamic | Number | False | Valid |  |  |
| EMT Deviation Filter | Integer | False | Valid |  |  |
| ART Crossed Dynamic | Integer | False | Valid |  |  |
| GH Crossed Dynamic | Integer | False | Valid |  |  |

### Measures — `Delay Type Slicer`

| Measure | Data type | Hidden | State | Description | Display folder |
| --- | --- | --- | --- | --- | --- |
| Selected Delay Type | Text | False | Valid |  |  |
| Selected Delay Type - Employee wise | Text | False | Valid |  |  |

### Measures — `Abandoned Summary`

| Measure | Data type | Hidden | State | Description | Display folder |
| --- | --- | --- | --- | --- | --- |
| Abandoned Count | Integer | False | Valid |  |  |
| Abandoned KMs | Number | False | Valid |  |  |
| Saved KMs by Abandoned Cases | Number | False | Valid |  |  |
| Selected Abandoned Type | Text | False | Valid |  |  |

## 6. AP108 business definitions

These are project business rules previously established for AP108 analytics. Prefer a matching existing measure after verifying its live expression. If an existing measure conflicts with a definition below, do not silently choose; flag the discrepancy.

### 6.1 Event and dispatch metrics

| KPI | Approved definition |
|---|---|
| Cases | Distinct count of `ERR[Event Id]`. |
| Dispatches | Distinct `Event Id` where `Assign Time` is not blank. |
| Abandoned | `Assign Time` is present and `At Scene Time` is blank. |
| ART Eligible | `At Scene Time` is present. |
| At Scene Closures | `Assign Time` and `At Scene Time` are present; `Enroute Time`, `Hospital Reached Time`, and `Hospital Handover Time` are blank. |
| Completed Cases | `Hospital Reached Time` is present. |
| Golden Hour Eligible | `Hospital Reached Time` is present and `Hospital To Hospital Transfer` is true, subject to the existing approved measure convention. |
| IFT | `Hospital To Hospital Transfer` is true. |
| MDT Used | `Accepted Time` is present and either `On Action Time` or `MDT Abandoned Time` is present. |

Rules:
- Use distinct `Event Id` for event-based counts unless a verified existing measure explicitly uses another approved method.
- Do not classify missing timestamps as operational failure unless the KPI definition says so.
- Do not treat a column as a measure or a measure as a column.
- Do not calculate percentages without verifying numerator, denominator, and population.

### 6.2 ART

- ART is the elapsed time from `Assign Time` to `At Scene Time`.
- ART eligibility requires `At Scene Time` to be present.
- Prefer existing ART measures.
- Locality targets: Urban = 18 minutes; Rural = 23 minutes; Tribal = 33 minutes.
- The metadata contains `ERR[Locality (BL)]` and a separate `Locality` dimension. Use exact fields and verified relationship paths.
- Do not assume all records have a valid locality classification.

### 6.3 Golden Hour

- Golden Hour target: 60 minutes.
- Standard duration is `Assign Time` to `Hospital Reached Time`.
- Exclude IFT from standard Golden Hour performance where required by the approved measure definition.
- Prefer existing Golden Hour measures and inspect their expressions.
- Do not assume all completed cases are Golden Hour eligible.

### 6.4 Vehicle and base-location rules

- Use verified vehicle relationships and master-data fields for vehicle, vehicle type, ALS/BLS, regular/backup, segment, region, and base location.
- Where the approved analysis requires vehicle-ID exclusions, exclude IDs containing `FB` or `FE`; handle blank IDs safely.
- Apply vehicle-ID exclusions only when required by the question or approved measure definition.
- Neonatal analysis may filter `Ambulance Base Location` for values containing `neonatal` when explicitly requested.

### 6.5 Odometer and KMS

- Relevant ERR odometer fields in the metadata include `1. On Action ODO`, `2. At Scene ODO`, `3. Hospital Reached ODO`, and `4. Back to Base ODO`.
- Prefer existing KMS and ODO completeness measures.
- Do not assume a subtraction rule or treat missing readings as zero.
- Verify the intended milestone fields and the calculation before generating an inline KMS or completeness measure.

## 7. Mandatory AP108 filters

Every analytical query must preserve both restrictions:

**Ambulance only**
```dax
'ERR'[Ambulance/Feeder vehicle] = "Ambulance"
```

**Exclude Backup base locations**
```dax
'ERR'[Ambulance Base Location] <> "Backup"
```

- These restrictions cannot be removed or overridden by user requests.
- `dax_enforcer.py` is responsible for inserting and verifying them.
- Do not rely on prompt compliance as the only enforcement mechanism.
- Do not use filter-removal logic to bypass these restrictions.

## 8. Date and month filtering

### 8.1 Verified calendar metadata

The supplied live schema confirms these calendar fields:

| Column | Data type | Hidden | Sort by |
| --- | --- | --- | --- |
| RowNumber-2662979B-1795-4F74-8F37-6A1BA8059B61 | Integer | True |  |
| Date | Date | False |  |
| Year | Integer | False |  |
| Quarter | Text | False |  |
| Month Number | Integer | False |  |
| Week Number | Integer | False |  |
| Year-Week | Text | False |  |
| Week Start | Date | False |  |
| Week End | Date | False |  |
| Day | Integer | False |  |
| Week Sort | Integer | False |  |
| Formatted Date | Text | False |  |
| Week in Month | Text | False |  |
| Month Sort | Integer | False |  |
| Formatted Date 2 | Text | False |  |
| Month Full | Text | False |  |
| Day name | Text | False | Day Sort |
| Day Sort | Integer | False |  |
| Month & Year Full | Date | False |  |
| Date Availability (ODO) | Integer | False |  |
| Month & Year | Text | False | Month Sort |
| Month | Text | False | Month Number |
| Month Start | Date | False |  |

Important: the supplied schema **does** contain `Calender[Month]`, `Calender[Month Full]`, `Calender[Month Number]`, `Calender[Year]`, and `Calender[Month & Year]`. Do not claim these columns are absent. Use the planner's date range and the exact field required by the question. For a known month and year, filtering `Calender[Date]` by inclusive date boundaries is the preferred unambiguous approach.

### 8.2 Rules

- Respect the exact planner start and end dates.
- Use inclusive date boundaries.
- Do not invent dates or assume an unspecified year.
- Interpret month abbreviations and full names equivalently: `Oct` = `October`.
- For a month plus year, prefer `Calender[Date]` with the first and last day of that month.
- For month-only analysis without a specified year, use the intended planner context or ask for clarification; do not silently select a year.
- Use `Calender[Month]` or `Calender[Month Full]` only when appropriate and after checking actual values and sort behaviour from the model.
- Apply date filters alongside the mandatory AP108 restrictions.

Example — October 2026:
```dax
FILTER(
    'Calender',
    'Calender'[Date] >= DATE(2026, 10, 1) &&
    'Calender'[Date] <= DATE(2026, 10, 31)
)
```

## 9. Measure selection and calculation policy

1. Identify candidate measures from live metadata.
2. Prefer an existing measure if its expression matches the requested KPI.
3. Retrieve and inspect measure expressions and dependencies when available.
4. Check that the measure is appropriate for the requested grouping and filter context.
5. Generate an inline calculation only when the required columns, relationships, and business definition are verified.
6. If the formula cannot be verified, request clarification or report missing metadata.
7. Never infer a formula from a measure name alone.

## 10. DAX generation standards

- Every query must begin with `EVALUATE`.
- Generate read-only DAX only.
- Use exact table, column, and measure names from live metadata.
- Use `SUMMARIZECOLUMNS` for grouped results where appropriate.
- Use `CALCULATETABLE(ROW(...))` for scalar results where appropriate.
- In `SUMMARIZECOLUMNS`, put grouping columns first, then filter-table expressions, then output name/expression pairs.
- Use `TOPN` for top and bottom rankings; descending for top and ascending for bottom. `BOTTOMN` is not a DAX function.
- Apply date and user filters before ranking.
- Use separate output names for multiple requested metrics.
- Confirm that metrics share a compatible population before presenting them together.
- Avoid unnecessary filter-removal functions, especially `ALL`, `REMOVEFILTERS`, and `ALLEXCEPT`.
- Do not generate write operations, model modifications, table creation, or destructive commands.

## 11. Clarification and refusal conditions

Do not generate speculative DAX when:
- The requested year or date range cannot be determined.
- The KPI is not defined and no verified measure exists.
- A required column or measure is missing.
- A required relationship path is absent or ambiguous.
- A requested calculation requires an unverified denominator, threshold, or population.
- The question conflicts with mandatory AP108 restrictions.

Never fabricate values, schema objects, relationships, measure formulas, or causal explanations.

## 12. Required generator response contract

The generator must preserve the application's agreed JSON response format:

```json
{
  "status": "success or needs_clarification",
  "dax": "complete DAX query or null",
  "selected_measure": "existing measure name or null",
  "calculation_type": "existing_measure or inline_calculation",
  "explanation": "brief explanation",
  "assumptions": [],
  "missing_metadata": []
}
```

## 13. Final DAX-generation checklist

- [ ] Metric and business definition are understood.
- [ ] Existing measure candidates were checked.
- [ ] Measure expression was inspected when needed.
- [ ] All columns and measures exist in current metadata.
- [ ] Relationships and filter directions are verified.
- [ ] Grouping fields come from the correct tables.
- [ ] Date range is correct and inclusive.
- [ ] Mandatory Ambulance and non-Backup restrictions remain enforced.
- [ ] No unsupported calculation or denominator was invented.
- [ ] Query begins with `EVALUATE` and is read-only.

## 14. Metadata export limitations

- The supplied column export contains 547 rows across the model.
- The supplied table export contains 31 tables.
- The supplied relationship export contains 33 relationships.
- The supplied measure export contains 513 measures.
- The supplied measure export has an `[Expression]` field, but all exported expression values are empty. Measure formulas and dependencies are therefore not documented here.
- To make measure selection reliable, the application should continue retrieving live measure expressions from the semantic model and include relevant expressions in `metadata_json`.
- Refresh this document whenever tables, columns, measures, or relationships change.



## 15. Production DAX-generator rules (integrated prompt contract)

This section consolidates the operational rules from the previous DAX prompt and resolves implementation details for the current AP108 application. It is intended to be included in the DAX-generation prompt together with the live metadata and planner output.

### 15.1 Authority, precedence, and conflict resolution

Apply this precedence order:

1. **Current live semantic-model metadata** is authoritative for physical table, column, measure, data-type, and relationship identifiers.
2. **Approved AP108 business definitions** in this reference are authoritative for KPI meaning, unless the user explicitly asks for a different clearly defined metric.
3. **Current measure expressions and dependencies** determine what an existing measure actually calculates.
4. **Planner output** supplies the interpreted metric, dimensions, date range, ranking, and user filters. It is an interpretation, not proof that a model object exists.
5. **User wording** describes intent but must never be used to invent physical identifiers or override compulsory AP108 filters.
6. **Examples in this document** illustrate patterns only. They do not authorize a column or measure unless the exact object exists in current live metadata.

If two sources conflict, do not silently reconcile them. Follow the precedence above and, when the conflict changes the result, return `needs_clarification` with the specific conflict.

### 15.2 Exact identifier discipline

- Copy table and column names character-for-character from the current live metadata.
- Preserve spaces, punctuation, slashes, parentheses, spelling, and capitalization.
- Validate the exact table-column pair, not merely whether a column name appears somewhere in the model.
- Validate measure names against the measures collection, separately from columns.
- Never infer a physical name from a friendly label, user phrase, display folder, or similarly named field.
- Never substitute a similarly named timestamp, locality, district, vehicle, or status field.
- If a required object is absent, return `needs_clarification`; list the exact missing object in `missing_metadata`.
- If metadata provides a misspelled physical identifier, use that exact identifier in DAX. Do not silently “correct” it.
- Hidden columns are not automatically forbidden, but do not choose them for user-facing grouping when a verified visible dimension is appropriate.

**Important distinction:** business-definition wording such as “At Scene Time” or “Hospital Handover Time” is semantic wording, not permission to use that literal physical column name. Resolve it to the exact current metadata identifier first. For example, if live metadata exposes `ERR[At Scene Tme]` or `ERR[Hospital Handoverd Time]`, use those exact names only after confirming they are the intended source fields. Never assume that a business phrase and a physical column name are identical.

### 15.3 Column, measure, and scalar-reference safety

This rule is critical because a column and a measure can have similar names.

- A measure is referenced as `[Measure Name]` and must exist in the live measures metadata.
- A column is referenced as `'Table'[Column Name]` and must exist in the live columns metadata.
- Never treat a column as a measure merely because its name looks like a KPI.
- Never emit a naked column reference in a scalar output expression where DAX requires a single scalar value.
- A column used in a scalar expression must be aggregated, reduced to one value with a justified context operation, or used as a row-level predicate inside a valid iterator/filter expression.
- Do not use `SELECTEDVALUE`, `MAX`, `MIN`, `COUNT`, `SUM`, or another aggregation merely to silence a scalar-context error. Choose it only when it matches the metric's business meaning.
- If a field such as `ERR[ART Eligible]` is a column in metadata, it is not automatically the `[ART Eligible]` measure. Search the measure catalogue for the actual measure and inspect its expression.
- When a measure expression references a column, verify that the expression aggregates or iterates that column correctly and does not rely on an unavailable row context.
- If a required measure expression is unavailable, do not claim its calculation is verified. Use a fully supported inline calculation only when all required logic is known; otherwise return `needs_clarification`.

### 15.4 Existing-measure selection and dependency audit

For each requested metric:

1. Search the live measure catalogue for exact and semantically relevant candidates.
2. Inspect the full DAX expression of the strongest candidate; do not select by name alone.
3. Inspect referenced measures and columns recursively when their definitions affect the requested result.
4. Verify the expression's population, numerator, denominator, timestamp boundaries, transfer treatment, and blank handling.
5. Verify that the measure behaves correctly under the requested date, grouping, and user filters.
6. Check for `ALL`, `REMOVEFILTERS`, `ALLEXCEPT`, `ALLSELECTED`, `CROSSFILTER`, `USERELATIONSHIP`, or other context/relationship-changing logic.
7. Determine whether any such logic is intentional and whether it removes or bypasses a compulsory AP108 restriction.
8. Reuse a suitable measure; do not recreate it inline without a reason.
9. If no suitable verified measure exists, use an inline calculation only when the approved definition and all required metadata are available.
10. If two plausible measures implement different populations or definitions, do not choose arbitrarily. Explain the difference and ask for clarification when it affects the answer.

An expression that removes either compulsory AP108 base restriction must not be used as-is. Do not attempt to “repair” a complex measure by wrapping it in another filter unless the resulting semantics can be proven from the expression and dependencies. If that cannot be proven, return `needs_clarification`.

### 15.5 AP108 KPI calculation requirements

Use the definitions in Section 6 as the canonical business definitions. The following operational details are mandatory:

- Event/case counts use `DISTINCTCOUNT` of the verified Event Id column.
- Dispatches require Assign Time to be nonblank.
- Abandoned requires Assign Time to be present and the verified At Scene timestamp to be blank.
- ART Eligible requires the verified At Scene timestamp to be present; do not confuse a similarly named text column with a measure.
- At Scene Closures require Assign and At Scene timestamps present, with Enroute, Hospital Reached, and Hospital Handover timestamps blank.
- Completed Cases require Hospital Reached Time present.
- MDT Used requires Accepted Time present and at least one of On Action Time or MDT Abandoned Time present.
- MDT Not Used is not automatically the complement of MDT Used unless the population and definition explicitly support that complement.
- ART uses Assign Time to At Scene Time; exclude records missing either required timestamp.
- ART SLA targets are Urban 18 minutes, Rural 23 minutes, and Tribal 33 minutes. Resolve locality through a verified field and relationship; do not infer missing locality.
- Golden Hour duration uses Assign Time to Hospital Reached Time, with a 60-minute target. Exclude IFT from standard Golden Hour performance where required by the approved measure definition.
- IFT is based on the verified Hospital To Hospital Transfer field being TRUE.
- KMS and ODO completeness must use verified existing measures or a documented calculation. Never infer odometer subtraction or replace blanks with zero.
- Neonatal filtering is relevant only when explicitly requested and must use a verified base-location field/value convention.

If an inline formula depends on a timestamp or field whose exact physical name is uncertain, do not guess. Resolve it from live metadata first.

### 15.6 Mandatory filter architecture: generator versus enforcement layer

The two compulsory restrictions apply to **every analytical result**:

- `'ERR'[Ambulance/Feeder vehicle] = "Ambulance"`
- `'ERR'[Ambulance Base Location] <> "Backup"`

They must affect every returned metric, every group, every ranking input, and every intermediate calculation that contributes to the result. A filter placed in an unrelated branch or unused intermediate table does not satisfy this requirement.

**Implementation contract for this application:**

- The DAX generator must NOT write these two mandatory filters into its initial DAX output. `dax_enforcer.py` owns insertion.
- The generator must still design a query shape that the enforcer supports and must never intentionally bypass the restrictions.
- The enforcer must insert both filters at the outer applicable filter context and verify that they are present in the correct structural location.
- The validator must reject unsupported or ambiguous query structures and invalid metadata references.
- The application must execute only after enforcement and validation both succeed.
- If either mandatory filter column is missing from current live metadata, stop and return `needs_clarification`; do not generate an executable success result.
- Never use `ALL`, `REMOVEFILTERS`, `ALLEXCEPT`, a disconnected intermediate table, or another technique to evade the restrictions.
- User-requested filters can narrow the permitted population but cannot broaden it beyond Ambulance and non-Backup records.

Do not add the mandatory filters a second time in the generator merely because they are compulsory. Duplicate insertion can create confusing or conflicting filter logic. The enforcement layer is the single owner of their insertion.

**Additional Vehicle Id exclusion:** when the analysis definition or question requires excluding Vehicle Id values containing `FB` or `FE`, apply that exclusion separately from the two compulsory filters. Confirm the exact Vehicle Id column in metadata and handle blanks deliberately. Do not silently apply this extra exclusion to every metric unless the approved measure or request requires it.

### 15.7 Date and month interpretation

- Use the exact planner `start` and `end` dates when present and valid.
- Date ranges are inclusive unless the request explicitly defines another interval.
- For a known month and year, prefer a filter on the verified calendar date field using the first and last date of that month.
- Month abbreviations and full names are equivalent (`Oct` = `October`).
- Do not confuse a month label with a date value.
- Do not invent a year when the user says only “October” or “in Oct”. Use a reliable planner date context only if the application explicitly supplies one; otherwise ask for the year.
- For relative periods such as “last month”, “this quarter”, or “previous week”, use the planner's resolved absolute start/end dates. Do not reinterpret them independently in the DAX prompt.
- For quarter requests, respect the calendar convention confirmed by the model/business rules. If calendar quarters are used: Q1 = Jan–Mar, Q2 = Apr–Jun, Q3 = Jul–Sep, Q4 = Oct–Dec.
- For a month-and-year request, do not use a text month column when a date range is available and unambiguous.
- If grouping by month across multiple years, include a year-aware month key/label. Do not group by month name alone, because January from different years would collapse together.
- If the user requests a trend, include a verified date/month grouping dimension and order chronologically using a verified sort key/date. Do not sort month labels alphabetically.
- Keep date filtering on the correct calendar relationship. If the required relationship is inactive, ambiguous, or absent, do not invent a relationship activation.

Example — October 2026 (illustrative; use only if the exact objects exist in live metadata):

```dax
FILTER(
    'Calender',
    'Calender'[Date] >= DATE(2026, 10, 1) &&
    'Calender'[Date] <= DATE(2026, 10, 31)
)
```

### 15.8 Grouping, filtering, and relationship discipline

- Use the exact grouping field selected by the planner after verifying it exists.
- Prefer a dimension-table field for user-facing groupings when a valid relationship to the fact table is confirmed.
- Do not substitute a fact-table text field for a dimension field, or vice versa, without a semantic reason.
- Verify relationship direction, active status, cardinality, and ambiguity before relying on filter propagation.
- Do not invent joins or relationship paths. DAX is not SQL; do not generate SQL joins.
- Apply all user-requested filters in the intended filter context without removing compulsory AP108 restrictions.
- Avoid unnecessary nested `FILTER` calls and repeated scans of the fact table when a simple Boolean filter argument is valid and semantically equivalent.
- Do not use `KEEPFILTERS`, `TREATAS`, `USERELATIONSHIP`, `CROSSFILTER`, or `ALLSELECTED` as decorative defaults; use them only when the request and model semantics require them.
- Do not use a dimension field from an unrelated/disconnected table as if it filtered ERR.
- If a grouping dimension has blank/unknown members, do not silently remove them unless the user asks or the approved measure definition does so.
- For multiple metrics in one result, confirm that they share a compatible grain and population. If not, explain the limitation or separate the calculations safely.

### 15.9 Query-shape contract

Return one complete, read-only DAX query beginning with `EVALUATE`.

**Ungrouped scalar metric:** use `CALCULATETABLE(ROW(...))` when no grouping, ranking, breakdown, or trend is requested. Include date and user-requested filters; leave compulsory base-filter insertion to the enforcer.

Illustrative shape:

```dax
EVALUATE
CALCULATETABLE(
    ROW(
        "Completed Cases", [Completed Cases]
    )
)
```

**Grouped metric:** use `SUMMARIZECOLUMNS` where appropriate. Argument order must be:

1. Grouping columns.
2. User-requested and date filter-table expressions.
3. Output name/expression pairs.

Do not put a filter expression after the first output name/expression pair. Leave compulsory base-filter insertion to the enforcer.

Illustrative shape:

```dax
EVALUATE
SUMMARIZECOLUMNS(
    'Districts & Regions'[District],
    FILTER(
        'Calender',
        'Calender'[Date] >= DATE(2026, 10, 1) &&
        'Calender'[Date] <= DATE(2026, 10, 31)
    ),
    "Dispatches", [Dispatches]
)
```

**Ranking:** build a correctly filtered grouped table first, then rank that table with `TOPN`. Use descending order for top results and ascending order for bottom results. `BOTTOMN` is not a DAX function. Use the exact requested N. Add a deterministic secondary sort only when a verified tie-break field is available and appropriate. Do not rank before the date/user filters have taken effect.

**Multiple metrics:** give every output expression a unique, meaningful output name. Do not use a column as a scalar expression. Prefer verified measures; otherwise create inline expressions with correct aggregation and filter context.

**No unsupported query forms:** do not generate `DEFINE MEASURE`, calculated-column definitions, calculated-table definitions, write operations, or model changes. Do not return partial DAX or prose mixed into the DAX field.

### 15.10 Filter-context and calculation correctness

- Understand the filter context before writing the expression.
- Use `CALCULATE` to modify filter context only when required and only with a clear understanding of which filters are replaced versus intersected.
- Do not use a filter expression that unintentionally replaces a user filter on the same column.
- Use `KEEPFILTERS` only when intersection semantics are required and verified.
- Do not remove filters from the fact table or required dimensions to make a measure return a value.
- For ratios and percentages, verify numerator, denominator, eligible population, and blank/zero behaviour from approved definitions or measure expressions.
- For averages, verify whether the intended calculation is average per event, average of a duration column, or ratio of totals. Do not assume these are interchangeable.
- For distinct event counts, preserve event grain and avoid double-counting caused by one-to-many relationships or expanded tables.
- For timestamp durations, exclude missing endpoints and verify the unit (seconds/minutes/hours) before converting.
- Do not treat text duration columns as numeric values without verified conversion logic.
- Do not coerce blanks to zero unless the business definition explicitly requires it.
- Do not invent “achieved”, “eligible”, “compliant”, “coverage”, or “utilization” logic from a label alone.

### 15.11 Ranking, sorting, and output quality

- Respect the planner's ranking direction and count.
- Rank the same metric the user requested, not a similarly named proxy.
- Ensure filters are applied before ranking.
- Do not return more rows than requested unless ties are explicitly meant to be included.
- If ties can cause `TOPN` to return more than N rows, use a verified tie-break rule only if appropriate; otherwise explain that ties may affect row count.
- Sort final output in the requested order.
- For time series and month names, sort chronologically using a verified date or sort column, never alphabetically.
- Do not invent ranking values, labels, categories, or tie-breakers.

### 15.12 Clarification policy

Return `needs_clarification` rather than speculative DAX when:

- A required table, column, measure, or relationship is missing from current metadata.
- A candidate measure's expression is unavailable or unclear and the result depends on its internal logic.
- A KPI has multiple plausible definitions or conflicting measure implementations.
- A date range/year cannot be resolved reliably.
- A requested grouping does not filter the fact table through a verified relationship.
- A percentage/ratio lacks a verified denominator or population.
- A duration lacks verified endpoints or units.
- A scalar expression would require an arbitrary aggregation of a column.
- The requested result conflicts with compulsory AP108 restrictions.
- The query cannot be represented using a structure supported by the enforcer and validator.

In `missing_metadata`, identify exact missing metadata objects or expression dependencies. In `assumptions`, include only assumptions that are genuinely necessary and explicitly safe. Do not use assumptions to conceal missing schema or business logic.

### 15.13 Response format and strict JSON

Return **only valid JSON**, with no Markdown fences, comments, leading explanation, or trailing text.

Use exactly this structure:

```json
{
  "status": "success",
  "dax": "EVALUATE ...",
  "selected_measure": "Measure Name or null",
  "calculation_type": "existing_measure",
  "explanation": "Brief description of the calculation and filters.",
  "assumptions": [],
  "missing_metadata": []
}
```

For clarification:

```json
{
  "status": "needs_clarification",
  "dax": null,
  "selected_measure": null,
  "calculation_type": "inline_calculation",
  "explanation": "State precisely why a safe query cannot be generated.",
  "assumptions": [],
  "missing_metadata": ["Exact missing table/column/measure/relationship/expression"]
}
```

Contract requirements:

- `status` must be `success` or `needs_clarification`.
- `dax` must be a complete query for success and `null` for clarification.
- `selected_measure` must be the exact selected measure name or `null`.
- `calculation_type` must be `existing_measure` or `inline_calculation`.
- `explanation` must be concise and factual.
- `assumptions` and `missing_metadata` must always be JSON arrays.
- Escape quotes and newlines correctly so the response parses as JSON.
- Never wrap the JSON in Markdown code fences.
- Never claim the query has been executed; execution belongs to the application after enforcement and validation.

### 15.14 Final pre-response audit

Before returning success, check all of the following:

- [ ] Planner intent is internally consistent and sufficient.
- [ ] Metric matches an approved AP108 definition or a verified existing measure.
- [ ] Candidate measure expression and relevant dependencies were inspected when needed.
- [ ] Every table, column, and measure reference exists exactly in current live metadata.
- [ ] No column is being mistaken for a measure or used as an invalid scalar.
- [ ] Every relationship path used by grouping/filtering is verified.
- [ ] Date boundaries and year are correct and inclusive.
- [ ] Month/quarter grouping is year-aware and chronologically sorted when applicable.
- [ ] User filters do not override the mandatory Ambulance and non-Backup restrictions.
- [ ] The generator has left insertion of the two compulsory filters to `dax_enforcer.py`.
- [ ] Query structure is supported by the enforcer and validator.
- [ ] `SUMMARIZECOLUMNS` argument ordering is correct.
- [ ] Ungrouped metrics use `CALCULATETABLE(ROW(...))` where appropriate.
- [ ] Rankings apply filters before `TOPN`, use correct direction, and use the requested count.
- [ ] No denominator, threshold, population, timestamp, unit, or calculation was invented.
- [ ] Query begins with `EVALUATE` and is read-only.
- [ ] JSON is syntactically valid and follows the exact response contract.

If any critical check fails, do not return `success`.

## 16. Implementation notes for the AP108 application

These are application-pipeline responsibilities, not DAX instructions to the model:

1. Retrieve live metadata for the target workspace and semantic model.
2. Include exact table/column/measure names and types in the prompt.
3. Retrieve relevant measure expressions and dependencies when the generator is expected to select or reuse those measures. The current CSV export does not contain usable measure expressions.
4. Give the generator the planner result, this reference document, and the live metadata.
5. Parse the model's JSON strictly; reject malformed or extra-text responses.
6. Pass generated DAX to `dax_enforcer.py`.
7. Pass enforced DAX to `dax_validator.py`.
8. Execute only if both enforcement and validation succeed.
9. Log the planner JSON, raw generated DAX, enforced DAX, validation result, and Power BI execution error separately for debugging. Do not log secrets or patient-identifiable data.
10. Keep the generator prompt, enforcement code, and validator responsibilities distinct. A prompt is guidance; enforcement and validation are the programmatic safety boundary.

**Key design principle:** the LLM proposes a query; deterministic application code enforces mandatory filters, validates metadata and query structure, and only then allows execution.

---

**End of revised AP108 DAX reference.**
