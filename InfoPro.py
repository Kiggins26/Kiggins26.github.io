import operator
def strToFloat(userList):
    newUserList = []
    holderDic = {}
    for i in userList:
        for x in i:
            if "k" in i.get(x):
                value = i.get(x).replace("k", "")
                holderDic[x] = (float(value)*1000)
            if "m" in i.get(x):
                value = i.get(x).replace("m", "")
                holderDic[x] = (float(value)*1000000)
            if "," in i.get(x):
                value = i.get(x).replace(",", "")
                holderDic[x] = float(value)

    #sort the the dics
    newUserList.append(holderDic)
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
pricetest = 250000
testlist = [[{'astral_selection': '61 ', 'rojasmanuel': '2,658 ', 'musicalsoul_vishal': '2,739 ', 'theaniketkaljunkar': '2,397 ', 'zantoutphotography': '2,500 ', 'm.sophie_karl': '147 ', 'txfuchxnn': '1,609 ', 'lastribotello43': '0 ', 'elizabethplus2dogs': '285 ', 'rosalie_portfolio': '73 ', 'asajjjj___': '37 ', 'rajicc_': '368 ', 'matejkubela': '491 ', 'burylova_olesya': '28.3k ', 'criaetif': '26 ', 'juliawphotography': '186 ', 'singhsandeep8312': '386 ', 'pumba_photo.studio': '176 ', 'smileplzz13': '3,134 ', 'dylan_officiel__': '1,449 ', 'gagen_sergei_photo': '105 ', 'paulgruber_arch': '42 ', 'billie_eilish_blog': '8,022 ', 'yairelav98': '1,515 ', 'anastasia_skreminska': '4,178 ', 'krissstina_d': '4,057 '}]]
print(getOptFollowerRange(25000,strToFloat(testlist[0])))
