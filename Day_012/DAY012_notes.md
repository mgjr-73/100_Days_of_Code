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