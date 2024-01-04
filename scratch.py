def order_coaches():
    while True:
        train_length = int(input())
        if train_length == 0:
            break

        while True:
            permutation = input()
            if permutation == "0":
                break
            
            permutation = [int(listItem) for listItem in permutation.split()]
            station_stack = []
            for coach in range(1, train_length + 1):
                while len(station_stack) > 0 and station_stack[-1] == permutation[0]:
                    station_stack.pop()
                    permutation.pop(0)

                if coach == permutation[0]:
                    permutation.pop(0)
                else:
                    station_stack.append(coach)
            
            if len(station_stack) == 0:
                print("Yes")
            else:
                print("No")
        print()

order_coaches()