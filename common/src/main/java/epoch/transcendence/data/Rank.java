package epoch.transcendence.data;

public record Rank(int level) {

    private static final Rank[] CACHE = new Rank[10];
    static {
        for (int i = 0; i <= 9; i++) CACHE[i] = new Rank(i);
    }

    public Rank {
        if (level < 0 || level > 9)
            throw new IllegalArgumentException("Rank level must be 0-9, got: " + level);
    }

    public static Rank of(int level) {
        if (level < 0 || level > 9)
            throw new IllegalArgumentException("Level out of range: " + level);
        return CACHE[level];
    }

    public Realm getRealm() { return Realm.fromLevel(level); }
    public boolean isMortal() { return level >= 5; }
    public boolean isLegend() { return level >= 3 && level <= 4; }
    public boolean isMythic() { return level <= 2; }
    public boolean isVertex() { return level == 5; }
}