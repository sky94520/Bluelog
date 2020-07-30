from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv(), override=True)

from bluelog import create_app
app = create_app()
