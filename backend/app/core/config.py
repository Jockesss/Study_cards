from dotenv import load_dotenv
import os

# Define the path to the .env file depending on the environment
ENV_FILE = ".env.local"
load_dotenv(ENV_FILE)


class Setting:
    DATABASE_URL = os.getenv("DATABASE_URL")
