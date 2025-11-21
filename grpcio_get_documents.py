import grpc
from contracts.services.gateway.users.rpc_create_user_pb2 import (
    CreateUserRequest, 
    CreateUserResponse)
from contracts.services.gateway.users.users_gateway_service_pb2_grpc import UsersGatewayServiceStub
from contracts.services.gateway.accounts.rpc_open_savings_account_pb2 import (
    OpenSavingsAccountRequest, 
    OpenSavingsAccountResponse)
from contracts.services.gateway.accounts.accounts_gateway_service_pb2_grpc import AccountsGatewayServiceStub
from contracts.services.gateway.documents.rpc_get_contract_document_pb2 import (
    GetContractDocumentRequest, 
    GetContractDocumentResponse)
from contracts.services.gateway.documents.documents_gateway_service_pb2_grpc import DocumentsGatewayServiceStub
from tools.fakers import fake

from contracts.services.gateway.documents.rpc_get_tariff_document_pb2 import (
    GetTariffDocumentRequest, 
    GetTariffDocumentResponse)

channel = grpc.insecure_channel("localhost:9003") 

user_gateway_service = UsersGatewayServiceStub(channel)

account_gateway_service = AccountsGatewayServiceStub(channel)

document_gateway_service = DocumentsGatewayServiceStub(channel)

# Формируем запрос на создание пользователя с рандомными данными
create_user_request = CreateUserRequest(
    email=fake.email(),
    last_name=fake.last_name(),
    first_name=fake.first_name(),
    middle_name=fake.middle_name(),
    phone_number=fake.phone_number()
)
# Отправляем запрос и получаем ответ
create_user_response: CreateUserResponse = user_gateway_service.CreateUser(create_user_request)
print('Create user response:', create_user_response)

# Формируем запрос на создание сберегательного счёта 
open_saving_accont_request = OpenSavingsAccountRequest(
    user_id = create_user_response.user.id
    )

# Отправляем запрос и получаем ответ
open_saving_accont_response: OpenSavingsAccountResponse = (
    account_gateway_service.OpenSavingsAccount(open_saving_accont_request))
print('Open Saving Accont Respons:', open_saving_accont_response)

# Формируем запрос на получение документа тарифа
get_tariff_document_request = GetTariffDocumentRequest(
    account_id = open_saving_accont_response.account.id
    )

# Отправляем запрос и получаем ответ
get_tariff_document_response: GetTariffDocumentResponse = (
    document_gateway_service.GetTariffDocument(get_tariff_document_request)
    )
print('Get tariff document response:', get_tariff_document_response)

# Формируем запрос на получение документа контракта
get_contract_document_request = GetContractDocumentRequest(
    account_id = open_saving_accont_response.account.id
    )

# Отправляем запрос и получаем ответ
get_contract_document_response: GetContractDocumentResponse = (
    document_gateway_service.GetContractDocument(get_contract_document_request)
    )
print('Get contract document response:', get_contract_document_response)