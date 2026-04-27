# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\DdsRequiredServiceInstance.py
from .DdsServiceInstanceProps import DdsServiceInstanceProps
from .RequiredApServiceInstance import RequiredApServiceInstance

class DdsRequiredServiceInstance(RequiredApServiceInstance, DdsServiceInstanceProps):

    def __init__(self):
        super().__init__()
        from .DdsServiceVersion import DdsServiceVersion
        from .DdsEventQosProps import DdsEventQosProps
        from .DdsFieldQosProps import DdsFieldQosProps
        from .DdsMethodQosProps import DdsMethodQosProps
        self._artop_requiredServiceInstanceId = None
        self._artop_blacklistedVersion = []
        self._artop_eventQosProps = []
        self._artop_fieldGetSetQosProps = []
        self._artop_fieldNotifierQosProps = []
        self._artop_methodQosProps = []
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({
         '_artop_blacklistedVersion': '"DDS-SERVICE-VERSION"', 
         '_artop_eventQosProps': '"DDS-EVENT-QOS-PROPS"', 
         '_artop_fieldGetSetQosProps': '"DDS-FIELD-QOS-PROPS"', 
         '_artop_fieldNotifierQosProps': '"DDS-FIELD-QOS-PROPS"', 
         '_artop_methodQosProps': '"DDS-METHOD-QOS-PROPS"'})

    @property
    def requiredServiceInstanceId_(self):
        return self._artop_requiredServiceInstanceId

    @property
    def blacklistedVersions_DdsServiceVersion(self):
        return self._artop_blacklistedVersion

    @property
    def eventQosProps_DdsEventQosProps(self):
        return self._artop_eventQosProps

    @property
    def fieldGetSetQosProps_DdsFieldQosProps(self):
        return self._artop_fieldGetSetQosProps

    @property
    def fieldNotifierQosProps_DdsFieldQosProps(self):
        return self._artop_fieldNotifierQosProps

    @property
    def methodQosProps_DdsMethodQosProps(self):
        return self._artop_methodQosProps
