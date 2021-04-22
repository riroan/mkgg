from keras.models import load_model
import numpy as np
from search.src import getData

modelList = ["model4.h5","model5.h5","model6.h5","model7.h5","model8.h5","model9.h5","model10.h5","model11.h5","model12.h5"]

model = [load_model(i) for i in modelList]
#model = load_model("model.h5")
#model.summary()


def f(c1,c2,c3,c4,c5):
    x = np.zeros(len(getData.championIxDict), dtype = np.float64)
    
    x[getData.championIxDict[int(getData.championDictInverse[c1])]] = 1
    x[getData.championIxDict[int(getData.championDictInverse[c2])]] = 1
    x[getData.championIxDict[int(getData.championDictInverse[c3])]] = 1
    x[getData.championIxDict[int(getData.championDictInverse[c4])]] = 1
    x[getData.championIxDict[int(getData.championDictInverse[c5])]] = 1
    y = np.array([m.predict(np.array([x]))[0][0] for m in model])
    
    cnt = 0
    
    for i in y:
        if i > 0.5:
            cnt+=1
            
    if cnt > y.shape[0] / 2:
        print("승리")
    else:
        print("패배")
    print(y)
    
f("레넥톤","그레이브즈","신드라","카이사","갈리오")
