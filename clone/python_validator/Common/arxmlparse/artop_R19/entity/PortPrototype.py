# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\PortPrototype.py
from .AtpPrototype import AtpPrototype
from .AtpBlueprintable import AtpBlueprintable

class PortPrototype(AtpBlueprintable, AtpPrototype):

    def __init__(self):
        super().__init__()
        from .SwComponentType import SwComponentType
        from .ClientServerAnnotation import ClientServerAnnotation
        from .DelegatedPortAnnotation import DelegatedPortAnnotation
        from .IoHwAbstractionServerAnnotation import IoHwAbstractionServerAnnotation
        from .ModePortAnnotation import ModePortAnnotation
        from .NvDataPortAnnotation import NvDataPortAnnotation
        from .ParameterPortAnnotation import ParameterPortAnnotation
        from .RPortPrototypeProps import RPortPrototypeProps
        from .SenderReceiverAnnotation import SenderReceiverAnnotation
        from .TriggerPortAnnotation import TriggerPortAnnotation
        from .VariationPoint import VariationPoint
        self._artop_swComponentType = None
        self._artop_clientServerAnnotation = []
        self._artop_delegatedPortAnnotation = None
        self._artop_ioHwAbstractionServerAnnotation = []
        self._artop_modePortAnnotation = []
        self._artop_nvDataPortAnnotation = []
        self._artop_parameterPortAnnotation = []
        self._artop_portPrototypeProps = None
        self._artop_senderReceiverAnnotation = []
        self._artop_triggerPortAnnotation = []
        self._artop_variationPoint = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({
         '_artop_swComponentType': '"SW-COMPONENT-TYPE"', 
         '_artop_clientServerAnnotation': '"CLIENT-SERVER-ANNOTATION"', 
         '_artop_delegatedPortAnnotation': '"DELEGATED-PORT-ANNOTATION"', 
         '_artop_ioHwAbstractionServerAnnotation': '"IO-HW-ABSTRACTION-SERVER-ANNOTATION"', 
         '_artop_modePortAnnotation': '"MODE-PORT-ANNOTATION"', 
         '_artop_nvDataPortAnnotation': '"NV-DATA-PORT-ANNOTATION"', 
         '_artop_parameterPortAnnotation': '"PARAMETER-PORT-ANNOTATION"', 
         '_artop_portPrototypeProps': '"R-PORT-PROTOTYPE-PROPS"', 
         '_artop_senderReceiverAnnotation': '"SENDER-RECEIVER-ANNOTATION"', 
         '_artop_triggerPortAnnotation': '"TRIGGER-PORT-ANNOTATION"', 
         '_artop_variationPoint': '"VARIATION-POINT"'})

    @property
    def ref_swComponentType_(self):
        return self._artop_swComponentType

    @property
    def swComponentType_(self):
        if self._artop_swComponentType is not None:
            if hasattr(self._artop_swComponentType, "uuid"):
                return self._artop_swComponentType.uuid
        return

    @property
    def clientServerAnnotations_ClientServerAnnotation(self):
        return self._artop_clientServerAnnotation

    @property
    def ref_delegatedPortAnnotation_(self):
        return self._artop_delegatedPortAnnotation

    @property
    def delegatedPortAnnotation_(self):
        if self._artop_delegatedPortAnnotation is not None:
            if hasattr(self._artop_delegatedPortAnnotation, "uuid"):
                return self._artop_delegatedPortAnnotation.uuid
        return

    @property
    def ioHwAbstractionServerAnnotations_IoHwAbstractionServerAnnotation(self):
        return self._artop_ioHwAbstractionServerAnnotation

    @property
    def modePortAnnotations_ModePortAnnotation(self):
        return self._artop_modePortAnnotation

    @property
    def nvDataPortAnnotations_NvDataPortAnnotation(self):
        return self._artop_nvDataPortAnnotation

    @property
    def parameterPortAnnotations_ParameterPortAnnotation(self):
        return self._artop_parameterPortAnnotation

    @property
    def ref_portPrototypeProps_(self):
        return self._artop_portPrototypeProps

    @property
    def portPrototypeProps_(self):
        if self._artop_portPrototypeProps is not None:
            if hasattr(self._artop_portPrototypeProps, "uuid"):
                return self._artop_portPrototypeProps.uuid
        return

    @property
    def senderReceiverAnnotations_SenderReceiverAnnotation(self):
        return self._artop_senderReceiverAnnotation

    @property
    def triggerPortAnnotations_TriggerPortAnnotation(self):
        return self._artop_triggerPortAnnotation

    @property
    def ref_variationPoint_(self):
        return self._artop_variationPoint

    @property
    def variationPoint_(self):
        if self._artop_variationPoint is not None:
            if hasattr(self._artop_variationPoint, "uuid"):
                return self._artop_variationPoint.uuid
        return
