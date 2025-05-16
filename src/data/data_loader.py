import json
import logging
from typing import Dict, Any, Optional

logger = logging.getLogger(__name__)

def load_json_data(file_path: str) -> Optional[Dict[str, Any]]:
    """Load data from a JSON file."""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        logger.error(f"Error loading {file_path}: {e}")
        return None