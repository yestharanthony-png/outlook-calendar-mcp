import requests

from config.settings import (
    TENANT_ID,
    CLIENT_ID,
    CLIENT_SECRET,
)


class GraphClient:

    def get_access_token(self):

        url = (
            f"https://login.microsoftonline.com/"
            f"{TENANT_ID}/oauth2/v2.0/token"
        )

        payload = {
            "client_id": CLIENT_ID,
            "client_secret": CLIENT_SECRET,
            "scope": "https://graph.microsoft.com/.default",
            "grant_type": "client_credentials"
        }

        response = requests.post(
            url,
            data=payload
        )

        response.raise_for_status()

        return response.json()["access_token"]