def print_hexagon_grid(rows, columns):
    def print_hexagon_top():
        for i in range(columns):
            print("  ___  ", end="")
        print()

    def print_hexagon_middle():
        for i in range(columns):
            print(" /   \\ ", end="")
        print()
        for i in range(columns):
            print("/     \\", end="")
        print()

    def print_hexagon_bottom():
        for i in range(columns):
            print("\\     /", end="")
        print()
        for i in range(columns):
            print(" \\___/ ", end="")
        print()

    for _ in range(rows):
        print_hexagon_top()
        print_hexagon_middle()
        print_hexagon_bottom()


rows = int(input("Enter the number of rows: "))
cols = int(input("Enter the number of columns: "))
print_hexagon_grid(rows, cols)



