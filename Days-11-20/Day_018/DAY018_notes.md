# Understanding Turtle graphics
- [Turtle Graphics Documentation](https://docs.python.org/3/library/turtle.html)
- Use google then stackoverflow if the documentation is TLDR.
  - Example query: "Turtle graphics change the shape Stackoverflow"
- Turtle colors
  - Uses pencolor() method which gets the colors from Tk color spec string ("red", "yellow", or "#33cc8c").
  - Tk colors: [tcl.tk/man/tcl8.4/TkCmd/colors.htm](tcl.tk/man/tcl8.4/TkCmd/colors.htm)
  - Tk is short for module tkinter (TK interface), used for creating GUI
  - [Trinket Turtle Colors](https://trinket.io/docs/colors)
  - [Turtle Colors](https://cs111.wellesley.edu/reference/colors)
  - [RGB colors](https://www.w3schools.com/colors/colors_rgb.asp)
- Learn to read documentation

# Importing Modules
- `import module_name`
- `from module_name import Module_class`
  - Best when you need to use the class.
- `from module_name import *`  
  - This imports EVERYTHING in the module.
  - Not good practice to use because it can be confusing where a method is coming from.

# Aliasing Modules
- `import module_name as alias`

# Installing Modules
- When you can't just import modules that are not part of Python standard library.
- Install from PyPI using `pip install`
  - in Pycharm, just hover the module and it will have a suggestion box asking if you want to install the module.
  - installed packages get installed in a local virtual environment (venv) folder on a per project basis.

# Tuples
- Is a data type in Python
- Example: `my_tuple = (1, 2, 3)`
- It is similar to a list except, Tuples are ordered and values cannot be changed or removed once it is created.
- In other words, Tuples are "immutable".
- You can convert your Tuple into a list:
  `list(my_tuple)`

# Colorgram Package
- Used for Hirst Painting Project
- https://pypi.org/project/colorgram.py/