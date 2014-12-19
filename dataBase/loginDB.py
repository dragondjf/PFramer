import json


class LoginDB(object):
    def __init__(self):
        super(LoginDB, self).__init__()
        self.init()
    
    def init(self):
        self.initData()

    def _set(self, loginDict):
        for key in loginDict:
            setattr(self, key, loginDict[key])

        self.loginDict = loginDict

    def initData(self):
        fd = open("DBFILE/login.db", "r")
        loginStr = fd.read()
        fd.close()
        loginDict = json.loads(loginStr)
        self._set(loginDict)
    
    def updateLoginDB(self, loginDict):
        loginStr = json.dumps(loginDict, indent=2)
        fd = open("DBFILE/login.db", "w")
        loginStr = fd.write(loginStr)
        fd.close()
        self._set(oginDict)


login_DB = LoginDB()