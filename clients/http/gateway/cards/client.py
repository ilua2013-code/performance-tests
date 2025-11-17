from typing import TypedDict

from httpx import Response

from clients.http.client import HTTPClient


class CardsGatewayRequestDict(TypedDict):
    """
    Структура данных для создания карты.
    """
    userId: str
    accountId: str


class CardsGatewayHTTPClient(HTTPClient):
    """
    Клиент для взаимодействия с /api/v1/cards/issue-virtual-card.
    """

    def issue_virtual_card_api(self, request: CardsGatewayRequestDict) -> Response:
        """
        Создает виртуальную карту для пользователя.

        :param request: Словарь с данными пользователя и аккаунта.
        :return: Ответ от сервера с данными созданной виртуальной карты.
        """
        return self.post("/api/v1/cards/issue-virtual-card", json=request)

    def issue_physical_card_api(self, request: CardsGatewayRequestDict) -> Response:
        """
        Создает физическую карту для пользователя.

        :param request: Словарь с данными пользователя и аккаунта.
        :return: Ответ от сервера с данными созданной физической карты.
        """
        return self.post("/api/v1/cards/issue-physical-card", json=request)