package cn.com.myorg.mal.coordinator;

public class BswModuleKind {
    private String name;
    private String desc;

    public BswModuleKind(String name, String desc) {
        this.name = name;
        this.desc = desc;
    }

    public String getName() {
        return this.name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getDesc() {
        return this.desc;
    }

    public String toString() {
        return this.name;
    }

    public int hashCode() {
        return this.name.hashCode();
    }
}
