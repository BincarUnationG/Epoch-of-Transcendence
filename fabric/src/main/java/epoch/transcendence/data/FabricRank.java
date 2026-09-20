package epoch.transcendence.data;

import com.mojang.serialization.Codec;
import epoch.transcendence.network.RankNetwork;
import net.fabricmc.fabric.api.attachment.v1.AttachmentRegistry;
import net.fabricmc.fabric.api.attachment.v1.AttachmentType;
import net.minecraft.resources.ResourceLocation;
import net.minecraft.world.entity.LivingEntity;

public final class FabricRank {

    public static final AttachmentType<Integer> RANK_ATTACHMENT =
            AttachmentRegistry.<Integer>builder()
                    .initializer(() -> 9)
                    .persistent(Codec.INT)
                    .copyOnDeath()
                    .buildAndRegister(
                            new ResourceLocation("epoch_of_transcendence", "rank_level")
                    );

    private FabricRank() {}

    public static Rank get(LivingEntity entity) {
        return Rank.of(entity.getAttachedOrCreate(RANK_ATTACHMENT));
    }

    public static void set(LivingEntity entity, Rank rank) {
        entity.setAttached(RANK_ATTACHMENT, rank.level());

        // 只在服务端触发同步
        if (!entity.level().isClientSide) {
            RankNetwork.syncToNearby(entity);
        }
    }

    public static void addLevel(LivingEntity entity, int delta) {
        int current = get(entity).level();
        int next = Math.max(0, Math.min(9, current + delta));
        set(entity, Rank.of(next));
    }
}