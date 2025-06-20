import pytest
import requests
import service
import unittest.mock as mock


@mock.patch("service.get_user")
def test_get_user(mock_get_user):
    mock_get_user.return_value = "Mock Alice"
    user_name = service.get_user(1)
    assert user_name == "Mock Alice"


@mock.patch("requests.get")
def test_get_users_from_api(mock_get):
    mock_response = mock.Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {
        "id": 1,
        "name": "Leanne Graham",
    }
    mock_get.return_value = mock_response
    data = service.get_users_from_api()
    assert data == {
        "id": 1,
        "name": "Leanne Graham",
    }


@mock.patch("requests.get")
def test_get_users_error(mock_get):
    mock_response = mock.Mock()
    mock_response.status_code = 400
    mock_get.return_value = mock_response
    with pytest.raises(requests.HTTPError):
        service.get_users_from_api()
