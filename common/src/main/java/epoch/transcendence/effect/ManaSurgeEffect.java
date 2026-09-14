package epoch.transcendence.effect;

import net.minecraft.world.effect.MobEffect;
import net.minecraft.world.effect.MobEffectCategory;

import java.util.UUID;

public class ManaSurgeEffect extends MobEffect {
    private static final UUID SPEED_UUID = UUID.fromString("a1b2c3d4-e5f6-7890-abcd-ef1234567890");

    public ManaSurgeEffect() {
        super(MobEffectCategory.BENEFICIAL, 0x85ffff);
    }
}
