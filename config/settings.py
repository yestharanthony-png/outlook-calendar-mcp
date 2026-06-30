from dotenv import load_dotenv
import os

load_dotenv()

# Microsoft Graph Configuration
TENANT_ID = os.getenv("TENANT_ID")
CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")
GRAPH_BASE_URL = "https://graph.microsoft.com/v1.0"

# Calendar Configuration
TIMEZONE = "India Standard Time"
DEFAULT_DURATION = 60
AVAILABILITY_INTERVAL = 30