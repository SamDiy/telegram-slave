from db import Settings
import json

class JSONData:

    def __init__(self, fileName):
        self.fileName = fileName
        try:
            open(fileName, 'r')
        except:
            self._writeJsonData({})

    def _readJsonData(self):
        with open(self.fileName, 'r') as text:
            data = json.load(text)
        return data

    def _writeJsonData(self, data):
        with open(self.fileName, 'w') as text:
            json.dump(data, text, indent=4)

    def getAllData(self):
        return self._readJsonData()

    def setAllData(self, data):
        self._writeJsonData(data)
    
    def getDataByKey(self, key):
        document = self._readJsonData()
        if hasattr(document, key):
            return document[key]
        else:
            return ""

    def setDataByKey(self, key, value):
        data = self._readJsonData()
        data[key] = value
        self._writeJsonData(data)

JSONDocument = JSONData('data.json')

JSONDocument.getDataByKey("api_key")
