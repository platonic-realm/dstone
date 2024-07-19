"""
Logging Module for DStone API

This module provides a flexible and extensible logging system for the DStone application
and its plugins. It offers functionality to configure logging for the main application
and individual plugins, allowing for centralized logging as well as plugin-specific logs.

Key Features:
- Configurable main logger with options for file and stdout logging
- Support for additional custom logging handlers
- Plugin-specific logging that integrates with the main logging system
- Flexible log level management
- Prevention of duplicate log entries

Usage:
1. Configure the main application logger:
   main_logger = configure_main_logger('INFO', 'app.log', log_to_stdout=True)

2. Create loggers for plugins:
   plugin_logger = get_plugin_logger('MyPlugin', 'plugin.log')

3. Use loggers in your application and plugins:
   main_logger.info("Application message")
   plugin_logger.info("Plugin-specific message")

Note:
The logging system uses Python's built-in logging module and leverages its hierarchical
nature. Plugin loggers inherit settings from the main logger, ensuring consistency
while allowing for plugin-specific customizations.

For advanced use cases, such as distributed systems or custom logging requirements,
additional handlers can be added to the main logger configuration.
"""

# Python Imports
import logging
import sys
from typing import Optional, List


def configure_main_logger(
    log_level: str,
    log_file: Optional[str] = None,
    log_to_stdout: bool = True,
    additional_handlers: List[logging.Handler] = None
) -> None:
    """
    Configure and get the main logger for the application.

    This function sets up logging handlers based on the provided parameters.
    It can log to a file, to stdout, or both, and allows for additional custom handlers.

    Args:
        log_level (str): The logging level (e.g., 'INFO', 'DEBUG', 'WARNING').
        log_file (Optional[str]): The path to the log file. If None, file logging is disabled.
        log_to_stdout (bool): Whether to log to standard output.
        additional_handlers (List[logging.Handler]): Additional logging handlers to add.

    Returns:
        logging.Logger: The configured logger object.

    Raises:
        ValueError: If an invalid log level is provided.
    """
    # Validate and set the log level
    numeric_level = getattr(logging, log_level.upper(), None)
    if not isinstance(numeric_level, int):
        raise ValueError(f"Invalid log level: {log_level}")

    # Get the root logger
    logger = logging.getLogger()

    # Remove all existing handlers to prevent duplicate logging
    for handler in logger.handlers[:]:
        logger.removeHandler(handler)

    # Set the log level
    logger.setLevel(numeric_level)

    # Create formatter
    formatter = logging.Formatter("%(asctime)s [%(levelname)s] %(name)s: %(message)s")

    # Configure file logging if a log file is provided
    if log_file is not None:
        file_handler = logging.FileHandler(log_file)
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

    # Configure stdout logging if enabled
    if log_to_stdout:
        stream_handler = logging.StreamHandler(sys.stdout)
        stream_handler.setFormatter(formatter)
        logger.addHandler(stream_handler)

    # Add any additional handlers
    if additional_handlers:
        for handler in additional_handlers:
            if handler not in logger.handlers:
                handler.setFormatter(formatter)
                logger.addHandler(handler)

    # Log the configured log level
    logger.info(f"Main logger configured with level: {log_level}")


def get_plugin_logger(plugin_name: str, log_file: Optional[str] = None) -> logging.Logger:
    """
    Create a logger for a specific plugin.

    This function creates a logger that will log to both the main application log
    and a plugin-specific log file if specified.

    Args:
        plugin_name (str): The name of the plugin.
        log_file (Optional[str]): The path to the plugin-specific log file. If None, only logs to the main log.

    Returns:
        logging.Logger: The configured logger for the plugin.
    """
    logger = logging.getLogger(plugin_name)

    if log_file:
        file_handler = logging.FileHandler(log_file)
        formatter = logging.Formatter("%(asctime)s [%(levelname)s] %(name)s: %(message)s")
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

    logger.info("Plugin logger configured")

    return logger
