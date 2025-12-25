import os
import logging
from azure.storage.filedatalake import DataLakeServiceClient

def upload_to_datalake(data: str, file_name: str, filesystem_name="bronze"):
    """
    Upload JSON string to Azure Data Lake Gen2.
    """
    try:
        connection_string = os.getenv("AZURE_STORAGE_CONNECTION_STRING")
        service = DataLakeServiceClient.from_connection_string(connection_string)
        filesystem = service.get_file_system_client(filesystem_name)
        file_client = filesystem.get_file_client(file_name)
        file_client.upload_data(data, overwrite=True,validate_content=False)
        logging.info(f"✅ Uploaded to Data Lake {filesystem_name}/{file_name}")
    except Exception as e:
        logging.error(f"❌ Failed to upload {file_name}: {e}")