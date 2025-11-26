from locust import User, between, task
from contracts.services.gateway.accounts.rpc_open_debit_card_account_pb2 import OpenDebitCardAccountResponse
from clients.grpc.gateway.users.client import UsersGatewayGRPCClient, build_users_gateway_locust_grpc_client
from contracts.services.gateway.users.rpc_create_user_pb2 import CreateUserResponse
from clients.grpc.gateway.accounts.client import AccountsGatewayGRPCClient, build_accounts_gateway_locust_grpc_client

class OpenDebitCardAccountScenarioUser(User):
    host = "localhost"
    wait_time = between(1, 3)
    users_gateway_client: UsersGatewayGRPCClient
    accounts_gateway_client: AccountsGatewayGRPCClient
    create_user_response: CreateUserResponse
    open_debit_card_account_response: OpenDebitCardAccountResponse
    
    
    def on_start(self) -> None:
        """
        Метод, вызываемый при старте каждого виртуального пользователя.
        Здесь происходит инициализация gRPC API клиента и создание пользователя.
        """
        # Шаг 1: создаем API клиент, встроенный в экосистему Locust (с хуками и поддержкой сбора метрик)
        self.users_gateway_client = build_users_gateway_locust_grpc_client(self.environment)
        self.accounts_gateway_client = build_accounts_gateway_locust_grpc_client(self.environment)
        
        # Шаг 2: создаем пользователя через API
        self.create_user_response = self.users_gateway_client.create_user()

    @task
    def open_debit_card(self):
        """
        Основная задача виртуального пользователя — открытие дебетовой карты.
        Метод будет многократно вызываться Locust-агентами.
        """
        
        # Шаг 3: открытие дебетовой карты через API
        self.open_debit_card_account_response = self.accounts_gateway_client.open_debit_card_account(self.create_user_response.user.id)