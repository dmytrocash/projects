def check_int(row, min, max):
    # 1. Check if row is iint
    try:
        row = int(row)
    except ValueError as e:
        return f"Error: {e}"

    # 2. Check if row in range
    if min > row > max:
        return check_int