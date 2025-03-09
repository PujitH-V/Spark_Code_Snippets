import time,logging,inspect
from datetime import datetime


def retry3(func):
    """
    A custom retry decorator that retries any function for a maximum of 3 times.
    """
    def wrapper(*args, **kwargs):
        attempts = 3
        while attempts > 0:
            try:
                return func(*args, **kwargs)
            except:
                time.sleep(3)
                attempts -= 1
    return wrapper

@retry3
def custom_logger(message, log_mode="DEBUG"):
    """
    A custom logging function for Databricks to print logs with a predefined start,
    logging mode (default is DEBUG), current timestamp, the line number where the log message is being executed, and the log message.

    :param message: The message to log.
    :param log_mode: The mode of logging (e.g., INFO, DEBUG, ERROR). Defaults to DEBUG.
    """

    frame = inspect.currentframe().f_back
    line_number = frame.f_lineno

    # Define the log prefix
    log_prefix = f"{client_name}-{env}"

    # Get the current timestamp
    current_timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Define the log message format
    log_message = f"\n{log_prefix} [{log_mode}] {current_timestamp} [Line NO - {line_number}]: {message}"

    # Print the log message to the console
    print(log_message)

    # Additionally, log to the default logger if needed
    if log_mode.upper() == "INFO":
        logging.info(log_message)
    elif log_mode.upper() == "DEBUG":
        logging.debug(log_message)
    elif log_mode.upper() == "WARNING":
        logging.warning(log_message)
    elif log_mode.upper() == "ERROR":
        logging.error(log_message)
    elif log_mode.upper() == "CRITICAL":
        logging.critical(log_message)
    else:
        logging.debug(log_message)  # Default to debug logging

# Example usage of the custom_logger function
custom_logger("This is a debug message by default.")
custom_logger("This is an informational message.", "INFO")
# custom_logger("An error occurred.", "ERROR")
