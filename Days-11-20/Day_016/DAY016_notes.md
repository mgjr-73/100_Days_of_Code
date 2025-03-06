## Object Orient Programming (OOP)
Example: Self-driving car modules
- Camera
- Radar detection
- Navigation
- Power Consumption Monitor

"Modularizing" code means, we can reuse them on other projects. For example,
if we decide to build a Drone that requires a camera, navigation, and
battery monitor, we can reuse the modules from the self-driving car
instead of coding them from scatch.

Object Oriented Programming (OOP) splits a large project into smaller tasks
or modules. This allows the program to be scalable.
- OOP models real-world objects
- When modeling, think in terms of "what it has" (Attributes) and 
"what it does" (Methods).
- Attributes is just a fancy word for variables of a modeled object
- Methods are simply functions. It's what a particular modeled object
can do.
- We can then create multiple variations of the same object from the
same blueprint, or in OOP... a Class.
- From Classes we can create multiple objects

  - ### How to use OOP: Classes and Objects
    Example: Virtual Restaurant, we have to model a virtual...
    - chef
    - Waiter
      - Has:
        ```py
          is_holding_a plate = True
          tables_responsible = [4, 5, 6]
          ```
      - Does:
        ```py
        def take_order(table, order):
        #takes order to chef
        def take_payment(amount):
        #add money to restaurant
        ```
    - Cleaner
    - Manager
    - ### Constructing Objects and Accessing their Attributes and Methods
      - Example Class: a Car
        - Remember, Class is a blueprint
             ```python
            class CarBlueprint():
                speed = 0
                fuel = 30
                
                def move():
                    speed = 60   
                
                def stop():
                    speed = 0
          
          
            car = CarBlueprint()
            # Car is the object, CarBlueprint is the class.
            # Notice the Pascal Case (or camel case) used for classes. 
            # This differentiates variables from classes
             ```
         - The CarBlueprint can have attribute such as speed and fuel
         - Once car is initialized, it can then use the Class attributes
             ```python
             car.speed
            ```
         - Calling a method from a class, we use:
            ```python
            car.stop()
            ```

## How to add Python packages and use PyPi
- pypi.org for different packages
- A package is a bundle of files put together for a single purpose.
- Example, if you want to create a table, instead of typing it yourself,
you could install prettytable package to automate the creation of table.
- In Pycharm, go to Settings > Project > Project Interpreter
  - Click on the + sign to open the Available Packages dialogue.
  - Search for 'PrettyTable', then click on "Install Package".
- Now you can use the package using `import`
  ```python
  import prettytable
  ```
- You can right-click on prettytable > Go To > Implementation to view the
source code, OR just go to the [Pretty Table Documentation](https://code.google.com/archive/p/prettytable/wikis/Tutorial.wiki).
- 
## Practice Modifying Object Attributes and Calling Methods
First install prettytable. Then...
```python
from prettytable import PrettyTable

table = PrettyTable()

# methods
table.add_column("Pokemon",["Chespin", "Fennekin", "Froakie", "Linoone"])
table.add_column("Type", ["Grass", "Fire", "Water", "Normal"])

# attributes - first we can print the attribute to see the default, if any.
# Then we can change it, as per documentation
print(table.align)
print(table)

table.align = "l"
print(table.align)
print(table)
```
## Building the Coffee Machine in OOP
