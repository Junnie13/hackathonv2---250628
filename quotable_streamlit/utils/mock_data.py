import json
from pathlib import Path

def load_mock_campaigns():
    """
    Load mock campaign performance data from JSON.
    """
    path = Path(__file__).parent.parent / "data" / "mock_campaigns.json"
    with open(path) as f:
        return json.load(f)