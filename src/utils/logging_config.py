import logging
from config.settings import LOG_LEVEL, LOG_FORMAT

def setup_logging():
    """Configure logging for the application."""
    # Set the log level based on the configuration
    log_level = getattr(logging, LOG_LEVEL, logging.INFO)
    
    # Configure the root logger
    logging.basicConfig(
        format=LOG_FORMAT,
        level=log_level
    )
    
    # Set higher logging level for httpx to avoid all GET and POST requests being logged
    logging.getLogger("httpx").setLevel(logging.WARNING)
    
    # Return the logger for the main module
    return logging.getLogger(__name__)