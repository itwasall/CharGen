from email.generator import DecodedGenerator
from chargen import *
from yaml import safe_load
from typing import Tuple, List


class ExaltedAttributeClass(BaseAttributeClass):
    def __init__(self, name):
        super().__init__(name, 0, 0)


class ExaltedCasteClass:
    def __init__(self, name: str, abilities: List[str]):
        self.name = name
        self.abilities = abilities
        self.associations = []
        self.example_concepts = []
        self.sobriquets = []
    def __repr__(self):
        return self.name


class ExaltedAbilityClass:
    def __init__(self, name: str, level: int = 0):
        self.name = name
        self.level = level
        self.is_favored: bool = False
        self.is_caste: bool = False
        self.is_supernal: bool = False
        self.is_specialty: bool = False
    def __repr__(self):
        return self.name
    def __add__(self, amt):
        self.level += amt
    def __iadd__(self, amt):
        self.__add__(amt)



class ExaltedCharmKeywordClass:
    def __init__(self, name: str, desc: str):
        self.name = name
        self.desc = desc

    def __repr__(self):
        return self.name


CHARM_TYPES = ['Simple', 'Supplemental', 'Reflexive', 'Permanent']

class ExaltedCharmClass:
    def __init__(
        self,
        name: str,
        cost: str,
        mins: List,
        charm_type: str,
        keywords: ExaltedCharmKeywordClass,
        duration: str,
        prerequisite_charms: List,
        desc: str
    ):
        self.name = name
        self.cost = cost
        self.mins = mins
        if charm_type not in CHARM_TYPES:
            raise ValueError
        self.charm_type = charm_type
        self.keywords = keywords
        self.duration = duration
        self.prerequisite_charms = prerequisite_charms
        self.desc = desc

    def __repr__(self):
        return self.name

