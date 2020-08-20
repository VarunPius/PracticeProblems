# My solution O(n) Time O(n) Space:

def turnstileTimes(numCustomers, arrTime, direction):
    start = arrTime[0]
    exiting  = []
    entering = []

    for i in range(0, numCustomers):
        if direction[i] == 0:
            entering.append((arrTime[i], i))
        else:
            exiting.append((arrTime[i], i))

    res = [-1 for _ in range(numCustomers)]

    enterI = 0
    exitI = 0
    exitPrio = True
    currTime = start
    prevTime = -1

    while enterI < len(entering) and exitI < len(exiting):
        currExitTime = max(exiting[exitI][0], currTime)
        currEnterTime = max(entering[enterI][0], currTime)
        if currEnterTime < currExitTime:
            res[entering[enterI][1]] = currEnterTime
            prevTime = currEnterTime
            currTime = prevTime + 1
            enterI += 1
            exitPrio = False
        elif currExitTime < currEnterTime:
            res[exiting[exitI][1]] = currExitTime
            prevTime = currExitTime
            currTime = prevTime + 1
            exitI += 1
            exitPrio = True
        else:
            if currTime - prevTime > 1:
                exitPrio = True
            if not exitPrio:
                res[entering[enterI][1]] = currEnterTime
                prevTime = currEnterTime
                currTime = prevTime + 1
                enterI += 1
            else:
                res[exiting[exitI][1]] = currExitTime
                prevTime = currExitTime
                currTime = prevTime + 1
                exitI += 1
                exitPrio = True

    while enterI < len(entering):
        res[entering[enterI][1]] = max(entering[enterI][0], currTime)
        currTime += 1
        enterI += 1

    while exitI < len(exiting):
        res[exiting[exitI][1]] = max(exiting[exitI][0], currTime)
        currTime += 1
        exitI += 1
    return res