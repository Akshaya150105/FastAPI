from fastapi import HTTPException
from fastapi.responses import JSONResponse
from fastapi import HTTPException, status


class UserCreationException(HTTPException):
    """
    Exception raised when unable to create a user.
    
    Inherits from HTTPException.
    """

    def __init__(self):
        super().__init__(status_code=500, detail="Unable to create the user")


def data_not_found() -> JSONResponse:
    """
    RETURN an jSONRESPONE with status code 206 and detail "Data not found".
    """
    return JSONResponse(status_code=status.HTTP_206_PARTIAL_CONTENT, content="Data not found")


def all_read_user_exist() -> JSONResponse:
    """
    RETURN an jSONRESPONE with status code 208 and detail "User already exist".
    """
    return JSONResponse(status_code=status.HTTP_208_ALREADY_REPORTED,
                        content="User already exist")


def user_created() -> JSONResponse:
    """
    RETURN an jSONRESPONE with status code 201 and detail "User created Sucessfully".
    """
    return JSONResponse(status_code=status.HTTP_201_CREATED,
                        content="User created successfully")


def update_user_sucess() -> JSONResponse:
    """
    RETURN an jSONRESPONE with status code 200 and detail "Updated Succesfully".
    """
    return JSONResponse(status_code=status.HTTP_200_OK, content="Updated Succesfully")


def functional_exception(exception_msg: str) -> JSONResponse:
    """
    RETURN an jSONRESPONE with status code 500 with exception message.
    """
    return JSONResponse(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                        content=exception_msg)


def success(user_record) -> JSONResponse:
    """
    RETURN an jSONRESPONE with status code 202 with user content.
    """
    return JSONResponse(status_code=status.HTTP_202_ACCEPTED, content=user_record)


def user_deleted() -> JSONResponse:
    """
    RETURN an jSONRESPONE with status code 410 with detail User deleted successfully.
    """
    return JSONResponse(status_code=status.HTTP_410_GONE, content={"message": "User deleted successfully"})
