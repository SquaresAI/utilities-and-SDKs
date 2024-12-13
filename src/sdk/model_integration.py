import requests
from typing import Dict, Any

class ModelIntegration:
    def __init__(self, base_url: str, headers: Dict[str, str]):
        self.base_url = base_url
        self.headers = headers

    def deploy_model(self, model_id: str, deployment_config: Dict[str, Any]) -> Dict:
        """
        Deploy a model on Squares AI.
        Args:
            model_id (str): ID of the model to deploy.
            deployment_config (Dict[str, Any]): Configuration for the deployment.
        Returns:
            Dict: API response.
        """
        deploy_endpoint = f"{self.base_url}/models/{model_id}/deploy"
        response = requests.post(deploy_endpoint, json=deployment_config, headers=self.headers)
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"Model deployment failed: {response.text}")

    def get_model_status(self, model_id: str) -> Dict:
        """
        Get the status of a deployed model.
        Args:
            model_id (str): ID of the model.
        Returns:
            Dict: API response.
        """
        status_endpoint = f"{self.base_url}/models/{model_id}/status"
        response = requests.get(status_endpoint, headers=self.headers)
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"Failed to retrieve model status: {response.text}")
