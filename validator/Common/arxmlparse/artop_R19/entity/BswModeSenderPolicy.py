# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\BswModeSenderPolicy.py
from .ARObject import ARObject

class BswModeSenderPolicy(ARObject):

    def __init__(self):
        super().__init__()
        from .BswInternalBehavior import BswInternalBehavior
        from .BswModeSwitchAckRequest import BswModeSwitchAckRequest
        from .ModeDeclarationGroupPrototype import ModeDeclarationGroupPrototype
        from .VariationPoint import VariationPoint
        self._artop_enhancedModeApi = None
        self._artop_queueLength = None
        self._artop_bswInternalBehavior = None
        self._artop_ackRequest = None
        self._artop_providedModeGroupRef = None
        self._artop_variationPoint = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({
         '_artop_bswInternalBehavior': '"BSW-INTERNAL-BEHAVIOR"', 
         '_artop_ackRequest': '"BSW-MODE-SWITCH-ACK-REQUEST"', 
         '_artop_providedModeGroupRef': '"MODE-DECLARATION-GROUP-PROTOTYPE"', 
         '_artop_variationPoint': '"VARIATION-POINT"'})

    @property
    def enhancedModeApi_(self):
        if self._artop_enhancedModeApi:
            if self._artop_enhancedModeApi == "true":
                return True
            return False
        else:
            return self._artop_enhancedModeApi

    @property
    def queueLength_(self):
        return self._artop_queueLength

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
    def ref_ackRequest_(self):
        return self._artop_ackRequest

    @property
    def ackRequest_(self):
        if self._artop_ackRequest is not None:
            if hasattr(self._artop_ackRequest, "uuid"):
                return self._artop_ackRequest.uuid
        return

    @property
    def ref_providedModeGroup_(self):
        return self._artop_providedModeGroupRef

    @property
    def providedModeGroup_(self):
        if self._artop_providedModeGroupRef is not None:
            if hasattr(self._artop_providedModeGroupRef, "uuid"):
                return self._artop_providedModeGroupRef.uuid
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
