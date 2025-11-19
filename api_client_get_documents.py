from clients.http.gateway.users.client import build_users_gateway_http_client
from clients.http.gateway.accounts.client import build_accounts_gateway_http_client
from clients.http.gateway.documents.client import build_documents_gateway_http_client

# Инициализация клиентов для работы с API
users_gateway_client = build_users_gateway_http_client()
accounts_gateway_client = build_accounts_gateway_http_client()
documents_gateway_client = build_documents_gateway_http_client()

# Создание пользователя
create_user = users_gateway_client.create_user()
user_id = create_user.user.id
print(f"Create user response: {create_user}")

# Открытие кредитного счета для пользователя
create_account = accounts_gateway_client.open_credit_card_account(user_id)
account_id = create_account.account.id
print(f"Open credit card account response: {create_account}")

# Получение документа тарифа по счету
create_tariff_document = documents_gateway_client.get_tariff_document(account_id)
print(f"Get tariff document response: {create_tariff_document}")

# Получение документа контракта по счету
create_contract_document = documents_gateway_client.get_contract_document(account_id)
print(f"Get contract document response: {create_contract_document}")