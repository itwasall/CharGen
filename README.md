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
- char_pathfinder_2e.py
- char_pokerole.py
- char_ryuutama.py
- char_savage_worlds.py
- char_tenra_kijin.py
- char_tenra_shiki.py
- char_tenra.py
- char_wta.py
- chargen.py


Cyberpunk 2020
Currently
  - A lot of background character info done.

## Cyberpunk RED
Progress unknown. Don't care enough to check

## DND 5e
Core Rulebook done

## DND 3.5e
Progress unknown. Don't care enough to check

## Exalted
Currently
  - Mostly charm stuff. Which I've done all wrong. The yaml file is like 600k 💀

## Kamigakari
Mostly served as a test for a workflow I hypothesised whilst working on Exalted.
Tests inconlusive, consider abandoned.

## Numenera
Currently
  - Foci data + character type data + descriptor data recorded
  - literally every cypher recorded
  - Lost in OOP hell

## Mork Borg
Core rulebook done

## Pathfinder 2E
Currently
  - Lost in OOP hell

## Pokerole
Currently
  - Crying at how many stats everything has
  - Trying a more imperative approach

## Savage Worlds
Consider Abandoned

## Ryuutama: Fantasy Roleplaying Game
Basically done

## Tenra Bansho Zero
Recording data 
  - archetypes 100% done
  - shiki talisman generation done
  - buddhist martial arts data recorded
  - hou-jutsu data recorded
  - kijin mechanica data recorded
  - kijin mechanica generation begun

## Werewolf: The Apocolaypse
Progress unknown. Don't care enough to check
