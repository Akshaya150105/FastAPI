
from pymongo import MongoClient
from exception.exception import data_not_found


client = MongoClient()
db = client.test_database
collection = db.sample


def check(name: str, age: int) -> int:
    """
       Check if user already exists
    Args:
      name (str): Name of the user to retrieve.
      
      age(int):Age of the user to retrieve.
    Returns:
          int:record is there or not
    """
    count = collection.count_documents({"name": name, "age": age})
    return count > 0


def check_name(name: str) -> bool:
    """
       Check if user already exists
    Args:
      name (str): Name of the user to retrieve.
      
      
    Returns:
          bool:record exist or not
    """
    count = collection.count_documents({"name": name})
    return count > 0


def create_user_db(name: str, age: int):
    """
       Creates a object and stores it in the datbase
    Args:
        name (str): Name of the user to retrieve.
      
        age(int):Age of the user to retrieve.
    """
    collection.insert_one({"name": name, "age": age})


def get_user_db(name: str):
    """
    Retrieve a user from the database.

    Args:
        name (str): Name of the user to retrieve.

    Returns:
        dict: User record if found.

    Raises:
        HTTPException: If the user is not found.
    """
    name = name.lower()

    user_record = collection.find_one({"name": name})

    if user_record:
        user_record['_id'] = str(user_record['_id'])
        return user_record
    else:
        return data_not_found()


def update_user_db(name: str, age: int) -> bool:
    """
    Update a user in the database.
    
    Args:
        name (str): Name of the user to update.
        age (int): New age of the user.

    Returns:
        dict: Dictionary containing information about the update operation.
    """
    if check_name(name):
      collection.update_one({'name': name}, {'$set': {'age': age}})
      return True
    else:
        return False


def delete_user_db(name: str, age: int):
    """
      Deletes a user from the databse
      """
    collection.delete_one({ "name": name , "age": age} )