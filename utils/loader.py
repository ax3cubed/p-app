import json

def load_data(file):
    """Load JSON data from the uploaded file."""
    return json.load(file)
