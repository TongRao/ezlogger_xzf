# Exzlogger 
##### *Extremely Easy Logger*

---
This package is made to easily create logger that is suit for most of the situations, including following functions:

- allow user to set log directory
- the log information will be displayed on stdout, and will also be stored in the `.log` file
- allow user to set the information level for both stdout and log file seperately
- nicely formatted log information, including the logger type, source function, timestamp
- provide a good practice to handle errors and its tracebacks

###### New on 0.0.2
- provide a decorator `magic_exception` to handle function exceptions

## Main Logger
### Parameters
- `stdout_level` \<str\>: The log level to be used for stdout ('INFO', 'ERROR', 'DEBUG', or 'WARNING'), Defaults to 'INFO'.
- `file_level` \<str\>: The log level to be used for the log file ('INFO', 'ERROR', 'DEBUG', or 'WARNING'), Defaults to 'DEBUG'.
- `log_file` \<str\>: The path and name of the log file to write the log messages, defaults to 'log/log.log'.

### Returns
- `logger` \<logging.Logger\>: The initialized logger instance.

### Useage
```python
# Imports
from exzlogger import initialize_logger

logger = initialize_logger(stdout_level='INFO', file_level='DEBUG', log_file='logfile.log')

# Error & Debug (suggest to import traceback for debug)
logger.error(f"[func_name]: error message<{e}>")
logger.debug(f"[func_name]: error message<{e}>\n**********\n{traceback.format_exc()}**********")

# Info
logger.info(f"[func_name]: message")

# Warning
logger.warning(f"[func_name]: warning message")
```

## Magic Exception
It is both hard and time consuming to write try-except if you have many functions. The goal of this decorator is to provide a good practice that I use in my real world project to handle function exceptions, with some very cool features:
- able to combine with the logger provide above to access all the features of exzlogger
- provide a very flexible way to format the exception message, the decorator is able to access all the parameters of the decorated function by directly use their variable name
- provide a way to return default result if the function fails, it is useful for handling the error chain, especially for a big project

### parameters
- `logger` \<logging.Logger\>: The logger instance to log the exception messages, use logger provide above to get best of them!
- `msg_format` \<str\>: The format of the message to be logged.
- `except_return` \<any\>: The value to be returned if the decorated function fails.

### Usage
```python
@magic_exception(logger, "[func_name]: error message with input {a}", None)
def func(a):
  # sample function that will fail
  print(a / 0)
```

