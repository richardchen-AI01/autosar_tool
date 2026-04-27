# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\DiagnosticSession.py
from .DiagnosticCommonElement import DiagnosticCommonElement

class DiagnosticSession(DiagnosticCommonElement):

    def __init__(self):
        super().__init__()
        self._artop_id = None
        self._artop_jumpToBootLoader = None
        self._artop_p2ServerMax = None
        self._artop_p2StarServerMax = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}

    @property
    def id_(self):
        return self._artop_id

    @property
    def jumpToBootLoader_(self):
        return self._artop_jumpToBootLoader

    @property
    def p2ServerMax_(self):
        return self._artop_p2ServerMax

    @property
    def p2StarServerMax_(self):
        return self._artop_p2StarServerMax
