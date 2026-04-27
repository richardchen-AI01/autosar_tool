# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\ConsistencyNeeds.py
from .AtpBlueprintable import AtpBlueprintable
from .AtpBlueprint import AtpBlueprint

class ConsistencyNeeds(AtpBlueprint, AtpBlueprintable):

    def __init__(self):
        super().__init__()
        from .DataPrototypeGroup import DataPrototypeGroup
        from .RunnableEntityGroup import RunnableEntityGroup
        from .VariationPoint import VariationPoint
        self._artop_dpgDoesNotRequireCoherency = []
        self._artop_dpgRequiresCoherency = []
        self._artop_regDoesNotRequireStability = []
        self._artop_regRequiresStability = []
        self._artop_variationPoint = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({
         '_artop_dpgDoesNotRequireCoherency': '"DATA-PROTOTYPE-GROUP"', 
         '_artop_dpgRequiresCoherency': '"DATA-PROTOTYPE-GROUP"', 
         '_artop_regDoesNotRequireStability': '"RUNNABLE-ENTITY-GROUP"', 
         '_artop_regRequiresStability': '"RUNNABLE-ENTITY-GROUP"', 
         '_artop_variationPoint': '"VARIATION-POINT"'})

    @property
    def dpgDoesNotRequireCoherencies_DataPrototypeGroup(self):
        return self._artop_dpgDoesNotRequireCoherency

    @property
    def dpgRequiresCoherencies_DataPrototypeGroup(self):
        return self._artop_dpgRequiresCoherency

    @property
    def regDoesNotRequireStabilities_RunnableEntityGroup(self):
        return self._artop_regDoesNotRequireStability

    @property
    def regRequiresStabilities_RunnableEntityGroup(self):
        return self._artop_regRequiresStability

    @property
    def ref_variationPoint_(self):
        return self._artop_variationPoint

    @property
    def variationPoint_(self):
        if self._artop_variationPoint is not None:
            if hasattr(self._artop_variationPoint, "uuid"):
                return self._artop_variationPoint.uuid
        return
