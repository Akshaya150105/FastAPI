from pydantic import BaseModel

class UserAndUpdate(BaseModel):
    """
    Model representing a user with name and age attributes.
    
    Attributes:
        name (str): Name of the user.
        age (int): Age of the user.
    """
    name: str
    age: int

