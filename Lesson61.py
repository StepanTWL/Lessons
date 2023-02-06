
def delayTransistorKeys(CNT:int, CNTi:int, delayTime:int, timeCycle:int) -> int:
    delayAlgo = 300
    minTimeCycleIrpFrame = 1980
    maxTimeCycleIrpFrame = 5100
    maxCount = 0
    tmpCount = 0
    delay = 0
    calc1, calc2 = 0, 0

    timeCycle *= 20
    if timeCycle >= minTimeCycleIrpFrame and timeCycle <= maxTimeCycleIrpFrame:
        maxCount = 2000000//timeCycle
        if not 2000000 % timeCycle:
            maxCount -= 1
    else:
        maxCount = 0

    if maxCount >= CNTi:
        if CNT < CNTi:
            calc1 = CNT - CNTi
            calc2 = CNT + maxCount - CNTi + 1
            if abs(calc1) > calc2:
                tmpCount = calc2
            else:
                tmpCount = calc1
        else:
            tmpCount = CNT - CNTi
    else:
        tmpCount = 0

    if delayTime - tmpCount*timeCycle < delayAlgo:
        return 0
    else:
        delay = delayTime - tmpCount*timeCycle
        if delay > 65535:
            return 0

    return delay