import time
import httpx

create_user_payload = {
    "email": f"user.{time.time()}@example.com",
    "lastName": "string",
    "firstName": "string",
    "middleName": "string",
    "phoneNumber": "string"
}

create_user_response = httpx.post("http://localhost:8003/api/v1/users", json=create_user_payload)
create_user_response_data = create_user_response.json()

data_user_deposit = {
    "userId": create_user_response_data["user"]["id"]
}

create_user_deposit = httpx.post("http://localhost:8003/api/v1/accounts/open-deposit-account",\
                                  json=data_user_deposit, timeout=8.0)

print("JSON Response:", create_user_deposit.json())
print("Status Code:", create_user_deposit.status_code)