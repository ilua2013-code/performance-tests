import grpc

from contracts.services.gateway.users.rpc_create_user_pb2 import (
    CreateUserRequest, 
    CreateUserResponse)
from contracts.services.gateway.users.users_gateway_service_pb2_grpc import UsersGatewayServiceStub
from contracts.services.gateway.accounts.rpc_open_credit_card_account_pb2 import (
    OpenCreditCardAccountRequest, 
    OpenCreditCardAccountResponse)
from contracts.services.gateway.accounts.accounts_gateway_service_pb2_grpc import AccountsGatewayServiceStub
from contracts.services.gateway.operations.rpc_make_purchase_operation_pb2 import (
    MakePurchaseOperationRequest, 
    MakePurchaseOperationResponse)
from contracts.services.gateway.operations.operations_gateway_service_pb2_grpc import OperationsGatewayServiceStub
from tools.fakers import fake
from contracts.services.operations.operation_pb2 import OperationStatus


channel = grpc.insecure_channel("localhost:9003") 

user_gateway_service = UsersGatewayServiceStub(channel)

account_gatway_service = AccountsGatewayServiceStub(channel)

operations_gateway_service = OperationsGatewayServiceStub(channel)


# Создаём gRPC-клиент для UsersGatewayService
users_gateway_service = UsersGatewayServiceStub(channel)

# Формируем запрос на создание пользователя с рандомными данными
create_user_request = CreateUserRequest(
    email=fake.email(),
    last_name=fake.last_name(),
    first_name=fake.first_name(),
    middle_name=fake.middle_name(),
    phone_number=fake.phone_number()
)
# Отправляем запрос и получаем ответ
create_user_response: CreateUserResponse = users_gateway_service.CreateUser(create_user_request)
print('Create user response:', create_user_response)

# Формируем запрос на создание кредитного счета
open_credit_card_account_request = OpenCreditCardAccountRequest(
    user_id = create_user_response.user.id
    )
# Отправляем запрос и получаем ответ
open_credit_card_account_response: OpenCreditCardAccountResponse = account_gatway_service.OpenCreditCardAccount(
    open_credit_card_account_request
    )
print('Open credit card account response:', open_credit_card_account_response)


# Формируем запрос на создание покупки 
make_purchase_operation_request = MakePurchaseOperationRequest(
    status = OperationStatus.OPERATION_STATUS_IN_PROGRESS,
    amount = fake.amount(),
    card_id = open_credit_card_account_response.account.cards[0].id,
    account_id =  open_credit_card_account_response.account.id,
    category = fake.category()
    )
# Отправляем запрос и получаем ответ
make_purchase_operation_response:  MakePurchaseOperationResponse = operations_gateway_service.MakePurchaseOperation(
    make_purchase_operation_request
    )
print('Make purchase operation response:', make_purchase_operation_response)
