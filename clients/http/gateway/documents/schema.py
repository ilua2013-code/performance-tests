from pydantic import BaseModel, HttpUrl


class DocumentSchema(BaseModel):
    """
    Описание структуры документа.
    """
    url: HttpUrl
    document: str


class GetTariffDocumentResponseSchema(BaseModel):
    """
    Описание структуры ответа для документа тарифа.
    """
    tariff: DocumentSchema


class GetContractDocumentResponseSchema(BaseModel):
    """
    Описание структуры ответа для документа контракта.
    """
    contract:DocumentSchema
