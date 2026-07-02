import requests

from graph_client import GraphClient
from helpers.error_handler import handle_graph_error
from helpers.logger import logger


class GraphService:
    """
    Handles all HTTP communication with Microsoft Graph.
    """

    def __init__(self):
        token = GraphClient().get_access_token()

        self.headers = {
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json"
        }

    # ----------------------------------
    # GET
    # ----------------------------------

    def get(self, url: str):

        logger.info(f"GET -> {url}")

        print("Listing URL:", url)

        response = requests.get(
        url,
        headers=self.headers
    )

        print("\n========== GET REQUEST ==========")
        print("URL:", url)
        print("Status Code:", response.status_code)
        print("Response:", response.text)
        print("=================================\n")

        if not handle_graph_error(response):
            return {
                "status_code": response.status_code,
                "error": response.text
            }

        return response.json()

    # ----------------------------------
    # POST
    # ----------------------------------

    def post(self, url: str, body: dict):

        logger.info(f"POST -> {url}")

        response = requests.post(
            url,
            headers=self.headers,
            json=body
        )

        print("\n========== POST REQUEST ==========")
        print("URL:", url)
        print("Status Code:", response.status_code)
        print("Response:", response.text)
        print("==================================\n")

        if not handle_graph_error(response):
            return {
                "status_code": response.status_code,
                "error": response.text
            }

        if response.text:
            return response.json()

        return {
            "status_code": response.status_code,
            "message": "Success"
        }

    # ----------------------------------
    # PATCH
    # ----------------------------------

    def patch(self, url: str, body: dict):

        logger.info(f"PATCH -> {url}")

        response = requests.patch(
            url,
            headers=self.headers,
            json=body
        )

        print("\n========== PATCH REQUEST ==========")
        print("URL:", url)
        print("Status Code:", response.status_code)
        print("Response:", response.text)
        print("===================================\n")

        if not handle_graph_error(response):
            return {
                "status_code": response.status_code,
                "error": response.text
            }

        if response.text:
            return response.json()

        return {
            "status_code": response.status_code,
            "message": "Event updated successfully."
        }

    # ----------------------------------
    # DELETE
    # ----------------------------------

    def delete(self, url: str):

        logger.info(f"DELETE -> {url}")

        response = requests.delete(
            url,
            headers=self.headers
        )

        print("\n========== DELETE REQUEST ==========")
        print("URL:", url)
        print("Status Code:", response.status_code)
        print("Response:", response.text)
        print("====================================\n")

        if not handle_graph_error(response):
            return {
                "status_code": response.status_code,
                "error": response.text
            }

        return {
            "status_code": response.status_code,
            "message": "Event deleted successfully."
        }