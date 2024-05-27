import os
import time

from loguru import logger

LOG_FORMAT = (
    "<green>{time:YYYY-MM-DD HH:mm:ss.SSS}</green> | "
    "<level>{level: <8}</level> | "
    "<cyan>{process.name}</cyan>:<cyan>{process.id}</cyan> | "
    "<cyan>{thread.name}</cyan>:<cyan>{thread.id}</cyan> | "
    "<yellow>{file.path}:{line}</yellow> | "
    "{message}"
)
today = time.strftime("%Y%m%d")  # 日志保存日期格式
compression = "zip"  # 压缩格式
encoding = "utf8"  # 日志格式
rotation = "50MB"  # 50MB后自动压缩 
retention = "1 day"  # 日志保存天数

class Logger():
    __instance = None

    def __new__(cls, *args, **kwargs):
        if not cls.__instance:
            cls.__instance = super(Logger, cls).__new__(cls, *args, **kwargs)
        return cls.__instance

    def __init__(self, log_path='./logs', log_level="DEBUG"):
        self.__log_level = log_level
        self.__log_path = log_path  # 设置日志路径
        self._init_log()

    def _init_log(self):
        os.makedirs(self.__log_path, exist_ok=True)
        levels = ['info', 'debug', 'warning', 'error', 'critical']
        for level in levels:
            logger.add(
                os.path.join(self.__log_path, f"{level}_{today}.log"),
                filter=lambda record: record["extra"]["name"] == level,
                compression=compression,
                level=level.upper(),
                enqueue=True,
                format=LOG_FORMAT,
                rotation=rotation,
                encoding=encoding,
                retention=retention  # 日志保存天数
            )

            setattr(self, level, logger.bind(name=level))

    def infoLog(self, log):
        self.info.info(log)

    def debugLog(self, log):
        self.debug.debug(log)

    def warningLog(self, log):
        self.warning.warning(log)

    def errorLog(self, log):
        self.error.error(log)

    def criticalLog(self, log):
        self.critical.critical(log)


if __name__ == '__main__':
    log2 = Logger()
    log2.infoLog("hello world")
    log2.debugLog("hello world")
    log2.warningLog("hello world")
    log2.errorLog("hello world")
    log2.criticalLog("hello world")
