import json
import socket
import time
from typing import Any

from healthcheck import HealthCheck

Result = dict[str, Any]


def check_service() -> tuple[bool, str]:
    return True, "Service ok"


def success_handler(results: list[Result]) -> str:
    return json.dumps(
        {
            "hostname": socket.gethostname(),
            "message": "success",
            "healthy": True,
            "timestamp": time.time(),
            "results": results,
        }
    )


def failure_handler(results: list[Result]) -> str:
    return json.dumps(
        {
            "hostname": socket.gethostname(),
            "message": "failure",
            "healthy": False,
            "timestamp": time.time(),
            "results": results,
        }
    )


health_check = HealthCheck(success_handler=success_handler, failure_handler=failure_handler)

health_check.add_check(check_service)
