package epoch.transcendence.registry;

import epoch.transcendence.EpochMod;
import epoch.transcendence.block.ManaBlock;
import epoch.transcendence.block.ManaOreBlock;
import net.minecraft.core.Registry;
import net.minecraft.core.registries.BuiltInRegistries;
import net.minecraft.resources.ResourceLocation;
import net.minecraft.world.level.block.Block;

/**
 * 方块对象定义(仅数据,不包含任何注册逻辑)。
 * 注册动作由各加载器模块完成:Fabric 在 onInitialize 中静态注册,
 * Forge 通过 DeferredRegister 注册。
 */
public final class ModBlocks {
    public static final Block MANA_ORE = new ManaOreBlock();
    public static final Block DEEPSLATE_MANA_ORE = new ManaOreBlock();
    public static final Block MANA_BLOCK = new ManaBlock();

    private ModBlocks() {

    }
    public static void register(){
        Registry.register(BuiltInRegistries.BLOCK,
                new ResourceLocation(EpochMod.MOD_ID, "mana_ore"),
                ModBlocks.MANA_ORE);

        Registry.register(BuiltInRegistries.BLOCK,
                new ResourceLocation(EpochMod.MOD_ID,  "deepslate_mana_ore"),
                ModBlocks.DEEPSLATE_MANA_ORE);

        Registry.register(BuiltInRegistries.BLOCK,
                new ResourceLocation(EpochMod.MOD_ID, "mana_block"),
                ModBlocks.MANA_BLOCK
        );
    }
}
