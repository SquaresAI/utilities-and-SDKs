import requests
from typing import Dict

class DataUploader:
    def __init__(self, base_url: str, headers: Dict[str, str]):
        self.base_url = base_url
        self.headers = headers

    def upload_dataset(self, file_path: str, metadata: Dict[str, str]) -> Dict:
        """
        Upload a dataset file to Squares AI.
        Args:
            file_path (str): Path to the file to be uploaded.
            metadata (Dict[str, str]): Metadata associated with the dataset.
        Returns:
            Dict: API response.
        """
        upload_endpoint = f"{self.base_url}/datasets/upload"
        files = {'file': open(file_path, 'rb')}
        response = requests.post(upload_endpoint, files=files, headers=self.headers, data=metadata)
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"Dataset upload failed: {response.text}")
