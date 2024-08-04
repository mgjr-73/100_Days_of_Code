## Functions
```Python
def my_function():
    #Do this
    #Then do this
    #Finally do this

my_function()
```
## Functions with Inputs
```Python
def my_function(something): # 123 is assigned to function variable 'something'
    #Do something with something (where something = 123)
    #Then do this
    #Finally do this

my_function(123)
```
In the context of functions, the variable **something** is called a parameter and
the value **123** entered in the function call is called an argument.

To explain another way:

**parameter** is the name of the data being passed into the function.

**argument** is the value assigned to the **parameter**

## Functions with multiple inputs - Positional
```Python
def my_function(something, anything):
    #Do something with something 123
    #Then do this with ABC
    #Finally do this

my_function(123, "ABC") # NOTE: These are positional arguments.
```

## Functions with multiple inputs - Keyword
```Python
def my_function(something, anything):
    #Do something with something 123
    #Then do this with ABC
    #Finally do this

my_function(something=123, anything="ABC") # NOTE: These are keyword arguments.
```