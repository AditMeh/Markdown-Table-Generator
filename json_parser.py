import json
import typing
from typing import Dict, List, Tuple

COLS_KEY = "columns"
DATA_KEY = "data"

def parse_json(fp: str) -> Tuple[List[str], List[Dict[str, str]]]:
    with open(fp) as f:
        data = json.load(f)
    return data[COLS_KEY], data[DATA_KEY]

