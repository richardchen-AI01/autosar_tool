# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\ExecutableEntityActivationReason.py
from .ImplementationProps import ImplementationProps

class ExecutableEntityActivationReason(ImplementationProps):

    def __init__(self):
        super().__init__()
        from .ExecutableEntity import ExecutableEntity
        self._artop_bitPosition = None
        self._artop_executableEntity = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({"_artop_executableEntity": "EXECUTABLE-ENTITY"})

    @property
    def bitPosition_(self):
        return self._artop_bitPosition

    @property
    def ref_executableEntity_(self):
        return self._artop_executableEntity

    @property
    def executableEntity_(self):
        if self._artop_executableEntity is not None:
            if hasattr(self._artop_executableEntity, "uuid"):
                return self._artop_executableEntity.uuid
        return
