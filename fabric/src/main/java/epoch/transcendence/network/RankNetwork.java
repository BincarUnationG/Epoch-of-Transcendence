package epoch.transcendence.network;

import epoch.transcendence.data.FabricRank;
import epoch.transcendence.data.Rank;
import net.fabricmc.fabric.api.networking.v1.PacketByteBufs;
import net.fabricmc.fabric.api.networking.v1.ServerPlayNetworking;
import net.minecraft.network.FriendlyByteBuf;
import net.minecraft.resources.ResourceLocation;
import net.minecraft.server.level.ServerLevel;
import net.minecraft.server.level.ServerPlayer;
import net.minecraft.world.entity.Entity;
import net.minecraft.world.entity.LivingEntity;
import net.minecraft.world.phys.Vec3;

import java.util.UUID;

public final class RankNetwork {

    public static final ResourceLocation CHANNEL =
            new ResourceLocation("epoch_of_transcendence", "rank_sync");

    /** 同步半径（格），超出此距离的玩家不会收到 */
    private static final double SYNC_RANGE = 64.0;
    private static final double SYNC_RANGE_SQ = SYNC_RANGE * SYNC_RANGE;

    private RankNetwork() {}

    // ===== 单实体同步（Rank 变化时调用）=====
    public static void syncToNearby(LivingEntity entity) {
        if (!(entity.level() instanceof ServerLevel serverLevel)) return;

        Rank rank = FabricRank.get(entity);
        RankSyncPacket rankSyncPacket = new RankSyncPacket(entity.getUUID(), rank.level());
        Vec3 pos = entity.position();

        for (ServerPlayer player : serverLevel.players()) {
            if (player.distanceToSqr(pos) <= SYNC_RANGE_SQ) {
                send(player, rankSyncPacket);
            }
        }
    }

    // ===== 玩家加入时全量同步 =====
    public static void syncAllTo(ServerPlayer player) {
        ServerLevel level = player.serverLevel();

        for (Entity entity : level.getAllEntities()) {   // ← 用 getAllEntities()
            if (entity instanceof LivingEntity living) {
                sendRank(player, living.getUUID(), FabricRank.get(living));
            }
        }
    }

    // ===== 内部工具：向单个玩家发送 =====
    private static void sendRank(ServerPlayer player, UUID uuid, Rank rank) {
        FriendlyByteBuf buf = PacketByteBufs.create();
        buf.writeUUID(uuid);
        buf.writeVarInt(rank.level());
        ServerPlayNetworking.send(player, CHANNEL, buf);
    }
    private static void send(ServerPlayer player, RankSyncPacket rankSyncPacket) {
        FriendlyByteBuf buf = PacketByteBufs.create();
        rankSyncPacket.write(buf);
        ServerPlayNetworking.send(player, CHANNEL, buf);
    }
}