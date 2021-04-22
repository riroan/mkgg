import json
import requests
import datetime
import numpy as np
from urllib import parse
import urllib.request

DEVELOPMENTAPIKEY = "RGAPI-6a4f9667-881f-4886-a40a-747ac29ada48"

headers = {
    "Origin": "https://developer.riotgames.com",
    "Accept-Charset": "application/x-www-form-urlencoded; charset=UTF-8",
    "X-Riot-Token": DEVELOPMENTAPIKEY,
    "Accept-Language": "ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36"
}


def apiKey():
    return DEVELOPMENTAPIKEY


def encryptAccountId(summonerName):
    data = getDataByName(summonerName)
    return data["accountId"]


def getDataByName(summonerName):
    encodingSummonerName = parse.quote(summonerName)
    APIURL = "https://kr.api.riotgames.com/lol/summoner/v4/summoners/by-name/" + encodingSummonerName
    res = requests.get(APIURL, headers=getHeaders())
    data = res.json()
    return data


def getPlayerInfo(summonerName):
    id = getDataByName(summonerName)['id']
    APIURL = "https://kr.api.riotgames.com/lol/league/v4/entries/by-summoner/" + id
    res = requests.get(APIURL, headers=getHeaders())
    data = res.json()
    return data


def getMatchData(summonerName):
    encrypId = encryptAccountId(summonerName)
    APIURL = "https://kr.api.riotgames.com/lol/match/v4/matchlists/by-account/" + encrypId
    res = requests.get(APIURL, headers=getHeaders())
    data = res.json()
    return data


def getMatchDataById(accountId, numMatch=10):
    APIURL = "https://kr.api.riotgames.com/lol/match/v4/matchlists/by-account/" + accountId
    res = requests.get(APIURL, headers=getHeaders())
    data = res.json()
    return data['matches'][:numMatch]


def getMatch(summonerName, numMatch=10):
    data = getMatchData(summonerName)
    print(len(data['matches']))
    return data["matches"]


def getRandomMatchId(accountId):
    matches = getMatchDataById(accountId, 100)
    randIx = np.random.randint(len(matches))
    return matches[randIx]['gameId']


def getMatchById(matchId):
    APIURL = "https://kr.api.riotgames.com/lol/match/v4/matches/" + matchId
    res = requests.get(APIURL, headers=getHeaders())
    data = res.json()
    return data


def getHeaders():
    return headers


def getChampionName(championNumber):
    return championDict[str(championNumber)]


def getChampionInfo(championName):
    return champions[championName]


def getAllChampionData():
    j = open("jsonfile/champions.json", 'rt', encoding='UTF8')
    json_data = json.load(j)
    return json_data['data']


def getAllItemData():
    j = open("jsonfile/items.json", "rt", encoding="UTF8")
    json_data = json.load(j)
    return json_data['data']


def downloadChampionIconImage(championName):
    url = 'http://ddragon.leagueoflegends.com/cdn/11.3.1/img/champion/' + championName + '.png'
    downloadImage(url, 'championIcon/' + championName + '.png')


def downloadItemIconImage(itemNumber):
    url = 'http://ddragon.leagueoflegends.com/cdn/11.3.1/img/item/' + itemNumber + '.png'
    downloadImage(url, 'itemIcon/' + itemNumber + '.png')


def downloadImage(url, filename):
    urllib.request.urlretrieve(url, filename)


def getChampionDict():
    championDict = {}
    for champ in champions:
        championDict[champions[champ]['key']] = champions[champ]['name']
    return championDict


def getChampionIxDict():
    championIxDict = {}
    ix = 0
    for champ in champions:
        championIxDict[int(champions[champ]['key'])] = ix
        ix += 1
    return championIxDict


def timestamp2datetime(timestamp):
    return datetime.datetime(timestamp / 1000)


champions = getAllChampionData()
championDict = getChampionDict()
championIxDict = getChampionIxDict()
championDictInverse = {v: k for k, v in championDict.items()}
