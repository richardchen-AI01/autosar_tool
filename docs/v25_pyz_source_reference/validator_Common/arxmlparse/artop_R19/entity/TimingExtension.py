# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\TimingExtension.py
from .ARElement import ARElement

class TimingExtension(ARElement):

    def __init__(self):
        super().__init__()
        from .TimingCondition import TimingCondition
        from .TimingDescription import TimingDescription
        from .TimingConstraint import TimingConstraint
        from .TimingExtensionResource import TimingExtensionResource
        self._artop_timingCondition = []
        self._artop_timingDescription = []
        self._artop_timingGuarantee = []
        self._artop_timingRequirement = []
        self._artop_timingResource = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({
         '_artop_timingCondition': '"TIMING-CONDITION"', 
         '_artop_timingDescription': '"TIMING-DESCRIPTION"', 
         '_artop_timingGuarantee': '"TIMING-CONSTRAINT"', 
         '_artop_timingRequirement': '"TIMING-CONSTRAINT"', 
         '_artop_timingResource': '"TIMING-EXTENSION-RESOURCE"'})

    @property
    def timingConditions_TimingCondition(self):
        return self._artop_timingCondition

    @property
    def timingDescriptions_TimingDescription(self):
        return self._artop_timingDescription

    @property
    def timingGuarantees_TimingConstraint(self):
        return self._artop_timingGuarantee

    @property
    def timingRequirements_TimingConstraint(self):
        return self._artop_timingRequirement

    @property
    def ref_timingResource_(self):
        return self._artop_timingResource

    @property
    def timingResource_(self):
        if self._artop_timingResource is not None:
            if hasattr(self._artop_timingResource, "uuid"):
                return self._artop_timingResource.uuid
        return
