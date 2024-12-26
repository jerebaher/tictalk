from dotenv import load_dotenv
import os

load_dotenv(override=True)

STATSIG_API_KEY = os.getenv("STATSIG_API_KEY")
DATABASE_URL = os.getenv("DATABASE_URL")