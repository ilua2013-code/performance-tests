from pydantic import BaseModel, Field, ConfigDict, HttpUrl
from enum import StrEnum
from datetime import datetime
from tools.fakers import fake

# Запрос
class OperationsStatus(StrEnum):
    FAILED = "FAILED"
    COMPLETED = "COMPLETED"
    IN_PROGRESS = "IN_PROGRESS"
    UNSPECIFIED = "UNSPECIFIED"


class GetOperationsQuerySchema(BaseModel): 
    """
    Структура данных для получения списка операций.
    """
    model_config = ConfigDict(populate_by_name=True)

    account_id: str = Field(alias="accountId")
    
class GetOperationsSummaryQuerySchema(BaseModel):  
    """
    Структура данных для получения статистики по операциям.
    """
    model_config = ConfigDict(populate_by_name=True)

    account_id: str = Field(alias="accountId")

class MakeFeeOperationRequestSchema(BaseModel):  
    """
    Структура данных для создание операции комиссии.
    """
    model_config = ConfigDict(populate_by_name=True)

    status: OperationsStatus = Field(default_factory=lambda: fake.enum(OperationsStatus))
    amount:  float = Field(default_factory=fake.amount)
    card_id:  str = Field(alias="cardId")
    account_id: str = Field(alias="accountId")

class MakeTopUpOperationRequestSchema(BaseModel):  
    """
    Структура данных для создание операции пополнения.
    """
    model_config = ConfigDict(populate_by_name=True)

    status: OperationsStatus = Field(default_factory=lambda: fake.enum(OperationsStatus))
    amount:  float = Field(default_factory=fake.amount)
    card_id:  str = Field(alias="cardId")
    account_id: str = Field(alias="accountId")

class MakeCashbackOperationRequestSchema(BaseModel):  
    """
    Структура данных для создание операции кэшбэка.
    """
    model_config = ConfigDict(populate_by_name=True)

    status: OperationsStatus = Field(default_factory=lambda: fake.enum(OperationsStatus))
    amount:  float = Field(default_factory=fake.amount)
    card_id:  str = Field(alias="cardId")
    account_id: str = Field(alias="accountId")

class MakeTransferOperationRequestSchema(BaseModel):  
    """
    Структура данных для создание операции перевода.
    """
    model_config = ConfigDict(populate_by_name=True)

    status: OperationsStatus = Field(default_factory=lambda: fake.enum(OperationsStatus))
    amount:  float = Field(default_factory=fake.amount)
    card_id:  str = Field(alias="cardId")
    account_id: str = Field(alias="accountId")

class MakePurchaseOperationRequestSchema(BaseModel):  
    """
    Структура данных для создание операции покупки.
    """
    model_config = ConfigDict(populate_by_name=True)

    status: OperationsStatus = Field(default_factory=lambda: fake.enum(OperationsStatus))
    amount:  float = Field(default_factory=fake.amount)
    card_id:  str = Field(alias="cardId")
    account_id: str = Field(alias="accountId")
    category: str = Field(default_factory=fake.category)

class MakeBillPaymentOperationRequestSchema(BaseModel):  
    """
    Структура данных для создание операции оплаты по счету.
    """
    model_config = ConfigDict(populate_by_name=True)

    status: OperationsStatus = Field(default_factory=lambda: fake.enum(OperationsStatus))
    amount:  float = Field(default_factory=fake.amount)
    card_id:  str = Field(alias="cardId")
    account_id: str = Field(alias="accountId")

class MakeCashWithdrawalOperationRequestSchema(BaseModel):  
    """
    Структура данных для создание операции снятия наличных денег.
    """
    model_config = ConfigDict(populate_by_name=True)
    
    status: OperationsStatus = Field(default_factory=lambda: fake.enum(OperationsStatus))
    amount:  float = Field(default_factory=fake.amount)
    card_id:  str = Field(alias="cardId")
    account_id: str = Field(alias="accountId")

# Ответы

class OperationType(StrEnum):
    FEE = "FEE"
    TOP_UP = "TOP_UP"
    PURCHASE = "PURCHASE"
    CASHBACK = "CASHBACK"
    TRANSFER = "TRANSFER"
    BILL_PAYMENT = "BILL_PAYMENT"
    CASH_WITHDRAWAL = "CASH_WITHDRAWAL"


class OperationSchema(BaseModel):
    """
    Структура данных операции.
    """
    model_config = ConfigDict(populate_by_name=True)  # Добавлено
    id: str
    type: OperationType
    status: OperationsStatus
    amount: float
    card_id:  str = Field(alias="cardId")
    category: str
    created_at: datetime = Field(alias="createdAt")
    account_id: str = Field(alias="accountId")

class OperationReceiptSchema(BaseModel):
    """
    Структура данных чека операции.
    """
    url: HttpUrl
    document: str


class OperationsSummarySchema(BaseModel):
    """
    Структура данных статистики по операциям.
    """
    model_config = ConfigDict(populate_by_name=True)  
    spent_amount: float = Field(alias="spentAmount")
    received_amount: float = Field(alias="receivedAmount")
    cashback_amount: float = Field(alias="cashbackAmount")

class GetOperationResponseSchema(BaseModel):
    """
    Структура ответа для получения одной операции.
    """
    operation: OperationSchema 

class GetOperationsResponseSchema(BaseModel):
    """
    Структура ответа для получения списка операций.
    """
    operations: list[OperationSchema]

class GetReceiptResponseSchema(BaseModel):
    """
    Структура ответа для получения чека операции.
    """
    receipt: OperationReceiptSchema

class GetOperationsSummaryResponseSchema(BaseModel):
    """
    Структура ответа для получения статистики по операциям.
    """
    summary: OperationsSummarySchema

class MakeFeeOperationResponseSchema(BaseModel):
    """
    Структура ответа операции списания комиссии.
    """
    operation: OperationSchema

class MakeTopUpOperationResponseSchema(BaseModel):
    """
    Структура ответа операции пополнения.
    """
    operation: OperationSchema

class MakeCashbackOperationResponseSchema(BaseModel):
    """
    Структура ответа операции кэшбэка.
    """
    operation: OperationSchema

class MakeTransferOperationResponseSchema(BaseModel):
    """
    Структура ответа операции перевода.
    """
    operation: OperationSchema

class MakePurchaseOperationResponseSchema(BaseModel):
    """
    Структура ответа операции создания покупки.
    """
    operation: OperationSchema

class MakeBillPaymentOperationResponseSchema(BaseModel):
    """
    Структура ответа операции оплаты по счету.
    """
    operation: OperationSchema

class MakeCashWithdrawalOperationResponseSchema(BaseModel):
    """
    Структура ответа операции снятия наличных.
    """
    operation: OperationSchema