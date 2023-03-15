# -------------------------------------- Task 1 -----------------------------------
def add(x, y):
    return x + y

# TODO: Add definitions of sub(), div(), mult(), exp(), as well as neg() and sqrt().
#       neg() should return the negation of the given number, and sqrt() should
#       return the square root of the given number. 

def sub(x, y):
    return x - y

def mult(x, y):
    return x * y

def div(x, y):
    return x / y

def exp(x, y):
    return x ** y

def neg(x):
    return x * -1

def sqrt(x):
    return x **(1/2)

# -------------------------------------- Task 2 -----------------------------------

# TODO: Implement the quadratic formula using *only* the functions defined here.
#       Do not use arithmetic operators directly. 
#       You're allowed to define other functions.
a = 1
b = -3
c = 1

four_a_c = mult(4,(mult(a,c)))
exp_b = exp(b,2)
b_sub_four_a_c = sub(exp_b,four_a_c)
two_a = mult(2,a)

x1 = div(add(neg(b),sqrt(b_sub_four_a_c)),two_a) # TODO: write a code to compute the first root of the quadratic equation
x2 = div(sub(neg(b),sqrt(b_sub_four_a_c)),two_a) # TODO: then do the same for the second root
# Note: Make sure to remove the ellipsis (...) when you're writing your code

print("First root:" + str(x1))
print("Second root:" + str(x2))
