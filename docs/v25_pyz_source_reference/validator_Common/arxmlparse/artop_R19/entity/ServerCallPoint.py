# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\ServerCallPoint.py
from .AbstractAccessPoint import AbstractAccessPoint

class ServerCallPoint(AbstractAccessPoint):

    def __init__(self):
        super().__init__()
        from .RunnableEntity import RunnableEntity
        from .ROperationInAtomicSwcInstanceRef import ROperationInAtomicSwcInstanceRef
        from .VariationPoint import VariationPoint
        self._artop_timeout = None
        self._artop_runnableEntity = None
        self._artop_operationIref = None
        self._artop_variationPoint = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_runnableEntity':"RUNNABLE-ENTITY", 
         '_artop_operationIref':"R-OPERATION-IN-ATOMIC-SWC-INSTANCE-REF", 
         '_artop_variationPoint':"VARIATION-POINT"})

    @property
    def timeout_(self):
        return self._artop_timeout

    @property
    def ref_runnableEntity_(self):
        return self._artop_runnableEntity

    @property
    def runnableEntity_(self):
        if self._artop_runnableEntity is not None:
            if hasattr(self._artop_runnableEntity, "uuid"):
                return self._artop_runnableEntity.uuid
        return

    @property
    def ref_operation_(self):
        return self._artop_operationIref

    @property
    def operation_(self):
        if self._artop_operationIref is not None:
            if hasattr(self._artop_operationIref, "uuid"):
                return self._artop_operationIref.uuid
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
