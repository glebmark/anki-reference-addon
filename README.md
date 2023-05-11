# anki-reference-addon

## Installation in Anki

1) Download archive with code
2) Locate addons folder: Anki > Tools > Add-ons > View files
3) Create folder with custom name, for example "ankireference" (only a-z and 0-9 allowed)
4) Copy files to created folder (`__init__.py` should be accessible at `~/ankireference/__init__.py` path)

TODO: edit some file, add link or IP to server

## Development

### Tested versions
- Python 3.9.6
- Anki 2.1+

### Guide

1) `git clone https://github.com/glebmark/anki-reference-addon.git`
2) Optional for MacOS or GNU/Linux: create symlink, so your addon directory will mirror development directory:

    `ln -s /path/to/development/folder /path/to/anki/addon/folder`

    for example:

    `ln -s /Users/username/code/python/anki_reference_addon /Users/username/Library/Application\ Support/Anki2/addons21`
3) Follow development instructions in [documentation](https://addon-docs.ankiweb.net/intro.html)