# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\DdsFieldQosProps.py
from .DdsQosProps import DdsQosProps

class DdsFieldQosProps(DdsQosProps):

    def __init__(self):
        super().__init__()
        from .ServiceFieldDeployment import ServiceFieldDeployment
        self._artop_fieldRef = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({"_artop_fieldRef": "SERVICE-FIELD-DEPLOYMENT"})

    @property
    def ref_field_(self):
        return self._artop_fieldRef

    @property
    def field_(self):
        if self._artop_fieldRef is not None:
            if hasattr(self._artop_fieldRef, "uuid"):
                return self._artop_fieldRef.uuid
        return
