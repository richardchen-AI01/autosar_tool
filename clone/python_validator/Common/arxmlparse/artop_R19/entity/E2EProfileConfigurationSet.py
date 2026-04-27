# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\artop_R19\entity\E2EProfileConfigurationSet.py
from .UploadablePackageElement import UploadablePackageElement

class E2EProfileConfigurationSet(UploadablePackageElement):

    def __init__(self):
        super().__init__()
        from .E2EProfileConfiguration import E2EProfileConfiguration
        self._artop_e2EProfileConfiguration = []
        if not hasattr(self, "_tag_to_attr"):
            self._tag_to_attr = {}
        self._tag_to_attr.update({"_artop_e2EProfileConfiguration": "E-2-E-PROFILE-CONFIGURATION"})

    @property
    def e2eProfileConfigurations_E2EProfileConfiguration(self):
        return self._artop_e2EProfileConfiguration
