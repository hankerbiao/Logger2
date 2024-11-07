import os
import sys
from loguru import logger
from enum import Enum

class LogLevel(Enum):
    DEBUG = "DEBUG"
    INFO = "INFO"
    ERROR = "ERROR"

class CustomLogger:
    def __init__(self, log_dir="logs", log_level=LogLevel.INFO):
        self.log_dir = log_dir
        self.log_level = log_level
        self._setup_loggers()

    def _setup_loggers(self):
        # 确保日志目录存在
        os.makedirs(self.log_dir, exist_ok=True)

        # 移除所有已存在的处理器
        logger.remove()

        # 设置日志格式
        log_format = "<green>{time:YYYY-MM-DD HH:mm:ss}</green> | <level>{level: <8}</level> | <cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - <level>{message}</level>"

        # 添加控制台输出
        logger.add(sys.stdout, format=log_format, level=self.log_level.value)

        # 配置 DEBUG 级别的日志文件
        if self.log_level.value in [LogLevel.DEBUG.value]:
            logger.add(
                os.path.join(self.log_dir, "debug.log"),
                format=log_format,
                filter=lambda record: record["level"].name == "DEBUG",
                rotation="1 day",
                retention="7 days",
                level="DEBUG",
                enqueue=True,
                encoding="utf-8"
            )

        # 配置 INFO 级别的日志文件
        if self.log_level.value in [LogLevel.DEBUG.value, LogLevel.INFO.value]:
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

        # 配置 ERROR 级别的日志文件
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

    def set_log_level(self, level: LogLevel):
        self.log_level = level
        self._setup_loggers()

    def debug(self, message):
        logger.debug(message)

    def info(self, message):
        logger.info(message)

    def error(self, message):
        logger.error(message)

# 使用示例
custom_logger = CustomLogger(log_level=LogLevel.INFO)

# 记录不同级别的日志
custom_logger.debug("This is a debug message")  # 只会显示在控制台（如果日志级别是 DEBUG）
custom_logger.info("This is an info message")   # 会记录到 info.log 和显示在控制台
custom_logger.error("This is an error message") # 会记录到 error.log 和显示在控制台

print("\nChanging log level to DEBUG\n")

# 更改日志级别
custom_logger.set_log_level(LogLevel.DEBUG)

# 现在 DEBUG 日志也会被记录到文件和控制台
custom_logger.debug("This debug message will be logged now")
custom_logger.info("This info message will still be logged")
custom_logger.error("This error message will be logged as well")