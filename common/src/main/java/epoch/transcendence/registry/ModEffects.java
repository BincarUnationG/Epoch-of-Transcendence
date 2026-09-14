package epoch.transcendence.registry;

import epoch.transcendence.EpochMod;
import epoch.transcendence.effect.ManaSurgeEffect;
import net.minecraft.core.Registry;
import net.minecraft.core.registries.BuiltInRegistries;
import net.minecraft.resources.ResourceLocation;
import net.minecraft.world.effect.MobEffect;
import net.minecraft.world.effect.MobEffectInstance;
import net.minecraft.world.item.alchemy.Potion;

public final class ModEffects {


    public static MobEffect MANA_SURGE;

    private ModEffects() {}
    public static void register(){
        ModEffects.MANA_SURGE = Registry.register(
                BuiltInRegistries.MOB_EFFECT,
                new ResourceLocation(EpochMod.MOD_ID, "mana_surge"),
                new ManaSurgeEffect()
        );


        ModPotions.MANA_SURGE_POTION = Registry.register(
                BuiltInRegistries.POTION,
                new ResourceLocation(EpochMod.MOD_ID, "mana_surge"),
                new Potion(new MobEffectInstance(ModEffects.MANA_SURGE, 3600, 0))
        );


        ModPotions.LONG_MANA_SURGE_POTION = Registry.register(
                BuiltInRegistries.POTION,
                new ResourceLocation(EpochMod.MOD_ID, "long_mana_surge"),
                new Potion(new MobEffectInstance(ModEffects.MANA_SURGE, 9600, 0))
        );
    }
}