# Check to see if a string has the same amount of 'x's and 'o's. 
# The method must return a boolean and be case insensitive. The string can contains any char.
def xos(string_to_test):    
    x_count = 0
    o_count = 0

    for letter in to_test:
        if(letter == 'x' or letter == 'X'):
            x_count += 1
        elif(letter == 'o' or letter == 'O'):
            o_count += 1
    
    return x_count == o_count
#

# Write a function, persistence, that takes in a positive parameter num and returns its multiplicative persistence, 
# which is the number of times you must multiply the digits in num until you reach a single digit.
def persistence(n):
    
    # if the param is a one digit num, should return zero since,
    # respecting the instructions, there's no multiplication to be made
    if len(str(n)) == 1:
        return 0

    # converting the "n" to a str
    n_str = str(n)
    # setting up our multiplication tracker
    persistence = 0

    # Now we can start multiplying until we get to a result which has just 1 single digit
    while len(n_str) > 1:
        result = 1
        persistence += 1
        for i in range(len(n_str)):
            result *= int(n_str[i])
        
        n_str = str(result)

    # returns the numb of multiplications made inside the while loop above        
    return persistence
#

# Your task is to make a function that can take any non-negative integer as a argument and return it 
# with it's digits in descending order. Essentially, rearrange the digits to create the highest possible number.
def descending_order(num):
    num_list = []
    
    # breaking the param into a str and passing each digit to the num_list
    for element in str(num):
        num_list.append(element)

    # join every element of the list in reverse order than convert back to int
    return int(''.join(sorted(num_list, reverse=True)))
#