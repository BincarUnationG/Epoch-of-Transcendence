package epoch.transcendence.data;

// 境界(凡/传/神)
public enum Realm {
    MORTAL,   // 凡尘（5~9阶）
    LEGEND,   // 传说（3~4阶）
    MYTHIC;   // 神话（0~2阶）

    public static Realm fromLevel(int level) {
        if (level >= 5) return MORTAL;
        if (level >= 3) return LEGEND;
        return MYTHIC;
    }
}
