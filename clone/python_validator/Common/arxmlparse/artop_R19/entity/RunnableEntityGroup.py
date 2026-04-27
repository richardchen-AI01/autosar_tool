# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\RunnableEntityGroup.py
from .AtpStructureElement import AtpStructureElement

class RunnableEntityGroup(AtpStructureElement):

    def __init__(self):
        super().__init__()
        from .InnerRunnableEntityGroupInCompositionInstanceRef import InnerRunnableEntityGroupInCompositionInstanceRef
        from .RunnableEntityInCompositionInstanceRef import RunnableEntityInCompositionInstanceRef
        from .VariationPoint import VariationPoint
        self._artop_runnableEntityGroupIref = []
        self._artop_runnableEntityIref = []
        self._artop_variationPoint = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_runnableEntityGroupIref':"INNER-RUNNABLE-ENTITY-GROUP-IN-COMPOSITION-INSTANCE-REF-IREF", 
         '_artop_runnableEntityIref':"RUNNABLE-ENTITY-IN-COMPOSITION-INSTANCE-REF-IREF", 
         '_artop_variationPoint':"VARIATION-POINT"})

    @property
    def runnableEntityGroups_InnerRunnableEntityGroupInCompositionInstanceRef(self):
        return self._artop_runnableEntityGroupIref

    @property
    def runnableEntities_RunnableEntityInCompositionInstanceRef(self):
        return self._artop_runnableEntityIref

    @property
    def ref_variationPoint_(self):
        return self._artop_variationPoint

    @property
    def variationPoint_(self):
        if self._artop_variationPoint is not None:
            if hasattr(self._artop_variationPoint, "uuid"):
                return self._artop_variationPoint.uuid
        return
