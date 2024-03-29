# anki-reference-addon

## Description
Anki Reference Addon is an addon which helps with language learning by automating of creation of [Anki](https://apps.ankiweb.net) flash cards. It allows download previously saved words and generated audio from Anki Reference Bot.

Currently supported only English and French languages.

This addon works together with [Anki Reference Bot](https://github.com/glebmark/anki-reference-bot)
## Installation to Anki
### Requirements
- [Anki](https://apps.ankiweb.net) 2.1+
### Deployment
- download archive with code
- locate addons folder: Anki > Tools > Add-ons > View files
- create folder with custom name, for example "ankireference" (only a-z and 0-9 allowed)
- Copy files to created folder (`__init__.py` should be accessible at `~/folder_name/__init__.py` path)

### Set variables
As it isn't standalone app but addon to Anki, variables couldn't be set in environment, but have to be edited in main.py directly:
- edit main.py and set "publicUrl", for example `http://localhost:3000` if you run bot locally, or `http://mydomainname:8080` if you run in Docker at your VPS and have domain name, or IP adress `http://0.0.0.0:8080` if you don't have domain name
- edit main.py and set "tempFilePath" to Anki addon directory at your device
- edit main.py and set "pathForResource" to your Anki's user and it's media collection directory

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
3) Follow development instructions in [Anki's documentation](https://addon-docs.ankiweb.net/intro.html)

### Examples
There is example of what would be downloaded from Bot and then saved to Anki, for example if word 'plain' has been added:
```
<b>plain</b><br><br>pleɪn[sound:54d8bf35-efb0-4271-bbc6-f81709763896.mp3]adjective<br><br><br><br>She wore a plain black dress.[sound:cf16ac26-77e6-4d2d-b0f7-ab6fef45e2cd.mp3]<br><br>We've chosen a plain carpet (= one without a pattern) and patterned curtains.[sound:233bce9f-7a7b-4c13-b027-905f116c4abc.mp3]<br><br>	not decorated in any way; with nothing added: [sound:decc2a1a-a836-4d69-9bee-577ad27287ef.mp3]<br><br>
not decorated in any way; with nothing added: [sound:decc2a1a-a836-4d69-9bee-577ad27287ef.mp3]<br><br>
```