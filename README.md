## Day 1 lesson topics:
- `print` function
- Debugging
- 'input` function
- variables
- Project: Band Name Generator

## Day 2 lesson topics:

**Data Types**

1. String

   "Hello"
    ```Python
   print("Hello"[0])   
   # will print 'H'  
   ```
   The method of pulling out an element from a string is called 'subscripting'.


2. Integer
    
    123
    123_456_999 Is still an integer. Python will ignore underscores.


3. Float

    3.14159


4. Boolean

    True

    False


5. Type Errors

    ```Python
    num_char = len(input("What is your name?"))
    print("Your name has " + num_char + " characters.")
   ```

6. Type Checking

    ```Python
   type()
    ```
   
7. Type Conversion

    ```Python
   str()
    int()
    float()
    bool()
    ```
   
8. Maths Operations

    ```Python
    3 + 5
    7 - 4
    3 * 2
    6 / 3
    2 ** 3
    ```
   
9. PEMDASLR (Parentheses, Exponents, Multiply & Divide, Add & Subtract, Left to Right)

    ```Python
   ()
    **
   * /
    + -

    print(3 * (3 + 3) / 3 - 3)
    ```
   
10. Rounding Numbers

    ```Python
    print(round(4.6666666666)) # result 5
    print(round(4.6666666666, 2))   # result 4.67
    ```

11. Floor division

    ```Python
    9 // 4  # chops off float without rounding, returns 'int' type instead of 'float'. Result is 2.
    ```

12. Shorthand Operators

    ```Python
    a += 2  short for a = a + 2
    -=
    *=
    /=

13. f-Strings

    ```Python
    score = 0
    height = 1.8
    isWinning = True
    print(f"your score is {score}, your height is {height}, you are winning is {isWinning}")