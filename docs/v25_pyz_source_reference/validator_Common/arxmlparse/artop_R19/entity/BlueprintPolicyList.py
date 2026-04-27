# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\BlueprintPolicyList.py
from .BlueprintPolicyModifiable import BlueprintPolicyModifiable

class BlueprintPolicyList(BlueprintPolicyModifiable):

    def __init__(self):
        super().__init__()
        from .PositiveIntegerValueVariationPoint import PositiveIntegerValueVariationPoint
        self._artop_maxNumberOfElements = None
        self._artop_minNumberOfElements = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_maxNumberOfElements':"POSITIVE-INTEGER-VALUE-VARIATION-POINT", 
         '_artop_minNumberOfElements':"POSITIVE-INTEGER-VALUE-VARIATION-POINT"})

    @property
    def ref_maxNumberOfElements_(self):
        return self._artop_maxNumberOfElements

    @property
    def maxNumberOfElements_(self):
        if self._artop_maxNumberOfElements is not None:
            if hasattr(self._artop_maxNumberOfElements, "uuid"):
                return self._artop_maxNumberOfElements.uuid
        return

    @property
    def ref_minNumberOfElements_(self):
        return self._artop_minNumberOfElements

    @property
    def minNumberOfElements_(self):
        if self._artop_minNumberOfElements is not None:
            if hasattr(self._artop_minNumberOfElements, "uuid"):
                return self._artop_minNumberOfElements.uuid
        return
