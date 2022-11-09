# cdt_2022
[![License: AGPL
v3](https://img.shields.io/badge/License-AGPL_v3-blue.svg)](https://www.gnu.org/licenses/agpl-3.0)

Dit is het repo voor CDT project. 
Onderhouden door Colin, Danae, Jimmy, Lex, Nina, Sven en Jara. 
Minor Data Science 2022.

## Onderzoeksdoel
Valideren van de interpretatie gemaakt door 23andMe (en mogelijk door andere commeciële partij) met het nieuweste onderzoekuitvinding.

## Roadmap

### Modal
1. Een library zal worden opgebouwd uit ClinVar database met behulp van text mining. 
2. De CDT is dan uitgevoerd dankzij een automatisering algoritme (te programeren).

### Wiki toevoegen
Onderstaande onderwerpen moet nog aanmaken.
- achtgrond en doelstelling in home page
- Installatie
- Syntax en Usage

## Usage
Query record with private id (the private id used in the example files under `res/` is `iid`) or rsid and export these record separately in a file can be done with `iid_query.sh`. The manpage of this script is under `man/`, usage of this script can also be checked by supplying `-h` option. Below is the syntax of the command:
```sh
$ src/iid_query.sh [-hr] [-s path/to/source_dir] [-D path/to/destination_dir]
```
Note:
- With `-r` the command will execute in reverse mode.
- Either case option `-s` and `-D` can be left empty. However, when `-s` is left empty, the script assumes that the file to be read is at the current working directory.
- The file to-be-read must in `.gt` format, if not please add `.gt` extension to the file.
- Each line in the file should starts with ID. The ID may present in different format (e.g. private ID may be `iid`, `aa`, `1234` etc.), however, rsid must start with `rs`.
- Comments in the file are omitted.

*tbd*

## Werken in dit Git repo
Vergeet niet eerst `pull` of `fetch` het repo voor dat je begin met werken!

- Source coden en installatie gids kunnen onder het map `src` vinden.
- Resource of een notitie van resource die in dit project gebruikt, vindt u onder het map `res`.
- Onder `man` vindt u het documentatie voor het gebruik van de software, andere documentaties vinden plaats onder `doc`.
- `test` bevat `yaml` of andere test automatisering om de coden te checken.

## Accreditatie en License
De gebruik van dit project wordt begeleid met AGPLv3 tenzij de gebuiker projectlid is. 
