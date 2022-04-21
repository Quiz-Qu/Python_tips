tr = [None, {'w': 2, 'v': 3}, {'w': 3, 'v': 4},
      {'w': 4, 'v': 8}, {'w': 5, 'v': 8},
      {'w': 9, 'v': 10}]
max_w = 20
m = {(i, w): 0 for i in range(len(tr))
     for w in range(max_w+1)}  # 前i个宝物，重量不超过w

for i in range(1, len(tr)):
    for w in range(1, max_w+1):
        if w < tr[i]['w']:
            m[i, w] = m[(i-1, w)]
        else:
            # 不装第i个货物，装第i个货物，两种情况下的最大价值
            m[i, w] = max(
                m[(i-1, w)],
                m[(i-1, w-tr[i]['w'])] + tr[i]['v'])

print(m[(len(tr)-1, max_w)])
