import pytest
from unittest import mock
import os
import gitlab
import requests
from my_module import lambda_handler, send_operation_notification

# Mock environment variables
mock_env = {
    'TELEGRAM_BOT_TOKEN': 'fake_bot_token',
    'TELEGRAM_API_URL': 'https://api.telegram.org/botfake_bot_token/sendMessage',
    'GITLAB_URL': 'https://gitlab.example.com',
    'GITLAB_TOKEN': 'fake_gitlab_token',
    'ADMIN_CHAT_ID': 'fake_admin_chat_id',
    'MAIN_GROUP_ID': '2'
}

# Mock the Telegram API
def mock_send_telegram_message(chat_id, message):
    print(f"Mocked message to {chat_id}: {message}")

# Mock GitLab
def mock_gitlab_user_create(user_data):
    class MockUser:
        def __init__(self, user_id, user_email):
            self.id = user_id
            self.email = user_email

    return MockUser(user_id=1234, user_email=user_data['email'])

def mock_gitlab_group_members_create(user_id, access_level):
    pass  # No-op for testing

def mock_gitlab_project_create(project_data):
    class MockProject:
        def __init__(self, project_id, project_url):
            self.id = project_id
            self.web_url = project_url

    return MockProject(project_id=5678, project_url='https://gitlab.example.com/project/5678')


# Test send_operation_notification
@mock.patch.dict('os.environ', mock_env)
@mock.patch('my_module.send_telegram_message', side_effect=mock_send_telegram_message)
def test_send_operation_notification(mock_send):
    # Act
    send_operation_notification("Test success message")
    
    # Assert
    mock_send.assert_called_once_with("fake_admin_chat_id", "Test success message")


# Test lambda_handler (Success case)
@mock.patch.dict('os.environ', mock_env)
@mock.patch('my_module.gitlab.Gitlab')
@mock.patch('my_module.send_telegram_message', side_effect=mock_send_telegram_message)
def test_lambda_handler_success(mock_gitlab_class, mock_send):
    # Arrange
    mock_gl_instance = mock.MagicMock()
    mock_gitlab_class.return_value = mock_gl_instance
    mock_gl_instance.users.create = mock_gitlab_user_create
    mock_gl_instance.groups.get.return_value = mock.MagicMock(members=mock_gitlab_group_members_create)
    mock_gl_instance.projects.create = mock_gitlab_project_create
    
    event = {
        'name': 'Test User',
        'email': 'test@example.com',
        'username': 'testuser',
        'password': 'password123'
    }

    # Act
    result = lambda_handler(event, None)

    # Assert
    assert result['statusCode'] == 200
    assert 'user_id' in result['details']
    assert 'project_id' in result['details']
    assert 'project_url' in result['details']
    mock_send.assert_called_with(
        "fake_admin_chat_id", 
        "Success: User and project created successfully!\nUser ID: 1234\nProject ID: 5678\nProject URL: https://gitlab.example.com/project/5678"
    )


# Test lambda_handler (Missing fields case)
@mock.patch.dict('os.environ', mock_env)
@mock.patch('my_module.send_telegram_message', side_effect=mock_send_telegram_message)
def test_lambda_handler_missing_fields(mock_send):
    # Arrange
    event = {
        'name': 'Test User',
        'email': 'test@example.com',
        'username': ''
    }

    # Act
    result = lambda_handler(event, None)

    # Assert
    assert result['statusCode'] == 400
    assert "All fields are required." in result['message']
    mock_send.assert_called_once_with("fake_admin_chat_id", "Failure: All fields are required.")


# Test lambda_handler (GitLab API error)
@mock.patch.dict('os.environ', mock_env)
@mock.patch('my_module.gitlab.Gitlab')
@mock.patch('my_module.send_telegram_message', side_effect=mock_send_telegram_message)
def test_lambda_handler_gitlab_error(mock_gitlab_class, mock_send):
    # Arrange
    mock_gl_instance = mock.MagicMock()
    mock_gitlab_class.return_value = mock_gl_instance
    mock_gl_instance.users.create = mock.MagicMock(side_effect=gitlab.exceptions.GitlabCreateError("GitLab create error"))
    
    event = {
        'name': 'Test User',
        'email': 'test@example.com',
        'username': 'testuser',
        'password': 'password123'
    }

    # Act
    result = lambda_handler(event, None)

    # Assert
    assert result['statusCode'] == 400
    assert "GitLab API error" in result['message']
    mock_send.assert_called_once_with(
        "fake_admin_chat_id", 
        "Failure: GitLab API error: GitLab create error"
    )


# Test lambda_handler (Unexpected error)
@mock.patch.dict('os.environ', mock_env)
@mock.patch('my_module.send_telegram_message', side_effect=mock_send_telegram_message)
def test_lambda_handler_unexpected_error(mock_send):
    # Arrange
    event = {
        'name': 'Test User',
        'email': 'test@example.com',
        'username': 'testuser',
        'password': 'password123'
    }

    # Act
    with mock.patch('my_module.gitlab.Gitlab', side_effect=Exception("Unexpected error")):
        result = lambda_handler(event, None)

    # Assert
    assert result['statusCode'] == 500
    assert "An unexpected error occurred" in result['message']
    mock_send.assert_called_once_with(
        "fake_admin_chat_id", 
        "Failure: An unexpected error occurred: Unexpected error"
    )


if __name__ == "__main__":
    pytest.main()