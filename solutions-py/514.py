def main():
    results = []
    while True:
        n = int(input())
        if n == 0:
            break
        result = []
        while True:
            line = input()
            if line == '0':
                break
            outputArr = line.split()
            outputArr = [int(outputArr[i]) for i in range(n)]
            result.append(canMarshalCoaches(outputArr, n))
        results.append(result)
    for result in results: #printing
        if len(result) > 1:
            for item in result:
                if item:
                    print("Yes")
                else:
                    print("No")
        else:
            if result[0]:
                print("Yes")
            else:
                print("No")
        print("")
    # print(results)

def canMarshalCoaches(outputArr, trainLength):
    stack = []
    currentTrainArr = [(i + 1) for i in range(trainLength)]
    # zeroArr = [0 for i in range(trainLength)]

    for i in range(trainLength):
        # print(outputArr[i])
        if stack and stack[-1] == outputArr[i]:
            stack.pop(-1)
            # print("1st ")
        elif stack and stack[-1] != outputArr[i] and len(currentTrainArr) == 0:
            break
        else:
            for j in range(len(currentTrainArr)):
                if currentTrainArr[0] == outputArr[i]:
                    currentTrainArr.pop(0)
                    # print("2nd ")
                    break
                elif currentTrainArr[0] != outputArr[i]:
                    stack.append(currentTrainArr[0])
                    currentTrainArr.pop(0)
        #             print("3rd" )
        #             print(currentTrainArr)
        # print(stack)
        # print(currentTrainArr)
    
    if stack:
        return False
    else:
        return True

main()