from pydantic import BaseModel, Field, EmailStr


class UserSchema(BaseModel):
    """
    Модель данных пользователя.
    
    Содержит все основные поля пользователя системы.
    """
    id: str
    email: EmailStr
    last_name: str = Field(alias="lastName")
    first_name: str = Field(alias="firstName")
    middle_name: str = Field(alias="middleName")
    phone_number: str = Field(alias="phoneNumber")


class CreateUserRequestSchema(BaseModel):
    """
    Модель запроса на создание пользователя.
    
    Используется для валидации входящих данных при создании пользователя.
    """
    email: EmailStr
    last_name: str = Field(alias="lastName")
    first_name: str = Field(alias="firstName")
    middle_name: str = Field(alias="middleName")
    phone_number: str = Field(alias="phoneNumber")


class CreateUserResponseSchema(BaseModel):
    """
    Модель ответа с данными созданного пользователя.
    
    Возвращается после успешного создания пользователя.
    """
    user: UserSchema