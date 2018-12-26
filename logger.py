"""
This module is used to provide simple warper for logging module
"""

import logging
import inspect

class Logger(object):
    """
   
    """
    logger_instance = None
    DEBUG = logging.DEBUG
    INFO = logging.INFO
    WARNING = logging.WARNING
    ERROR = logging.ERROR
    CRITICAL = logging.CRITICAL


    def __init__(self):
        """
        
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
            function_name = inspect.stack()[1][3]
        except IndexError:
            function_name = "None"
        Logger.logger_instance.log(level,"{} | {}".format(function_name,message))

    def debug(message):
        self.log(Logger.DEBUG,message)

    def info(message):
        self.log(Logger.INFO,message)

    def warning(message):
        self.log(Logger.WARNING,message)

    def error(message):
        self.log(Logger.ERROR,message)

    def critical(message):
        self.log(Logger.CRITICAL,message)


