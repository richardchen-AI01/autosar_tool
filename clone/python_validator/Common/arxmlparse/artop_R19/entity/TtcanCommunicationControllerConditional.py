# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\TtcanCommunicationControllerConditional.py
from .TtcanCommunicationControllerContent import TtcanCommunicationControllerContent

class TtcanCommunicationControllerConditional(TtcanCommunicationControllerContent):

    def __init__(self):
        super().__init__()
        from .TtcanCommunicationController import TtcanCommunicationController
        from .VariationPoint import VariationPoint
        self._artop_ttcanCommunicationController = None
        self._artop_variationPoint = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_ttcanCommunicationController':"TTCAN-COMMUNICATION-CONTROLLER", 
         '_artop_variationPoint':"VARIATION-POINT"})

    @property
    def ref_ttcanCommunicationController_(self):
        return self._artop_ttcanCommunicationController

    @property
    def ttcanCommunicationController_(self):
        if self._artop_ttcanCommunicationController is not None:
            if hasattr(self._artop_ttcanCommunicationController, "uuid"):
                return self._artop_ttcanCommunicationController.uuid
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
