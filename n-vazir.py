import random

def get_conflicts(board, n):
    """Calculates total number of attacking pairs."""
    conflicts = 0
    row_counts = [0] * n
    main_diag = {} # r - c
    anti_diag = {} # r + c
    
    for c, r in enumerate(board):
        row_counts[r] += 1
        main_diag[r - c] = main_diag.get(r - c, 0) + 1
        anti_diag[r + c] = anti_diag.get(r + c, 0) + 1
        
    for count in row_counts:
        conflicts += (count * (count - 1)) // 2
    for count in main_diag.values():
        conflicts += (count * (count - 1)) // 2
    for count in anti_diag.values():
        conflicts += (count * (count - 1)) // 2
        
    return conflicts

def get_queen_conflicts(board, row, col, n):
    """Calculates conflicts for a specific queen at board[col]."""
    conflicts = 0
    for c in range(n):
        if c == col: continue
        r = board[c]
        if r == row or abs(r - row) == abs(c - col):
            conflicts += 1
    return conflicts

def solve_n_queens_local_search(n, max_steps=1000):
    # Step 1: Random Initial State (one queen per column)
    board = [random.randint(0, n - 1) for _ in range(n)]
    
    for i in range(max_steps):
        current_conflicts = get_conflicts(board, n)
        if current_conflicts == 0:
            return board # Solution found!

        # Step 2: Pick a random conflicted queen
        conflicted_queens = [c for c in range(n) if get_queen_conflicts(board, board[c], c, n) > 0]
        col = random.choice(conflicted_queens)

        # Step 3: Move queen to the row with minimum conflicts
        min_conflicts = n
        best_rows = []
        for r in range(n):
            conf = get_queen_conflicts(board, r, col, n)
            if conf < min_conflicts:
                min_conflicts = conf
                best_rows = [r]
            elif conf == min_conflicts:
                best_rows.append(r)

        board[col] = random.choice(best_rows)

    return None # Failed to find solution in max_steps (Local Optimum)

def print_board(board):
    n = len(board)
    for r in range(n):
        row_str = ""
        for c in range(n):
            row_str += "Q " if board[c] == r else ". "
        print(row_str)

# Run the solver
try:
    n = int(input("Enter the value of N for N-Queens: "))
except ValueError:
    print("Please enter a valid integer.")
    exit(1)
    
solution = solve_n_queens_local_search(n)

if solution:
    print(f"Solution for {n}-Queens found using Local Search:")
    print_board(solution)
else:
    print("No solution found. Try increasing max_steps or restarting.")