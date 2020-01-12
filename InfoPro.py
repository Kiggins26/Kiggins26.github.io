import operator
def strToFloat(userList):
    newUserList = []
    for i in userList:
        for key, value in i.items():
            holderDic = {}
            if "k" in value:
                value = value.replace("k", "")
                print(value)
                holderDic[key] = (float(value)*1000)
            if "m" in value:
                value = value.replace("m", "")
                holderDic[key] = (float(value)*1000000)
            if "," in value:
                value = value.replace(",", "")
                holderDic[key] = float(value)
        newUserList.append(holderDic)
    #sort the the dics
    for i in range(len(newUserList)):
        newUserList[i] = dict( sorted(newUserList[i].items(), key=operator.itemgetter(1),reverse=True))
    return newUserList
def cutList(followers, userList):
    for i in userList:
        for key, value in i.items():
            if(value > followers):
                i.pop(key)
    return userList
def getOptFollowerRange(price,userList):
    CONST_PRICEPERPOST = [200,1250,1600,3000,5000,240000] #upperbound
    if CONST_PRICEPERPOST[3] > price:
        if CONST_PRICEPERPOST[2] > price:
            if(CONST_PRICEPERPOST[1] > price):
                if CONST_PRICEPERPOST[0] > price:
                    userList = cutList(10000,userList)
                else:
                    userList = cutList(25000,userList)
            else:
                userList = cutList(50000,userList)
        else:
            userList = cutList(100000,userList)
    else:
        userList = cutList(250000,userList)
    return userList

userdict = {"test":"1.2k"}
userdict1 = {"test":"1,000"}

userlist = [userdict,userdict1]
print(strToFloat(userlist))
#andrew did this, he is so sexy
