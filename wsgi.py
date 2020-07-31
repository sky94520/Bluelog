from dotenv import load_dotenv, find_dotenv
from bluelog import create_app

load_dotenv(find_dotenv('.flaskenv'), override=True)
load_dotenv(find_dotenv('.env'), override=True)

app = create_app()
