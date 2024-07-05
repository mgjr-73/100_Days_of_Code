## Python Dictionary
 
Here's an example of a dictionary. Note the last pair is capped off with a 
comma. This keeps it open-ended so you can add to the dictionary in the 
future.
```python
scores = {"john": 59, "alex": 85, "kate": 25, "ricky": 5,}
```
Another way of writing a dictionary, especially for ones that has a long string
value. Notice the placement of curly braces and the indentation of the
key:value pairs.
```python
serial_numbers = {
    "bork": "087038740LJH876NNJLGVKIFDDCH887"
    "chips": "JKSLJNF9898402NN88300030308830398",
}
```

### Retrieve dictionary values.
```python
print(scores["john"])   # Will print out John's score of 59 points.
```

### Adding to a dictionary
```python
# Add "michael": 79 to the scores dictionary
scores["michael"] = 79
print(scores)
```
the `print(scores)` statement will result in:
{"john": 59, "alex": 85, "kate": 25, "ricky": 5, "michael": 79}

### Create an empty dictionary
```python
empty_dict = {}
```

An empty dictionary can be useful for wiping out the contents of a dictionary,
for example in a game reset. Let's say our players are now on round two and
we're not sure who will play but we need to reset the scoreboard. We can simply
wipe out the `scores` dictionary.
```python
scores = {}
print(scores)
```
### Edit an item in the dictionary 
For example, let's say we're still in round
one and everyone is still playing and Kate earned another 10 points, giving
here a total of 35.
```python
scores["kate"] = 35
```
### Looping though a dictionary
```python
for key in serial_numbers:
    # print key first
    print(key)
    # print value of key next
    print(serial_numbers[key])
    print()
```
Result:
```console
bork
087038740LJH876NNJLGVKIFDDCH887

chips
JKSLJNF9898402NN88300030308830398
```

## Nesting Lists and Dictionaries
```python
{
   key1:[list],
   key2:{dict},
}
```

```python
# Nesting a list in a dictionary so that one key can carry multiple values
travel_log = {
    "France": ["Paris", "Lille", "Dijon"]
}

# Nesting a list in a list, however it's not very useful
["A", "B", ["C", "D"]]

# Nesting a dictionary in a dictionary
travel_log = {
    "France": {"cities_visited": ["Paris", "Lille", "Dijon"], "total_visits": 12},
    "Germany": {"cities_visited": ["Berlin", "Hamburg", "Stuttgart"], "total_visits": 5},
}

# Nesting dictionaries inside a list
[{
    Key: [list],
    Key2: {dict},
},
{
    Key: Value,
    Key2: Value,
}
}]

# Example of dictionary in a list
travel_log = [
    {
        "country": "France", 
        "cities_visited": ["Paris", "Lille", "Dijon"], 
        "total_visits": 12
    },
    {
        "country": "Germany", 
        "cities_visited": ["Berlin", "Hamburg", "Stuttgart"], 
        "total_visits": 5
    },
]
```
Remember that you access list items by their index number, while dictionary
items are accessed via their keys.

### Quiz
Question 1:
Which line of code will change the starting_dictionary to the final_dictionary?
```python
starting_dictionary = {
    "a": 9,
    "b": 8,
}


final_dictionary = {
    "a": 9,
    "b": 8,
    "c": 7,
}
```
![Screenshot 2024-05-20 at 11.14.55 PM.png](..%2F..%2F..%2F..%2F..%2F..%2Fvar%2Ffolders%2Fvc%2F99bc31r9327f7lmtwxwvyybc0000gn%2FT%2FTemporaryItems%2FNSIRD_screencaptureui_A2VGI0%2FScreenshot%202024-05-20%20at%2011.14.55%E2%80%AFPM.png)

Question 2:
Which line of code will produce an error?
```python
dict = {
    "a": 1,
    "b": 2,
    "c": 3,
}
```
![Screenshot 2024-05-20 at 11.16.58 PM.png](..%2F..%2F..%2F..%2F..%2F..%2Fvar%2Ffolders%2Fvc%2F99bc31r9327f7lmtwxwvyybc0000gn%2FT%2FTemporaryItems%2FNSIRD_screencaptureui_RF9VcH%2FScreenshot%202024-05-20%20at%2011.16.58%E2%80%AFPM.png)

Question 3:
Which line of code will print "Steak"?
```python
order = {
    "starter": {1: "Salad", 2: "Soup"},
    "main": {1: ["Burger", "Fries"], 2: ["Steak"]},
    "dessert": {1: ["Ice Cream"], 2: []},
}
```
![Screenshot 2024-05-20 at 11.18.22 PM.png](..%2F..%2F..%2F..%2F..%2F..%2Fvar%2Ffolders%2Fvc%2F99bc31r9327f7lmtwxwvyybc0000gn%2FT%2FTemporaryItems%2FNSIRD_screencaptureui_HM1cGT%2FScreenshot%202024-05-20%20at%2011.18.22%E2%80%AFPM.png)

### Project
The objective is to write a program that will collect the names and bids of different people. The program should ask for each bidder's name and their bid individually.

```
Welcome to the secret auction program. 
What is your name?: Angela
```
```
What's your bid?: $123
```
```
Are there any other bidders? Type 'yes' or 'no'.
yes
```

If there are other bidders, the screen should clear, so you can pass your phone to the next person. If there are no more bidders, then the program should display the name of the winner and their winning bid.
```
The winner is Elon with a bid of $55000000000
```
Use your knowledge of Python dictionaries and loops to solve this challenge.

**My console doesn't clear!**

This will happen if you’re using an IDE other than replit (e.g., VSCode, PyCharm etc). Similar to how we used the "random" module previously, in this project we will use the "replit" module. The `clear()` function is available here via the replit module without any extra configuration.

I’ll cover how to use PyCharm and import modules on Day 15. That said, you can write your own `clear()` function or configure your IDE like so:

**Solution**

https://replit.com/@appbrewery/blind-auction-completed

**Project Flowchart**
![Screenshot 2024-05-20 at 11.51.03 PM.png](..%2F..%2F..%2F..%2F..%2F..%2Fvar%2Ffolders%2Fvc%2F99bc31r9327f7lmtwxwvyybc0000gn%2FT%2FTemporaryItems%2FNSIRD_screencaptureui_rbbGN4%2FScreenshot%202024-05-20%20at%2011.51.03%E2%80%AFPM.png)
