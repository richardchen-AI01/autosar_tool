# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\SomeipFieldDeployment.py
from .ServiceFieldDeployment import ServiceFieldDeployment

class SomeipFieldDeployment(ServiceFieldDeployment):

    def __init__(self):
        super().__init__()
        from .SomeipMethodDeployment import SomeipMethodDeployment
        from .SomeipEventDeployment import SomeipEventDeployment
        self._artop_get = None
        self._artop_notifier = None
        self._artop_set = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_get':"SOMEIP-METHOD-DEPLOYMENT", 
         '_artop_notifier':"SOMEIP-EVENT-DEPLOYMENT", 
         '_artop_set':"SOMEIP-METHOD-DEPLOYMENT"})

    @property
    def ref_get_(self):
        return self._artop_get

    @property
    def get_(self):
        if self._artop_get is not None:
            if hasattr(self._artop_get, "uuid"):
                return self._artop_get.uuid
        return

    @property
    def ref_notifier_(self):
        return self._artop_notifier

    @property
    def notifier_(self):
        if self._artop_notifier is not None:
            if hasattr(self._artop_notifier, "uuid"):
                return self._artop_notifier.uuid
        return

    @property
    def ref_set_(self):
        return self._artop_set

    @property
    def set_(self):
        if self._artop_set is not None:
            if hasattr(self._artop_set, "uuid"):
                return self._artop_set.uuid
        return
