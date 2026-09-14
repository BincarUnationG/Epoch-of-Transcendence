package epoch.transcendence.registry;

import epoch.transcendence.EpochMod;
import net.minecraft.core.Registry;
import net.minecraft.core.registries.BuiltInRegistries;
import net.minecraft.core.registries.Registries;
import net.minecraft.network.chat.Component;
import net.minecraft.resources.ResourceKey;
import net.minecraft.resources.ResourceLocation;
import net.minecraft.world.item.CreativeModeTab;
import net.minecraft.world.item.ItemStack;
import net.minecraft.world.item.Items;
import net.minecraft.world.item.alchemy.PotionUtils;

import java.util.ArrayList;
import java.util.List;

/**
 * 创造模式标签页:提供 ResourceKey 与构建好的 CreativeModeTab 实例。
 * <p>
 * 本类只负责「数据 + 构建」,不执行注册动作(common 不依赖任何加载器 API):
 * Fabric 在 {@code EpochFabricMod.onInitialize()} 中用 Registry.register 注册,
 * Forge 通过 DeferredRegister&lt;CreativeModeTab&gt; 注册。
 */
public final class ModCreativeTab {

    public static final ResourceKey<CreativeModeTab> EPOCH_TAB_KEY =
            ResourceKey.create(Registries.CREATIVE_MODE_TAB,
                    new ResourceLocation(EpochMod.MOD_ID, "epoch_tab"));

    private ModCreativeTab() {
    }

    /** 该标签页展示的全部物品。 */
    public static List<ItemStack> getTabItems() {
        List<ItemStack> items = new ArrayList<>();
        items.add(new ItemStack(ModItems.MANA_CRYSTAL));
        items.add(new ItemStack(ModItems.MANA_ORE_ITEM));
        items.add(new ItemStack(ModItems.DEEPSLATE_MANA_ORE_ITEM));
        items.add(new ItemStack(ModItems.MANA_BLOCK_ITEM));
        items.add(new ItemStack(ModItems.MANA_DUST));
        items.add(PotionUtils.setPotion(new ItemStack(Items.POTION), ModPotions.MANA_SURGE_POTION));
        items.add(PotionUtils.setPotion(new ItemStack(Items.POTION), ModPotions.LONG_MANA_SURGE_POTION));
        items.add(PotionUtils.setPotion(new ItemStack(Items.SPLASH_POTION), ModPotions.MANA_SURGE_POTION));
        items.add(PotionUtils.setPotion(new ItemStack(Items.LINGERING_POTION), ModPotions.MANA_SURGE_POTION));
        return items;
    }

    /**
     * 构建(但不注册)标签页实例。
     * <p>
     * 图标/内容只在客户端构建标签页时才被求值,因此即使物品此刻还未
     * 完成注册也不会出问题;但保险起见仍建议各加载器先注册物品再注册标签页。
     */
    public static CreativeModeTab build() {
        return CreativeModeTab.builder(CreativeModeTab.Row.TOP, 0)
                .title(Component.translatable("itemGroup." + EpochMod.MOD_ID + ".epoch_tab"))
                .icon(() -> new ItemStack(ModItems.MANA_CRYSTAL))
                .displayItems((parameters, output) -> getTabItems().forEach(output::accept))
                .build();
    }
    public static void register(){
        Registry.register(BuiltInRegistries.CREATIVE_MODE_TAB,
                ModCreativeTab.EPOCH_TAB_KEY.location(),
                ModCreativeTab.build());
    }
}
