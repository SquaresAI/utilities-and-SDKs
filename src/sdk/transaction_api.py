import requests
from typing import Dict

class TransactionAPI:
    def __init__(self, base_url: str, headers: Dict[str, str]):
        self.base_url = base_url
        self.headers = headers

    def initiate_transaction(self, transaction_data: Dict) -> Dict:
        """
        Initiate a transaction on the Squares AI marketplace.
        Args:
            transaction_data (Dict): Details of the transaction.
        Returns:
            Dict: API response.
        """
        transaction_endpoint = f"{self.base_url}/transactions/initiate"
        response = requests.post(transaction_endpoint, json=transaction_data, headers=self.headers)
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"Transaction initiation failed: {response.text}")

    def get_transaction_status(self, transaction_id: str) -> Dict:
        """
        Retrieve the status of a transaction.
        Args:
            transaction_id (str): ID of the transaction.
        Returns:
            Dict: API response.
        """
        status_endpoint = f"{self.base_url}/transactions/{transaction_id}/status"
        response = requests.get(status_endpoint, headers=self.headers)
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"Failed to retrieve transaction status: {response.text}")
