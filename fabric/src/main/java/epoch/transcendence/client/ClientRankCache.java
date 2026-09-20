package epoch.transcendence.client;

import epoch.transcendence.data.Rank;
import net.fabricmc.api.Environment;
import net.fabricmc.api.EnvType;

import java.util.Map;
import java.util.UUID;
import java.util.concurrent.ConcurrentHashMap;

@Environment(EnvType.CLIENT)
public final class ClientRankCache {

    private static final Map<UUID, Rank> CACHE = new ConcurrentHashMap<>();

    private ClientRankCache() {}

    public static void put(UUID uuid, int level) {
        CACHE.put(uuid, Rank.of(level));
    }

    /** 客户端查询：没收到过就默认9阶 */
    public static Rank get(UUID uuid) {
        return CACHE.getOrDefault(uuid, Rank.of(9));
    }

    public static void clear() {
        CACHE.clear();
    }
}