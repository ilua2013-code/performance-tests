import time
import httpx

# 1. Создание пользователя
create_user_payload = {
    "email": f"user.{time.time()}@example.com",
    "lastName": "string",
    "firstName": "string",
    "middleName": "string",
    "phoneNumber": "string"
}

create_user_response = httpx.post("http://localhost:8003/api/v1/users", json=create_user_payload)
create_user_response_data = create_user_response.json()
user_id = create_user_response_data["user"]["id"]

# 2. Создание кредитного счета
data_user_credit_card = {
    "userId": user_id
}

create_user_credit_card_response = httpx.post(
    "http://localhost:8003/api/v1/accounts/open-credit-card-account",
    json=data_user_credit_card,
    timeout=8.0
)
credit_card_data = create_user_credit_card_response.json()
account_id = credit_card_data["account"]["id"]
card_id = credit_card_data["account"]["cards"][0]["id"]

# 3. Совершение операции покупки
data_purchase_operation = {
    "status": "IN_PROGRESS",
    "amount": 77.99,
    "cardId": card_id,
    "accountId": account_id,
    "category": "taxi"
}

purchase_operation_response = httpx.post(
    "http://localhost:8003/api/v1/operations/make-purchase-operation",
    json=data_purchase_operation
)
purchase_operation_data = purchase_operation_response.json()
operation_id = purchase_operation_data["operation"]["id"]

# 4. Получение чека по операции
operation_receipt_response = httpx.get(
    f'http://localhost:8003/api/v1/operations/operation-receipt/{operation_id}'
)

# Вывод чека в консоль
print("JSON Response:", operation_receipt_response.json())
print("Status Code:", operation_receipt_response.status_code)