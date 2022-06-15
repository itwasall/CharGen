# CharGen
I didn't know how to start programming, so I attempted to make a bunch of TTRPG character generators

Work has stared on at least:
- Cyberpunk 2020
- Cyberpunk RED
- Dungeons & Dragons 3.5
- Dungeons & Dragons 5th Edition
- Exalted 3rd Edition
- Kamigakari
- Mork Borg
- Numenera
- Pathfinder 2nd Edition
- Pokerole
- Ryuutama
- Savage Worlds
- Tenra Bansho Zero
- Werewolf the Apocolaypse

## Usage
If a file works (which most don't, as either I'm incompetent, they're unfinished, or I wrote these on linux and didn't think how the code would work on other operating systems), you should just be able to use
```bash
$ python chargen_dnd_5e.py
```
replacing *dnd_5e.py* with the suffix of the generator you want to run (or see fail to run)

### File Breakdown
- char_cyberpunk_2020.py
  - The **CharGen** file for **Cyberpunk 2020**
  - A decent amount of data has been pulled in, most of it superflueous
- char_cyberpunk_red.py
  - The **CharGen** file for **Cyberpunk RED**
  - This hasn't been worked on for a long time, and even then it wasn't worked on for very long
- char_dnd_3.5e_yamltest.py
  - I kept forgetting how PyYaml works so this is a leftover file from me figuring that out for the `nth` time
  - It's kept here to remind me how far I've come, not needing to remember how PyYaml works
- char_dnd_3.5e.py
  - The **CharGen** file for **Dungeons & Dragons 3.5**
  - Not as complete as **char_5e.py** but the basics are there. The list of ints on the first line of output correlates to the ability scores of that character
  - No I don't understand why barbarians have a speed of *Wizardft*
- char_dnd_5e_chance_tables.py
  - I'm sure this had a purpose at some point
- char_dnd_5e.py
  - The **CharGen** file for **Dungeons & Dragons 5th Edition**
  - Easily the most feature complete **CharGen**. Only does level 1 characters, only includes stuff from the PHB, so no funky Xanathar's stuff. Yet.
- char_exalted_3e.py
  - The **CharGen** file for **Exalted 3rd Edition**
  - Fun fact: Did you know this **CharGen** has the highest line count when factoring in all the corressponding `.yaml` data files? Thanks `charms.yaml`!
- char_kamigakari.py
  - The **CharGen** file for **Kamigakari**
  - Pretty much abandoned
- char_mork_borg.py
  - The **CharGen** file for **Mork Borg**
  - No 3rd party stuff is included, but it does have all the stuff from the core book. Was more an exercise in finishing something quickly, there's some really cool MB character generators out there
- char_numenera_old.py
  - Old **Numenera** file
- char_numenera_very_old.py
  - An even older **Numenera** file. Just when you thought the quality of the repo couldn't get worse, *it did*.
- char_numenera.py
  - The **CharGen** file for **Numenera**
  - The most recent crack at a Numenera character generator. Foundations are laid, not much else
- char_pathfinder_2e.py
  - The **CharGen** file for **Pathfinder 2nd Edition**
  - A cautionary tale on OOP abuse
- char_pokerole.py
  - The **CharGen** file for **Poke Role 2nd Edition**
  - Traier stuff done, pokemon not
- char_ryuutama.py
  - The **CharGen** file for **Ryuutama**
  - Not much too generate in **Ryuutama** in all honesty, it's technically done but functionally quite pointless
- char_savage_worlds.py
  - The **CharGen** file for **Savage Worlds**
  - I don't know for which edition. This is considered abandoned
- char_tenra.py
  - The **CharGen** file for **Tenra Bansho Zero**
  - Right now the idea is to split off parts of the character generation into their own separate files, as TBZ's character generation is obtuse and depending on which (for lack of a better word) ""class"" you play determines a whole bunch of mechanics which are unique to that (again, lack of better wording) ""class"".
  - char_tenra_kijin.py
    - The **Tenra Bansho Zero** file for **Kijin** characters
    - I will solve this one day. If this message is still here, then today is not that day.
  - char_tenra_shiki.py
    - The **Tenra Bansho Zero** file for **Shiki** magics
    - Does as it says. Generates legal shiki spells

 - char_wta.py
   - The **CharGen** file for **Werewolf: The Apocolaypse**
   - One of the earlier **CharGen** files, considered abandoned.
- chargen.py
