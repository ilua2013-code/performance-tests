from locust import HttpUser, between, task
from tools.fakers import fake

class OpenDebitCardAccountScenarioUser(HttpUser):
    wait_time = between(2, 5)
    user_data: dict
    user_id: str

    def on_start(self) -> None:
        """
        Метод on_start вызывается один раз при запуске каждой сессии виртуального пользователя.
        Здесь мы создаем нового пользователя, отправляя POST-запрос к /api/v1/users.
        """
        request = {
            "email": fake.email(),
            "lastName": fake.last_name(),
            "firstName": fake.first_name(),
            "middleName": fake.middle_name(),
            "phoneNumber": fake.phone_number()
        }
        response = self.client.post("/api/v1/users", json=request)
        
        self.user_data = response.json()
        self.user_id = self.user_data['user']['id']  

    @task
    def open_debit_card(self):
        """
        Основная нагрузочная задача: открытие дебетовой карты.
        Здесь мы выполняем POST-запрос к /api/v1/accounts/open-debit-card-account.
        """
        request = {
            "userId": self.user_id 
        }
        response = self.client.post(
            "/api/v1/accounts/open-debit-card-account", 
            json=request,
            name="/api/v1/accounts/open-debit-card-account"
        )