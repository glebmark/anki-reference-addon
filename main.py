import requests
import json

from aqt import mw
from aqt.utils import showInfo, qconnect
from aqt.qt import *
from anki.importing import TextImporter

tempFilePath = "/Users/gleb/Library/Application Support/Anki2/addons21/anki_reference_addon"
tempFileName = "/sample.txt"
path = tempFilePath + tempFileName

def opener(path, flags):
    return os.open(path, flags, 0o777)

def importTitles():
    ti = TextImporter(mw.col, path)
    ti.initMapping()
    ti.run()

def loadTitlesAndSave() -> None:
    responseJson = requests.get('http://localhost:3000/title')
    response = json.loads(responseJson.content)
    text = response['text']

    if "".__eq__(text):
        showInfo('All titles have been saved')
        return

    # TODO save audio files to folder

    with open(path , "wb", opener=opener) as f:
        f.write(text.encode('utf-8'))

    importTitles()

    # confirm titles were saved
    requests.post('http://localhost:3000/title', params={'titles': response['titleIds']})

    showInfo(str(response['titleNames']))

# TODO make separate button for french?


action = QAction("Load new cards", mw)
# set it to call testFunction when it's clicked
qconnect(action.triggered, loadTitlesAndSave)
# and add it to the tools menu
mw.form.menuTools.addAction(action)
