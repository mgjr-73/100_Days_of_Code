## Namespaces: Local vs Global Scope

```python
################### Scope ####################

enemies = 1

def increase_enemies():
  enemies = 2
  print(f"enemies inside function: {enemies}")

increase_enemies()
print(f"enemies outside function: {enemies}")
```
Output:
```python
enemies inside function: 2
enemies outside function: 1
```
**Local Scope**
Variables defined inside a function can only be accessed by methods
within that function.
```python
def local_demo():
    local_var = 1
    print(local_var)


local_demo()
print(local_var)
```
The `print(local_var)` outside of the `local_demo` function will cause
a `NameError` because the variable `local_var` is not defined outside of
the `local_demo` function. It is only used "locally" inside of the `local_demo`
function.

**Global Scope**
```python
global_var = 100
def local_demo():
    local_var = 1
    print(local_var)
    print(global_var)


local_demo()
```
Global Scope is demonstrated by having `global_var` being accessed by the
`local_demo` function. Global variables are placed outside of functions and
can be accessed by functions inside and outside of functions.

**Namespace**
Anything that you give a name to has a Namespace.

## Does Python have Block Scope?
There is no Block Scope in Python unless a variable is within a function.
```python
game_level = 3
def create_enemy():
    enemies = ["Skeleton", "Zombie", "Alien"]
    if game_level < 5:
        new_enemy = enemies[0]
# new_enemy at this this level of indentation will be undefined because it
# is outside of function `create_enemy`. It needs to be indented at 
# the `if` statement.

print(new_enemy)

```
## How to Modify a Global Variable
```python
# This variable has Global Scope
enemies = 1

def increase_enemies():
    # This variable has Local Scope
    enemies = 2
    print(f"enemies inside function: {enemies}")

increase_enemies()
print(f"enemies outside function: {enemies}")
```
It's usually not a good idea Global and Local variables to have the same name.
But in the case above, the intention is to modify the value of `enemies` from
an outside function call.

> Note: It's also not a good idea to modify a Global variable from within
> a function that has local scope, even if there is method for it because 
> it will make your
> program prone to bugs.
> ```python
> def increase_enemies():
>   global enemies
>   enemies += 1
> ``` 

A better way... use `return`
```python
enemies = 1

# This function can be placed anywhere in the code and all you have to do
# is call it whenever you need to increase the number of enemies.
def increase_enemies():
    print(f"enemies inside function: {enemies}")
    return enemies + 1

enemies = increase_enemies()
print(f"enemies outside function: {enemies}")
```
## Python Constants and Global Scope
Global scopes are useful when defining constants. Constants are values
you define and do not intend to change. The usual naming convention for
constants is to write them in all caps.

```python
PI = 3.14159
URL = "https://www.google.com"
TWITTER_HANDLE = "@boo"
```

## FINAL PROJECT: Number Guessing Game
Get your [ASCII Text](https://patorjk.com/software/taag/#p=display&f=Graffiti&t=Type%20Something%20)

**Number Guessing Game Objectives:**
- Include an ASCII art logo.
- Allow the player to submit a guess for a number between 1 and 100.
- Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer.
- If they got the answer correct, show the actual answer to the player.
- Track the number of turns remaining.
- If they run out of turns, provide feedback to the player.
- Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).




