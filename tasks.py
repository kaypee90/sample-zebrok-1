import logging
import time
import requests
from zebrok import app
from config import UPSTREAM_URL

logger = logging.getLogger(__name__)

@app.Task
def create_todo_item(todo_details):
    time.sleep(2)
    response = requests.post(UPSTREAM_URL, todo_details)
    logger.info(f"Post request response code: {response.status_code}")
    return response.status_code