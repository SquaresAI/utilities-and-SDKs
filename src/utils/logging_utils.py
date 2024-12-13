import logging
from logging.handlers import RotatingFileHandler

class LoggingUtils:
    """Utility to configure and manage logging."""

    @staticmethod
    def setup_logger(logger_name, log_file, level=logging.INFO, max_bytes=5*1024*1024, backup_count=5):
        """Sets up a logger with a rotating file handler."""
        logger = logging.getLogger(logger_name)
        logger.setLevel(level)

        # Create handlers
        console_handler = logging.StreamHandler()
        file_handler = RotatingFileHandler(log_file, maxBytes=max_bytes, backupCount=backup_count)

        # Create formatters and add them to the handlers
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        console_handler.setFormatter(formatter)
        file_handler.setFormatter(formatter)

        # Add handlers to the logger
        logger.addHandler(console_handler)
        logger.addHandler(file_handler)

        return logger

# Example usage
if __name__ == "__main__":
    logger = LoggingUtils.setup_logger('SquaresAI', 'app.log')
    logger.info("This is an info message.")
    logger.error("This is an error message.")
