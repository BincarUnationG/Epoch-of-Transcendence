package epoch.transcendence.client;

import epoch.transcendence.client.particle.ManaSparkParticle;
import epoch.transcendence.registry.ModParticles;
import net.fabricmc.api.ClientModInitializer;
import net.fabricmc.fabric.api.client.particle.v1.ParticleFactoryRegistry;

public class EpochFabricClientMod implements ClientModInitializer {

    @Override
    public void onInitializeClient() {
        // 注册粒子工厂(渲染相关，只能在客户端)
        ParticleFactoryRegistry.getInstance().register(
                ModParticles.MANA_SPARK,
                ManaSparkParticle.Provider::new
        );

        System.out.println("[Transcendence] 客户端粒子工厂注册完成！");
    }

}