def dpMuseumThief(treasureList, maxWeight):
    maxValue = 0
    choosenList = []
    treasureUsed = {(i, w): None for i in range(len(treasureList)+1)
                    for w in range(maxWeight+1)}  # 前i个宝物，重量不超过w

    m = {(i, w): 0 for i in range(len(treasureList)+1)
         for w in range(maxWeight+1)}  # 前i个宝物，重量不超过w

    for i in range(1, len(treasureList)+1):
        for w in range(1, maxWeight+1):
            if w < treasureList[i-1]['w']:
                m[i, w] = m[(i-1, w)]
                treasureUsed[i,w] = None
            else:
                # 不装第i个货物，装第i个货物(以及装i个货物后
                # 剩下重量的最大值)，两种情况下的最大价值
                m[i, w] = max(
                    m[(i-1, w)],
                    m[(i-1, w-treasureList[i-1]['w'])] + treasureList[i-1]['v'])
                if m[(i-1, w)] < (m[(i-1, w-treasureList[i-1]['w'])]\
                     + treasureList[i-1]['v']):
                     newtreasure = i-1
                     treasureUsed[i,w] = newtreasure
                else:
                    newtreasure = None
    maxValue = m[len(treasureList), maxWeight]
    treasure = len(treasureList)
    weight = maxWeight
    while treasure > 0 and weight > 0:
        if treasureUsed[treasure,weight] != None:
            thistreasure = treasureList[treasureUsed[treasure,weight]]
            weight = weight - thistreasure['w']
            treasure = treasure - 1
            choosenList.append(thistreasure)
        else:
            treasure = treasure - 1
    return maxValue, choosenList


# 检验
print("=========== 1 博物馆大盗问题 ============")
treasureList = [[{'w': 2, 'v': 3}, {'w': 3, 'v': 4}, {
    'w': 4, 'v': 8}, {'w': 5, 'v': 8}, {'w': 9, 'v': 10}]]
treasureList.append([{'w': 1, 'v': 2}, {'w': 2, 'v': 2}, {'w': 2, 'v': 3}, {'w': 4, 'v': 5}, {'w': 4, 'v': 6}, {'w': 4, 'v': 7}, {'w': 5, 'v': 7},
                     {'w': 5, 'v': 8}, {'w': 6, 'v': 8}, {'w': 6, 'v': 10}, {'w': 7, 'v': 10}, {'w': 7, 'v': 12}, {'w': 8, 'v': 12}, {'w': 8, 'v': 13}, {'w': 9, 'v': 14}, {'w': 9, 'v': 16}])
treasureList.append([{'w': 1, 'v': 2}, {'w': 2, 'v': 2}, {'w': 2, 'v': 3}, {'w': 3, 'v': 4}, {'w': 3, 'v': 5}, {'w': 4, 'v': 6}, {'w': 4, 'v': 7},
                     {'w': 5, 'v': 7}, {'w': 5, 'v': 8}, {'w': 6, 'v': 8}, {'w': 6, 'v': 10}, {
                         'w': 7, 'v': 11}, {'w': 7, 'v': 12}, {'w': 8, 'v': 13},
                     {'w': 8, 'v': 14}, {'w': 9, 'v': 15}, {'w': 9, 'v': 16}, {'w': 9, 'v': 17}, {'w': 10, 'v': 17}, {'w': 10, 'v': 18}, {'w': 11, 'v': 18}])
treasureList.append([{'w': 1, 'v': 2}, {'w': 2, 'v': 2}, {'w': 2, 'v': 3}, {'w': 3, 'v': 4}, {'w': 3, 'v': 5}, {'w': 4, 'v': 5}, {'w': 4, 'v': 6},
                     {'w': 5, 'v': 6}, {'w': 5, 'v': 7}, {'w': 6, 'v': 8}, {'w': 6, 'v': 9}, {
                         'w': 7, 'v': 10}, {'w': 7, 'v': 11}, {'w': 8, 'v': 12},
                     {'w': 8, 'v': 13}, {'w': 9, 'v': 14}, {'w': 9, 'v': 15}, {'w': 9, 'v': 16}, {
                         'w': 10, 'v': 16}, {'w': 10, 'v': 17}, {'w': 11, 'v': 18},
                     {'w': 12, 'v': 18}, {'w': 12, 'v': 19}, {'w': 13, 'v': 20}, {'w': 13, 'v': 21}, {'w': 14, 'v': 21}, {'w': 14, 'v': 22}])
treasureList.append([{'w': 1, 'v': 2}, {'w': 2, 'v': 2}, {'w': 2, 'v': 3}, {'w': 3, 'v': 4}, {'w': 3, 'v': 5}, {'w': 4, 'v': 5}, {'w': 4, 'v': 6},
                     {'w': 5, 'v': 6}, {'w': 5, 'v': 7}, {'w': 6, 'v': 8}, {'w': 6, 'v': 9}, {
                         'w': 7, 'v': 9}, {'w': 7, 'v': 10}, {'w': 8, 'v': 11},
                     {'w': 8, 'v': 12}, {'w': 9, 'v': 13}, {'w': 9, 'v': 14}, {'w': 9, 'v': 15}, {
                         'w': 10, 'v': 16}, {'w': 10, 'v': 17}, {'w': 11, 'v': 18},
                     {'w': 11, 'v': 19}, {'w': 12, 'v': 20}, {'w': 13, 'v': 20}, {
                         'w': 13, 'v': 21}, {'w': 14, 'v': 21}, {'w': 14, 'v': 22},
                     {'w': 14, 'v': 23}, {'w': 15, 'v': 24}, {'w': 15, 'v': 25}, {'w': 16, 'v': 26}, {'w': 17, 'v': 27}, {'w': 18, 'v': 28}])

maxWeightList = [20, 50, 80, 100, 150]
for i in range(len(treasureList)):
    maxValue,choosenList = dpMuseumThief(treasureList[i], maxWeightList[i])
    print(maxValue)
    print(choosenList)
