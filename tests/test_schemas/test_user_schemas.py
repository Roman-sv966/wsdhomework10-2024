from builtins import str
import pytest
from pydantic import ValidationError
from datetime import datetime
from app.schemas.user_schemas import UserBase, UserCreate, UserUpdate, UserResponse, UserListResponse, LoginRequest
from uuid import UUID

# Utility function to create a consistent test password
def create_test_password():
    return "StrongPass789!"

# Fixture for basic user data
@pytest.fixture
def basic_user_data():
    return {
        "nickname": "example_user",
        "email": "example_user@example.com",
        "profile_picture_url": "https://example.com/avatar.jpg",
    }

# Fixture for user creation data
@pytest.fixture
def user_creation_data():
    return {
        "nickname": "new_example",
        "email": "new_example@example.com",
        "password": create_test_password(),
    }

# Fixture for user update data
@pytest.fixture
def user_modification_data():
    return {
        "email": "modified_user@example.com",
        "first_name": "ModifiedName",
    }

# Fixture for user response data
@pytest.fixture
def user_response_details():
    return {
        "id": UUID('123e4567-e89b-12d3-a456-426614174000'),
        "nickname": "example_user",
        "email": "example_user@example.com",
        "profile_picture_url": "https://example.com/avatar.jpg",
        "last_login_at": "2024-12-04T12:00:00Z",
    }

# Fixture for login request data
@pytest.fixture
def login_data():
    return {
        "email": "example_user@example.com",
        "password": create_test_password(),
    }


# Tests for UserBase
def test_user_base_valid(user_base_data):
    user = UserBase(**user_base_data)
    assert user.nickname == user_base_data["nickname"]
    assert user.email == user_base_data["email"]

# Tests for UserCreate
def test_user_create_valid(user_create_data):
    user = UserCreate(**user_create_data)
    assert user.nickname == user_create_data["nickname"]
    assert user.password == user_create_data["password"]

# Tests for UserUpdate
def test_user_update_valid(user_update_data):
    user_update = UserUpdate(**user_update_data)
    assert user_update.email == user_update_data["email"]
    assert user_update.first_name == user_update_data["first_name"]

# Tests for UserResponse
def test_user_response_valid(user_response_data):
    user = UserResponse(**user_response_data)
    assert user.id == user_response_data["id"]
    # assert user.last_login_at == user_response_data["last_login_at"]

# Tests for LoginRequest
def test_login_request_valid(login_request_data):
    login = LoginRequest(**login_request_data)
    assert login.email == login_request_data["email"]
    assert login.password == login_request_data["password"]

# Parametrized tests for nickname and email validation
@pytest.mark.parametrize("nickname", ["test_user", "test-user", "testuser123", "123test"])
def test_user_base_nickname_valid(nickname, user_base_data):
    user_base_data["nickname"] = nickname
    user = UserBase(**user_base_data)
    assert user.nickname == nickname

@pytest.mark.parametrize("nickname", ["test user", "test?user", "", "us"])
def test_user_base_nickname_invalid(nickname, user_base_data):
    user_base_data["nickname"] = nickname
    with pytest.raises(ValidationError):
        UserBase(**user_base_data)

# Parametrized tests for URL validation
@pytest.mark.parametrize("url", ["http://valid.com/profile.jpg", "https://valid.com/profile.png", None])
def test_user_base_url_valid(url, user_base_data):
    user_base_data["profile_picture_url"] = url
    user = UserBase(**user_base_data)
    assert user.profile_picture_url == url

@pytest.mark.parametrize("url", ["ftp://invalid.com/profile.jpg", "http//invalid", "https//invalid"])
def test_user_base_url_invalid(url, user_base_data):
    user_base_data["profile_picture_url"] = url
    with pytest.raises(ValidationError):
        UserBase(**user_base_data)

def test_user_base_invalid_email():
    invalid_data = {
        "nickname": "sample_user",
        "email": "invalid_email",
        "profile_picture_url": "profile.jpg",
    }
    with pytest.raises(ValidationError) as exc_info:
        UserBase(**invalid_data)
    assert "value is not a valid email address" in str(exc_info.value)
