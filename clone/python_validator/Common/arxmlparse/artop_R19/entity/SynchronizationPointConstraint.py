# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\SynchronizationPointConstraint.py
from .TimingConstraint import TimingConstraint

class SynchronizationPointConstraint(TimingConstraint):

    def __init__(self):
        super().__init__()
        from .EOCExecutableEntityRefGroup import EOCExecutableEntityRefGroup
        from .AbstractEvent import AbstractEvent
        self._artop_sourceEecRef = []
        self._artop_sourceEventRef = []
        self._artop_targetEecRef = []
        self._artop_targetEventRef = []
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({
         '_artop_sourceEecRef': '"EOC-EXECUTABLE-ENTITY-REF-GROUP"', 
         '_artop_sourceEventRef': '"ABSTRACT-EVENT"', 
         '_artop_targetEecRef': '"EOC-EXECUTABLE-ENTITY-REF-GROUP"', 
         '_artop_targetEventRef': '"ABSTRACT-EVENT"'})

    @property
    def ref_sourceEecs_(self):
        return self._artop_sourceEecRef

    @property
    def sourceEecs_(self):
        return self._artop_sourceEecRef

    @property
    def ref_sourceEvents_(self):
        return self._artop_sourceEventRef

    @property
    def sourceEvents_(self):
        return self._artop_sourceEventRef

    @property
    def ref_targetEecs_(self):
        return self._artop_targetEecRef

    @property
    def targetEecs_(self):
        return self._artop_targetEecRef

    @property
    def ref_targetEvents_(self):
        return self._artop_targetEventRef

    @property
    def targetEvents_(self):
        return self._artop_targetEventRef
