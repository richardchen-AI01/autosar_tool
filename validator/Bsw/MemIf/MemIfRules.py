from Common.Public import getURIPath, getIntegerValue
from Common.arxmlparse.artop import def_elements
from Common.arxmlparse.constant.BswPathConstant import BswPath as BP
from Common.base.BaseClass import BaseRule
from Common.base.BaseDecorator import RuleHandler


class RuleBSWMemIfR23(BaseRule):
    """
        MemIf模块校验基类
        @Author changhui.li
    """

    @RuleHandler()
    def Rule_BSW_MemIf_TCPP_2171(self) -> list:
        """
            实现校验TCPP-2171
        """
        lst_ret = []
        general_list = def_elements.get(BP.MemIf_MemIfGeneral.value)
        if general_list:
            general = general_list[0]
            numberOfDevices = getIntegerValue(general, BP.MemIf_MemIfNumberOfDevices.shortName)
            if numberOfDevices:
                nvmFeeRefs = def_elements.get(BP.NvM_NvMFeeRef.value)
                nvmEaRefs = def_elements.get(BP.NvM_NvMEaRef.value)
                if not nvmFeeRefs and not nvmEaRefs:
                    target_uri = getURIPath(general, BP.MemIf_MemIfNumberOfDevices.shortName)
                    message_args = [numberOfDevices]
                    lst_ret.append((target_uri, message_args, [], general))
        return lst_ret

    @RuleHandler()
    def Rule_BSW_MemIf_TCPP_2170(self) -> list:
        """
            实现校验TCPP-2170
        """
        lst_ret = []
        general_list = def_elements.get(BP.MemIf_MemIfGeneral.value)
        if general_list:
            general = general_list[0]
            numberOfDevices = getIntegerValue(general, BP.MemIf_MemIfNumberOfDevices.shortName)
            if numberOfDevices == 1:
                nvmFeeRefs = def_elements.get(BP.NvM_NvMFeeRef.value)
                nvmEaRefs = def_elements.get(BP.NvM_NvMEaRef.value)
                if nvmFeeRefs and nvmEaRefs:
                    target_uri = getURIPath(general, BP.MemIf_MemIfNumberOfDevices.shortName)
                    message_args = [numberOfDevices]
                    lst_ret.append((target_uri, message_args, [], general))
        return lst_ret
