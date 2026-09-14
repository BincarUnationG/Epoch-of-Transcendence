package epoch.transcendence.block;

import epoch.transcendence.registry.ModParticles;
import net.minecraft.core.BlockPos;
import net.minecraft.core.Direction;
import net.minecraft.core.particles.DustParticleOptions;
import net.minecraft.core.particles.ParticleTypes;
import net.minecraft.sounds.SoundEvents;
import net.minecraft.sounds.SoundSource;
import net.minecraft.util.RandomSource;
import net.minecraft.world.level.BlockGetter;
import net.minecraft.world.level.Level;
import net.minecraft.world.level.block.Block;
import net.minecraft.world.level.block.state.BlockBehaviour;
import net.minecraft.world.level.block.state.BlockState;
import net.minecraft.world.level.material.MapColor;
import org.joml.Vector3f;

public class ManaBlock extends Block {
    // ===== 亮蓝紫色粒子定义 =====
    // RGB 值范围 0.0~1.0
    // (0.6, 0.4, 1.0) = 亮蓝紫（薰衣草偏蓝）
    private static final DustParticleOptions MANA_DUST = new DustParticleOptions(
            new Vector3f(0.6f, 0.4f, 1.0f),  // RGB 亮蓝紫色
            1.2f                              // 粒子大小（越大越显眼）
    );

    // 更亮的核心色（接近白蓝紫）
    private static final DustParticleOptions MANA_CORE_DUST = new DustParticleOptions(
            new Vector3f(0.8f, 0.6f, 1.0f),  // RGB 更亮的蓝紫色
            1.5f
    );

    // 深紫色（用于边缘粒子）
    private static final DustParticleOptions MANA_DEEP_DUST = new DustParticleOptions(
            new Vector3f(0.4f, 0.2f, 0.9f),  // RGB 深蓝紫色
            1.0f
    );

    public ManaBlock() {
        super(BlockBehaviour.Properties.of() // 1. 使用 of() 开始
                .mapColor(MapColor.COLOR_LIGHT_BLUE)    // 2. 设置方块颜色
                .strength(5.0f, 6.0f)        // 3. 设置硬度
                .requiresCorrectToolForDrops()
                .lightLevel(state -> 10)
        );
    }
    @Override
    public void animateTick(BlockState state, Level level, BlockPos pos, RandomSource random) {
        // 在方块上方随机位置生成光点
        if (random.nextFloat() < 0.3f) {  // 30% 概率每 tick 生成
            double offsetX = (random.nextDouble() - 0.5) * 1.5;
            double offsetY = (random.nextDouble() - 0.5) * 1.5;
            double offsetZ = (random.nextDouble() - 0.5) * 1.5;

            double x = pos.getX() + 0.3 + offsetX;
            double y = pos.getY() + 1.0 + offsetY;
            double z = pos.getZ() + 0.3 + offsetZ;

            double speedX = offsetX * 0.02;
            double speedY = 0.02 + random.nextDouble() * 0.02;
            double speedZ = offsetZ * 0.02;

            level.addParticle(
                    ModParticles.MANA_SPARK,
                    x, y, z,
                    0.0, 0.02, 0.0
            );
        }
        if (random.nextFloat() < 0.05f) {  // 5% 概率
            level.playLocalSound(pos.getX()+0.5,
                    pos.getY()+0.5,
                    pos.getZ()+0.5,
                    SoundEvents.AMETHYST_BLOCK_CHIME,
                    SoundSource.BLOCKS,
                    0.5f, 0.8f + random.nextFloat() * 0.4f,
                    true);
        }
    }
    @Override
    public boolean isSignalSource(BlockState state) {
        return true;
    }
    @Override
    public int getSignal(BlockState state, BlockGetter level, BlockPos pos, Direction direction) {
        return 15;
    }
}
