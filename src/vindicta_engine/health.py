import time


def check_health() -> dict[str, object]:
    """Returns the health status of the service."""
    return {"status": "ok", "realm": "vindicta-engine", "timestamp": time.time()}
