class SavageRaceClass:
    def __init__(
        self,
        name: str,
        desc: str,
    ):
        self.name = name
        self.desc = desc

android_desc = 'Androids are semi-organic beings created by advanced technology. The example here mimcs humans in most ways and can generaly pass for them when desired (and not examied by a physician). Their advanced neural netowrk gives them artificial intelligence complete with individaul personalities, quirks, and emotions just like any other sapient being.'
aquarian_desc = 'From the crushing ocean depths come aquatic folk. They are thick and sturdy beneath the waves but often vulnerable in the dry air or searing heat of the surface'
avion_desc = 'Avions are humanoids with wings. They tend to be very slight of build owing to their hollow bones. Some are feathered while others are leathery or even scaled.'
dwarves_desc = 'Dwarves are sahort but stout, hardy people who come from massive caverns or high mountains. They aree a proud, warlike race, usually made so by frequent contact with hostile races such as orcs or goblins'

Aquarian = SavageRaceClass('Aquarian', aquarian_desc)