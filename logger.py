"""
This module is used to provide simple warper for logging module
"""

import logging
import inspect

class Logger(object):
    """
    The warper class for logging module.
    
    Attributes:
        CRITICAL: Logging level.
        DEBUG: Logging level.
        ERROR: Logging level.
        INFO: Logging level.
        logger_instance: Logger instance.
        WARNING: Logging level.
    """
    
    logger_instance = None
    DEBUG = logging.DEBUG
    INFO = logging.INFO
    WARNING = logging.WARNING
    ERROR = logging.ERROR
    CRITICAL = logging.CRITICAL


    def __init__(self):
        """
        Singleton design.
        """
        if not Logger.logger_instance:
            logger = logging.getLogger()
            handler = logging.StreamHandler()
            formatter = logging.Formatter(
                    '[%(asctime)s] %(levelname)s | %(message)s') 
            handler.setFormatter(formatter)
            logger.addHandler(handler)
            logger.setLevel(logging.DEBUG)
            Logger.logger_instance = logger

    def log(self,level, message):
        """
        The function that logs massage
        
        Args:
            level (level): Level of the message, i.e.`Logger.DEBUG`
            message (String): message
        """
        try:
            function_name = inspect.stack(1)[1][3]
        except IndexError:
            function_name = "None"
        Logger.logger_instance.log(level,"{} | {}".format(function_name,message))

    def debug(self,message):
        self.log(Logger.DEBUG,message)

    def info(self,message):
        self.log(Logger.INFO,message)

    def warning(self,message):
        self.log(Logger.WARNING,message)

    def error(self,message):
        self.log(Logger.ERROR,message)

    def critical(self,message):
        self.log(Logger.CRITICAL,message)


