import random
import char_dnd_5e_core as Core

"""
KOBOLD PRESS - TALES OF THE OLD MARGREVE
"""
# LANGUAGES
ERINA_L = Core.Language("Erina", speakers='Erina', script='Erina')
PINEY_L = Core.Language("Piney", speakers='Piney', script=None)
# RACES
ALSEID = Core.Race("Alseid", ab_score=[(Core.DEX, 2), (Core.WIS, 1)], age=[20, 100], alignment=('Chaotic', 'Neutral') languages=[Core.COMMON, Core.ELVISH], size='Medium', speed=40, third_party=True, third_party_book='Kobold Press - Tales of the Old Margreve', darkvision=60, racial_profs={'Weapon': [Core.SPEAR, Core.SHORTBOW]})
ERNIA = Core.Race("Ernia", ab_score=[(Core.DEX, 2), {'Choose 1': [Core.WIS, Core.CHA], 'Bonus': 1}], age=[15, 60], alignment=('Chaotic', 'Good') languages=[ERINA_L, {'Choose 1': [Core.COMMON, Core.SYLVAN]}], size='Small', speed=25, third_party=True, third_party_book='Kobold Press - Tales of the Old Margreve', darkvision=60, racial_profs={'Skill': [Core.PERCEPTION]})
PINEY = Core.Race("Piney", ab_score=[(Core.CON, 2), (Core.WIS, 1)], age=[18, 80], alignment=('Lawful', 'None'), languages=[Core.COMMON, PINEY_L], size='Medium', speed=30, third_party=True, third_party_book='Kobold Press - Tales of the Old Margreve', darkvision=60, racial_profs={'Skill': [Core.NATURE, Core.SURVIVAL]})

