API Endpoint Matrix
===================

Summary
-------
This matrix lists endpoints found in the OpenAPI JSON provided.

| Method | Endpoint | Purpose | Authentication | Request | Response |
| ------ | -------- | ------- | -------------- | ------- | -------- |
| GET | /api/Transaction/SearchAccount | Search accounts by account name (acctName) | Not documented | Query param: acctName (string) | 200 Success — no schema |
| GET | /api/Transaction/AccountByCifId | Retrieve account(s) by CIF ID (cifId) | Not documented | Query param: cifId (string) | 200 Success — no schema |

Notes
-----
- "Authentication" is Not documented; behavior unknown.
- Both endpoints present in OpenAPI JSON. No other endpoints present.
- Implemented but not present in Postman: Postman collection not available for comparison.
