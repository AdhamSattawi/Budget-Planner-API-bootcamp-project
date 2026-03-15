#This code shows the boolean logic in Python

print('Please enter three integer numbers (a b c):')
a = int(input('Enter the first number (a): '))
b = int(input('Enter the second number (b): '))
c = int(input('Enter the third number (c): '))


print (f'{a = }, {b = }, {c = }')
print (f'''
    - Is `a` equal to `c`? {a == c}
    - Is `a` less than `b`? {a < b}
    - Is `b` greater than or equal to `a`? {b >= a}
    - Is `a` not equal to `b`? {a != b}
    - Are both conditions true: `a < b` AND `b > c`? {a < b and b > c}
    - Is at least one condition true: `a > b` OR `a == c`? {a > b or a == c}
    - Is it NOT true that `a` equals `b`? {a != b}
       ''')

print('\nPlease enter two words')
word_1 = input("Enter the first word: ")
word_2 = input("Enter the second word: ")

print(f''' 
    - Are the strings equal? {word_1 == word_2}
    - Are the strings equal when comparing lowercase versions? {word_1.lower() == word_2.lower()}
    - What is the length of the first word? {len(word_1)}
''')