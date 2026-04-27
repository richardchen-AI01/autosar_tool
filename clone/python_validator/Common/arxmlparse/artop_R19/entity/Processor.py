# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\Processor.py
from .Identifiable import Identifiable

class Processor(Identifiable):

    def __init__(self):
        super().__init__()
        from .Machine import Machine
        from .ProcessorCore import ProcessorCore
        self._artop_machine = None
        self._artop_core = []
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_machine':"MACHINE", 
         '_artop_core':"PROCESSOR-CORE"})

    @property
    def ref_machine_(self):
        return self._artop_machine

    @property
    def machine_(self):
        if self._artop_machine is not None:
            if hasattr(self._artop_machine, "uuid"):
                return self._artop_machine.uuid
        return

    @property
    def cores_ProcessorCore(self):
        return self._artop_core
