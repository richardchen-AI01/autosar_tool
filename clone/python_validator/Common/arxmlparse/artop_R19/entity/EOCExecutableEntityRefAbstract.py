# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\EOCExecutableEntityRefAbstract.py
from .Identifiable import Identifiable

class EOCExecutableEntityRefAbstract(Identifiable):

    def __init__(self):
        super().__init__()
        from .ExecutionOrderConstraint import ExecutionOrderConstraint
        self._artop_executionOrderConstraint = None
        self._artop_directSuccessorRef = []
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_executionOrderConstraint':"EXECUTION-ORDER-CONSTRAINT", 
         '_artop_directSuccessorRef':"EOC-EXECUTABLE-ENTITY-REF-ABSTRACT"})

    @property
    def ref_executionOrderConstraint_(self):
        return self._artop_executionOrderConstraint

    @property
    def executionOrderConstraint_(self):
        if self._artop_executionOrderConstraint is not None:
            if hasattr(self._artop_executionOrderConstraint, "uuid"):
                return self._artop_executionOrderConstraint.uuid
        return

    @property
    def ref_directSuccessors_(self):
        return self._artop_directSuccessorRef

    @property
    def directSuccessors_(self):
        return self._artop_directSuccessorRef
