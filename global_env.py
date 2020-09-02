import os
import pickle

mainWin = None
myCardWindow = None
enemyCardWindow = None
npcWindow = None
battleReadyWindow = None
dailyBattleWindow = None
pvpWindow = None

myCardList = None
enemyCardList = None
npcList = None
equipStorageDict = None
threads = 4
tests = 1000
verbose = 1

run_args = "bnpc"
saveData = None

test_mode = False


class MyCardListClass(dict):
    def __init__(self, *args, **kwargs):
        super(MyCardListClass, self).__init__(*args, **kwargs)

    def __setitem__(self, *args, **kwargs):
        super(MyCardListClass, self).__setitem__(*args, **kwargs)
        if myCardWindow is not None:
            myCardWindow.myCardListUpdate()

    def __delitem__(self, *args, **kwargs):
        super(MyCardListClass, self).__delitem__(*args, **kwargs)
        myCardWindow.myCardListUpdate()


class EnemyCardListClass(dict):
    def __init__(self, *args, **kwargs):
        super(EnemyCardListClass, self).__init__(*args, **kwargs)

    def __setitem__(self, *args, **kwargs):
        super(EnemyCardListClass, self).__setitem__(*args, **kwargs)
        if enemyCardWindow is not None:
            enemyCardWindow.myCardListUpdate()

    def __delitem__(self, *args, **kwargs):
        super(EnemyCardListClass, self).__delitem__(*args, **kwargs)
        enemyCardWindow.myCardListUpdate()


class NPCListClass(dict):
    def __init__(self, *args, **kwargs):
        super(NPCListClass, self).__init__(*args, **kwargs)

    def __setitem__(self, *args, **kwargs):
        super(NPCListClass, self).__setitem__(*args, **kwargs)
        if npcWindow is not None:
            npcWindow.npcListUpdate()

    def __delitem__(self, *args, **kwargs):
        super(NPCListClass, self).__delitem__(*args, **kwargs)
        npcWindow.npcListUpdate()


def equipStorageDictINIT():
    print("初始化equipStorageDict")
    return {
        "weapon": {
            "不改变": None
        },
        "glove": {
            "不改变": None
        },
        "Armor": {
            "不改变": None
        },
        "helmet": {
            "不改变": None
        }
    }


def initSaveData():
    global saveData, myCardList, enemyCardList, npcList, threads, tests, verbose, equipStorageDict
    saveData = {
        'setting': {"exeDir": None},
        'data': {
            "myCardList": MyCardListClass({"新卡片": None}),
            "enemyCardList": EnemyCardListClass({"新卡片": None}),
            "npcList": NPCListClass({"新npc": None}),
            "equipStorageDict": equipStorageDictINIT(),
            "threads": threads,
            "tests": tests,
            "verbose": verbose
        }
    }
    myCardList = saveData["data"]["myCardList"]
    enemyCardList = saveData["data"]["enemyCardList"]
    npcList = saveData["data"]["npcList"]
    equipStorageDict = saveData["data"]["equipStorageDict"]


def storeSaveData():
    saveData["data"]["myCardList"] = myCardList
    saveData["data"]["enemyCardList"] = enemyCardList
    saveData["data"]["npcList"] = npcList
    saveData["data"]["equipStorageDict"] = equipStorageDict
    saveData["data"]["threads"] = threads
    saveData["data"]["tests"] = tests
    saveData["data"]["verbose"] = verbose

    file_path = os.path.join(".", "ggzgui")
    with open(file_path, 'wb') as f:
        pickle.dump(saveData, f)
        # data_saved = True


def readSaveData():
    global saveData, myCardList, enemyCardList, npcList, equipStorageDict, threads, tests, verbose
    file_path = os.path.join(".", "ggzgui")
    try:
        with open(file_path, 'rb') as f:
            saveData = pickle.load(f)
            myCardList = saveData["data"]["myCardList"]
            enemyCardList = saveData["data"]["enemyCardList"]
            npcList = saveData["data"]["npcList"]
            if saveData["data"].__contains__("equipStorageDict"):
                equipStorageDict = saveData["data"]["equipStorageDict"]
            else:
                equipStorageDict = equipStorageDictINIT()
            if saveData["data"].__contains__("threads"):
                threads = saveData["data"]["threads"]
            if saveData["data"].__contains__("tests"):
                tests = saveData["data"]["tests"]
            if saveData["data"].__contains__("verbose"):
                verbose = saveData["data"]["verbose"]

    except FileNotFoundError:
        return False
    return True
