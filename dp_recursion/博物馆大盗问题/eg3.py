tr = {(2,3), (3,4), (4,8), (5,8), (9,10)}

max_w = 20

m = {} #记录考虑宝物tr，重量w的最大value

def thief(tr, w):
    if tr == set() or w == 0:
        m[(tuple(tr),w)] = 0
        return 0
    elif (tuple(tr),w) in m:
        return m[(tuple(tr),w)]
    else:
        vmax = 0
        for t in tr:
            if w >= t[0]:
                v = thief(tr-{t},w-t[0]) + t[1]
                vmax = max(vmax,v)
        m[tuple(tr),w]=vmax
        return vmax

print(thief(tr, max_w))