from httpx import Response, QueryParams
from locust.env import Environment
from clients.http.client import HTTPClient, HTTPClientExtensions
from clients.http.gateway.client import (
    build_gateway_http_client, 
    build_gateway_locust_http_client
    )
from clients.http.gateway.operations.schema import (
    CreateBillPaymentOperationResponseSchema, 
    CreateCashWithdrawalOperationResponseSchema, 
    CreateCashbackOperationResponseSchema, 
    CreateFeeOperationResponseSchema, 
    CreatePurchaseOperationResponseSchema, 
    CreateTopUpOperationResponseSchema, 
    CreateTransferOperationResponseSchema, 
    GetOperationResponseSchema, 
    GetOperationsQuerySchema, 
    GetOperationsResponseSchema, 
    GetOperationsSummaryQuerySchema, 
    GetOperationsSummaryResponseSchema, 
    GetReceiptResponseSchema, 
    MakeBillPaymentOperationRequestSchema, 
    MakeCashWithdrawalOperationRequestSchema, 
    MakeCashbackOperationRequestSchema, 
    MakeFeeOperationRequestSchema, 
    MakePurchaseOperationRequestSchema, 
    MakeTopUpOperationRequestSchema, 
    MakeTransferOperationRequestSchema
    )


  
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
        return self.get(
            f"/api/v1/operations/{operation_id}",
            extensions = HTTPClientExtensions(route = "/api/v1/operations/{operation_id}"))

    def get_operations_receipt_api(self, operation_id: str) -> Response:
        """
        Выполняет GET-запрос на получение чека по операции.

        :param operation_id: Идентификатор операции.
        :return: Объект httpx.Response с данными чека по операции.
        """
        return self.get(
            f"/api/v1/operations/operation-receipt/{operation_id}",
            extensions = HTTPClientExtensions(route = "/api/v1/operations/operation-receipt/{operation_id}"))
    
    def get_operations_api(self, query: GetOperationsQuerySchema) -> Response:  
        """
        Выполняет GET-запрос на получение списка операций.

        :param query: Словарь с параметрами запроса (accountId).
        :return: Объект httpx.Response со списком операций.
        """
        return self.get(
            "/api/v1/operations", 
            params=QueryParams(**query.model_dump(by_alias=True)),
            extensions = HTTPClientExtensions(route = "/api/v1/operations"))
    
    def get_operations_summary_api(self, query: GetOperationsSummaryQuerySchema) -> Response:  
        """
        Выполняет GET-запрос на получение статистики по операциям.

        :param query: Словарь с параметрами запроса (accountId).
        :return: Объект httpx.Response со статистикой операций.
        """
        return self.get(
            "/api/v1/operations/operations-summary", 
            params=QueryParams(**query.model_dump(by_alias=True)),
            extensions = HTTPClientExtensions(route = "/api/v1/operations/operations-summary")) 
    
         
    def make_fee_operation_api(self, request: MakeFeeOperationRequestSchema) -> Response:
        """
        Выполняет POST-запрос для создания операции списания комиссии.

        :param request: Словарь с данными для создания операции комиссии.
        :return: Объект httpx.Response с результатом операции.
        """
        return self.post(
            "/api/v1/operations/make-fee-operation", 
            json=request.model_dump(by_alias=True))
    
    def make_top_up_operation_api(self, request: MakeTopUpOperationRequestSchema) -> Response:
        """
        Выполняет POST-запрос для создания операции пополнения.

        :param request: Словарь с данными для создания операции пополнения.
        :return: Объект httpx.Response с результатом операции.
        """
        return self.post(
            "/api/v1/operations/make-top-up-operation", 
            json=request.model_dump(by_alias=True))
    
    def make_cashback_operation_api(self, request: MakeCashbackOperationRequestSchema) -> Response:
        """
        Выполняет POST-запрос для создания операции кэшбэка.

        :param request: Словарь с данными для создания операции кэшбэка.
        :return: Объект httpx.Response с результатом операции.
        """
        return self.post(
            "/api/v1/operations/make-cashback-operation", 
            json=request.model_dump(by_alias=True))

    def make_transfer_operation_api(self, request: MakeTransferOperationRequestSchema) -> Response:
        """
        Выполняет POST-запрос для создания операции перевода.

        :param request: Словарь с данными для создания операции перевода.
        :return: Объект httpx.Response с результатом операции.
        """
        return self.post(
            "/api/v1/operations/make-transfer-operation", 
            json=request.model_dump(by_alias=True))
    
    def make_purchase_operation_api(self, request: MakePurchaseOperationRequestSchema) -> Response:
        """
        Выполняет POST-запрос для создания операции покупки.

        :param request: Словарь с данными для создания операции покупки.
        :return: Объект httpx.Response с результатом операции.
        """
        return self.post(
            "/api/v1/operations/make-purchase-operation", 
            json=request.model_dump(by_alias=True))
    
    def make_bill_payment_operation_api(self, request: MakeBillPaymentOperationRequestSchema) -> Response:
        """
        Выполняет POST-запрос для создания операции оплаты по счету.

        :param request: Словарь с данными для создания операции оплаты по счету.
        :return: Объект httpx.Response с результатом операции.
        """
        return self.post(
            "/api/v1/operations/make-bill-payment-operation", 
            json=request.model_dump(by_alias=True))
    
    def make_cash_withdrawal_operation_api(self, request: MakeCashWithdrawalOperationRequestSchema) -> Response:
        """
        Выполняет POST-запрос для создания операции снятия наличных денег.

        :param request: Словарь с данными для создания операции снятия наличных денег.
        :return: Объект httpx.Response с результатом операции.
        """
        return self.post(
            "/api/v1/operations/make-cash-withdrawal-operation", 
            json=request.model_dump(by_alias=True))
    
    def get_operation(self, operation_id: str) -> GetOperationResponseSchema:
        response = self.get_operation_api(operation_id)
        return GetOperationResponseSchema.model_validate_json(response.text)
    
    def get_operations_receipt(self, operation_id: str) -> GetReceiptResponseSchema:
        response = self.get_operations_receipt_api(operation_id)
        return GetReceiptResponseSchema.model_validate_json(response.text)
    
    def get_operations(self, account_id: str) -> GetOperationsResponseSchema:
        query = GetOperationsQuerySchema(account_id = account_id)
        response = self.get_operations_api(query)
        return GetOperationsResponseSchema.model_validate_json(response.text)
    
    def get_operations_summary(self, account_id: str) -> GetOperationsSummaryResponseSchema:
        query = GetOperationsSummaryQuerySchema(account_id = account_id)
        response = self.get_operations_summary_api(query)
        return GetOperationsSummaryResponseSchema.model_validate_json(response.text)
    
    def make_fee_operation(self, card_id: str, account_id: str) -> CreateFeeOperationResponseSchema:
        request = MakeFeeOperationRequestSchema(
            card_id=card_id,
            account_id=account_id
        )
        response = self.make_fee_operation_api(request)
        return CreateFeeOperationResponseSchema.model_validate_json(response.text)

    def make_top_up_operation(self, card_id: str, account_id: str) -> CreateTopUpOperationResponseSchema:
        request = MakeTopUpOperationRequestSchema(
            card_id=card_id,
            account_id=account_id
        )
        response =self.make_top_up_operation_api(request)
        return CreateTopUpOperationResponseSchema.model_validate_json(response.text)

    def make_cashback_operation(self, card_id: str, account_id: str) -> CreateCashbackOperationResponseSchema:
        request = MakeCashbackOperationRequestSchema(
            card_id=card_id,
            account_id=account_id
        )
        response =self.make_cashback_operation_api(request)
        return CreateCashbackOperationResponseSchema.model_validate_json(response.text)
    
    def make_transfer_operation(self, card_id: str, account_id: str) -> CreateTransferOperationResponseSchema:
        request = MakeTransferOperationRequestSchema(
            card_id=card_id,
            account_id=account_id
        )
        response =self.make_transfer_operation_api(request)
        return CreateTransferOperationResponseSchema.model_validate_json(response.text)
    
    def make_purchase_operation(self, card_id: str, account_id: str) -> CreatePurchaseOperationResponseSchema:
        request = MakePurchaseOperationRequestSchema(
            card_id=card_id,
            account_id=account_id
        )
        response =self.make_purchase_operation_api(request)
        return CreatePurchaseOperationResponseSchema.model_validate_json(response.text)
    
    def make_bill_payment_operation(self, card_id: str, account_id: str) -> CreateBillPaymentOperationResponseSchema:
        request = MakeBillPaymentOperationRequestSchema(
            card_id=card_id,
            account_id=account_id
        )
        response =self.make_bill_payment_operation_api(request)
        return CreateBillPaymentOperationResponseSchema.model_validate_json(response.text)
    
    def make_cash_withdrawal_operation(self, card_id: str, account_id: str) -> CreateCashWithdrawalOperationResponseSchema:
        request = MakeCashWithdrawalOperationRequestSchema(
            card_id=card_id,
            account_id=account_id
        )
        response =self.make_cash_withdrawal_operation_api(request)
        return CreateCashWithdrawalOperationResponseSchema.model_validate_json(response.text)
    
def build_operations_gateway_http_client() -> OperationsGatewayHTTPClient:
    """
    Функция создаёт экземпляр OperationsGatewayHTTPClient с уже настроенным HTTP-клиентом.

    :return: Готовый к использованию OperationsGatewayHTTPClient.
    """
    return OperationsGatewayHTTPClient(client=build_gateway_http_client())


def build_operations_gateway_locust_http_client(environment: Environment) -> OperationsGatewayHTTPClient:
    """
    Функция создаёт экземпляр OperationsGatewayHTTPClient адаптированного под Locust.

    Клиент автоматически собирает метрики и передаёт их в Locust через хуки.
    Используется исключительно в нагрузочных тестах.

    :param environment: объект окружения Locust.
    :return: экземпляр OperationsGatewayHTTPClient с хуками сбора метрик.
    """
    return OperationsGatewayHTTPClient(client=build_gateway_locust_http_client(environment))
