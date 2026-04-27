# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\PerformanceMonitor.py
import time
from Common import logger
from Common.Utils import singletonFunc

@singletonFunc
class PerformanceMonitor:
    _PerformanceMonitor__timelist = dict()

    def __init__(self) -> None:
        return

    def start(self, name, namespace='') -> None:
        self._PerformanceMonitor__timelist[name] = {}
        self._PerformanceMonitor__timelist[name]["Start"] = time.time()
        if namespace:
            self._PerformanceMonitor__timelist[name]["Namespace"] = namespace

    def stop(self, name) -> None:
        self._PerformanceMonitor__timelist[name]["Stop"] = time.time()

    def stop_print_msg(self, name, msg: str='') -> None:
        self._PerformanceMonitor__timelist[name]["Stop"] = time.time()
        logger.info(msg + ", time consumed: " + self.getElapsed(name))

    def deleteTimer(self, name):
        if name in self._PerformanceMonitor__timelist:
            try:
                del self._PerformanceMonitor__timelist[name]["Start"]
                del self._PerformanceMonitor__timelist[name]["Stop"]
                del self._PerformanceMonitor__timelist[name]
            except:
                logger.error("Except about delete PM.Timer('%s')" % name)

    def getElapsed(self, name) -> str:
        elapsed = self._PerformanceMonitor__timelist[name]["Stop"] - self._PerformanceMonitor__timelist[name]["Start"]
        elapsed = "{:.3f}".format(elapsed)
        if "Namespace" not in self._PerformanceMonitor__timelist[name]:
            self.deleteTimer(name)
        return str(elapsed) + "(s)"

    def getNamespaceElapsed(self, namespace) -> str:
        elapsed = 0
        if namespace:
            for name in list(self._PerformanceMonitor__timelist.keys()):
                if "Start" in self._PerformanceMonitor__timelist[name] and "Stop" in self._PerformanceMonitor__timelist[name] and "Namespace" in self._PerformanceMonitor__timelist[name] and self._PerformanceMonitor__timelist[name]["Namespace"] == namespace:
                    elapsed += self._PerformanceMonitor__timelist[name]["Stop"] - self._PerformanceMonitor__timelist[name]["Start"]
                    self.deleteTimer(name)

        elapsed = "{:.3f}".format(elapsed)
        return str(elapsed) + "(s)"


PM = PerformanceMonitor()
