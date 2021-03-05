import time
import requests
from zebrok import app
from config import UPSTREAM_URL

@app.Task
def create_todo_item(todo_details):
    time.sleep(2)
    response = requests.post(UPSTREAM_URL, todo_details)
    return response.status_code