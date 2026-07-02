from helpers.logger import logger


def handle_graph_error(response):

    if response.status_code in (200, 201, 204):
        return True

    logger.error(f"Status Code: {response.status_code}")
    logger.error(f"Response Body: {response.text}")

    return False