charm_names = [
    "Wise Arrows", "Sight Without Eyes", "Blood Without Balance", "Force Without Fire", "Trance of Unhesitating Speed", "Phantom Arrow Technique", "Fiery Arrow Attack", "There Is No Wind", "Accuracy Without Distance", "Arrow Storm Technique", "Flashing Vengeance Draw", "Hunters Swift Answer", "Immaculate Golden Bow", "Dazzling Flare Attack", "Seven Omens Shot", "Revolving Bow Discipline", "Finishing Snipe", "Rain of Feathered Death", "Shadow-Seeking Arrow", "Searing Sunfire Interdiction", "Solar Spike", "Heart-Eating Incineration", "Dust and Ash Sleight", "Heavens Crash Down", "Streaming Arrow Stance", "Whispered Prayer of Judgment", "Graceful Crane Stance", "Monkey Leap Technique", "Soaring Crane Leap", "Foe-Vaulting Method", "Lightning Speed", "Winning Stride Discipline", "Increasing Strength Exercise", "Ten Ox Meditation", "Thunderbolt Attack Prana", "Feather Foot Style",
    "Spider Foot Style", "Unbound Eagle Approach", "Leaping Tiger Attack", "Racing Hare Method", "Onrush Burst Method", "Arete-Driven Marathon Stride", "Armor-Eating Strike", "Thunders Might", "Mountain-Crossing Leap Technique", "Eagle-Wing Style", "Demon-Wasting Rush", "Hurricane Spirit Speed", "Godspeed Steps", "Power Suffusing Form Technique", "Legion Aurochs Method", "Triumph-Forged God-Body", "One Extra Step", "Bonfire Anima Wings", "Aegis of Unstoppable Force", "Living Wind Approach", "Nine Aeons Thew", "Sensory Acuity Prana", "Surprise Anticipation Method", "Keen Sight Technique", "Unswerving Eye Method", "Keen Taste and Smell Technique", "Genius Palate Summation", "Foe-Scenting Method", "Keen Hearing and Touch Technique", "Studied Ear Espial", "Eyeless Harbinger Awareness", "Awakening Eye", "Inner Eye Focus", "Scent-Honing Prana", "Knowing Beyond Silence", "Living Pulse Perception",
    "Roused Dragon Detection", "Unsurpassed Sight Discipline", "Blink", "Unsurpassed Taste and Smell Discipline", "Unsurpassed Hearing and Touch Discipline", "Dedicated Unerring Ear", "Eye of the Unconquered Sun", "Fists of Iron Technique", "Iron Battle Focus", "Ferocious Jab", "Wind and Stones Defense", "Heaven Thunder Hammer", "Vicious Lunge", "Unbreakable Grasp", "Devil-Strangling Attitude", "Crashing Wave Throw", "Thunderclap Rush Attack", "Falling Hammer Strike", "Reckless Fury Discard", "Solar Cross-Counter", "Ox-Stunning Blow", "Burning Fist Burial", "Force-Rending Strike", "Blade-Rebuking Wrath", "Sledgehammer Fist Punch", "Oak-Curling Clinch", "Burning Proof of Authority", "Hammer on Iron Technique", "One With Violence", "Dancing With Strife Technique", "Knockout Blow", "Cancel the Apocalypse", "Adamantine Fists of Battle", "Intercepting Fury Smite", "Fire-Eating Fist", "River-Binding Wrath",
    "Wicked Dissolve Dust", "Rapturous Cradle", "Dragon Coil Technique", "Ten Calamities Technique", "Titan-Straightening Method", "Shockwave Technique", "Lightning Strikes Twice", "Fivefold Fury Onslaught", "Striving Aftershock Method", "Superior Violent Knowledge", "Inevitable Victory Meditation", "Incarnated Fury Attack", "Orichalcum Fists of Battle", "Raging Wrath Repeated", "Rampage-Berserker Attack", "Supremacy of War Meditation", "Apocalypse Flare Attack", "Heaven Fury Smite", "Ascendant Battle Visage", "Frugal Merchant Method", "Insightful Buyer Technique", "Consumer-Evaluating Glance", "All-Seeing Master Procurer", "Illimitable Master Fence", "Deft Officials Way", "Measuring Glance", "Enigmatic Bureau Understanding", "Speed the Wheels", "Bureau-Rectifying Method", "Enlightened Discourse Method", "Irresistible Salesman Spirit", "Ungoverned Market Awareness", "Bureau-Reforming Kata", "Indolent Official Charm", "Semantic Argument Technique", "Empowered Barter Stance",
    "Soul-Snaring Pitch", "Woe-Capturing Web", "Omen-Spawning Beast", "Foul Air of Argument Technique", "Eclectic Verbiage of Law", "Infinitely-Efficient Register", "Taboo-Inflicting Diatribe", "Subject-Hailing Ideology", "Order-Conferring Action", "Tireless Workhorse Method", "Efficient Craftsman Technique", "Arete-Shifting Prana", "Supreme Celestial Focus", "Sublime Transference", "Ages-Echoing Wisdom", "Dragon Soul Emergence", "Copper Spider Conception", "Clay and Breath Practice", "Spirit-Gathering Industry", "Summit-Piercing Touch", "Vice-Miracle Technique", "Unwinding Gyre Meditation", "God-Forge Within", "Exegesis of the Distilled Form", "Spirit-Stoking Elevation", "Sun-Heart Tenacity", "Wonder-Forging Genius", "Dual Magnus Prana", "Brass Scales Falling", "Red Anvils Ringing", "Chains Fall Away", "Craftsman Needs No Tools", "Peerless Paragon of Craft", "Supreme Perfection of Craft", "Thousand-Forge Hands", "Divine Transcendence of Craft",
    "Words-as-Workshop Method", "Shattering Grasp", "Durability-Enhancing Technique", "Crack-Mending Technique", "Time Heals Nothing", "Blood Diamond Sweat", "Object-Strengthening Touch", "Chaos-Resistance Preparation", "Breach-Healing Method", "Design Beyond Limit", "The Art of Permanence", "Realizing the Form Supernal", "Celestial Reforging Technique", "Flawless Handiwork Method", "Triumph-Forging Eye", "Supreme Masterwork Focus", "Bright-Forging Prana", "Experiential Conjuring of True Void", "Unbroken Image Focus", "First Movement of the Demiurge", "Essence-Forging Kata", "Mind-Expanding Meditation", "Inspiration-Renewing Vision", "Divine Inspiration Technique", "Horizon-Unveiling Insight", "Holistic Miracle Understanding", "Reed in the Wind", "Dust Motes Whirling", "Shadow Dancer Method", "Reflex Sidestep Technique", "Leaping Dodge Method", "Searing Quicksilver Flight", "Drifting Leaf Elusion", "Shadow Over Water", "Fleet Dreaming Image", "Drifting Shadow Focus",
    "Force-Stealing Feint", "Seven Shadow Evasion", "Safety Between Heartbeats", "Fourfold Shiver Binding", "Flow Like Blood", "Rumor of Form", "Way of Whispers Technique", "Vaporous Division", "Sunlight Bleeding Away", "Thousand Steps Stillness", "Unbowed Willow Meditation", "Hundred Shadow Ways", "Living Bonds Unburdened", "Unbridled Shade Attitude", "Harm-Dismissing Meditation", "Refinement of Flowing Shadows", "Enduring Mental Toughness", "Stubborn Boar Defense", "Integrity-Protecting Prana", "Destiny-Manifesting Method", "Legend-Soul Revival", "Spirit-Maintaining Maneuver", "Undying Solar Resolve", "Temptation-Resisting Stance", "Mind-Cleansing Prana", "Clear Mind Discipline", "Energy Restoration Prana", "Steel Heart Stance", "Righteous Lion Defense", "Watchful Eyes of Heaven", "Accord of the Unbreakable Spirit", "Phoenix Renewal Tactic", "Sun King Radiance", "Soul-Nourishing Technique", "Spirit-Tempering Practice", "Empowered Soul Technique",
    "Transcendent Heros Meditation", "Righteous Soul Judgment", "Barque of Transcendent Vision", "Unhesitating Dedication", "Invincible Solar Aegis", "Eminent Paragon Approach", "Divine Mantle", "Body-Restoring Benison", "Inviolable Essence-Merging", "Watchmans Infallible Eye", "Inquisitors Unfailing Notice", "Crafty Observation Method", "Divine Induction Technique", "Evidence-Discerning Method", "Judges Ear Technique", "Miraculous Stunning Insight", "Watchful Justiciars Eye", "Irresistible Questioning Technique", "Dauntless Inquisitor Attitude", "Evidence-Restoring Prana", "Ten Magistrate Eyes", "Unknown Wisdom Epiphany", "Enlightened Touch Insight", "Judge-Generals Stance", "Empathic Recall Discipline", "Mind Manse Meditation", "Seasoned Criminal Method", "Spurious Presence", "Preying on Uncertainty Approach", "Clever Bandits Rook", "Swift Gamblers Eye", "Lightning-Hand Sleight", "Flawless Pickpocketing Technique", "Lock-Opening Touch", "Flawlessly Impenetrable Disguise", "Phantom Hood Technique",
    "Doubt-Sealing Heist", "Living Shadow Preparedness", "Unshakable Rogues Spirit", "Master Plan Meditation", "Proof-Eating Palm", "Stealing From Plain Sight Spirit", "Magpies Invisible Talon", "Perfect Mirror", "Fate-Shifting Solar Arete", "Skillful Reappropriation (Phantom Sting Search)", "Reversal of Fortune", "Iron Wolves Grasp", "Door-Evading Technique", "Flashing Ruse Prana", "Split Deception Method", "Null Anima Gloves", "Nights Eye Meditation", "Unbroken Darkness Approach", "Whirling Brush Method", "Flawless Brush Discipline", "Letter-Within-A-Letter Technique", "Subtle Speech Method", "Flowing Elegant Hand", "Strange Tongue Understanding", "Poetic Expression Style", "Mingled Tongue Technique", "Sagacious Reading of Intent", "Word-Shield Invocation", "Stolen Voice Technique", "Moving the Unseen Hand", "Essence-Laden Missive", "Voice-Caging Calligraphy", "Single Voice Kata", "Vanishing Immersion Style", "Discerning Savants Eye", "Power-Snaring Image",
    "Flashing Quill Atemi", "Mind-Swallowing Missive", "Cup Boils Over", "Twisted Words Technique", "Excellent Emissarys Tongue", "Perfect Recollection Discipline", "Swift Sages Eye", "Mind-Scribing Method", "Heaven-Drawing Discipline", "Perfect Celestial Author", "Unbreakable Fascination Method", "Wyld-Dispelling Prana", "Chaos-Repelling Pattern", "Harmonious Academic Methodology", "First Knowledges Grace", "Flowing Mind Prana", "Essence-Lending Method", "Will-Bolstering Method", "Hidden Wisdom Bestowal", "Tireless Learner Method", "Bottomless Wellspring Approach", "Lore-Inducing Concentration", "Truth-Rendering Gaze", "Wound-Accepting Technique", "Essence Font Technique", "Legendary Scholars Curriculum", "Selfsame Master Instructor", "Sacred Relic Understanding", "Wake the Sleeper", "Heaven-Turning Calculations", "Injury-Forcing Technique", "Essence-Draining Touch", "Essence-Twining Method", "Force-Draining Whisper", "Immanent Solar Glory", "Flowing Essence Conversion",
    "Power-Restoring Invocation", "Surging Essence Flow", "Order-Affirming Blow", "Wyld-Shaping Technique", "Hero-Induction Method", "Wyld Cauldron Mastery", "Wyld-Called Weapon", "Wyld-Forging Focus", "Tome-Rearing Gesture", "Power-Awarding Prana", "Prophet of Seventeen Cycles", "Will-Shattering Illusion", "Surging Inner Fire", "Seal of Infinite Wisdom", "Sevenfold Savant Mantle", "Power Beyond Reason", "Manse-Raising Method", "Demiurgic Suspiration", "God-Kings Shrike (Dogstar Ruminations)", "Incalculable Flowing Mind", "Unstoppable Magnus Approach", "Savant of Nine Glories", "Ailment-Rectifying Method", "Plague-Banishing Incitation", "Wound-Mending Care Technique", "Wound-Cleansing Meditation", "Flawless Diagnosis Technique", "Contagion-Curing Touch", "Instant Treatment Methodology", "Wound-Banishing Strike", "Touch of Blissful Release", "Feit of Imparted Nature", "Body-Purifying Admonitions", "Anointment of Miraculous Health", "Body-Sculpting Essence Method", "Wholeness-Restoring Meditation",
    "Healing Trance Meditation", "Life-Exchanging Prana", "Anodyne of Celestial Dreaming", "Master Chirurgeon Meditation", "Benison of Celestial Healing", "Life-Sculpting Hands Technique", "Healers Unerring Hands", "Immaculate Solar Physician", "Perfect Celestial Chirurgeon", "Excellent Strike", "Fire and Stones Strike", "One Weapon, Two Blows", "Peony Blossom Technique", "Dipping Swallow Defense", "Bulwark Stance", "War Lion Stance", "Guard-Breaking Technique", "Solar Counterattack", "Call the Blade", "Summoning the Loyal Steel", "Rising Sun Slash", "Agile Dragonfly Blade", "Iron Whirlwind Attack", "Fivefold Bulwark Stance", "Heavenly Guardian Defense", "Hail-Shattering Practice", "Calm and Ready Focus", "Unassailable Guardian Posture", "Ready in Eight Directions Stance", "Glorious Solar Saber", "Iron Raptor Technique", "Sandstorm-Wind Attack", "Edge of Morning Sunlight", "Foe-Cleaving Focus", "Hungry Tiger Technique", "Invincible Fury of the Dawn",
    "Perfect Strike Discipline", "Flashing Edge of Dawn", "Fervent Blow", "Over-and-Under Method", "Immortal Blade Triumphant", "Corona of Radiance", "Sharp Light of Judgment Stance", "Blazing Solar Bolt", "Heaven Sword Flash", "Circle of Bright Reaving", "Protection of Celestial Bliss", "Spirit-Detecting Glance", "Uncanny Perception Technique", "Keen Unnatural Eye", "Spirit-Cutting Attack", "Spirit-Draining Stance", "Ghost-Eating Technique", "Phantom-Seizing Strike", "Spirit-Slaying Stance", "Uncanny Shroud Defense", "Spirit-Manifesting Word", "Ancient Tongue Understanding", "Supernal Control Method", "All-Encompassing Sorcerers Sight", "Carnal Spirit Rending", "Burning Exorcism Technique", "Breath-Drinker Method", "Spirit-Repelling Diagram", "Nine Specters Ban", "Spirit-Caging Mandala", "Material Exegesis Prana", "Dark-Minders Observances", "Burning Eye of the Deliverer", "Soul Projection Method", "Wyld-Binding Prana", "Spirit-Draining Mudra",
    "Demon-Compelling Noose", "All Souls Benediction", "Gloaming Eye Understanding", "Sorcerers Burning Chakra", "Immortal Soul Vigil", "Spirit-Shredding Exorcism", "Spirit-Drawing Oculus", "Ephemeral Induction Technique", "Terrestrial Circle Sorcery", "Celestial Circle Sorcery", "Solar Circle Sorcery", "Masterful Performance Exercise", "Soul-Firing Performance", "Stillness-Drawing Meditation", "Trance of Fugue Vision", "Penultimate Unity of Form", "Soul-Bracing Momentous Power", "Unmatched Showmanship Style", "Soul Voice", "Pivotal Encore Performance", "Respect-Commanding Attitude", "Phantom-Conjuring Performance", "Memory-Reweaving Discipline", "Demon Wracking Shout", "Impassioned Orator Technique", "Fury Inciting Speech", "Dogmatic Contagion Discipline", "Infectious Zealotry Approach", "Perfect Harmony Technique", "Mood-Inducing Music", "Battle Anthem (of the Solar Exalted)", "Plectral Harbingers Approach", "Heart-Compelling Method", "Soul-Stirring Cantata", "Heroism-Encouraging Ballad", "Graceful Reed Dancing",
    "Battle-Dancer Method", "Shining Expression Style", "Winding Sinuous Motion", "Monk-Seducing Demon Dance", "Master Thespian Style", "Voice-Hurling Method", "Cunning Mimicry Technique", "Most Excellent Mockingbird", "Splendid Magpie Approach", "Thousand Courtesan Ways", "Celestial Bliss Trick", "Listener-Swaying Argument", "Harmonious Presence Meditation", "Excellent Friend Approach", "Tigers Dread Symmetry", "Impassioned Discourse Technique", "Empowering Shout", "Majestic Radiant Presence", "Underling-Promoting Touch", "Threefold Magnetic Ardor", "Awakened Carnal Demiurge", "Enemy-Castigating Solar Judgment", "Fulminating Word", "Authority-Radiating Stance", "Terrifying Apparition of Glory", "Blazing Glorious Icon", "Mind-Wiping Gaze", "Hypnotic Tongue Technique", "Worshipful Lackey Acquisition", "Prophet-Uplifting Evocation", "Shedding Infinite Radiance", "Rose-Lipped Seduction Style", "Crowned King of Eternity", "Favor-Conferring Prana", "Countenance of Vast Wrath", "Durability of Oak Meditation",
    "Spirit Strengthens the Skin", "Iron Skin Concentration", "Ox-Body Technique", "Body-Mending Meditation", "Front-Line Warriors Stamina", "Whirlwind Armor-Donning Prana", "Armored Scouts Invigoration", "Poison-Resisting Meditation", "Essence-Gathering Temper", "Diamond-Body Prana", "Iron Kettle Body", "Adamant Skin Technique", "Tiger Warriors Endurance", "Hauberk-Summoning Gesture", "Illness-Resisting Meditation", "Willpower-Enhancing Spirit", "Battle Fury Focus", "Wound-Knitting Exercise", "Unbreakable Warriors Mastery", "Ruin-Abasing Shrug", "Glorious Solar Plate", "Immunity to Everything Technique", "Fury-Fed Ardor", "Bloodthirsty Sword-Dancer Spirit", "Aegis of Invincible Might", "Master Horsemans Techniques", "Flashing Thunderbolt Steed", "Elusive Mount Technique", "Wind-Racing Essence Infusion", "Single Spirit Method", "Seasoned Beast-Riders Approach", "Worthy Mount Technique", "Mount Preservation Method", "Harmonious Tacking Technique", "Untouchable Horsemans Attitude", "Immortal Chargers Gallop",
    "Supernal Lash Discipline", "Speed-Fury Focus", "Inexhaustible Destriers Gait", "Coursing Firebolt Flash", "Saddle-Staying Courses", "Horse-Stealing Leap", "Immortal Riders Advantage", "Horse-Healing Technique", "Rousing Backlash Assault", "Woe and Storm Evasion", "Resilience of the Chosen Mount", "Phantom Steed", "Hero Rides Away", "Phantom Riders Approach", "Fierce Chargers Pulse", "Grizzled Cataphracts Way", "Rapid Cavalry Approach", "Sometimes Horses Fly Approach", "Soaring Pegasus Style", "Whirlwind Horse-Armoring Prana", "Bard-Lightening Prana", "Untouchable Solar Steed", "Wrathful Mount Invigoration", "Seven Cyclones Rearing", "Iron Simhata Style", "Salty Dog Method", "Shipwreck-Surviving Stamina", "Fathoms-Fed Spirit", "Safe Bearing Technique", "Ship-Claiming Stance", "Ship-Sleeking Technique", "Orichalcum Letters of Marque", "Immortal Mariners Advantage", "Legendary Captains Signature", "Sea Ambush Technique", "Deck-Sweeping Fusillade",
    "Ship-Breaker Method", "Superior Positioning Technique", "Ship-Imperiled Vigor", "Weather-Anticipating Intuition", "Tide-Cutting Essence Infusion", "Wave-Riding Discipline", "Hull-Preserving Technique", "Hull-Taming Transfusion", "Ship-Leavening Meditation", "Indomitable Voyagers Perseverance", "Ocean-Conquering Avatar", "Wind-Defying Course Technique", "Current-Cutting Technique", "Implacable Sea Wolf Spirit", "Deadly Ichneumon Assault", "Rail-Storming Fervor", "Sea Serpent Flash", "Tide-Carried Omens", "Chaos-Cutting Galley", "Blood and Salt Bondage", "Ship-Sustaining Spirit", "Burning Anima Sails", "Storm-Weathering Essence Infusion", "Invincible Admiral Method", "Sea Devil Training Technique", "Ship-Rolling Juggernaut Method", "Ship-Razing Renewal", "Black Fathoms Blessed", "Mastery of Small Manners", "Motive-Discerning Technique", "Quicksilver Falcons Eye", "Umbral Eyes Focus", "Humble Servant Approach", "Shadow Over Day", "Night Passes Over", "Intent-Tracing Stare",
    "Culture Hero Approach", "Unimpeachable Discourse Technique", "Indecent Proposal Method", "Dauntless Assayer Method", "Preeminent Gala Knife", "Wise-Eyed Courtier Method", "Discretionary Gesture", "Deep-Eyed Soul Gazing", "Easily-Discarded Presence Method", "Guarded Thoughts Meditation", "Penumbra Self Meditation", "Inverted Ego Mask", "Cunning Insight Technique", "Doubt-Sowing Contention Method", "Effective Counterargument", "Wise Counsel (Flashing Soul Reform)", "Endless Obsession Feint", "Aspersions Cast Aside", "Asp Bites Its Tail", "Fete-Watcher Stance", "Seen and Seeing Method", "Face-Charming Prana", "Selfsame Master Procurer", "Soul-Void Kata", "Knowing the Souls Price", "Understanding the Court", "Unbound Social Mastery", "Heart-Eclipsing Shroud", "Hundred-Faced Stranger", "Legend Mask Methodology", "Friend of a Friend Approach", "Venomous Rumors Technique", "Even-Touched Prophet", "Elusive Dream Defense", "Draw the Curtain", "At Your Service",
    "Fugue-Empowered Other", "Soul Reprisal", "Perfect Shadow Stillness", "Invisible Statue Spirit", "Easily-Overlooked Presence Method", "Blinding Battle Feint", "Stalking Wolf Attitude", "Guardian Fog Approach", "Blurred Form Style", "Mental Invisibility Technique", "Shadow Victors Repose", "Flash-Eyed Killers Insight", "Hidden Snake Recoil", "Dark Sentinels Way", "Smoke and Shadow Cover", "Sun Swallowing Practice", "Vanishing From Minds Eye Method", "Sound and Scent Banishing Attitude", "Ten Whispers Silence Meditation", "Mind Shroud Meditation", "Shadow Replacement Technique", "Shadow-Crossing Leap Technique", "Fivefold Shadow Burial", "False Image Feint", "Flashing Nocturne Prana", "Food-Gathering Exercise", "Hardship-Surviving Mendicant Spirit", "Friendship with Animals Approach", "Trackless Region Navigation", "Unshakeable Bloodhound Technique", "Spirit-Tied Pet", "Beast-Mastering Behavior", "Deadly Onslaught Coordination", "Bestial Traits Technique", "Hide-Hardening Practice", "Life of the Aurochs",
    "Familiar-Honing Instruction", "Spirit-Hunting Hound", "Ambush Predator Style", "Element-Resisting Prana", "Traceless Passage", "Eye-Deceiving Camouflage", "Red-Toothed Execution Order", "Ghost Panther Slinking", "Saga Beast Virtue", "Phantom-Rending Fangs", "Force-Building Predator Style", "Crimson Talon Vigor", "Deadly Predator Method", "Precision of the Striking Raptor", "Steel Storm Descending", "Flashing Draw Mastery", "Joint-Wounding Attack", "Angle-Tracing Edge", "Triple Distance Attack Technique", "Cascade of Cutting Terror", "Swarm-Culling Instinct", "Mist on Water Attack", "Observer-Deceiving Attack", "Flying Steel Ruse", "Empty Palm Technique", "Fallen Weapon Deflection", "Mist-Gathering Practice", "Shower of Deadly Blades", "Shrike Saving Discretion", "Crimson Razor Wind", "Sharp Hand Feint", "Shadow Wind Slash (Shadow Wind Kill)", "Shadow Thrust Spark", "Savage Wolf Attack", "Falling Icicle Strike", "Fiery Solar Chakram",
    "Cutting Circle of Destruction", "War God Descendent", "Immortal Commanders Presence", "League of Iron Preparation", "Rout-Stemming Gesture", "Holistic Battle Understanding", "Ideal Battle Knowledge Prana", "Tiger Warrior Training Technique", "Magnanimity of the Unstoppable Icon", "Redoubt-Raising Gesture", "General of the All-Seeing Sun", "Immortal Warlords Tactic", "Battle Path Ascendant", "March of the Returner", "Supremacy of the Divine Army", "Four Glories Meditation", "Transcendent Warlords Genius", "Battle-Visionarys Foresight"
]

