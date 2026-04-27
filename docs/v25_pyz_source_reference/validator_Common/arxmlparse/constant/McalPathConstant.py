# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.11.15 (main, Mar 11 2026, 17:14:47) [Clang 20.1.8 ]
# Embedded file name: Common\arxmlparse\constant\McalPathConstant.py
"""
此文件禁止手动修改，输入的def文件在def目录下更新后，运行脚本（mp_updater.py）生成！！！
此文件禁止手动修改，输入的def文件在def目录下更新后，运行脚本（mp_updater.py）生成！！！
此文件禁止手动修改，输入的def文件在def目录下更新后，运行脚本（mp_updater.py）生成！！！
"""

class McalPath:
    default_version = "R23"

    @staticmethod
    def Lin_LIN_E_TIMEOUT(version: str=default_version):
        dict_Lin_LIN_E_TIMEOUT = {'422':"/AUTOSAR/Lin/LinDemEventParameterRefs/LIN_E_TIMEOUT", 
         'R19':"/AUTOSAR/Lin/LinDemEventParameterRefs/LIN_E_TIMEOUT", 
         'R23':"/AUTOSAR/Lin/LinDemEventParameterRefs/LIN_E_TIMEOUT"}
        return dict_Lin_LIN_E_TIMEOUT.get(version, None)

    @staticmethod
    def Lin_Lin(version: str=default_version):
        dict_Lin_Lin = {'422':"/AUTOSAR/Lin", 
         'R19':"/AUTOSAR/Lin", 
         'R23':"/AUTOSAR/Lin"}
        return dict_Lin_Lin.get(version, None)

    @staticmethod
    def Lin_LinChannel(version: str=default_version):
        dict_Lin_LinChannel = {'422':"/AUTOSAR/Lin/LinGlobalConfig/LinChannel", 
         'R19':"/AUTOSAR/Lin/LinGlobalConfig/LinChannel", 
         'R23':"/AUTOSAR/Lin/LinGlobalConfig/LinChannel"}
        return dict_Lin_LinChannel.get(version, None)

    @staticmethod
    def Lin_LinChannelBaudRate(version: str=default_version):
        dict_Lin_LinChannelBaudRate = {'422':"/AUTOSAR/Lin/LinGlobalConfig/LinChannel/LinChannelBaudRate", 
         'R19':"/AUTOSAR/Lin/LinGlobalConfig/LinChannel/LinChannelBaudRate", 
         'R23':"/AUTOSAR/Lin/LinGlobalConfig/LinChannel/LinChannelBaudRate"}
        return dict_Lin_LinChannelBaudRate.get(version, None)

    @staticmethod
    def Lin_LinChannelEcuMWakeupSource(version: str=default_version):
        dict_Lin_LinChannelEcuMWakeupSource = {'422':"/AUTOSAR/Lin/LinGlobalConfig/LinChannel/LinChannelEcuMWakeupSource", 
         'R19':"/AUTOSAR/Lin/LinGlobalConfig/LinChannel/LinChannelEcuMWakeupSource", 
         'R23':"/AUTOSAR/Lin/LinGlobalConfig/LinChannel/LinChannelEcuMWakeupSource"}
        return dict_Lin_LinChannelEcuMWakeupSource.get(version, None)

    @staticmethod
    def Lin_LinChannelEcucPartitionRef(version: str=default_version):
        dict_Lin_LinChannelEcucPartitionRef = {'R19':"/AUTOSAR/Lin/LinGlobalConfig/LinChannel/LinChannelEcucPartitionRef", 
         'R23':"/AUTOSAR/Lin/LinGlobalConfig/LinChannel/LinChannelEcucPartitionRef"}
        return dict_Lin_LinChannelEcucPartitionRef.get(version, None)

    @staticmethod
    def Lin_LinChannelId(version: str=default_version):
        dict_Lin_LinChannelId = {'422':"/AUTOSAR/Lin/LinGlobalConfig/LinChannel/LinChannelId", 
         'R19':"/AUTOSAR/Lin/LinGlobalConfig/LinChannel/LinChannelId", 
         'R23':"/AUTOSAR/Lin/LinGlobalConfig/LinChannel/LinChannelId"}
        return dict_Lin_LinChannelId.get(version, None)

    @staticmethod
    def Lin_LinChannelWakeupSupport(version: str=default_version):
        dict_Lin_LinChannelWakeupSupport = {'422':"/AUTOSAR/Lin/LinGlobalConfig/LinChannel/LinChannelWakeupSupport", 
         'R19':"/AUTOSAR/Lin/LinGlobalConfig/LinChannel/LinChannelWakeupSupport", 
         'R23':"/AUTOSAR/Lin/LinGlobalConfig/LinChannel/LinChannelWakeupSupport"}
        return dict_Lin_LinChannelWakeupSupport.get(version, None)

    @staticmethod
    def Lin_LinClockRef(version: str=default_version):
        dict_Lin_LinClockRef = {'422':"/AUTOSAR/Lin/LinGlobalConfig/LinChannel/LinClockRef", 
         'R19':"/AUTOSAR/Lin/LinGlobalConfig/LinChannel/LinClockRef", 
         'R23':"/AUTOSAR/Lin/LinGlobalConfig/LinChannel/LinClockRef"}
        return dict_Lin_LinClockRef.get(version, None)

    @staticmethod
    def Lin_LinDemEventParameterRefs(version: str=default_version):
        dict_Lin_LinDemEventParameterRefs = {'422':"/AUTOSAR/Lin/LinDemEventParameterRefs", 
         'R19':"/AUTOSAR/Lin/LinDemEventParameterRefs", 
         'R23':"/AUTOSAR/Lin/LinDemEventParameterRefs"}
        return dict_Lin_LinDemEventParameterRefs.get(version, None)

    @staticmethod
    def Lin_LinDevErrorDetect(version: str=default_version):
        dict_Lin_LinDevErrorDetect = {'422':"/AUTOSAR/Lin/LinGeneral/LinDevErrorDetect", 
         'R19':"/AUTOSAR/Lin/LinGeneral/LinDevErrorDetect", 
         'R23':"/AUTOSAR/Lin/LinGeneral/LinDevErrorDetect"}
        return dict_Lin_LinDevErrorDetect.get(version, None)

    @staticmethod
    def Lin_LinEcucPartitionRef(version: str=default_version):
        dict_Lin_LinEcucPartitionRef = {'R19':"/AUTOSAR/Lin/LinGeneral/LinEcucPartitionRef", 
         'R23':"/AUTOSAR/Lin/LinGeneral/LinEcucPartitionRef"}
        return dict_Lin_LinEcucPartitionRef.get(version, None)

    @staticmethod
    def Lin_LinGeneral(version: str=default_version):
        dict_Lin_LinGeneral = {'422':"/AUTOSAR/Lin/LinGeneral", 
         'R19':"/AUTOSAR/Lin/LinGeneral", 
         'R23':"/AUTOSAR/Lin/LinGeneral"}
        return dict_Lin_LinGeneral.get(version, None)

    @staticmethod
    def Lin_LinGlobalConfig(version: str=default_version):
        dict_Lin_LinGlobalConfig = {'422':"/AUTOSAR/Lin/LinGlobalConfig", 
         'R19':"/AUTOSAR/Lin/LinGlobalConfig", 
         'R23':"/AUTOSAR/Lin/LinGlobalConfig"}
        return dict_Lin_LinGlobalConfig.get(version, None)

    @staticmethod
    def Lin_LinIndex(version: str=default_version):
        dict_Lin_LinIndex = {'422':"/AUTOSAR/Lin/LinGeneral/LinIndex", 
         'R19':"/AUTOSAR/Lin/LinGeneral/LinIndex", 
         'R23':"/AUTOSAR/Lin/LinGeneral/LinIndex"}
        return dict_Lin_LinIndex.get(version, None)

    @staticmethod
    def Lin_LinNodeType(version: str=default_version):
        dict_Lin_LinNodeType = {'R19':"/AUTOSAR/Lin/LinGlobalConfig/LinChannel/LinNodeType", 
         'R23':"/AUTOSAR/Lin/LinGlobalConfig/LinChannel/LinNodeType"}
        return dict_Lin_LinNodeType.get(version, None)

    @staticmethod
    def Lin_LinTimeoutDuration(version: str=default_version):
        dict_Lin_LinTimeoutDuration = {'422':"/AUTOSAR/Lin/LinGeneral/LinTimeoutDuration", 
         'R19':"/AUTOSAR/Lin/LinGeneral/LinTimeoutDuration", 
         'R23':"/AUTOSAR/Lin/LinGeneral/LinTimeoutDuration"}
        return dict_Lin_LinTimeoutDuration.get(version, None)

    @staticmethod
    def Lin_LinVersionInfoApi(version: str=default_version):
        dict_Lin_LinVersionInfoApi = {'422':"/AUTOSAR/Lin/LinGeneral/LinVersionInfoApi", 
         'R19':"/AUTOSAR/Lin/LinGeneral/LinVersionInfoApi", 
         'R23':"/AUTOSAR/Lin/LinGeneral/LinVersionInfoApi"}
        return dict_Lin_LinVersionInfoApi.get(version, None)
