def is_even(number):
    """Return True if *number* is even"""
    for element in range(number):
        if number % 2 == 0:
            return True

    return False

