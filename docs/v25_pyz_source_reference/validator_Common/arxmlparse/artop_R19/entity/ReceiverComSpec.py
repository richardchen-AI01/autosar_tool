# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\ReceiverComSpec.py
from .RPortComSpec import RPortComSpec

class ReceiverComSpec(RPortComSpec):

    def __init__(self):
        super().__init__()
        from .CompositeNetworkRepresentation import CompositeNetworkRepresentation
        from .AutosarDataPrototype import AutosarDataPrototype
        from .PositiveIntegerValueVariationPoint import PositiveIntegerValueVariationPoint
        from .SwDataDefProps import SwDataDefProps
        from .VariableAccess import VariableAccess
        from .TransformationComSpecProps import TransformationComSpecProps
        from .BooleanValueVariationPoint import BooleanValueVariationPoint
        self._artop_dataUpdatePeriod = None
        self._artop_handleOutOfRange = None
        self._artop_handleOutOfRangeStatus = None
        self._artop_maxNoNewOrRepeatedData = None
        self._artop_receiverCapability = None
        self._artop_syncCounterInit = None
        self._artop_compositeNetworkRepresentation = []
        self._artop_dataElementRef = None
        self._artop_externalReplacementRef = None
        self._artop_maxDeltaCounterInit = None
        self._artop_networkRepresentation = None
        self._artop_replaceWith = None
        self._artop_transformationComSpecProps = []
        self._artop_usesEndToEndProtection = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({
         '_artop_compositeNetworkRepresentation': '"COMPOSITE-NETWORK-REPRESENTATION"', 
         '_artop_dataElementRef': '"AUTOSAR-DATA-PROTOTYPE"', 
         '_artop_externalReplacementRef': '"AUTOSAR-DATA-PROTOTYPE"', 
         '_artop_maxDeltaCounterInit': '"POSITIVE-INTEGER-VALUE-VARIATION-POINT"', 
         '_artop_networkRepresentation': '"SW-DATA-DEF-PROPS"', 
         '_artop_replaceWith': '"VARIABLE-ACCESS"', 
         '_artop_transformationComSpecProps': '"TRANSFORMATION-COM-SPEC-PROPS"', 
         '_artop_usesEndToEndProtection': '"BOOLEAN-VALUE-VARIATION-POINT"'})

    @property
    def dataUpdatePeriod_(self):
        return self._artop_dataUpdatePeriod

    @property
    def handleOutOfRange_(self):
        return self._artop_handleOutOfRange

    @property
    def handleOutOfRangeStatus_(self):
        return self._artop_handleOutOfRangeStatus

    @property
    def maxNoNewOrRepeatedData_(self):
        return self._artop_maxNoNewOrRepeatedData

    @property
    def receiverCapability_(self):
        return self._artop_receiverCapability

    @property
    def syncCounterInit_(self):
        return self._artop_syncCounterInit

    @property
    def compositeNetworkRepresentations_CompositeNetworkRepresentation(self):
        return self._artop_compositeNetworkRepresentation

    @property
    def ref_dataElement_(self):
        return self._artop_dataElementRef

    @property
    def dataElement_(self):
        if self._artop_dataElementRef is not None:
            if hasattr(self._artop_dataElementRef, "uuid"):
                return self._artop_dataElementRef.uuid
        return

    @property
    def ref_externalReplacement_(self):
        return self._artop_externalReplacementRef

    @property
    def externalReplacement_(self):
        if self._artop_externalReplacementRef is not None:
            if hasattr(self._artop_externalReplacementRef, "uuid"):
                return self._artop_externalReplacementRef.uuid
        return

    @property
    def ref_maxDeltaCounterInit_(self):
        return self._artop_maxDeltaCounterInit

    @property
    def maxDeltaCounterInit_(self):
        if self._artop_maxDeltaCounterInit is not None:
            if hasattr(self._artop_maxDeltaCounterInit, "uuid"):
                return self._artop_maxDeltaCounterInit.uuid
        return

    @property
    def ref_networkRepresentation_(self):
        return self._artop_networkRepresentation

    @property
    def networkRepresentation_(self):
        if self._artop_networkRepresentation is not None:
            if hasattr(self._artop_networkRepresentation, "uuid"):
                return self._artop_networkRepresentation.uuid
        return

    @property
    def ref_replaceWith_(self):
        return self._artop_replaceWith

    @property
    def replaceWith_(self):
        if self._artop_replaceWith is not None:
            if hasattr(self._artop_replaceWith, "uuid"):
                return self._artop_replaceWith.uuid
        return

    @property
    def transformationComSpecProps_TransformationComSpecProps(self):
        return self._artop_transformationComSpecProps

    @property
    def ref_usesEndToEndProtection_(self):
        return self._artop_usesEndToEndProtection

    @property
    def usesEndToEndProtection_(self):
        if self._artop_usesEndToEndProtection is not None:
            if hasattr(self._artop_usesEndToEndProtection, "uuid"):
                return self._artop_usesEndToEndProtection.uuid
        return
