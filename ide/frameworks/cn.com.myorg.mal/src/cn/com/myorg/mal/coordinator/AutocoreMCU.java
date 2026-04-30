package cn.com.myorg.mal.coordinator;

public class AutocoreMCU {
    private String name;
    private String manufacturer;
    private String mcuModel;
    private boolean multicore = false;
    private int numberOfCores = 1;

    public AutocoreMCU(String name, String manufacturer, String mcuModel, boolean multicore, int numberOfCores) {
        this.name = name;
        this.manufacturer = manufacturer;
        this.multicore = multicore;
        this.numberOfCores = numberOfCores;
        this.mcuModel = mcuModel;
    }

    public String getName() {
        return this.name;
    }

    public String getManufacturer() {
        return this.manufacturer;
    }

    public boolean getMulticore() {
        return this.multicore;
    }

    public int getNumberOfCores() {
        return this.numberOfCores;
    }

    public String getMcuModel() {
        return this.mcuModel;
    }

    public void setMcuModel(String mcuModel) {
        this.mcuModel = mcuModel;
    }
}
