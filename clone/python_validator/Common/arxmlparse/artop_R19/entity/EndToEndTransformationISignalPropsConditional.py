# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\EndToEndTransformationISignalPropsConditional.py
from .EndToEndTransformationISignalPropsContent import EndToEndTransformationISignalPropsContent

class EndToEndTransformationISignalPropsConditional(EndToEndTransformationISignalPropsContent):

    def __init__(self):
        super().__init__()
        from .EndToEndTransformationISignalProps import EndToEndTransformationISignalProps
        from .VariationPoint import VariationPoint
        self._artop_endToEndTransformationISignalProps = None
        self._artop_variationPoint = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_endToEndTransformationISignalProps':"END-TO-END-TRANSFORMATION-I-SIGNAL-PROPS", 
         '_artop_variationPoint':"VARIATION-POINT"})

    @property
    def ref_endToEndTransformationISignalProps_(self):
        return self._artop_endToEndTransformationISignalProps

    @property
    def endToEndTransformationISignalProps_(self):
        if self._artop_endToEndTransformationISignalProps is not None:
            if hasattr(self._artop_endToEndTransformationISignalProps, "uuid"):
                return self._artop_endToEndTransformationISignalProps.uuid
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
