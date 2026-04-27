# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\ProcessorCore.py
from .Identifiable import Identifiable

class ProcessorCore(Identifiable):

    def __init__(self):
        super().__init__()
        from .Processor import Processor
        self._artop_coreId = None
        self._artop_processor = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({"_artop_processor": "PROCESSOR"})

    @property
    def coreId_(self):
        return self._artop_coreId

    @property
    def ref_processor_(self):
        return self._artop_processor

    @property
    def processor_(self):
        if self._artop_processor is not None:
            if hasattr(self._artop_processor, "uuid"):
                return self._artop_processor.uuid
        return
