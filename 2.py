def print_operation_table(num_rows=6, num_columns=6):
    for x in range(1, num_columns+1):
        for y in range(1, num_rows+1):
            print(x*y, end = ' ')
        print()

print_operation_table()