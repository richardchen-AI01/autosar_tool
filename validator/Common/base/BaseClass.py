# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\base\BaseClass.py
import Common.ArxmlValidator as ArxmlValidator

class BaseRule:

    def __init__(self):
        super().__init__()

    def getMessage(self, ruleId, *args) -> str:
        message = (ArxmlValidator.dict_message.get(ruleId)["message"].format)(*args)
        return message
