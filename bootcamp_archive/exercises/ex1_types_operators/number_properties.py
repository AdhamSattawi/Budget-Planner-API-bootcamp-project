#This code prints the meta data behind a number.
import sys
the_number = int(input("Please enter a number: "))
print(f'''
    Number: {the_number}
    Type: {type(the_number)}
    Size in bytes: {sys.getsizeof(the_number)}
    Number squared: {the_number ** 2}
    As float: {float(the_number)}
    As string: {str(the_number)}
    Is positive: {the_number > 0}
      ''')