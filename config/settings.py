from dotenv import load_dotenv
import os

# Loading env variables from .env file
load_dotenv()

class Config:
    ES_HOST = os.getenv('ES_URL')
    ES_INDEX = os.getenv('ES_INDEX')