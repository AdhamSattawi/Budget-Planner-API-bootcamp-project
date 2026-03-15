#This code caculate the rectangle measurments

rectangle_width = float(input("please enter the width of the rectangle: "))
rectangle_height = float(input("please enter the height of the rectangle: "))

rectangle_area = rectangle_width * rectangle_height

rectangle_perimeter = 2 * (rectangle_width + rectangle_height)

rectangle_diagonal = (rectangle_width**2 + rectangle_height**2)**0.5

print(f'''
    Width: {rectangle_width}
    Height: {rectangle_height}
    Area: {rectangle_area}
    Perimeter: {rectangle_perimeter}
    Diagonal: {rectangle_diagonal}
      ''')