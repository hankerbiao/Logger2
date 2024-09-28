import os
from loguru import logger


class CustomLogger:
    def __init__(self, log_dir="logs"):
        self.log_dir = log_dir
        self._setup_loggers()

    def _setup_loggers(self):
        # 确保日志目录存在
        os.makedirs(self.log_dir, exist_ok=True)

        # 移除默认的 logger
        logger.remove()

        # 设置日志格式
        log_format = "<green>{time:YYYY-MM-DD HH:mm:ss}</green> | <level>{level: <8}</level> | <cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - <level>{message}</level>"

        # 配置 INFO 级别的日志
        logger.add(
            os.path.join(self.log_dir, "info.log"),
            format=log_format,
            filter=lambda record: record["level"].name == "INFO",
            rotation="1 day",
            retention="7 days",
            level="INFO",
            enqueue=True,
            encoding="utf-8"
        )

        # 配置 ERROR 级别的日志
        logger.add(
            os.path.join(self.log_dir, "error.log"),
            format=log_format,
            filter=lambda record: record["level"].name == "ERROR",
            rotation="1 day",
            retention="7 days",
            level="ERROR",
            enqueue=True,
            encoding="utf-8"
        )

    def info(self, message):
        logger.info(message)

    def error(self, message):
        logger.error(message)

custom_logger = CustomLogger()
