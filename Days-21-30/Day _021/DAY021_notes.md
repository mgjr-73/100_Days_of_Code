# 21.153 - Class Inheritance
- You can inherit appearance or behavior
    ```python
    class Fish(Animal):   # class Fish inherits attributes from class Animal
    def __init__(self):
        super().__init__()   # super() refers to the superclass which is Animal. This initializes everything that 
                             # Animal can do in Fish class.
    ```

Example:
```python
class Animal:
    def __init__(self):
        self.num_eyes = 2
        
    def breathe(self):
        print("Inhale, exhale")

class Fish(Animal):
    def __init__(self):
        super().__init__()   # Inherit attributes and methods in Animal
        
    def breathe_2(self):
        super().breathe()   # Takes breathe method in superclass Animal
        print("doing this underwater.")   # Extends super method and applies action unique to fish class.
    
    def swim(self):
        print("moving in water")

nemo = Fish()
nemo.swim()   # moving in water
nemo.breathe()   # Inhale, exhale (method inherited from Animal via super method)
nemo.breathe_2()   # Inhale,exhale doing this underwater
print(nemo.num_eyes)   # 2 (attribute inherited from Animal via super method)
```

# 21.154 Detect Collisions with Food
- Inherit Turtle attributes and methods in Food class.
- Use turtle shape and shape size to create food. (https://docs.python.org/3/library/turtle.html#turtle.shape)
- Use turtle.distance to detect collision between snake.head and food.

# 21.155 Create a Scoreboard and Keep Score
- Use turtle.write (https://docs.python.org/3/library/turtle.html#turtle.write)
    ```python
    # Parameters:
    # arg – object to be written to the TurtleScreen
    # move – True/False
    # align – one of the strings “left”, “center” or right”
    # font – a triple (fontname, fontsize, fonttype) 
  
    turtle.write(arg, move=False, align='left', font=('Arial', 8, 'normal'))
    ```
- Moving hard coded variable values to the top as CONSTANTS
- Challenge: 
  - Create a new file called a scoreboard.py. 
  - Inside this file, create a new scoreboard class.
  - This scoreboard class is going to inherit from the turtle class.
  - The scoreboard is going to be a turtle which knows how to keep track of the score and how to display it.
  - The score is going to need to be tracked inside that scoreboard class. 
  - It needs to be increased by one every single time the snake eats a piece of food.
  - You're also probably going to need this turtle.clear so that you clear the writing every time you update the score.

# 21.156 Detect Collisions With The Wall

# 21.157 Detect Collision With Tail
- Snake gets longer as it gets food
  - Create a function in snake class that adds a snake segment
  - Move code in create_snake to add_segment function
- It's game over when snake's head collides with its own tail