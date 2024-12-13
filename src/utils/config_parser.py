import yaml
import json
from pathlib import Path

class ConfigParser:
    """Utility to parse and validate configuration files."""

    def __init__(self, config_path):
        self.config_path = Path(config_path)
        self.config = None

    def load(self):
        """Loads the configuration file into memory."""
        if not self.config_path.exists():
            raise FileNotFoundError(f"Config file not found: {self.config_path}")
        
        if self.config_path.suffix == '.yaml' or self.config_path.suffix == '.yml':
            self.config = self._load_yaml()
        elif self.config_path.suffix == '.json':
            self.config = self._load_json()
        else:
            raise ValueError(f"Unsupported config file format: {self.config_path.suffix}")
        
        return self.config

    def _load_yaml(self):
        """Loads a YAML configuration file."""
        with open(self.config_path, 'r') as file:
            try:
                return yaml.safe_load(file)
            except yaml.YAMLError as e:
                raise ValueError(f"Error parsing YAML file: {e}")

    def _load_json(self):
        """Loads a JSON configuration file."""
        with open(self.config_path, 'r') as file:
            try:
                return json.load(file)
            except json.JSONDecodeError as e:
                raise ValueError(f"Error parsing JSON file: {e}")

    def validate(self, schema):
        """Validates the configuration against a given schema."""
        from jsonschema import validate, ValidationError
        try:
            validate(instance=self.config, schema=schema)
        except ValidationError as e:
            raise ValueError(f"Configuration validation error: {e}")

# Example usage
if __name__ == "__main__":
    parser = ConfigParser('config.yaml')
    config = parser.load()
    print(f"Loaded config: {config}")
