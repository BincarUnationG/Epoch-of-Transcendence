package epoch.transcendence.datagen;

import epoch.transcendence.registry.*;
import net.fabricmc.fabric.api.datagen.v1.FabricDataOutput;
import net.fabricmc.fabric.api.datagen.v1.provider.FabricLanguageProvider;


public class ModZhCnLangProvider extends FabricLanguageProvider {
    protected ModZhCnLangProvider(FabricDataOutput dataOutput) {
        super(dataOutput, "zh_cn");
    }

    @Override
    public void generateTranslations(TranslationBuilder translationBuilder) {
        translationBuilder.add(ModBlocks.MANA_BLOCK, "魔力块");
        translationBuilder.add(ModBlocks.DEEPSLATE_MANA_ORE, "深层魔力矿石");
        translationBuilder.add(ModBlocks.MANA_ORE, "魔力矿石");
        translationBuilder.add(ModItems.MANA_BLOCK_ITEM, "魔力块");
        translationBuilder.add(ModItems.MANA_ORE_ITEM, "魔力矿石");
        translationBuilder.add(ModItems.DEEPSLATE_MANA_ORE_ITEM, "深层魔力矿石");
        translationBuilder.add(ModItems.MANA_CRYSTAL, "魔力结晶");
        translationBuilder.add(ModItems.MANA_DUST,"魔力粉尘");
        translationBuilder.add(ModCreativeTab.EPOCH_TAB_KEY,"超凡纪元");
        translationBuilder.add(ModEffects.MANA_SURGE,"魔力涌动");

    }
}
