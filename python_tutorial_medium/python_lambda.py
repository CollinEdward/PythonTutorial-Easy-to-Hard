# Add 10 to argument a, and return the result:

x = lambda a : a + 10
print(x(5))


# Multiply argument a with argument b and return the result:

x = lambda a, b : a * b
print(x(5, 6))


# Summarize argument a, b, and c and return the result:

x = lambda a, b, c : a + b + c
print(x(5, 6, 2))


# You can also use lambda inside functions
def myfunc(n): # and we can set a parament inside the function, then call it in the lambda
  return lambda a : a * n

mydoubler = myfunc(2)

print(mydoubler(11))