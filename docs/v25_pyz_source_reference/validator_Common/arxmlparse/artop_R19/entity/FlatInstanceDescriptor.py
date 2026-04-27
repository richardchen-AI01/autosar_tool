# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\FlatInstanceDescriptor.py
from .Identifiable import Identifiable

class FlatInstanceDescriptor(Identifiable):

    def __init__(self):
        super().__init__()
        from .FlatMap import FlatMap
        from .RtePluginProps import RtePluginProps
        from .SwDataDefProps import SwDataDefProps
        from .AnyInstanceRef import AnyInstanceRef
        from .VariationPoint import VariationPoint
        self._artop_role = None
        self._artop_flatMap = None
        self._artop_rtePluginProps = None
        self._artop_swDataDefProps = None
        self._artop_upstreamReferenceIref = None
        self._artop_ecuExtractReferenceIref = None
        self._artop_variationPoint = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({
         '_artop_flatMap': '"FLAT-MAP"', 
         '_artop_rtePluginProps': '"RTE-PLUGIN-PROPS"', 
         '_artop_swDataDefProps': '"SW-DATA-DEF-PROPS"', 
         '_artop_upstreamReferenceIref': '"ANY-INSTANCE-REF-IREF"', 
         '_artop_ecuExtractReferenceIref': '"ANY-INSTANCE-REF-IREF"', 
         '_artop_variationPoint': '"VARIATION-POINT"'})

    @property
    def role_(self):
        return self._artop_role

    @property
    def ref_flatMap_(self):
        return self._artop_flatMap

    @property
    def flatMap_(self):
        if self._artop_flatMap is not None:
            if hasattr(self._artop_flatMap, "uuid"):
                return self._artop_flatMap.uuid
        return

    @property
    def ref_rtePluginProps_(self):
        return self._artop_rtePluginProps

    @property
    def rtePluginProps_(self):
        if self._artop_rtePluginProps is not None:
            if hasattr(self._artop_rtePluginProps, "uuid"):
                return self._artop_rtePluginProps.uuid
        return

    @property
    def ref_swDataDefProps_(self):
        return self._artop_swDataDefProps

    @property
    def swDataDefProps_(self):
        if self._artop_swDataDefProps is not None:
            if hasattr(self._artop_swDataDefProps, "uuid"):
                return self._artop_swDataDefProps.uuid
        return

    @property
    def ref_upstreamReference_(self):
        return self._artop_upstreamReferenceIref

    @property
    def upstreamReference_(self):
        if self._artop_upstreamReferenceIref is not None:
            if hasattr(self._artop_upstreamReferenceIref, "uuid"):
                return self._artop_upstreamReferenceIref.uuid
        return

    @property
    def ref_ecuExtractReference_(self):
        return self._artop_ecuExtractReferenceIref

    @property
    def ecuExtractReference_(self):
        if self._artop_ecuExtractReferenceIref is not None:
            if hasattr(self._artop_ecuExtractReferenceIref, "uuid"):
                return self._artop_ecuExtractReferenceIref.uuid
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
