# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\BswModeReceiverPolicy.py
from .ARObject import ARObject

class BswModeReceiverPolicy(ARObject):

    def __init__(self):
        super().__init__()
        from .BswInternalBehavior import BswInternalBehavior
        from .ModeDeclarationGroupPrototype import ModeDeclarationGroupPrototype
        from .VariationPoint import VariationPoint
        self._artop_enhancedModeApi = None
        self._artop_supportsAsynchronousModeSwitch = None
        self._artop_bswInternalBehavior = None
        self._artop_requiredModeGroupRef = None
        self._artop_variationPoint = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_bswInternalBehavior':"BSW-INTERNAL-BEHAVIOR", 
         '_artop_requiredModeGroupRef':"MODE-DECLARATION-GROUP-PROTOTYPE", 
         '_artop_variationPoint':"VARIATION-POINT"})

    @property
    def enhancedModeApi_(self):
        if self._artop_enhancedModeApi:
            if self._artop_enhancedModeApi == "true":
                return True
            return False
        else:
            return self._artop_enhancedModeApi

    @property
    def supportsAsynchronousModeSwitch_(self):
        if self._artop_supportsAsynchronousModeSwitch:
            if self._artop_supportsAsynchronousModeSwitch == "true":
                return True
            return False
        else:
            return self._artop_supportsAsynchronousModeSwitch

    @property
    def ref_bswInternalBehavior_(self):
        return self._artop_bswInternalBehavior

    @property
    def bswInternalBehavior_(self):
        if self._artop_bswInternalBehavior is not None:
            if hasattr(self._artop_bswInternalBehavior, "uuid"):
                return self._artop_bswInternalBehavior.uuid
        return

    @property
    def ref_requiredModeGroup_(self):
        return self._artop_requiredModeGroupRef

    @property
    def requiredModeGroup_(self):
        if self._artop_requiredModeGroupRef is not None:
            if hasattr(self._artop_requiredModeGroupRef, "uuid"):
                return self._artop_requiredModeGroupRef.uuid
        return

    @property
    def ref_variationPoint_(self):
        return self._artop_variationPoint

    @property
    def variationPoint_(self):
        if self._artop_variationPoint is not None:
            if hasattr(self._artop_variationPoint, "uuid"):
                return self._artop_variationPoint.uuid
        return
