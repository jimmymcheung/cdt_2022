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
Query record with private id (the private id used in the example files under `res/` is `iid`) or rsid and export these record separately in a file can be done with `snp_query`. The manpage of this script is under `man/`, usage of this script can also be checked by supplying `-h` option. Below is the syntax of the command:
```sh
$ snp_query [-h|-?|--help] [-r|--reverse] [-v|--version] [-s|--source path/to/source] [-D|--destination path/to/destination] [-f|--file path/to/file]
```
Note:
- With `-r` or `--reverse` the command will execute in reverse mode. In the reverse mode RSID is queried.
- Either case option `-s` and `-D` can be left empty. However, when `-s` is left empty, the script assumes that the file to be read is at the current working directory.
- With `-f` or `--file` single file can be supplied to query either rsid or private SNP ID.
- In normal mode, the file to-be-read must in `.gt` format, if not please add `.gt` extension to the file. However, in single file mode the file extension can be anything than empty.
- Each line in the file should starts with ID. The ID may present in different format (e.g. private ID may be `iid`, `aa`, `1234` etc.), however, rsid must start with `rs`.
- Comments in the file are omitted.

*tbd*

## Known issues
1. The man page could not be opened in macOS Ventura (maybe onwards) due to the removal of `groff`. `groff` is a typesetting system for creating formatted output from text with inline formatting commands.

## Werken in dit Git repo
Vergeet niet eerst `pull` of `fetch` het repo voor dat je begin met werken!

- Source coden en installatie gids kunnen onder het map `src` vinden.
- Resource of een notitie van resource die in dit project gebruikt, vindt u onder het map `res`.
- Onder `man` vindt u het documentatie voor het gebruik van de software, andere documentaties vinden plaats onder `doc`.
- `test` bevat `yaml` of andere test automatisering om de coden te checken.
- **Elke Python web app scripts moeten `#!/usr/bin/env python` hebben op het eerst lijn.**

## Accreditatie en Licentie
Het gebruik van dit project wordt begeleid met AGPLv3 licentie tenzij de gebruiker een van de projectleden is. Wanneer een projectlid gebruik van deze project maken voor hunzelf of hun onderneming, gelden dat de coden van desbetreffende project/product niet hoeft openbaar maken, maar moet wel verklaren voor het gebruik. 

*English Version*

The use of this project (including but not limited to implanting/redistributing the original/modified full/partial codes) shall be guided with AGPLv3 licence, unless the person who tries to make use of this project is/was a contributor of this project during the period 2022/September-2023/January (Hereinafter called "project member"). In case a project member use the code or other resource in this project for themselves or company/for-profit organisation they own, they and the related organisation is exempt from disclosing code/material of related project/product. However, this usage must be declared with the project/product. If this project is used by a project member owned company/organisation, the aforementioned exemption will be revoked when the project member is no longer the largest owner of the organisation.

The aforementioned exemption is not transferable but can be inherited as legacy. After receiving the legacy, the heir(s) is/are regulated as (a) project member(s).
