import httpx

# ==================== БАЗОВЫЙ GET-ЗАПРОС ====================
print("=== Базовый GET-запрос ===")
response = httpx.get("https://jsonplaceholder.typicode.com/todos/1")

print(response.status_code)  # 200
print(response.json())       # {'userId': 1, 'id': 1, 'title': 'delectus aut autem', 'completed': False}

# ==================== POST С JSON-ДАННЫМИ ====================
print("\n=== POST с JSON-данными ===")
data = {
    "title": "Новая задача",
    "completed": False,
    "userId": 1
}

response = httpx.post("https://jsonplaceholder.typicode.com/todos", json=data)

print(response.status_code)  # 201 (Created)
print(response.json())       # Ответ с созданной записью

# ==================== POST С FORM-ДАННЫМИ ====================
print("\n=== POST с form-данными ===")
data = {"username": "test_user", "password": "123456"}

response = httpx.post("https://httpbin.org/post", data=data)

print(response.json())  # {'form': {'username': 'test_user', 'password': '123456'}, ...}

# ==================== ЗАПРОСЫ С ЗАГОЛОВКАМИ ====================
print("\n=== Запросы с заголовками ===")
headers = {"Authorization": "Bearer my_secret_token"}

response = httpx.get("https://httpbin.org/get", headers=headers)

print(response.json())  # Заголовки включены в ответ

# ==================== ПАРАМЕТРЫ ЗАПРОСА (QUERY PARAMS) ====================
print("\n=== Параметры запроса (query params) ===")
params = {"userId": 1}

response = httpx.get("https://jsonplaceholder.typicode.com/todos", params=params)

print(response.url)    # https://jsonplaceholder.typicode.com/todos?userId=1
print(response.json()) # Фильтрованный список задач

# ==================== ЗАГРУЗКА ФАЙЛОВ ====================
print("\n=== Загрузка файлов ===")
# Создаем тестовый файл
with open("example.txt", "w") as f:
    f.write("Hello, World!")

files = {"file": ("example.txt", open("example.txt", "rb"))}

response = httpx.post("https://httpbin.org/post", files=files)

print(response.json())  # Ответ с данными о загруженном файле

# ==================== ИСПОЛЬЗОВАНИЕ КЛИЕНТА (SESSION) ====================
print("\n=== Использование клиента (сессия) ===")
with httpx.Client() as client:
    response1 = client.get("https://jsonplaceholder.typicode.com/todos/1")
    response2 = client.get("https://jsonplaceholder.typicode.com/todos/2")

print(response1.json())  # Данные первой задачи
print(response2.json())  # Данные второй задачи

# Альтернативный способ использования клиента
print("\n=== Клиент с настройками ===")
client = httpx.Client(headers={"Authorization": "Bearer my_secret_token"})

response = client.get("https://httpbin.org/get")

print(response.json())  # Заголовки включены в ответ
client.close()

# ==================== ОБРАБОТКА ОШИБОК ====================
print("\n=== Обработка ошибок ===")
# Обработка HTTP ошибок
try:
    response = httpx.get("https://jsonplaceholder.typicode.com/invalid-url")
    response.raise_for_status()  # Вызовет исключение при 4xx/5xx
except httpx.HTTPStatusError as e:
    print(f"Ошибка запроса: {e}")

# Обработка таймаутов
try:
    response = httpx.get("https://httpbin.org/delay/5", timeout=2)
except httpx.ReadTimeout:
    print("Запрос превысил лимит времени")