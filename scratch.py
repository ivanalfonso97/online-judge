def calculate_moves():
    set_number = 1

    while True:
        columns = int(input())
        if columns == 0:
            break

        heights = [int(height) for height in input().split()]
        total_bricks = sum(heights)
        average_height = total_bricks // columns

        bricks_to_move = 0
        for height in heights:
            if height > average_height:
                bricks_to_move += height - average_height
        
        print(f"Set #{set_number}")
        print(f"The minimum number of moves is {bricks_to_move}.\n")

        set_number += 1

calculate_moves()