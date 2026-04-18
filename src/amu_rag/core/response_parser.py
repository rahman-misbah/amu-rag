import json
from typing import Dict

from ..config import PROCESSED_DATA_DIR

class ResponseParser:
    @staticmethod
    def parse(response: str) -> Dict:
        processed_response = response.replace("---METADATA---", "").strip().split("---SUMMARY---")

        response_dict = {
            "metadata": json.loads(processed_response[0].strip()),
            "summary": processed_response[1].strip()
        }
        
        return response_dict
    
    @staticmethod
    def parse_file(file_name: str) -> Dict:
        with open(f"{PROCESSED_DATA_DIR}/{file_name}", "r") as f:
            response = f.read()
        
        return ResponseParser.parse(response)