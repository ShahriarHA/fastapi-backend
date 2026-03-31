import json
import logging
from pathlib import Path
from typing import List, Dict, Any

BASE_DIR = Path(__file__).resolve().parent.parent
FILE_PATH = BASE_DIR / "data1" / "products.json"

logger = logging.getLogger(__name__)

def load_products_json() -> List[Dict]:
    if not FILE_PATH.exists():
        logger.error(f"File not found: {FILE_PATH}")
        return []

    try:
        with open(FILE_PATH, mode="r", encoding="utf-8") as file:
            return json.load(file)
            # print(file.read())
    except json.JSONDecodeError as e:
        logger.error(f"Invalid JSON format in {FILE_PATH}: {e}")
    except Exception as e:
        logger.exception(f"Unexpected error loading products: {e}")
    
    return []

def get_all_data() -> List[Dict]:
    return load_products_json()

# load_products_json()