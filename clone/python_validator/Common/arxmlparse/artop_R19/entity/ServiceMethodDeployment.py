# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\ServiceMethodDeployment.py
from .Identifiable import Identifiable

class ServiceMethodDeployment(Identifiable):

    def __init__(self):
        super().__init__()
        from .ServiceInterfaceDeployment import ServiceInterfaceDeployment
        from .ClientServerOperation import ClientServerOperation
        self._artop_serviceInterfaceDeployment = None
        self._artop_methodRef = None
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({'_artop_serviceInterfaceDeployment':"SERVICE-INTERFACE-DEPLOYMENT", 
         '_artop_methodRef':"CLIENT-SERVER-OPERATION"})

    @property
    def ref_serviceInterfaceDeployment_(self):
        return self._artop_serviceInterfaceDeployment

    @property
    def serviceInterfaceDeployment_(self):
        if self._artop_serviceInterfaceDeployment is not None:
            if hasattr(self._artop_serviceInterfaceDeployment, "uuid"):
                return self._artop_serviceInterfaceDeployment.uuid
        return

    @property
    def ref_method_(self):
        return self._artop_methodRef

    @property
    def method_(self):
        if self._artop_methodRef is not None:
            if hasattr(self._artop_methodRef, "uuid"):
                return self._artop_methodRef.uuid
        return
