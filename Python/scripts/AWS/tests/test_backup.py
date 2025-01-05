import pytest
from unittest import mock
from my_module import backup_files, send_telegram_message, list_files_in_prefix, lambda_handler
import boto3
from moto import mock_s3
import requests

# Mock environment variables
mock_env = {
    'TELEGRAM_BOT_TOKEN': 'fake_bot_token',
    'TELEGRAM_CHAT_ID': 'fake_chat_id'
}

# Mock function for Telegram
def mock_send_telegram_message(message):
    print(f"Mocked message: {message}")

# Test send_telegram_message
@mock.patch('my_module.requests.post')
def test_send_telegram_message(mock_post):
    # Arrange
    mock_post.return_value.status_code = 200
    message = "Test message"
    
    # Act
    send_telegram_message(message)
    
    # Assert
    mock_post.assert_called_once_with(
        "https://api.telegram.org/botfake_bot_token/sendMessage",
        json={"chat_id": "fake_chat_id", "text": message}
    )

# Test list_files_in_prefix
@mock_s3
def test_list_files_in_prefix():
    # Arrange
    bucket_name = "test-bucket"
    s3 = boto3.client('s3')
    s3.create_bucket(Bucket=bucket_name)
    s3.put_object(Bucket=bucket_name, Key='files_to_backup/file1.txt', Body='test')
    s3.put_object(Bucket=bucket_name, Key='files_to_backup/file2.txt', Body='test')
    
    # Act
    files = list_files_in_prefix(bucket_name, "files_to_backup/")
    
    # Assert
    assert "files_to_backup/file1.txt" in files
    assert "files_to_backup/file2.txt" in files

# Test backup_files
@mock_s3
@mock.patch.dict('os.environ', mock_env)
@mock.patch('my_module.send_telegram_message', side_effect=mock_send_telegram_message)
def test_backup_files(mock_send):
    # Arrange
    bucket_name = "test-bucket"
    s3 = boto3.client('s3')
    s3.create_bucket(Bucket=bucket_name)
    s3.put_object(Bucket=bucket_name, Key='files_to_backup/file1.txt', Body='test')
    s3.put_object(Bucket=bucket_name, Key='files_to_backup/file2.txt', Body='test')
    
    # Act
    backup_files(bucket_name)
    
    # Assert
    backup_folder = f"{mock_env['BACKUP_PREFIX']}{datetime.now().strftime('%d-%m-%Y')}/"
    assert len(mock_send.mock_calls) == 2  # Check if 2 messages are sent (success and backup completion)
    assert "Backed up 'files_to_backup/file1.txt'" in [call[0][0] for call in mock_send.mock_calls]
    assert "Backed up 'files_to_backup/file2.txt'" in [call[0][0] for call in mock_send.mock_calls]

# Test lambda_handler
@mock_s3
@mock.patch.dict('os.environ', mock_env)
@mock.patch('my_module.send_telegram_message', side_effect=mock_send_telegram_message)
def test_lambda_handler(mock_send):
    # Arrange
    bucket_name = "test-bucket"
    s3 = boto3.client('s3')
    s3.create_bucket(Bucket=bucket_name)
    s3.put_object(Bucket=bucket_name, Key='files_to_backup/file1.txt', Body='test')
    
    event = {}
    context = {}
    
    # Act
    lambda_handler(event, context)
    
    # Assert
    assert len(mock_send.mock_calls) == 2  # Check if 2 messages are sent (success and backup completion)

if __name__ == "__main__":
    pytest.main()