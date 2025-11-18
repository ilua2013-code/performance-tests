from typing import TypedDict
from httpx import Response, QueryParams
from clients.http.client import HTTPClient
from clients.http.gateway.client import build_gateway_http_client


# Запрос
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

# Ответы
class OperationDict(TypedDict):
    """
    Структура данных операции.
    """
    id: str
    type: str
    status: str
    amount: float
    cardId: str
    category: str
    createdAt: str
    accountId: str

class OperationReceiptDict(TypedDict):
    """
    Структура данных чека операции.
    """
    url: str
    document: str

class OperationsSummaryDict(TypedDict):
    """
    Структура данных статистики по операциям.
    """
    spentAmount: float
    receivedAmount: float
    cashbackAmount: float

class GetOperationResponseDict(TypedDict):
    """
    Структура ответа для получения списка по  операции.
    """
    operations: OperationDict

class GetOperationsResponseDict(TypedDict):
    """
    Структура ответа для получения списка операций.
    """
    operations: list[OperationDict]

class GetReceiptResponseDict(TypedDict):
    """
    Структура ответа для получения чека операции.
    """
    receipt: OperationReceiptDict

class GetOperationsSummaryResponseDict(TypedDict):
    """
    Структура ответа для получения статистики по операциям.
    """
    summary: OperationsSummaryDict

class CreateFeeOperationResponseDict(TypedDict):
    """
    Структура ответа операции списания комиссии.
    """
    operation: OperationDict


class CreateTopUpOperationResponseDict(CreateFeeOperationResponseDict):
    """
    Структура ответа операции пополнения.
    """
    pass
class CreateCashbackOperationResponseDict(CreateFeeOperationResponseDict):
    """
    Структура ответа операции кэшбэка.
    """
    pass

class CreateTransferOperationResponseDict(CreateFeeOperationResponseDict):
    """
    Структура ответа операции перевода.
    """
    pass

class CreatePurchaseOperationResponseDict(CreateFeeOperationResponseDict):
    """
    Структура ответа операции создания покупки.
    """
    pass

class CreateBillPaymentOperationResponseDict(CreateFeeOperationResponseDict):
    """
    Структура ответа операции оплаты по счету.
    """
    pass

class CreateCashWithdrawalOperationResponseDict(CreateFeeOperationResponseDict):
    """
    Структура ответа операции снятия наличных.
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

    def get_operations_receipt_api(self, operation_id: str) -> Response:
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
    
    def get_operation(self, operation_id: str) -> GetOperationResponseDict:
        response = self.get_operation_api(operation_id)
        return response.json()
    
    def get_operations_receipt(self, operation_id: str) -> GetReceiptResponseDict:
        response = self.get_operations_receipt_api(operation_id)
        return response.json()
    
    def get_operations(self, account_id: str) -> GetOperationsResponseDict:
        query = GetOperationsQueryDict(accountId = account_id)
        response = self.get_operations_api(query)
        return response.json()
    
    def get_operations_summary(self, account_id: str) -> GetOperationsSummaryResponseDict:
        query = GetOperationsSummaryQueryDict(accountId = account_id)
        response = self.get_operations_summary_api(query)
        return response.json()
    
    def make_fee_operation(self, card_id: str, account_id: str) -> CreateFeeOperationResponseDict:
        request = MakeFeeOperationRequestDict(
            status="COMPLETED",
            amount=55.77,
            cardId=card_id,
            accountId=account_id
        )
        response = self.make_fee_operation_api(request)
        return response.json()

    def make_top_up_operation(self, card_id: str, account_id: str) -> CreateTopUpOperationResponseDict:
        request = MakeTopUpOperationRequestDict(
            status="COMPLETED",
            amount=55.77,
            cardId=card_id,
            accountId=account_id
        )
        response =self.make_top_up_operation_api(request)
        return response.json()

    def make_cashback_operation(self, card_id: str, account_id: str) -> CreateCashbackOperationResponseDict:
        request = MakeCashbackOperationRequestDict(
            status="COMPLETED",
            amount=55.77,
            cardId=card_id,
            accountId=account_id
        )
        response =self.make_cashback_operation_api(request)
        return response.json()
    
    def make_transfer_operation(self, card_id: str, account_id: str) -> CreateTransferOperationResponseDict:
        request = MakeTransferOperationRequestDict(
            status="COMPLETED",
            amount=55.77,
            cardId=card_id,
            accountId=account_id
        )
        response =self.make_transfer_operation_api(request)
        return response.json()
    
    def make_purchase_operation(self, card_id: str, account_id: str) -> CreatePurchaseOperationResponseDict:
        request = MakePurchaseOperationRequestDict(
            status="COMPLETED",
            amount=55.77,
            cardId=card_id,
            accountId=account_id,
            category='Taxi'
        )
        response =self.make_purchase_operation_api(request)
        return response.json()
    
    def make_bill_payment_operation(self, card_id: str, account_id: str) -> CreateBillPaymentOperationResponseDict:
        request = MakeBillPaymentOperationRequestDict(
            status="COMPLETED",
            amount=55.77,
            cardId=card_id,
            accountId=account_id
        )
        response =self.make_bill_payment_operation_api(request)
        return response.json()
    
    def make_cash_withdrawal_operation(self, card_id: str, account_id: str) -> CreateCashWithdrawalOperationResponseDict:
        request = MakeCashWithdrawalOperationRequestDict(
            status="COMPLETED",
            amount=55.77,
            cardId=card_id,
            accountId=account_id
        )
        response =self.make_cash_withdrawal_operation_api(request)
        return response.json()
    
def build_operations_gateway_http_client() -> OperationsGatewayHTTPClient:
    """
    Функция создаёт экземпляр OperationsGatewayHTTPClient с уже настроенным HTTP-клиентом.

    :return: Готовый к использованию OperationsGatewayHTTPClient.
    """
    return OperationsGatewayHTTPClient(client=build_gateway_http_client())