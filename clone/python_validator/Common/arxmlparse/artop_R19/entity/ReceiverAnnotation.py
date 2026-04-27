# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\ReceiverAnnotation.py
from .SenderReceiverAnnotation import SenderReceiverAnnotation

class ReceiverAnnotation(SenderReceiverAnnotation):

    def __init__(self):
        super().__init__()
        from .MultidimensionalTime import MultidimensionalTime
        self._artop_signalAge = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({"_artop_signalAge": "MULTIDIMENSIONAL-TIME"})

    @property
    def ref_signalAge_(self):
        return self._artop_signalAge

    @property
    def signalAge_(self):
        if self._artop_signalAge is not None:
            if hasattr(self._artop_signalAge, "uuid"):
                return self._artop_signalAge.uuid
        return