AttributeStrength = ExaltedAttributeClass('Strength')
AttributeDexterity = ExaltedAttributeClass('Dexterity')
AttributeStamina = ExaltedAttributeClass('Stamina')
AttributeCharisma = ExaltedAttributeClass('Charisma')
AttributeManipulation = ExaltedAttributeClass('Manipulation')
AttributeAppearance = ExaltedAttributeClass('Appearance')
AttributePerception = ExaltedAttributeClass('Perception')
AttributeIntelligence = ExaltedAttributeClass('Intelligence')
AttributeWits = ExaltedAttributeClass('Wits')

AbilityArchery = ExaltedAbilityClass('Archery')
AbilityAthletics = ExaltedAbilityClass('Athletics')
AbilityAwareness = ExaltedAbilityClass('Awareness')
AbilityBrawl = ExaltedAbilityClass('Brawl')
AbilityBureaucracy = ExaltedAbilityClass('Bureaucracy')
AbilityCraft = ExaltedAbilityClass('Craft')
AbilityDodge = ExaltedAbilityClass('Dodge')
AbilityIntegrity = ExaltedAbilityClass('Integrity')
AbilityInvestigation = ExaltedAbilityClass('Investigation')
AbilityLarceny = ExaltedAbilityClass('Larceny')
AbilityLinguistics = ExaltedAbilityClass('Linguistics')
AbilityLore = ExaltedAbilityClass('Lore')
AbilityMartialArts = ExaltedAbilityClass('MartialArts')
AbilityMedicine = ExaltedAbilityClass('Medicine')
AbilityMelee = ExaltedAbilityClass('Melee')
AbilityOccult = ExaltedAbilityClass('Occult')
AbilityPerformance = ExaltedAbilityClass('Performance')
AbilityPresence = ExaltedAbilityClass('Presence')
AbilityResistance = ExaltedAbilityClass('Resistance')
AbilityRide = ExaltedAbilityClass('Ride')
AbilitySail = ExaltedAbilityClass('Sail')
AbilitySocialize = ExaltedAbilityClass('Socialize')
AbilityStealth = ExaltedAbilityClass('Stealth')
AbilitySurvival = ExaltedAbilityClass('Survival')
AbilityThrown = ExaltedAbilityClass('Thrown')
AbilityWar = ExaltedAbilityClass('War')

