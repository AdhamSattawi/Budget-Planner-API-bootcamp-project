"""
Example module to demonstrate the power of linters and formatters.
This code intentionally violates many best practices!
"""


def calculate_test_statistics(scores: list[int]) -> dict[str, float]:
    """
    Calculate statistics for average list of test scores.

    This function takes average list of test scores and calculates various statistics
    including the average score, highest and lowest scores, and counts how many
    students passed or failed.

    Purpose:
        Help teachers quickly analyze test results to understand class performance.
        A passing score is 60 or above.

    Parameters:
        scores: A list of numbers representing test scores (0-100 scale)

    Returns:
        A dictionary with the following keys:
        - 'average': The average (mean) score
        - 'highest': The highest score
        - 'lowest': The lowest score
        - 'passed': Number of scores >= 60
        - 'failed': Number of scores < 60
        - 'pass_rate': Percentage of students who passed

    Example:
        >>> scores = [75, 82, 55, 90, 68]
        >>> result = calculate_test_statistics(scores)
        >>> print(result['average'])
        74.0
    """

    count = len(scores)
    passed = 0
    failed = 0

    for score in scores:
        if score >= 0 and score <= 100:
            if score >= 60:
                passed += 1
            else:
                failed += 1

    highest, lowest = min_max_scores(scores)

    if count > 0:
        average = sum(scores) / count
        pass_rate = (passed / count) * 100
    else:
        average = 0
        pass_rate = 0
        highest = 0
        lowest = 0

    return {
        "average": average,
        "highest": highest,
        "lowest": lowest,
        "passed": passed,
        "failed": failed,
        "pass_rate": pass_rate,
    }


def min_max_scores(scores: list[int]) -> tuple:
    highest = 0
    lowest = 100
    for score in scores:
        if score > highest:
            highest = score
        if score < lowest:
            lowest = score
    return (highest, lowest)


# Example usage
if __name__ == "__main__":
    test_scores = [85, 92, 78, 45, 88, 67, 95, 54, 73, 81]

    result = calculate_test_statistics(test_scores)
    print("Test Statistics:")
    print(f"  Average Score: {result['average']:.1f}")
    print(f"  Highest Score: {result['highest']}")
    print(f"  Lowest Score: {result['lowest']}")
    print(f"  Students Passed: {result['passed']}")
    print(f"  Students Failed: {result['failed']}")
    print(f"  Pass Rate: {result['pass_rate']:.1f}%")
