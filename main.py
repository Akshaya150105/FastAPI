from fastapi import FastAPI
from uvicorn import run
from logic.logic import insert_user, get_user, update_user_check, delete_user_check
from model.model import UserAndUpdate


app = FastAPI()


@app.get("/")
def index():
    """
    Root endpoint to check if the API is running.
    """
    return {"message": "Welcome"}


@app.post("/create-user/")
def create_user(user_update: UserAndUpdate):
    """
    Create a new user.

    Args:
        user_update (UserAndUpdate): User details to create.

    Returns:
        dict: Message indicating the success or failure of user creation.
    """
    return insert_user(user_update)


@app.get("/get-user/{name}")
def get_user_details(name: str):
    """
    Retrieve details of a specific user.

    Args:
        name (str): Name of the user to retrieve.

    Returns:
        JSONResponse: JSON response containing user details.
    """
    return get_user(name)


@app.put("/update-user/")
def update_user(name: str, age: int):
    """
    Update age of an existing user.

    Args:
        name (str): Name of the user to update.
        age (int): New age of the user.

    Returns:
        JSONResponse: JSON response containing message and updated user details.
    """
    return update_user_check(name, age)


@app.delete("/delete-user/")
def delete_user(name: str, age: int):
    """
    Delete an existing user.

    Args:
        name (str): Name of the user to delete.
        age (int): Age of the user to delete.

    Returns:
        JSONResponse: JSON response containing message indicating success of deletion.
    """
    return delete_user_check(name, age)


if __name__ == "__main__":
    run(app, host="0.0.0.0", port=8080)
