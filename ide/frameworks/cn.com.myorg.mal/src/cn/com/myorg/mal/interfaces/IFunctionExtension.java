package cn.com.myorg.mal.interfaces;

import java.util.Map;

/**
 * Reference: cn.com.isoft.mal.interfaces.IFunctionExtension.
 *
 * <p>Trimmed to the marker-interface subset for E3-B-4. Reference declares
 * 9 EOperation hook constants (Mcu_LTCFrequencyCalc, Pwm_Config, etc.) and
 * 3 abstract methods (getUIDefinitionMap, getModuleInit, getDataHandleMap)
 * — those depend on UIDefinitionMap + DataHandle which we haven't ported.
 * Modules that need to plug functional extensions implement this; for v0.2
 * MemIf doesn't, so the marker form is sufficient.
 *
 * <p>Full method signatures are deferred to a later phase when an actual
 * module needs them.
 */
public interface IFunctionExtension {
}
