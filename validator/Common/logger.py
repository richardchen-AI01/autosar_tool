# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\logger.py
import sys
from Common import Constant
from Common.ArgParser import RunArgParser
from loguru import logger as loggerPro
log_counts = {
 'DEBUG': 0, 
 'INFO': 0, 
 'WARNING': 0, 
 'ERROR': 0, 
 'CRITICAL': 0}

def count_logs(message):
    level = message.record["level"].name
    if level in log_counts:
        log_counts[level] += 1


def countShow():
    loggerPro.info(f"Log counts: {log_counts}")


def debug(txt):
    loggerPro.debug(txt)


def info(txt):
    loggerPro.info(txt)


def warning(txt):
    loggerPro.warning(txt)


def error(txt):
    loggerPro.error(txt)


def critical(txt):
    loggerPro.critical(txt)


def setupLogger():
    level_value = "DEBUG" if RunArgParser.isDebugMode else "INFO"
    loggerPro.configure(handlers=[
     {'sink':sys.stderr, 
      'format':"<green>{time:YYYY/MM/DD HH:mm:ss}</green>|<lvl>{level: <8}</>|<lvl>{message}</>", 
      'level':level_value},
     {'sink':Constant.LOG_FILE, 
      'mode':"w", 
      'format':"{time:YYYY/MM/DD HH:mm:ss}|{level: <8}|{message}", 
      'level':level_value}])
    loggerPro.add(count_logs)
