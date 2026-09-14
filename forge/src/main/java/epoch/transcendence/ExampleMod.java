package epoch.transcendence;

import epoch.transcendence.EpochMod;
import epoch.transcendence.registry.ModBlocks;
import epoch.transcendence.registry.ModItems;
import net.minecraft.world.item.Item;
import net.minecraft.world.level.block.Block;
import net.minecraftforge.eventbus.api.IEventBus;
import net.minecraftforge.fml.common.Mod;
import net.minecraftforge.fml.javafmlmod.FMLJavaModLoadingContext;
import net.minecraftforge.registries.DeferredRegister;
import net.minecraftforge.registries.ForgeRegistries;

@Mod(EpochMod.MOD_ID)
public class ExampleMod {

    private static final DeferredRegister<Block> BLOCKS = DeferredRegister.create(ForgeRegistries.BLOCKS, EpochMod.MOD_ID);
    private static final DeferredRegister<Item> ITEMS = DeferredRegister.create(ForgeRegistries.ITEMS, EpochMod.MOD_ID);

    static {
        BLOCKS.register("mana_ore", () -> ModBlocks.MANA_ORE);
        ITEMS.register("mana_crystal", () -> ModItems.MANA_CRYSTAL);
        ITEMS.register("mana_ore", () -> ModItems.MANA_ORE_ITEM);
    }

    public ExampleMod() {

        // This method is invoked by the Forge mod loader when it is ready
        // to load your mod. You can access Forge and Common code in this
        // project.

        // Register the contents of our DeferredRegisters on the mod event bus.
        IEventBus modEventBus = FMLJavaModLoadingContext.get().getModEventBus();
        BLOCKS.register(modEventBus);
        ITEMS.register(modEventBus);

        EpochMod.LOG.info("Hello Forge world!");
    }
}
