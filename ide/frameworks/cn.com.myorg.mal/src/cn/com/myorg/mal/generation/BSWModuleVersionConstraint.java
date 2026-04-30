package cn.com.myorg.mal.generation;

public class BSWModuleVersionConstraint {
    public int major;
    public int minor;
    public Integer patch;

    public BSWModuleVersionConstraint(int major, int minor, Integer patch) {
        this.major = major;
        this.minor = minor;
        this.patch = patch;
    }
}
