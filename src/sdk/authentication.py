import requests
from typing import Dict

class Authentication:
    def __init__(self, base_url: str, client_id: str, client_secret: str):
        self.base_url = base_url
        self.client_id = client_id
        self.client_secret = client_secret
        self.access_token = None

    def authenticate(self) -> str:
        """
        Authenticate with the Squares AI API and retrieve an access token.
        """
        auth_endpoint = f"{self.base_url}/auth/token"
        payload = {
            "client_id": self.client_id,
            "client_secret": self.client_secret,
            "grant_type": "client_credentials"
        }
        response = requests.post(auth_endpoint, data=payload)
        if response.status_code == 200:
            self.access_token = response.json().get("access_token")
            return self.access_token
        else:
            raise Exception(f"Authentication failed: {response.text}")

    def get_headers(self) -> Dict[str, str]:
        """
        Get authorization headers for authenticated requests.
        """
        if not self.access_token:
            raise Exception("Access token not available. Please authenticate first.")
        return {"Authorization": f"Bearer {self.access_token}"}

