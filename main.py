from search.src import getData
import numpy as np
import time

x = []
y = []

start = time.time()

gameKey = 4963050171

def getTrainData(matchId):
    if type(matchId) == int:
        matchId = str(matchId)
    data = getData.getMatchById(matchId)
    
    for i in range(2):
        t = np.zeros(len(getData.championIxDict))
        t_x = np.array([t])
        for j in range(i*5,(i+1)*5):
            championId = data['participants'][j]['championId']
            t[getData.championIxDict[championId]] = 1.
        if data['teams'][i]['win'] == 'Win':
            y.append([1])
            t_y = np.array([[1]])
        else:
            y.append([0])
            t_y = np.array([[0]])
        x.append(t)
    gameKeys = getData.getMatchDataById(data['participantIdentities'][np.random.randint(10)]['player']['currentAccountId'], 100)
    time.sleep(1.5)
    return gameKeys
x = np.load("x1.npy")
y = np.load("y1.npy")
x = x.tolist()
y = y.tolist()
print(len(x))

gameKeys = getTrainData(gameKey)
for _ in range(100):
    u = 0
    for i, key in enumerate(gameKeys):
        if key['queue'] != 420:
            time.sleep(1.5)
            print("no RankGame!!")
            continue
        print(_, i)
        try:
            u = getTrainData(key['gameId'])
        except:
            time.sleep(1.5)
            print('error')
            continue
    gameKeys = u
    
    np.save("x1",np.array(x))
    np.save("y1",np.array(y))
    
    print("length : ", len(x))
    print("elapsed time : ", time.time()-start)

numValidation = int(len(x) * 0.3)
print(len(x))



x = np.array(x)
y = np.array(y)
np.save("x1",x)
np.save("y1",y)

