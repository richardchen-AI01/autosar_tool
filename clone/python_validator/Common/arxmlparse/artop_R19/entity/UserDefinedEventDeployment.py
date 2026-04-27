# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\UserDefinedEventDeployment.py
from .ServiceEventDeployment import ServiceEventDeployment

class UserDefinedEventDeployment(ServiceEventDeployment):

    def __init__(self):
        super().__init__()
        from .UserDefinedFieldDeployment import UserDefinedFieldDeployment
        self._artop_userDefinedFieldDeployment = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({"_artop_userDefinedFieldDeployment": "USER-DEFINED-FIELD-DEPLOYMENT"})

    @property
    def ref_userDefinedFieldDeployment_(self):
        return self._artop_userDefinedFieldDeployment

    @property
    def userDefinedFieldDeployment_(self):
        if self._artop_userDefinedFieldDeployment is not None:
            if hasattr(self._artop_userDefinedFieldDeployment, "uuid"):
                return self._artop_userDefinedFieldDeployment.uuid
        return
