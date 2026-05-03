package cn.com.myorg.mal.interfaces;

import cn.com.myorg.mal.uidefinition.UIDefinitionMap;
import java.util.HashMap;
import java.util.Map;

/**
 * Reference: cn.com.isoft.mal.interfaces.IFunctionExtension.
 *
 * <p>Per-module hook surface plugged into AutocoreMetaModelDescriptor. Host
 * widgets dispatch via MetaModelDescriptorParser.getUIDefinitionList(..);
 * the 9 EOperation string constants are well-known hook keys retained from
 * reference (used by MCU/PWM modules; NvM/MemIf don't consume them but the
 * surface is shared).
 */
public interface IFunctionExtension {
    String Mcu_LTCFrequencyCalc = "ltcGroup.frequency";
    String Mcu_LTCListByIndex = "ltcs.by.index";
    String Muc_SystemClockCalculator = "system.clock";
    String Pwm_ChannelDutyCycle = "pwm.channel.dutycycle";
    String Pwm_ChannelFrequency = "pwm.channel.frequency";
    String Pwm_Config = "pwm.Config";
    String Pwm_LtcRefChannelId = "pwm.ltcRef.channelId";
    String Pwm_UsedLtcs = "pwm.used.ltcs";
    String Pwm_UsedIsrs = "pwm.used.isrs";

    UIDefinitionMap getUIDefinitionMap();

    IModuleInit getModuleInit();

    Map<String, DataHandle> getDataHandleMap();

    abstract class DataHandle {
        protected Map<String, Object> mapParameter = new HashMap<>();

        public void put(String key, Object value) {
            this.mapParameter.put(key, value);
        }

        protected abstract Object doGetDataHandleReturnValue();

        public Object getDataHandleReturnValue() {
            try {
                return this.doGetDataHandleReturnValue();
            } catch (Exception ex) {
                return null;
            }
        }
    }
}
