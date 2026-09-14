package epoch.transcendence.block;

import net.minecraft.world.level.block.Block;
import net.minecraft.world.level.block.state.BlockBehaviour;
import net.minecraft.world.level.material.MapColor; // 注意这里

public class ManaOreBlock extends Block {
    public ManaOreBlock() {
        super(BlockBehaviour.Properties.of() // 1. 使用 of() 开始
                .mapColor(MapColor.STONE)    // 2. 设置方块颜色
                .strength(3.0f, 3.0f)        // 3. 设置硬度
                .requiresCorrectToolForDrops() // 4. 设置需要正确工具
        );
    }
}