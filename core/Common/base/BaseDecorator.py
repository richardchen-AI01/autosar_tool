"""BaseDecorator — V25.10 Common/base/BaseDecorator.py (validator side).

Reverse-engineered from validator's pyz_source. Provides @RuleHandler decorator
used in <Module>Rules.py:

    @RuleHandler()
    def Rule_BSW_MemIf_TCPP_2170(self) -> list:
        ...

Decorated functions are auto-registered: when invoked they look up their own
name in ArxmlValidator.dict_message, return list of (uri, args, [], container)
tuples that the framework turns into Problem markers.

D1 STATUS: simplified single-pass version — no time-tracking/easy-mode flags.
M2 will add the missing bells.
"""
from __future__ import annotations
import functools
import time
from typing import Any, Callable


def RuleHandler(isPrintTime: bool = False, isEasyModel: bool = False) -> Callable:
    """Decorator factory. Returned wrapper:
      1. Looks up rule metadata in ArxmlValidator.dict_message via function name
      2. Skips if rule is inactive
      3. Calls the actual rule function
      4. (M2) feeds result tuples into validator output infrastructure
    """
    def decorator(func: Callable[..., Any]) -> Callable[..., Any]:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            from Common import ArxmlValidator
            funcName = func.__name__
            data_msg = ArxmlValidator.dict_message.get(funcName)
            if data_msg is None or not data_msg.get('active', False):
                return None
            t0 = time.time()
            result = func(*args, **kwargs)
            if isPrintTime:
                print(f'  [{funcName}] {time.time()-t0:.3f}s')
            return result
        return wrapper
    return decorator
