set = 0

def main():
    n = None
    heights = []
    
    while n != 0:
        n = int(input())
        if (n == 0):
            quit()
        heights_input = input().split()
        heights = [int(heights_input[i]) for i in range(n)] #to convert the height from strings to ints
        getMoves(n, heights)
        
def getMoves(n, heights):
    sum = 0
    ave = 0
    moves = 0
    global set

    #gets the average
    for i in range(n):
        sum += heights[i]
    ave = round(sum / n)

    #checks how many blocks need to be moved
    for i in range(n):
        if heights[i] > ave:
            moves += (heights[i] - ave)

    #increments the set nubmer
    set += 1

    #output
    print("Set #" + str(set))
    print("The minimum number of moves is " + str(moves) + ".")
    print("")

main()

#initialize the following
    #n for number of columns
    #heights array of size n for the height
    #set = 0 for set number
#do
#get number of columns
#get height of each column and store it in the array
#getMoves function
# decalre sum , ave, and # of moves
#get the average of the array
    #sum all the numbers in the array
    #divide the sum by n
#map through the array
    #if h[i] > average
        #moves += (h[i] - average)
#set++
#print('Set #' + str(set))
#print('The minimum number of moves is ' + str(moves))
#while n != 0