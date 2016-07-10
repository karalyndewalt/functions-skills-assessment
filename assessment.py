# PART ONE

# 1. We have some code which is meant to calculate an item cost
#    by adding tax. Tax is normally 5% but it's higher in
#    California (7%).

#    Turn this into a function. Your function will pass in
#    the default tax amount (5%), a state abbreviation, and the
#    cost amount as parameters.

#    If the state is California, apply a 7% tax within the function.
#    Your function should return the total cost of the item,
#    including tax.

#    If the user does not provide a tax rate it should default to 5%

#Did the function practice in the morning and it took two hours, started the 
#skills assessment in the afternoon at 4pm.

def tax_by_state(state_abbreviation, cost_amount, tax=.05):
    """ This function calculates a total cost including tax.

    This function calculates a total cost including tax, either with a default
    rate of .05 or tests for a California state abbreviation and uses a different
    default rate. I am inclined to write a greeting, raw input assignments, input 
    formatting, bad input error handling and a print statement to this function 
    but in the real world it could be a function designed to have arguments 
    passed in from another function and to be called by yet other functions. So
    I am paying very close attention to the wording of the question and trying 
    to use that to determine how far I go. Before this stuff eats my weekend."""
    if state_abbreviation == "CA":
        tax = .07
        return cost_amount + (cost_amount*tax)
    elif state_abbreviation != "CA":
        return cost_amount + (cost_amount*tax)

# these comment blocks were used for testing my function
# total = tax_by_state("CA", 10)
# print total

#####################################################################
# PART TWO

# 1. (a) Write a function, `is_berry()`, which takes a fruit name as a string
#        and returns a boolean if the fruit is a "strawberry", "cherry", or
#        "blackberry".

#this block for testing
#fruit_name = "cherry"


def is_berry():
    fruit_name = raw_input("Please enter a fruit name: ")
    if fruit_name == "strawberry":
        is_berry_result = True
        return is_berry_result
    elif fruit_name == "cherry":
        is_berry_result = True
        return is_berry_result
    elif fruit_name == "blackberry":
        is_berry_result = True
        return is_berry_result
    else:
        is_berry_result = False
        return is_berry_result


# result = is_berry('strawberry')
# print result

#    (b) Write another function, shipping_cost(), which calculates shipping cost
#        by taking a fruit name as a string, calling the `is_berry()` function
#        within the `shipping_cost()` function and returns `0` if ``is_berry()
#        == True``, and `5` if ``is_berry() == False``.


def shipping_cost():
    fruit_name = raw_input("Please enter a fruit name: ")
    if is_berry(fruit_name) is True:
        shipping_cost_result = 0
        return shipping_cost_result
    elif is_berry(fruit_name) is False:
        shipping_cost_result = 5
        return shipping_cost_result

#this block for testing
#cost = shipping_cost(fruit_name)
#print cost


# 2. (a) Write a function, `is_hometown()`, which takes a town name as a string
#        and evaluates to `True` if it is your hometown, and `False` otherwise.
#

def is_hometown(town_name):
    home_town = "Boston"
    if home_town == town_name:
        return True
    if home_town != town_name:
        return False

#    (b) Write a function, `full_name()`, which takes a first and last name as
#        arguments as strings and returns the concatenation of the two names in
#        one string.


def full_name(first_name, last_name):
    return first_name + " " + last_name

#name = full_name()
#print name

#    (c) Write a function, `hometown_greeting()`, which takes a home town, a
#        first name, and a last name as strings as arguments, calls both
#        `is_hometown()` and `full_name()` and prints "Hi, 'full name here',
#        we're from the same place!", or "Hi 'full name here', where are you
#        from?" depending on what `is_hometown()` evaluates to.


def hometown_greeting(town_name, first_name, last_name):
    if is_hometown(town_name) is True:
        print "Hi, " + full_name(first_name, last_name) + ", we're from the same place!"
    if is_hometown(town_name) is False:
        print "Hi, " + full_name(first_name, last_name) + ", where are you from?"

#for testing
#hometown_greeting("San Francisco", "Ilsa", "Gordon")


#####################################################################

# PART THREE

# 1. Write a function ``increment()`` with a nested inner function, ``add()`` 
#    inside of it. The outer function should take ``x``, an integer which
#    defaults to 1. The inner function should take ``y`` and add ``x`` and ``y`` together.

# 2. Call the function ``increment()`` with x = 5. Assign what is returned to a variable name, addfive. Call 
#    addone with y = 5. Call again with y = 20. 

# 3. Make a function that takes in a number and a list of numbers. It should append
#    the number to the list of numbers and return the list.

#####################################################################