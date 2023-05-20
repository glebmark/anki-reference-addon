import requests
import json

from aqt import mw
from aqt.utils import showInfo, qconnect
from aqt.qt import *
from anki.importing import TextImporter

tempFilePath = "/Users/gleb/Library/Application Support/Anki2/addons21/anki_reference_addon"
tempFileName = "/temp.txt"
pathForTitles = tempFilePath + tempFileName

pathForResource = "/Users/gleb/Library/Application Support/Anki2/testuser/collection.media"

publicUrl = 'http://localhost:3000'

def opener(path, flags):
    return os.open(path, flags, 0o777)

def importTitles():
    ti = TextImporter(mw.col, pathForTitles)
    ti.initMapping()
    ti.run()

def loadTitlesAndSave() -> None:
    responseJson = requests.get(publicUrl + '/title')
    response = json.loads(responseJson.content)
    text = response['text']

    if "".__eq__(text):
        showInfo('All titles have been saved')
        return

    with open(pathForTitles , "wb", opener=opener) as f:
        f.write(text.encode('utf-8'))

    uuids = response['audioUUIDs']

    for uuid in uuids:
        responseResource = requests.get(publicUrl + '/resource/' + uuid)
        resourceFileName = "/" + uuid + ".mp3"
        with open(pathForResource + resourceFileName, "wb", opener=opener) as f:
            f.write(responseResource.content)

    importTitles()

    # confirm titles were saved
    requests.post(publicUrl + '/title', params={'titles': response['titleIds']})

    showInfo(str(response['titleNames']))

# TODO make separate button for french?


action = QAction("Load new cards", mw)
# set it to call testFunction when it's clicked
qconnect(action.triggered, loadTitlesAndSave)
# and add it to the tools menu
mw.form.menuTools.addAction(action)
