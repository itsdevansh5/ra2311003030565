VALID_STACK = ["backend"]
VALID_LEVEL = ["debug", "info", "warn", "error", "fatal"]
VALID_BACKEND_PACKAGE = ["handler", "repository", "route", "service","cache","controller","cron_job","db","domain","auth","config","middleware","utils"]

def validate_log(stack, level, package):
    if stack not in VALID_STACK:
        raise ValueError("Invalid stack")

    if level not in VALID_LEVEL:
        raise ValueError("Invalid level")

    if stack == "backend" and package not in VALID_BACKEND_PACKAGE:
        raise ValueError("Invalid backend package")