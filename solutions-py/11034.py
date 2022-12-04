def main():
    c = int(input())
    scores = [0 for s in range(c)]
    for i in range(c):
        scores[i] = ferryRide()
    for j in range(c):
        print(scores[j])

def ferryRide():
    counter = 1 #this is the additional trip that always happens at the end
    lmArr = input().split()
    l = int(lmArr[0]) * 100
    m = int(lmArr[1])
    currentLength = l
    currentSide = 'left'
    for i in range(m):
        carArr = input().split()
        carLength = int(carArr[0])
        carSide = carArr[1]
        if (carSide != currentSide ):
            counter += 1
            currentSide = changeSides(currentSide)
            currentLength = l - carLength
            # print("1st")
        elif (carSide == currentSide and carLength <= currentLength):
            currentLength -= carLength
            # print("2nd")
        elif (carSide == currentSide and carLength > currentLength):
            counter += 2
            currentLength = l - carLength
        #     print("3rd")
        # print(currentLength)
        # print(currentSide)
        # print(counter)
    return counter

def changeSides(currentSide):
    if (currentSide == 'left'):
        return ('right')
    elif (currentSide == 'right'):
        return ('left')

main()

