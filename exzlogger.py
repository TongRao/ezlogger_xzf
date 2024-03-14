import logging, sys
from pathlib import Path


def initialize_logger(stdout_level='INFO', file_level='DEBUG', log_file='log.log'):
    """
    Initialize a custom logger that logs messages to both stdout and a file,
    with the specified format "LEVEL  current_datetime message".

    Parameters:
        - stdout_level <str>: The log level to be used for stdout ('INFO', 'ERROR', 'DEBUG', or 'WARNING'). Defaults to 'INFO'.
        - file_level <str>: The log level to be used for the log file ('INFO', 'ERROR', 'DEBUG', or 'WARNING'). Defaults to 'DEBUG'.
        - log_file <str>: The path and name of the log file to write the log messages. Defaults to 'log.log'.

    Returns:
        - logger <logging.Logger>: The initialized logger instance.

    Examples:
        - Error & Debug (import traceback)
            - logger.error(f"[func_name]: error message<{e}>")
            - logger.debug(f"[func_name]: error message<{e}>\n**********\n{traceback.format_exc()}**********")

        - Info
            - logger.info(f"[func_name]: message")

        - Warning
            - logger.warning(f"[func_name]: warning message")

    Dependencies:
        import sys, logging, traceback
        from pathlib import Path

    Initialization:
        logger = initialize_logger(stdout_level='INFO', file_level='DEBUG', log_file='log/log.log')
    """
    # create log folder
    Path('log').mkdir(exist_ok=True)

    log_levels = {
        'INFO': logging.INFO,
        'ERROR': logging.ERROR,
        'DEBUG': logging.DEBUG,
        'WARNING': logging.WARNING
    }

    stdout_log_level = log_levels.get(stdout_level.upper(), logging.INFO)
    file_log_level = log_levels.get(file_level.upper(), logging.DEBUG)

    # Set up the logger
    logger = logging.getLogger('tripAnalysis')
    logger.setLevel(logging.DEBUG)  # Set to the lowest level (DEBUG) to handle all log levels

    # Prevent log messages from propagating to other loggers
    logger.propagate = False

    # Check if the logger already has handlers
    if not logger.handlers:
        # Remove any existing handlers
        logger.handlers = []

        # Create a custom log format
        log_format = logging.Formatter("%(levelname)-7s  [%(asctime)s] %(message)s", datefmt="%Y-%m-%d %H:%M:%S")

        # Add stdout handler
        stdout_handler = logging.StreamHandler(sys.stdout)
        stdout_handler.setFormatter(log_format)
        stdout_handler.setLevel(stdout_log_level)  # Set stdout handler log level
        logger.addHandler(stdout_handler)

        # Add file handler
        file_handler = logging.FileHandler(log_file)
        file_handler.setFormatter(log_format)
        file_handler.setLevel(file_log_level)  # Set file handler log level
        logger.addHandler(file_handler)
    return logger
