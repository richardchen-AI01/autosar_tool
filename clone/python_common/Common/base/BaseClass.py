"""BaseClass — V25.10 Common/base/BaseClass.py (validator side).

Reverse-engineered from `autosar-cfg/ORIENTAISBswVal.exe/pyz_source/Common/base/BaseClass.py`:

```python
import Common.ArxmlValidator as ArxmlValidator

class BaseRule:
    def __init__(self):
        super().__init__()

    def getMessage(self, ruleId, *args) -> str:
        message = (ArxmlValidator.dict_message.get(ruleId)["message"].format)(*args)
        return message
```

This is the base for every <Module>Rules.py — used as `class RuleBSWMemIfR23(BaseRule)`.
"""
from typing import Any


class BaseRule:
    """Base class for ECUC validation rule classes."""

    def __init__(self) -> None:
        super().__init__()

    def getMessage(self, ruleId: str, *args: Any) -> str:
        from Common import ArxmlValidator
        rec = ArxmlValidator.dict_message.get(ruleId)
        if rec is None:
            return f'<missing rule: {ruleId}>'
        return rec['message'].format(*args)
