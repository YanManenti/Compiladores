def printTable(table):
    for rowIndex, row in enumerate(table):
        for colIndex, col in enumerate(row):
            col = "None" if col is None else col
            print(f"[{rowIndex:>2}][{colIndex:>2}] = {col:<50}", end='')
        print()