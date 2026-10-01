package epoch.transcendence.item;

import net.minecraft.world.food.FoodProperties;
import net.minecraft.world.item.Item;

public class ManaBread extends Item {
    public ManaBread(){
        super(new Properties()
                .fireResistant()
                .food(new FoodProperties.Builder()
                        .nutrition(1)
                        .saturationMod(3.0F)
                        .alwaysEat()
                        .fast()
                        .build()
                )
        );
    }
}
