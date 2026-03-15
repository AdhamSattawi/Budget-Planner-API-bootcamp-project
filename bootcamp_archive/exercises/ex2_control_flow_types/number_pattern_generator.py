#This code generates pyramid of numbers up to 9 floors.


def generate_pyramid(height: int) -> str:
    if height < 1:
        raise ValueError("Height must be at least 1.")
    if height > 9:
        raise ValueError("Height cannot exceed 9.")
    pyramid = ''
    right_side = ''
    for i in range((height-1),-1,-1):
        right_side = ''
        pyramid += (' '*i)
        for j in range(1, (height-i)+1):
            pyramid += str(j)
            if j > 1:
                right_side = str(j-1) + right_side
        pyramid += right_side
        pyramid += ('\n')
    return pyramid

