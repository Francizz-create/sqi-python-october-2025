import requests

def fetch_user_data():
    """Fetches user names from JSONPlaceholder API."""
    url = "https://jsonplaceholder.typicode.com/users"
    response = requests.get(url)
    response.raise_for_status() 
    users = response.json()
    return [user["name"] for user in users]