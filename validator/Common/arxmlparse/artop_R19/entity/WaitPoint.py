# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\WaitPoint.py
from .Identifiable import Identifiable

class WaitPoint(Identifiable):

    def __init__(self):
        super().__init__()
        from .RunnableEntity import RunnableEntity
        from .RTEEvent import RTEEvent
        self._artop_timeout = None
        self._artop_runnableEntity = None
        self._artop_triggerRef = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_runnableEntity':"RUNNABLE-ENTITY", 
         '_artop_triggerRef':"RTE-EVENT"})

    @property
    def timeout_(self):
        return self._artop_timeout

    @property
    def ref_runnableEntity_(self):
        return self._artop_runnableEntity

    @property
    def runnableEntity_(self):
        if self._artop_runnableEntity is not None:
            if hasattr(self._artop_runnableEntity, "uuid"):
                return self._artop_runnableEntity.uuid
        return

    @property
    def ref_trigger_(self):
        return self._artop_triggerRef

    @property
    def trigger_(self):
        if self._artop_triggerRef is not None:
            if hasattr(self._artop_triggerRef, "uuid"):
                return self._artop_triggerRef.uuid
        return
