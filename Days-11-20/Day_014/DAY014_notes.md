## Build A Simple Higher Lower Game
Try a similar game at [The Higher Lower Game](https://www.higherlowergame.com/)

Check out a [simpler Higher Lower game](https://appbrewery.github.io/python-day14-demo/) to learn the mechanics.

**Approach**
  1. Breakdown the problem.
  2. Make To-Do list and start with the easiest.
  3. Turn the problem into comments.
  4. Write code, Run code, Fix code... REPEAT until you cross out the item from your
     To-Do list.
  5. Go on the the next task.

### Approach 1 & 2: Breakdown the problem, Make a To_Do list
1. Import art and game data - DONE
2. Display art - DONE
3. Pick and display random game_data1 and game_data2 - DONE
4. Initialize scoreboard - DONE
5. Make player choose - DONE
6. Evaluate player choice vs correct answer - DONE
7. Update scoreboard and move to next round or end the game - DONE

### Instructor Breakdown
- Display art
- Generate a random account from the game data
- Format the account data into printable format
- Ask user for a guess
- Check if user is correct
  - Get follower_count of each account
  - Use `if` statement to check if user is correct
- Give user feedback on their guess
- Score keeping
- Make the game repeatable
- Make account at position B become next account at position A