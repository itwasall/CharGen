import random

character = {
  'inner': ["eccentric", "BTL addict", "gesturing to AR apps", "eyes fixed on commlink", "is beeing followed", "paranoid", "toxic aura", "guilt-ridden", "driven by vengeance", "charismatic", "inquisitive", "curious", "seeking companionship", "avoids physical contact", "VR game addict", "drug addict", "awakened drug addict", "extremely intelligent", "altruistic", "greedy", "narcissistic", "lonely", "well-versed", "multilinguist", "tech-savvy", "high-level firewall"],
  'outer': ["good-looking", "sly smile", "gesturing wildly", "itchy", "scarred", "chrome arms", "chrome face", "chrome legs", "rainbow hair", "mohawk", "mood hair", "cybered up completely", "visible dataport", "blue hair", "violet hair", "pink hair", "black hair", "brunette hair", "skinhead", "bald", "nano tattoos", "glowing tattoos", "punk jacket", "wearing combat gear", "holstered pistol", "sword on their back", "sheathed katana", "flashing commlink", "overweight", "severly underweight", "heavily overweight", "corporate suit", "biker gear", "gang tattoos", "coughing"],
  'mood': ["in party mood", "wants to sleep", "good mood", "annoyed", "focussed on work", "tired", "flirty", "happy", "depressed", "forthcoming", "open arms", "worried", "scared"]
}
job = {
  'description': ["Accessory designer", "Advertising designer", "Animator", "Architect", "Art administrator", "Artisan", "Arts administration", "Baker", "Ceramics artist", "Chief creative officer", "Colorist", "Concept Artist", "Curator", "Dancer", "Design director", "Design strategist", "Essayist", "Event planner", "Fashion designer", "Floral designer", "Graphic designer", "Hairstylist", "Illustrator", "Tattoo artist", "Interior designer", "Jewellery designer", "Lyricist", "Make-up artist", "Marine designer", "Media designer", "Music", "Party planner", "Penciller", "Photographer", "Photojournalist", "Production designer", "Sculptor", "Set decorator", "Set dresser", "Web designer", "Wedding planner", "Writer", "Anesthesiologist", "Nurse", "Respiratory Therapist", "Cardiologist", "Dermatologist", "Emergency physician", "Geriatrician", "Haematologist", "Laboratory Tech", "Phlebotomist", "Neurologist", "Optometrist", "Pharmacist", "Pediatrician", "Neonatal Nurse", "Psychiatrist", "Psychologist", "Biokineticist", "Athletic Trainer", "Yoga Instructor", "Radiologist", "Radiographer", "Obstetrician", "Gynaecologist", "Neurosurgeon", "General Doctor", "Dental Nurse", "Attorney", "Actor", "Comedian", "Dancer", "Drag Queen", "Drag King", "Filmmaker", "Geisha", "Poet", "Showgirl", "Showman", "Showrunner", "Skomorokh", "Stunt performer", "Theatre practitioner", "Writer", "Porn Actor", "Musician", "Painter", "Party princess", "Lighting technician", "Video editor", "News presenter", "Reporter", "Newscaster", "Anchorman", "Production", "Executive producer", "Author", "Blogger", "Creative consultant", "Freelance writer", "Hack writer", "Journalist", "Literary editor", "Manuscript format", "Novelist", "Screenwriter", "Script doctor", "Scrivener", "Songwriter", "Speechwriter", "Technical writer", "Writer", "Auto mechanic", "Foreman", "Maintenance engineering", "Mechanic", "Miller", "Patternmaker", "Plant operator", "Plumber", "Welder", "Stationary engineer", "Woodworker", "Bartender", "Waiter", "Construction worker", "Factory worker", "Gunsmith", "Furniture maker", "Rigger", "Laborer", "Miner", "Mechanical engineer", "Chemical engineer", "Industrial engineer", "Materials engineer", "Tailor", "Taxidermist", "Taxi driver", "Chauffeur", "Test driver", "Delivery driver", "Bus driver", "Truck driver", "Rapid prototyper", "Test engineer", "Visual designer", "Cook", "Clerk", "Barber", "Drone Rigger", "VR designer", "Matrix guide", "Grid guide", "Tourist guide", "Hotel Clerk", "Painter", "Aircraft Mechanic", "Cleaner", "Firefighter", "Dishwasher", "Farm worker", "Soy wrangler", "Electrician", "Childcare worker", "Parking lot Attendant", "Bartender", "Shadowrunner", "Pro gamer", "Streamer", "Influencer", "Waiter"],
  'level': ["Senior", "Junior", "Principal", "Specialist", "Chief", "Chief Executive"],
  'position': ["Analyst", "Lead", "Manager", "Vice Director", "Director", "Analyst", "Assistant", "Auditor", "Assessor", "Officer", "Accountant", "Team Lead", "Specialist", "Developer", "Consultant", "Consulting Manager", "Consultat Director", "Intern", "Secretary", "Attorney",],
  'branch': ["Management", "Facility", "Business", "Small Business", "Large Business", "Account", "Key Account", "Regional", "International", "Corporate", "Inter-Corporate", "Social Media", "Matrix", "Corporate Grid", "Territory", "Financial", "Finance", "Accounting", "Bookkeeping", "Budget", "Cash", "Controlling", "Credit", "Tax", "Asset", "Corporate Asset", "Trade", "Expansion", "Technology", "Research", "QA", "Magic", "Software", "Liquidation", "Early Adoption", "Hardware", "Enterprise", "Outsourcing", "Strategic", "Upscaling", "Rightscaling", "Data Science", "Lifecycle", "Customer", "Personalization", "Human Resources", "Resources", "Diversification", "Buzzword", "Legal", "Production", "Public relations", "Innovation", "Investment", "Communication", "Compliance", "Risk", "Brand"]
}
runner = {
  'profession': ["Decker", "Shaman", "Rigger", "Mage", "Gun Nut", "Sharpshooter", "Technomancer", "Mage Adept", "Street Samurai", "Adept", "Street Sam", "Combat Mage", "Drone Rigger", "Security Decker", "Johnson", "Assassin", "Corporate Spy", "Face", "Fixer", "Sharpshooter", "Sniper", "Thief", "Martial Artist", "Decker", "Shaman", "Rigger", "Mage", "Gun Nut"],
  'level': ["Veteran", "Proficient", "Newbie", "Aspiring", "Settled-down", "Average", "Below average", "Above average", "Legendary", "Specialized", "Competent", "Incompetent", "Professional", "Ex", "Former", "Good"]
}

class NPC:
    def __init__(self, name: None, **kwargs):
        self.name = name
        for k, d in kwargs.items():
            self.__setattr__(k, d)


def get_job(data, desc=False):
    position = random.choice(data['position'])
    level = random.choice(data['level'])
    branch = random.choice(data['branch'])
    a_an = ['an' if branch[0].lower() in "aeiou" else 'a' for _ in range(1)][0]
    if desc:
        job_string = f"NPC is a {level} {description} {position} for {a_an} {branch} organisation"
        return job_string
    else:
        job_string = f"NPC is a {level} {position} for {a_an} {branch} organisation"
        return job_string

def get_runner(data):
    profession = random.choice(data['profession'])
    level = random.choice(data['level'])
    if level[0].lower() in "aeiou":
        runner_string = f"Runner is an {level} {profession}"
    else:
        runner_string = f"Runner is a {level} {profession}"
    return runner_string

print(get_job(job))
print(get_runner(runner))
