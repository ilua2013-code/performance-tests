import uvicorn  # импортируем Uvicorn для программного запуска
from fastapi import FastAPI, Query, Path, Body, APIRouter
from pydantic import BaseModel

app = FastAPI(title="basics")
router = APIRouter(prefix="/api/v1", tags=["Basics"])


class User(BaseModel):
    username: str
    email: str
    age: int


class UserResponse(BaseModel):
    username: str
    email: str
    message: str

class Product(BaseModel):
    name: str
    description: str
    price: float
    category: str
    in_stock: bool
    stock_quantity: int

class ProductResponse(BaseModel):
    name: str
    description: str
    price: float
    category: str
    in_stock: bool
    stock_quantity: int
    message: str

@router.get("/basics/{item_id}")
async def get_basics(
        name: str = Query("Alise", description="Имя пользователя"),
        item_id: int = Path(..., description="Идентификатор элемента")
):
    return {
        "message": f"Hello, {name}!",
        "description": f"Item number {item_id}"
    }


@router.post("/basics/users", response_model=UserResponse)
async def create_user(user: User = Body(..., description="Данные нового пользователя")):
    return UserResponse(
        username=user.username,
        email=user.email,
        message="User created successfully!"
    )

@router.put("/basics/products/{product_id}", response_model=ProductResponse)
async def put_basics(
    product_id: int = Path(..., description="Идентификатор продукта"), 
    product: Product = Body(..., description="Новые данные продукта" )):
    return ProductResponse(
        name = product.name,
        description = product.description,
        price = product.price,
        category = product.category,
        in_stock = product.in_stock,
        stock_quantity = product.stock_quantity,
        message = f"Продукт  {product_id} успешно изменен")




app.include_router(router)

# --------------------------------------------------------
# Программный запуск приложения
# --------------------------------------------------------
if __name__ == "__main__":
    # Запускаем Uvicorn с указанием:
    # - имя модуля и объекта приложения (fastapi_basics:app)
    # - адрес и порт (host, port)
    # - авто-перезагрузка при изменении кода (reload=True)
    uvicorn.run(
        "fastapi_basics:app",  # "<module_name>:<app_instance>"
        host="127.0.0.1",  # адрес, на котором слушаем входящие подключения
        port=8000,  # порт
        reload=True,  # перезагрузка при изменении файлов
        log_level="info"  # уровень логирования
    )