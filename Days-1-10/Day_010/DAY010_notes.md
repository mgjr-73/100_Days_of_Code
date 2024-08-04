# Functions with Outputs

**Functions**
```python
def my_function():
    # Do this
    # Then do this
    # Finally do this


my_function()
```

** Functions with Inputs
Where 123 is the argument in the function call which is passed
to 'something' parameter.
```python
def my_function(something):
    # Do this with something
    # Then do this
    # Finally do this


my_function(123)
```

**Function with Outputs**
When function is called, whatever the return value of the function
becomes the value of the function call. In the example,
output = 6.
```python
def my_function():
    result = 3 * 2
    return result

    # Or to simplify...
    return 3 * 2


output = my_function()

```

# Multiple Return Values

**Notes On 'return' Statements**

- When Python encounters a ```return``` statement, it indicates the
end and exits the function.
- You can have multiple ```return``` keywords in a function.
- ```return``` can be by itself (in case of needing to escape a
function and return 'None' if a condition is not met).
For example:
```python
def format_name(f_name, l_name):
    if f_name == "" or l_name == "":
        return "One or both inputs were blank."
    formatted_f_name = f_name.title()
    formatted_l_name = l_name.title()
    return f"Result: {formatted_f_name} {formatted_l_name}"


print(format_name("john", "jones"))
```

# Docstrings
```python
def format_name(f_name, l_name):
    """Take first name and last name and format it to 
    return title case version."""
    if f_name == "" or l_name == "":
        return "One or both inputs were blank."
    formatted_f_name = f_name.title()
    formatted_l_name = l_name.title()
    return f"Result: {formatted_f_name} {formatted_l_name}"
```
**Notes**
- Avoid using docstring quotes for multiline comments. Use hash
symbol instead. It is not necessarily wrong or prohibited but
it is a generally accepted style usage to differentiate between
comments and docstrings.


# Print vs Return
You can use the output of a return for any further calculation
or function, other than just printing it.


# While Loops, Flags and Recursion
`while` loops gets rid of repeating code, and actually reuse it
over and over until an exit is encountered.

A 'Flag' is a variable that can be set with an initial 'True' value 
and can be used in a `while` loop. The 'Flag' is reset to 'False'
when a certain exit condition is met, thus ending the loop.

Example, the flag here is `end_function`.
```python
end_function = True

while end_function:
    yes_or_no = input(f"Type 'y' to continue calculating with {answer} or 'n' to exit: ")
    if yes_or_no == "y":
        old_answer = answer
        # Overwrite original operand_choice and calculate values.
        operand_choice = input("Pick another operation: ")
        new_number = int(input("What's the next number? "))
        calculate = operations[operand_choice]

        new_answer = calculate(old_answer, new_number)
        print(f"{old_answer} {operand_choice} {new_number} = {new_answer}")
        answer = new_answer
    else:
        end_function = False
```
**Recursion** is the idea that a function can call itself.

