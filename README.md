# Ezlogger

This package is made to easily create logger that is suit for most of the situations, including following functions:

- automatically create "log" folder under the work directory
- the log information will be displayed on std, and will also be stored in the .log file
- allow user to set the information level for both stdout and log file

## Parameters:
- `stdout_level` \<str\>: The log level to be used for stdout ('INFO', 'ERROR', 'DEBUG', or 'WARNING'), Defaults to 'INFO'.
- `file_level` \<str\>: The log level to be used for the log file ('INFO', 'ERROR', 'DEBUG', or 'WARNING'), Defaults to 'DEBUG'.
- `log_file` \<str\>: The path and name of the log file to write the log messages, defaults to 'logfile.log'.

## Returns:
- `logger` \<logging.Logger\>: The initialized logger instance.

## Useage:
```python
# Imports
import sys, logging, traceback
from ezlogger_xzf import initialize_logger
from pathlib import Path

logger = initialize_logger(stdout_level='INFO', file_level='DEBUG', log_file='logfile.log')

# Error & Debug (need to import traceback)
logger.error(f"[func_name]: error message<{e}>")
logger.debug(f"[func_name]: error message<{e}>\n**********\n{traceback.format_exc()}**********")

# Info
logger.info(f"[func_name]: message")

# Warning
logger.warning(f"[func_name]: warning message")
```

