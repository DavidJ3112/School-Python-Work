def totalcalc(numbers) -> int:
    """Calculate and return the total of all numbers."""
    return sum(numbers)


def averagecalc(numbers) -> float:
    """Calculate and return the average of all numbers."""
    return sum(numbers) / len(numbers)


def maxcalc(numbers) -> int:
    """Find and return the highest value in the list."""
    return max(numbers)

numbers = [3,3,2,4,8,1,102,321]

print(totalcalc(numbers))
print(averagecalc(numbers))
print(maxcalc(numbers))