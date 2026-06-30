from helpers.logger import logger


def handle_graph_error(response):

    if response.status_code in (200, 201, 204):
        return True

    if response.status_code == 400:
        logger.error("Bad Request")

    elif response.status_code == 401:
        logger.error("Authentication Failed")

    elif response.status_code == 403:
        logger.error("Permission Denied")

    elif response.status_code == 404:
        logger.error("User or Event Not Found")

    elif response.status_code == 500:
        logger.error("Microsoft Graph Internal Error")

    else:
        logger.error(f"Unexpected Error: {response.status_code}")

    # Return False instead of raising an exception
    return False