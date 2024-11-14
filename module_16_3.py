from fastapi import FastAPI, Path
from typing import Annotated

app = FastAPI()

users = {'1': 'Имя: Example, возраст: 18'}


# реализация CRUD запросов
# get запрос по маршруту '/users'
@app.get("/users")
async def get_users() -> dict:
    return users


# post запрос по маршруту '/user/{username}/{age}'
@app.post("/user/{username}/{age}")
async def create_users(
        username: Annotated[str, Path(min_length=5, max_length=20,
                                      description="Enter username", example="UrbanUser")],
        age: Annotated[int, Path(ge=18, le=120, description="Enter age", example="24")]) -> str:
    user_id = str(int(max(users, key=int)) + 1)
    users.update({user_id: f"Имя: {username}, возраст: {age}"})
    return f"User {user_id} is registered!"


# put запрос по маршруту '/user/{user_id}/{username}/{age}'
@app.put("/user/{user_id}/{username}/{age}")
async def update_users(
        user_id: Annotated[int, Path(ge=1, le=100, description="Enter User ID", example="1")],
        username: Annotated[str, Path(min_length=5, max_length=20,
                                      description="Enter username", example="UrbanUser")],
        age: Annotated[int, Path(ge=18, le=120, description="Enter age", example="24")]) -> str:
    users[user_id] = f"Имя: {username}, возраст: {age}"
    return f"The user {user_id} is updated"


# delete запрос по маршруту '/user/{user_id}'
@app.delete("/user/{user_id}")
async def delete_user(
        user_id: Annotated[int, Path(ge=1, le=100, description="Enter User ID", example="1")]) -> str:
    users.pop(str(user_id))
    return f"The user {user_id} is deleted"
