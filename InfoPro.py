import operator
def strToFloat(userList):
    newUserList = []
    holderDic ={}
    for i in userList:
        for key, value in d.items():
            if "k" in value:
                value = value[0:value.find("k")]
                holderDic[key] = (float(value)*1000)
            if "m" in value:
                value = value[0:value.find("m")]
                holderDic[key] = (float(value)*1000000)
            if "," in value:
                value = value.replace(",", "")
                holderDic[key] = float(value)
        newUserList.append(holderDic)
        holderDic.clear()
    #sort the the dics
    for i in len(newUserList):
        newUserList[i] = dict( sorted(newUserList[i].items(), key=operator.itemgetter(1),reverse=True))
    return newUserList

def getOptFollowerRange(price,userList):
        
