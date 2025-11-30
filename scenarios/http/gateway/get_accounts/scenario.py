from locust import task

from clients.http.gateway.locust import GatewayHTTPTaskSet
from clients.http.gateway.users.schema import CreateUserResponseSchema
from tools.locust.user import LocustBaseUser


class GetAccountsTaskSet(GatewayHTTPTaskSet):
    """
    Нагрузочный сценарий, который последовательно:
    1. Создаёт нового пользователя.
    2. Открытие депозитного счёта.
    3. Получение списка всех счетов, связанных с пользователем.

    Использует базовый GatewayHTTPTaskSet и уже созданных в нём API клиентов.
    """

    create_user_response: CreateUserResponseSchema | None = None
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


class GetAccountsScenarioUser(LocustBaseUser):
    """
    Пользователь Locust, исполняющий операции со счетами.
    """
    tasks = [GetAccountsTaskSet] 