package epoch.transcendence.registry;

import epoch.transcendence.EpochMod;
import net.minecraft.core.Registry;
import net.minecraft.core.registries.BuiltInRegistries;
import net.minecraft.resources.ResourceLocation;
import net.minecraft.world.item.BlockItem;
import net.minecraft.world.item.Item;

/**
 * 物品对象定义(仅数据,不包含任何注册逻辑)。
 * 注册动作由各加载器模块完成:Fabric 在 onInitialize 中静态注册,
 * Forge 通过 DeferredRegister 注册。
 */
public final class ModItems {
    public static final Item MANA_CRYSTAL = new Item(new Item.Properties());
    public static final Item MANA_ORE_ITEM = new BlockItem(ModBlocks.MANA_ORE, new Item.Properties());
    public static final Item DEEPSLATE_MANA_ORE_ITEM = new BlockItem(ModBlocks.DEEPSLATE_MANA_ORE, new Item.Properties());
    public static final Item MANA_BLOCK_ITEM = new BlockItem(ModBlocks.MANA_BLOCK, new Item.Properties());
    public static final Item MANA_DUST = new Item(new Item.Properties());

    private ModItems() {

    }
    public static void register(){
        Registry.register(BuiltInRegistries.ITEM,
                new ResourceLocation(EpochMod.MOD_ID, "deepslate_mana_ore"),
                ModItems.DEEPSLATE_MANA_ORE_ITEM);

        Registry.register(BuiltInRegistries.ITEM,
                new ResourceLocation(EpochMod.MOD_ID, "mana_crystal"),
                ModItems.MANA_CRYSTAL);

        Registry.register(BuiltInRegistries.ITEM,
                new ResourceLocation(EpochMod.MOD_ID, "mana_ore"),
                ModItems.MANA_ORE_ITEM);

        Registry.register(BuiltInRegistries.ITEM,
                new ResourceLocation(EpochMod.MOD_ID,"mana_block"),
                ModItems.MANA_BLOCK_ITEM
        );

        Registry.register(BuiltInRegistries.ITEM,
                new ResourceLocation(EpochMod.MOD_ID,"mana_dust"),
        ModItems.MANA_DUST
        );
    }

}
