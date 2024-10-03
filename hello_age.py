#!/usr/bin/env python3
try:
    if __name__ == '__main__':
        name = input('Hello, what is your name? ')
        name = name.capitalize()

        year_now = int(input('What year is it today? '))
        year_born = int(input('And what year were you born? '))
        if year_now < year_born:
            print('Invalid input')
        else:
            age = year_now - year_born
            print(f'Hello, {name}. It is good to meet you. This year you will be {age} years old.')

except ValueError:
    print('Invalid input')