# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\ExecutionOrderConstraint.py
from .TimingConstraint import TimingConstraint

class ExecutionOrderConstraint(TimingConstraint):

    def __init__(self):
        super().__init__()
        from .CompositionSwComponentType import CompositionSwComponentType
        from .EOCExecutableEntityRefAbstract import EOCExecutableEntityRefAbstract
        self._artop_executionOrderConstraintType = None
        self._artop_ignoreOrderAllowed = None
        self._artop_isEvent = None
        self._artop_permitMultipleReferencesToEe = None
        self._artop_baseCompositionRef = None
        self._artop_orderedElement = []
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_baseCompositionRef':"COMPOSITION-SW-COMPONENT-TYPE", 
         '_artop_orderedElement':"EOC-EXECUTABLE-ENTITY-REF-ABSTRACT"})

    @property
    def executionOrderConstraintType_(self):
        return self._artop_executionOrderConstraintType

    @property
    def ignoreOrderAllowed_(self):
        if self._artop_ignoreOrderAllowed:
            if self._artop_ignoreOrderAllowed == "true":
                return True
            return False
        else:
            return self._artop_ignoreOrderAllowed

    @property
    def isEvent_(self):
        if self._artop_isEvent:
            if self._artop_isEvent == "true":
                return True
            return False
        else:
            return self._artop_isEvent

    @property
    def permitMultipleReferencesToEe_(self):
        if self._artop_permitMultipleReferencesToEe:
            if self._artop_permitMultipleReferencesToEe == "true":
                return True
            return False
        else:
            return self._artop_permitMultipleReferencesToEe

    @property
    def ref_baseComposition_(self):
        return self._artop_baseCompositionRef

    @property
    def baseComposition_(self):
        if self._artop_baseCompositionRef is not None:
            if hasattr(self._artop_baseCompositionRef, "uuid"):
                return self._artop_baseCompositionRef.uuid
        return

    @property
    def orderedElements_EOCExecutableEntityRefAbstract(self):
        return self._artop_orderedElement
