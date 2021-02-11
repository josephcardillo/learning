#!/usr/bin/python3

# Program to check if a string is a palindrome

#TODO - use re module to strip spaces and punctuation from input

def check_palindrome1(string):
    '''using for loop'''
    reversed_string = []
    for i in string:
        reversed_string.insert(0, i)
    if ''.join(reversed_string).lower() == string.lower():
        return True
    else:
        return False

def check_palindrome2(string):
    '''using reversed()'''
    reversed_string = list(reversed(string))
    if ''.join(reversed_string).lower() == string.lower():
        return True
    else:
        return False

# The program
print('This script will check if a word or phrase is a palindrome.')
is_palindrome = input('What word or phrase would you like to check? > ')

print(f'Checking if {is_palindrome} is a palindrome.')
print('Using a for loop ... \n')
test1 = check_palindrome(is_palindrome)
print(f"Is '{is_palindrome}' a palindrome? {test1}")
print()
print('Using reversed() ... \n')
test2 = check_palindrome_ver_2(is_palindrome)
print(f"Is '{is_palindrome}' a palindrome? {test2}")