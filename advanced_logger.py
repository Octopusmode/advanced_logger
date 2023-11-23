# Данный класс позволяет реализовать вывод отладочных сообщений только если они меняются
class AdvancedMessageLogger:
    def __init__(self, logger, console_logger):
        self.logger = logger
        self.console_logger = console_logger
        self.last_message = None
        self.message_counts = {}

    def log(self, method, message):
        if message != self.last_message:
            count = self.message_counts.get(message, 0) + 1
            self.message_counts[message] = count
            method(message + (f' x{count}' if count > 1 else ''))
            self.last_message = message

    def info(self, message):
        self.log(self.logger.info, message)
        self.console_logger.info(message)

    def error(self, message):
        self.log(self.logger.error, message)
        self.console_logger.error(message)

    def debug(self, message):
        self.log(self.logger.debug, message)
        self.console_logger.debug(message)

    def warning(self, message):
        self.log(self.logger.warning, message)
        self.console_logger.warning(message)

    def critical(self, message):
        self.log(self.logger.critical, message)
        self.console_logger.critical(message)

# Path: unifint/tools/unique_message_logger.py

# Пример инициализации и использования:
# import logging
# from unique_message_logger import UniqueMessageLogger
#
# logger = logging.getLogger(__name__)
# console_logger = logging.getLogger('console')
# unique_logger = UniqueMessageLogger(logger, console_logger)
