package epoch.transcendence.client;

import epoch.transcendence.client.particle.ManaSparkParticle;
import epoch.transcendence.network.RankNetwork;
import epoch.transcendence.registry.ModParticles;
import net.fabricmc.api.ClientModInitializer;
import net.fabricmc.fabric.api.client.networking.v1.ClientPlayConnectionEvents;
import net.fabricmc.fabric.api.client.networking.v1.ClientPlayNetworking;
import net.fabricmc.fabric.api.client.particle.v1.ParticleFactoryRegistry;

import java.util.ArrayList;
import java.util.List;
import java.util.UUID;

public class EpochFabricClientMod implements ClientModInitializer {

    @Override
    public void onInitializeClient() {
        // 注册粒子工厂(渲染相关，只能在客户端)
        ParticleFactoryRegistry.getInstance().register(
                ModParticles.MANA_SPARK,
                ManaSparkParticle.Provider::new
        );

        System.out.println("[Transcendence] 客户端粒子工厂注册完成！");

        ClientPlayNetworking.registerGlobalReceiver(RankNetwork.CHANNEL,
                (client, handler, buf, responseSender) -> {
                    // 在 IO 线程读取数据
                    UUID uuid = buf.readUUID();
                    int level = buf.readVarInt();

                    // 切回客户端主线程执行
                    client.execute(() -> ClientRankCache.put(uuid, level));
                });

        // 断开连接时清空缓存
        ClientPlayConnectionEvents.DISCONNECT.register((handler, client) ->
                ClientRankCache.clear());

        System.out.println("[Transcendence] 客户端网络接收器注册完成！");
    }
}