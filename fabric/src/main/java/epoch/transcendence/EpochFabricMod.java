package epoch.transcendence;

import epoch.transcendence.registry.*;
import net.fabricmc.api.ModInitializer;
import net.fabricmc.fabric.api.particle.v1.FabricParticleTypes;
import net.fabricmc.fabric.api.registry.FuelRegistry;
import net.minecraft.core.Registry;
import net.minecraft.core.particles.SimpleParticleType;
import net.minecraft.core.registries.BuiltInRegistries;
import net.minecraft.resources.ResourceLocation;
import net.minecraft.world.item.alchemy.Potions;
import net.minecraft.world.item.crafting.Ingredient;

import net.minecraft.world.item.alchemy.Potion;
import net.minecraft.world.item.alchemy.PotionUtils;
import net.minecraft.world.item.alchemy.PotionBrewing;

public class EpochFabricMod implements ModInitializer {

    @Override
    public void onInitialize() {

        ModBlocks.register();
        ModItems.register();
        ModEffects.register();
        potionRecipeRegister();
        particleRegister();
        fuelRegister();


        ModCreativeTab.register();

        System.out.println("[Transcendence] Fabric 注册完成！");
    }
    private void particleRegister(){
        SimpleParticleType manaSpark = FabricParticleTypes.simple();
        ModParticles.MANA_SPARK = Registry.register(
                BuiltInRegistries.PARTICLE_TYPE,
                new ResourceLocation(EpochMod.MOD_ID, "mana_spark"),
                manaSpark);
    }
    private void fuelRegister(){
        FuelRegistry.INSTANCE.add(ModItems.MANA_CRYSTAL, FuelValues.MANA_CRYSTAL_BURN_TIME);
        FuelRegistry.INSTANCE.add(ModItems.MANA_BLOCK_ITEM, FuelValues.MANA_BLOCK_BURN_TIME);
    }
    private void potionRecipeRegister(){
        PotionBrewing.addMix(
                Potions.AWKWARD,                              // 输入药水
                ModItems.MANA_CRYSTAL,         // 酿造材料
                ModPotions.MANA_SURGE_POTION                  // 输出药水
        );
    }
}
