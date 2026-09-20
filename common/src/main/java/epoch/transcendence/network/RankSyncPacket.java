package epoch.transcendence.network;

import net.minecraft.network.FriendlyByteBuf;

import java.util.UUID;

// 位阶同步数据包
public record RankSyncPacket(UUID uuid, int level) {
    public void write(FriendlyByteBuf buf) {
        buf.writeUUID(uuid);
        buf.writeVarInt(level);
    }

    public static RankSyncPacket read(FriendlyByteBuf buf) {
        return new RankSyncPacket(buf.readUUID(), buf.readVarInt());
    }
}
