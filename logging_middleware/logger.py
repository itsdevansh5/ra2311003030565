from .validator import validate_log
from .client import send_log

def Log(stack, level, package, message):
    try:
        validate_log(stack, level, package)

        payload = {
            "stack": stack,
            "level": level,
            "package": package,
            "message": message
        }

        send_log(payload)

    except:
        pass