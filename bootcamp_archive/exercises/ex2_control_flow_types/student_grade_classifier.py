# This code return student letter grade accourding to their numerical grade.


def classify_grade(score: int) -> str:
    if not (0 <= score <= 100):
        raise ValueError("Score must be between 0 and 100")
    if score >= 90:
        return "A"
    if score >= 80:
        return "B"
    if score >= 70:
        return "C"
    if score >= 60:
        return "D"
    else:
        return "F"


print(classify_grade(59))
