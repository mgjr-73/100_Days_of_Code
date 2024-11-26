# How to create your own Class in Python
- Class is a blueprint to create our own objects
- Syntax: `class` keyword followed by the `<className>` and end with a colon
- Naming convention for Class is to capitalize the first letter of every word.
For example: `CarCamshaftPulley`. This is also known as "PascalCase".

# Attributes, Class Constructors, \_\_init\_\_ Function
- one method of adding attributes is the dot notation
    ```python
    class Car:
      pass
      
    
    car1 = Car()
    car1.top_speed = 180
    car1.model = "Mustang"
    
    print(car1.model)
    ```
    This is inefficient though, because it will become unwieldy if you have a lot of attributes
    and adding a lot of car objects. You will have to repeat this method over and over for each
    of the car objects.
- A better way to handle this is by using a Constructor where we could initialize an object to
populate starting attributes and corresponding values.
- A Constructor uses a special function, `__init__`.
```python
    class Car:
        def __init__(self, top_speed, model):
            print("Initializing car object...")
            self.top_speed = top_speed
            self.model = model
            self.seats = 0   # This value has a default and can be changed directly
    
    car1 = Car(180, "Mustang")
    car1.seats = 4
    car2 = Car(250, "Formula 1")
    car2.seats = 1
    
    
    print(f"Model: {car1.model}, Top Speed: {car1.top_speed}, # of Seats: {car1.seats}")
    print(f"Model: {car2.model}, Top Speed: {car2.top_speed}, # of Seats: {car2.seats}"")
```

# Adding Methods To A Class
- Attributes are what an object "has".
- Methods are things that an object "does".
- Example, let's say our default value for attribute "seats" is 5. We can override this default value 
by defining a method that changes it.
```python
class Car:
        def __init__(self, top_speed, model):
            print("Initializing car object...")
            self.top_speed = top_speed
            self.model = model
            self.seats = 5

        def enter_race_mode(self):
            self.seats = 2

car1 = Car(180, "Mustang")
car1.enter_race_mode()
```

# Quiz Project Part 1: Create the Question Class
- Attributes
  - question text
  - answer
- A new_question object is initialized with the above attributes
- Task: Create a Question class with an \_\_init\_\_ method with two attributes, 'text' and 'answer'.
  (work file: question_model.py)




# Example Code
```python
class Car:
  pass
  

# Create an object instance of the class Car
car1 = Car()
car2 = Car()
```
