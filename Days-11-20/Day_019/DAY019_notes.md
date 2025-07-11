# Event Listeners
- Turtle documentation has section for "Using Screen Events"
  ![Screenshot 2025-04-30 at 00.45.45.png](..%2F..%2F..%2F..%2F..%2F..%2F..%2Fvar%2Ffolders%2Fvc%2F99bc31r9327f7lmtwxwvyybc0000gn%2FT%2FTemporaryItems%2FNSIRD_screencaptureui_eLXLSh%2FScreenshot%202025-04-30%20at%2000.45.45.png)
- https://docs.python.org/3/library/turtle.html#turtle.listen

# Higher Order Function
- Function that can work with other functions
- Function as inputs to another function
  - You don't need to include the brackets.
  - In the following example, func_b is a higher order function because
    it takes another function as an input:
    ```python
    def func_a():
      pass
    
    def func_b(func_a):
      pass
    ```

# Object State and Instances
- Use turtle class to create multiple turtle instances
   ```python
  tim = Turtle()
  jim = Turtle()
   ```
- Each instance can have its own state, meaning they can have their own
unique attributes, like color for example.
   ```python
   tim.color = green
   jim.color = red
   ```
  
# Understanding the Turtle Coordinate System
- [Turtle `textinput` method](https://docs.python.org/3.1/library/turtle.html#turtle.textinput)
   ```plaintext
   turtle.textinput(title, prompt)
  
  or
  
   screen.textinput(title, prompt)
   ```  
# Challenges
1. Etch-A-Sketch App