CasteDawn = ExaltedCasteClass('Dawn', ['Archery', 'Awareness', 'Brawl/Martial Arts', 'Dodge', 'Melee', 'Resistance', 'Thrown', 'War'])
CasteZenith = ExaltedCasteClass('Zenith', ['Athletics', 'Integrity', 'Performance', 'Lore', 'Presense', 'Resistance', 'Survival', 'War'])
CasteTwilight = ExaltedCasteClass('Twilight', ['Bureaucracy', 'Craft', 'Integrity', 'Investigation', 'Linguistics', 'Lore', 'Medicine', 'Occult'])
CasteNight = ExaltedCasteClass('Night', ['Athletics', 'Awareness', 'Dodge', 'Investigation', 'Larceny', 'Ride', 'Stealth', 'Socialize'])
CasteEclipse = ExaltedCasteClass('Eclipse', ['Bureaucracy', 'Larceny', 'Linguistics', 'Occult', 'Presence', 'Ride', 'Sail', 'Socialize'])

KeywordAggravated = ExaltedCharmKeywordClass("Aggravated", "The Health Track damage inflicted by this Charm cannot be healed magically, nor can magic be used to speed up the natural process of healing it.")
KeywordBridge = ExaltedCharmKeywordClass("Bridge",  "A Charm with this keyword can be purchased with alternate prerequisites from another Ability. If all the prerequisites used to buy a Bridge Charm enjoy a Caste/Favored cost discount, so does the Bridge Charm. No non-Integrity Charm can act as a prerequisite for more than one Bridge Charm, and Integrity Charms can never serve as an alternate Bridge prerequisite. If Integrity is Caste or Favored, the character may buy in via half the listed number of Bridge prerequisites (round up, or round down if Supernal).")
KeywordClash = ExaltedCharmKeywordClass("Clash", "Cannot be used simultaneously with or in response to a Charm with the Counterattack keyword.")
KeywordCounterattack = ExaltedCharmKeywordClass("Counterattack", "Cannot be used in reaction to a Charm with the Counterattack or Clash keyword")
KeywordDecisiveOnly = ExaltedCharmKeywordClass("Decisive-only", "If it’s an attack Charm, the Charm can only be used with a decisive attack. If it is a defensive Charm, it can only be used to defend against a decisive attack.")
KeywordDual = ExaltedCharmKeywordClass("Dual", "This Charm has two different functions, one for withering and one for decisive.")
KeywordMute = ExaltedCharmKeywordClass("Mute", "This Charm’s cost will not add to the Exalt’s anima level unless she wants it to.")
KeywordPilot = ExaltedCharmKeywordClass("Pilot", "The character must be the captain or the helmsman of the sailing vessel to use this Charm.")
KeywordPsyche = ExaltedCharmKeywordClass("Psyche", "A power with this keyword is an unnatural, hypnotic, or sorcerous power that magically influences, controls, or cripples an opponent’s thoughts or feelings.")
KeywordPerilous = ExaltedCharmKeywordClass("Perilous", "Be cautious about your reliance on this Charm! Charms with this keyword cannot be used in Initiative Crash.")
KeywordSalient = ExaltedCharmKeywordClass("Salient", "This keyword indicates that the Charm’s cost requires silver, gold, and white points for major, superior, and legendary craft projects, respectively.")
KeywordStackable = ExaltedCharmKeywordClass("Stackable", "This Charm’s effects can stack. • Uniform: This Charm has the same function for both withering and decisive attacks or defenses.")
KeywordWitheringOnly = ExaltedCharmKeywordClass("Withering-only", "If it’s an attack Charm, the Charm can only be used with a withering attack. If it is a defensive Charm, it can only be used to defend against a withering attack.")
KeywordWrittenOnly = ExaltedCharmKeywordClass("Written-only", "A Charm with this keyword can only be used to enhance, supplement, or create written social influence.")

