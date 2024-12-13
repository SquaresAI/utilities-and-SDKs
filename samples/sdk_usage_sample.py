# SDK Usage Sample for Squares AI
from utilities_and_sdks.python_sdk.client import SquaresAIClient

def main():
    # Initialize the Squares AI SDK Client
    client = SquaresAIClient(api_key="your_api_key", base_url="https://api.squareslabs.ai")
    
    # Authenticate the client
    authenticated = client.authenticate()
    if not authenticated:
        print("Authentication failed. Please check your API key.")
        return

    # Example: Upload a dataset
    dataset_path = "path/to/your/dataset.csv"
    upload_result = client.upload_dataset(dataset_path)
    print(f"Dataset upload status: {upload_result}")

    # Example: List available models
    models = client.list_models()
    print("Available Models:")
    for model in models:
        print(f"- {model['name']} (ID: {model['id']})")

    # Example: Fine-tune a model
    model_id = models[0]['id'] if models else None
    if model_id:
        fine_tune_result = client.fine_tune_model(model_id=model_id, dataset_path=dataset_path)
        print(f"Fine-tuning status: {fine_tune_result}")
    else:
        print("No models available for fine-tuning.")

    # Example: Make a prediction
    input_data = {"text": "Sample input text for prediction"}
    prediction_result = client.predict(model_id=model_id, input_data=input_data)
    print("Prediction Result:")
    print(prediction_result)

if __name__ == "__main__":
    main()
