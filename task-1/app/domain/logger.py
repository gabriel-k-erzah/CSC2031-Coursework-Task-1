import logging, time
from flask import current_app, request

#-------------------------------------- logger function ----------------------------------------------------------------
def log_event(level, message, **context):
    """logger for security events.
    level: 'info' or 'warning'
    message: short description of the event
    context: extra data (username, email, etc.)
    """
    # use Flask's logger if available, else default Python logger
    logger = current_app.logger if current_app else logging.getLogger(__name__)
    # get client IP if possible
    ip = request.remote_addr if request else "N/A"
    # build context string
    details = " | ".join(f"{k}={v}" for k, v in context.items())
    # final log entry
    entry = f"ip={ip} | {message} | {details}"
    # log at correct level
    if level.lower() == "warning":
        logger.warning(entry)
    else:
        logger.info(entry)

#-----------------------------------------------------------------------------------------------------------------------