LIST_ATTRIBUTE = [AttributeStrength, AttributeDexterity, AttributeStamina, AttributeCharisma, AttributeManipulation, AttributeAppearance, AttributePerception, AttributeWits]
LIST_CHARM_KEYWORDS = [KeywordAggravated, KeywordBridge, KeywordClash, KeywordCounterattack, KeywordDecisiveOnly, KeywordDual, KeywordMute, KeywordPilot, KeywordPsyche, KeywordPerilous, KeywordSalient, KeywordWitheringOnly, KeywordWrittenOnly]
LIST_CASTE = [CasteDawn, CasteZenith, CasteTwilight, CasteNight, CasteEclipse]
LIST_ABILITIES = [AbilityArchery, AbilityAthletics, AbilityAwareness, AbilityBrawl, AbilityBureaucracy, AbilityCraft, AbilityDodge, AbilityIntegrity, AbilityInvestigation, AbilityLarceny, AbilityLinguistics, AbilityLore, AbilityMartialArts,AbilityMedicine, AbilityMelee, AbilityOccult, AbilityPerformance, AbilityPresence, AbilityResistance, AbilityRide, AbilitySail, AbilitySocialize, AbilityStealth, AbilitySurvival, AbilityThrown, AbilityWar]
LIST_CHARMS = charm_names

if __name__ == "__main__":

    DataExaltedCharms = safe_load(open('exalted_3e_data/charms.yaml', 'rt'))

    def get_charm(charm:str = None):
        if charm is None or charm not in charm_names:
            charm = choice(charm_names)
        return ExaltedCharmClass(
            charm,
            DataExaltedCharms[charm]['Cost'],
            DataExaltedCharms[charm]['Mins'],
            DataExaltedCharms[charm]['Type'],
            DataExaltedCharms[charm]['Keywords'],
            DataExaltedCharms[charm]['Duration'],
            DataExaltedCharms[charm]['Prerequisite Charms'],
            DataExaltedCharms[charm]['Description']
        )

