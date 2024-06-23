
from fastapi.responses import JSONResponse
from model.model import UserAndUpdate
from exception.exception import all_read_user_exist, user_created, functional_exception, success, data_not_found, user_deleted, update_user_sucess
from db.db import create_user_db, get_user_db, update_user_db, delete_user_db, check, check_name


def preprocess_user_name(name: str) -> str:
    """
    Validate and normalize user name.
    
    Args:
        name (str): User name to validate.

    Returns:
        str: Validated and normalized user name.
    """
    return ' '.join(part.strip().lower() for part in name.split())


def insert_user_check(user_name: str, age: int) -> bool:
    """
    Check if a user can be inserted into the database.

    Args:
        user_name (str): Name of the user to insert.
        age (int): Age of the user to insert.
        user_records (List): List of existing user records.

    Returns:
        bool: True if the user can be inserted, False otherwise.
    """
    name = preprocess_user_name(name=user_name)
    if check(name=name, age=age):
        return False
    return True


''' working code start'''


def insert_user(user_record: UserAndUpdate) -> JSONResponse:
    """
    Insert a new user into the database.
    
    Args:
        user_record (UserAndUpdate): User record to insert.

    Returns:
        bool: True if the user is inserted successfully, False otherwise.
    """
    try:
        name: str = preprocess_user_name(name=user_record.name)
        if check(name=name, age=user_record.age):
            return all_read_user_exist()

        create_user_db(name=name, age=user_record.age)
        return user_created()
    except Exception as ex:
        return functional_exception(exception_msg=ex.__str__)


def get_user(name: str) -> JSONResponse:
    """
    Retrieve a user from the database.
    
    Args:
        name (str): Name of the user to retrieve.

    Returns:
        dict: User record if found.

    Raises:
        HTTPException: If the user is not found.
    """
    name = preprocess_user_name(name)
    try:

        user_record = get_user_db(name)
        return success(user_record)
    except Exception as ex:
        return ex


def update_user(name: str, age: int) -> JSONResponse:
    """
    Update a user in the database.
    
    Args:
        user_record (UserAndUpdate): New user record.
        name (str): Name of the user to update.
        age (int): New age of the user.

    Returns:
        bool: True if the user is updated successfully, False otherwise.
    """
    name = preprocess_user_name(name)
    if check_name(name):
        user_record = update_user_db(name, age)
        return success(user_record)
    else:
        return data_not_found()


def update_user_check(name: str, age: int) -> JSONResponse:
    """
    Update a user in the database and perform a check.
    
    Args:
        name (str): Name of the user to update.
        age (int): New age of the user.

    Returns:
        dict: Updated user details.

    Raises:
        HTTPException: If the user is not found.
    """
    name = preprocess_user_name(name)
    if check_name(name):
        user_updated_info = update_user_db(name, age)
        if user_updated_info:
            return update_user_sucess()
        else:
           return data_not_found()
    else:
        return data_not_found()


def delete_user_check(name: str, age: int) -> JSONResponse:
    """
    Delete a user from the database.
    
    Args:
        name (str): Name of the user to delete.
        age (int): Age of the user to delete.
    """
    name = preprocess_user_name(name)
    if check(name=name, age=age):
        delete_user_db(name, age)
        return user_deleted()

    else:
        return data_not_found()


''' working code end'''
