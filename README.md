# Gas Utility Service

Install all [requirements.txt] on your environment
import postman collection

- jwt token auth added
- automatically set jwt token in cookie
-------------------------------------------------------------------------------
# signup examples:        -> http://127.0.0.1:8000/backend/register
    "username":"Mayur",
    "email":"mayur123@gmail.com",
    "password":"Pass@123"

# login examples:          -> http://127.0.0.1:8000/backend/login
    "email":"Admin123@gmail.com",
    "password":"Admin@123"
   or
   
    "username":"Admin",
    "password":"Admin@123"

--------------------------------------------------------------------------------
# api's:
GET  -> http://127.0.0.1:8000/backend/user/          # Customer's

POST -> http://127.0.0.1:8000/backend/service/
GET  -> http://127.0.0.1:8000/backend/service/?customer=<id>

GET  -> http://127.0.0.1:8000/backend/tracking/
PATCH -> http://127.0.0.1:8000/backend/tracking/<id>

--------------------------------------------------------------------------------
Admin Panel  -> http://127.0.0.1:8000/admin     

--------------------------------------------------------------------------------
