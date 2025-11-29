from locust import User, between, task
from clients.grpc.gateway.locust import GatewayGRPCTaskSet
from contracts.services.gateway.users.rpc_create_user_pb2 import CreateUserResponse


class GetAccountsTaskSet(GatewayGRPCTaskSet):
    """
    Нагрузочный сценарий, который последовательно:
    1. Создаёт нового пользователя.
    2. Открытие депозитного счёта.
    3. Получение списка всех счетов, связанных с пользователем.

    Примечание: требования к shared state различаются для HTTP и gRPC.
    Для удобства реализации сохраняем оба значения - create_user_response и user_id.
    """

    create_user_response: CreateUserResponse | None = None
    user_id: str 

    @task(2)
    def create_user(self):
        """
        Создаём нового пользователя и сохраняем результат для последующих шагов.
        """
        self.create_user_response = self.users_gateway_client.create_user()
        self.user_id = self.create_user_response.user.id

    @task(2)
    def open_deposit_account(self):
        """
        Открываем сберегательный счёт для созданного пользователя.
        Проверяем, что создание пользователя было успешным.
        """
        if not self.create_user_response:
            return  

        self.accounts_gateway_client.open_deposit_account(self.user_id)

    @task(6)
    def get_accounts(self):
        """
        Получение списка всех счетов, если счёт был успешно открыт.
        Проверяем, что создание пользователя было успешным.
        """
        if not self.create_user_response:
            return  

        
        self.accounts_gateway_client.get_accounts(
            self.user_id)


class GetAccountsScenarioUser(User):
    """
    Пользователь Locust, исполняющий операции со счетами.
    """
    host = "localhost"
    tasks = [GetAccountsTaskSet]
    wait_time = between(1, 3)  