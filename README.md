# 日志记录模块，开箱即用

该模块提供了一个用于日志记录的Logger类,基于loguru二次开发，可以很方便地将不同级别的日志记录到不同的日志文件中。将Logger.py复制到工程下可直接使用。

## 特性

- 使用Loguru库实现高性能日志记录
- 支持将不同级别的日志记录到不同文件(info.log, debug.log, warning.log, error.log, critical.log)
- 支持日志文件的自动轮转和压缩
- 日志格式富有信息,包括时间、级别、进程ID、线程ID、文件路径和行号等
- 使用单例模式,确保全局只有一个Logger实例

## 用法

1. 导入Logger类
2. 创建Logger实例,可以指定日志路径和日志级别
3. 使用Logger实例的infoLog、debugLog、warningLog、errorLog和criticalLog方法记录相应级别的日志

```python
from logger import Logger

# 创建Logger实例,日志路径为./logs,日志级别为DEBUG
log = Logger(log_path='./logs', log_level='DEBUG')

# 记录INFO级别日志
log.infoLog('This is an info log')

# 记录DEBUG级别日志 
log.debugLog('This is a debug log')
```

## 配置

你可以通过修改以下变量来自定义日志配置:

- `LOG_FORMAT`: 日志格式字符串
- `today`: 日期字符串,用于生成日志文件名
- `compression`: 日志文件压缩格式,默认为zip
- `encoding`: 日志文件编码,默认为utf8
- `rotation`: 日志文件轮转大小,默认为50MB

```python
# 例如,修改日志格式为:
# 2023-05-16 10:20:30.456 | INFO     | main:123 | helper.py:10 | This is a log message
LOG_FORMAT = "<green>{time:YYYY-MM-DD HH:mm:ss.SSS}</green> | <level>{level: <8}</level> | <cyan>{process.name}:{process.id}</cyan> | <yellow>{file.path}:{line}</yellow> | {message}"
```

## 注意事项

- 该模块使用单例模式,全局只有一个Logger实例,多次创建会返回同一个实例
- 日志文件默认保存在./logs目录下,如果不存在会自动创建该目录
- 日志级别从低到高为: DEBUG < INFO < WARNING < ERROR < CRITICAL



# Installation

需要安装依赖loguru

```bash
pip install loguru
```

[GitHub - Delgan/loguru: Python logging made (stupidly) simple](https://github.com/Delgan/loguru)
