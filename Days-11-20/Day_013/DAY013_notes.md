## Describe the Problem
Try to run a block of code then ask questions. For example, if you run this 
code, it will not print anything.
```python
def my_function():
    for i in range(1, 20)
        if i == 20:
            print("You got it")
my_function()   
```
- What is the for-loop doing?
  - *It is iterating through a range 1 through 20 but excluding 20*
- When is the function meant to print `"You got it!"`?
  - *When `i` equals `20`*
- What are your assumptions about `i`?
  - *The `range` function iterates from the first value up to, but not including the last value.*
  - *`i` will never reach `20`*
  - *To fix it, change the upper bound to `21`.*

## Play Computer and Evaluate Each Line: Reproduce the bug
