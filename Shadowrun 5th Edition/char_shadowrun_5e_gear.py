import char_shadowrun_5e_data as Core
import char_shadowrun_5e_item as Item
import random


def get_gear(ch: Core.Character, budget: int) -> Core.Character:
    gear_shopping_list = []
    essentials_out = get_essentials(ch)
    gear_shopping_list.append([i for i in essentials_out])
    ch.Gear = gear_shopping_list
    return ch


def get_essentials(ch: Core.Character) -> list[Core.Gear]:
    gear_essentials = []
    if Core.SINNER_NATIONAL in ch.Qualities or Core.SINNER_CRIMINAL in ch.Qualities:
        Core.REAL_SIN.rating = 1
        gear_essentials.append(Core.REAL_SIN)
    elif Core.SINNER_CORPORATE_LIMITED in ch.Qualities:
        Core.REAL_SIN.rating = 2
        gear_essentials.append(Core.REAL_SIN)
    elif Core.SINNER_CORPORATE in ch.Qualities:
        Core.REAL_SIN.rating = 3
        gear_essentials.append(Core.REAL_SIN)
    else:
        gear_essentials.append(Item.get_item(Core.FAKE_SIN))


    return gear_essentials
        


def get_lifestyle(ch: Core.Character) -> None:
    if ch.PrimaryLifestyle is None:
        ch.PrimaryLifestyle = random.choice(Core.LIFESTYLES)
    elif isinstance(ch.PrimaryLifestyle, Core.Lifestyle):
        lifestyles = [
                i for i in Core.Lifestyle.items if 
                i.cost < ch.PrimaryLifestyle.cost
                ]
        ch.PrimaryLifestyle = random.choice(lifestyles)
