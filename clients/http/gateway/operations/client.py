from typing import TypedDict
from httpx import Response, QueryParams
from clients.http.client import HTTPClient


class GetOperationsQueryDict(TypedDict): 
    """
    Структура данных для получения списка операций.
    """
    accountId: str
    
class GetOperationsSummaryQueryDict(TypedDict):  
    """
    Структура данных для получения статистики по операциям.
    """
    accountId: str

class MakeFeeOperationRequestDict(TypedDict):  
    """
    Структура данных для создание операции комиссии.
    """
    status: str 
    amount:  float
    cardId:  str
    accountId: str

class MakeTopUpOperationRequestDict(MakeFeeOperationRequestDict):  
    """
    Структура данных для создание операции пополнения.
    """
    pass

class MakeCashbackOperationRequestDict(MakeFeeOperationRequestDict):  
    """
    Структура данных для создание операции кэшбэка.
    """
    pass

class MakeTransferOperationRequestDict(MakeFeeOperationRequestDict):  
    """
    Структура данных для создание операции перевода.
    """
    pass

class MakePurchaseOperationRequestDict(MakeFeeOperationRequestDict):  
    """
    Структура данных для создание операции покупки.
    """
    category: str

class MakeBillPaymentOperationRequestDict(MakeFeeOperationRequestDict):  
    """
    Структура данных для создание операции оплаты по счету.
    """
    pass

class MakeCashWithdrawalOperationRequestDict(MakeFeeOperationRequestDict):  
    """
    Структура данных для создание операции снятия наличных денег.
    """
    pass

class OperationsGatewayHTTPClient(HTTPClient):
    """
    Клиент для взаимодействия с /api/v1/operations сервиса http-gateway.
    """

    def get_operation_api(self, operation_id: str) -> Response:
        """
        Выполняет GET-запрос на получение информации об операции по operation_id.

        :param operation_id: Идентификатор операции.
        :return: Объект httpx.Response с данными об операции.
        """
        return self.get(f"/api/v1/operations/{operation_id}")

    def get_operation_receipt_api(self, operation_id: str) -> Response:
        """
        Выполняет GET-запрос на получение чека по операции.

        :param operation_id: Идентификатор операции.
        :return: Объект httpx.Response с данными чека по операции.
        """
        return self.get(f"/api/v1/operations/operation-receipt/{operation_id}")
    
    def get_operations_api(self, query: GetOperationsQueryDict) -> Response:  
        """
        Выполняет GET-запрос на получение списка операций.

        :param query: Словарь с параметрами запроса (accountId).
        :return: Объект httpx.Response со списком операций.
        """
        return self.get("/api/v1/operations", params=QueryParams(**query))
    
    def get_operations_summary_api(self, query: GetOperationsSummaryQueryDict) -> Response:  
        """
        Выполняет GET-запрос на получение статистики по операциям.

        :param query: Словарь с параметрами запроса (accountId).
        :return: Объект httpx.Response со статистикой операций.
        """
        return self.get("/api/v1/operations/operations-summary", params=QueryParams(**query)) 
    
         
    def make_fee_operation_api(self, request: MakeFeeOperationRequestDict) -> Response:
        """
        Выполняет POST-запрос для создания операции списания комиссии.

        :param request: Словарь с данными для создания операции комиссии.
        :return: Объект httpx.Response с результатом операции.
        """
        return self.post("/api/v1/operations/make-fee-operation", json=request)
    
    def make_top_up_operation_api(self, request: MakeTopUpOperationRequestDict) -> Response:
        """
        Выполняет POST-запрос для создания операции пополнения.

        :param request: Словарь с данными для создания операции пополнения.
        :return: Объект httpx.Response с результатом операции.
        """
        return self.post("/api/v1/operations/make-top-up-operation", json=request)
    
    def make_cashback_operation_api(self, request: MakeCashbackOperationRequestDict) -> Response:
        """
        Выполняет POST-запрос для создания операции кэшбэка.

        :param request: Словарь с данными для создания операции кэшбэка.
        :return: Объект httpx.Response с результатом операции.
        """
        return self.post("/api/v1/operations/make-cashback-operation", json=request)

    def make_transfer_operation_api(self, request: MakeTransferOperationRequestDict) -> Response:
        """
        Выполняет POST-запрос для создания операции перевода.

        :param request: Словарь с данными для создания операции перевода.
        :return: Объект httpx.Response с результатом операции.
        """
        return self.post("/api/v1/operations/make-transfer-operation", json=request)
    
    def make_purchase_operation_api(self, request: MakePurchaseOperationRequestDict) -> Response:
        """
        Выполняет POST-запрос для создания операции покупки.

        :param request: Словарь с данными для создания операции покупки.
        :return: Объект httpx.Response с результатом операции.
        """
        return self.post("/api/v1/operations/make-purchase-operation", json=request)
    
    def make_bill_payment_operation_api(self, request: MakeBillPaymentOperationRequestDict) -> Response:
        """
        Выполняет POST-запрос для создания операции оплаты по счету.

        :param request: Словарь с данными для создания операции оплаты по счету.
        :return: Объект httpx.Response с результатом операции.
        """
        return self.post("/api/v1/operations/make-bill-payment-operation", json=request)
    
    def make_cash_withdrawal_operation_api(self, request: MakeCashWithdrawalOperationRequestDict) -> Response:
        """
        Выполняет POST-запрос для создания операции снятия наличных денег.

        :param request: Словарь с данными для создания операции снятия наличных денег.
        :return: Объект httpx.Response с результатом операции.
        """
        return self.post("/api/v1/operations/make-cash-withdrawal-operation", json=request)