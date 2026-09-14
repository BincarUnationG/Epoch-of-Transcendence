package epoch.transcendence.datagen;

import epoch.transcendence.registry.ModBlocks;
import epoch.transcendence.registry.ModItems;
import net.fabricmc.fabric.api.datagen.v1.FabricDataGenerator;
import net.fabricmc.fabric.api.datagen.v1.FabricDataOutput;
import net.fabricmc.fabric.api.datagen.v1.provider.FabricTagProvider;
import net.minecraft.core.HolderLookup;
import net.minecraft.tags.BlockTags;
import net.minecraft.util.random.WeightedEntry;

import java.util.concurrent.CompletableFuture;

public class ModBlockTagsProvider extends FabricTagProvider.BlockTagProvider {
    public ModBlockTagsProvider(FabricDataOutput output, CompletableFuture<HolderLookup.Provider> registriesFuture) {
        super(output,registriesFuture);
    }


    @Override
    protected void addTags(HolderLookup.Provider arg) {
        getOrCreateTagBuilder(BlockTags.MINEABLE_WITH_PICKAXE)
                .add(ModBlocks.MANA_BLOCK)
                .add(ModBlocks.DEEPSLATE_MANA_ORE)
                .add(ModBlocks.MANA_ORE);
        getOrCreateTagBuilder(BlockTags.NEEDS_IRON_TOOL)
                .add(ModBlocks.MANA_ORE)
                .add(ModBlocks.DEEPSLATE_MANA_ORE)
                .add(ModBlocks.MANA_BLOCK);
    }
}
