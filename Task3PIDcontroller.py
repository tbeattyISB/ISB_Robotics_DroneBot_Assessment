from robot import MainRun
import time

def go(bot):
    bot.wait(2000)
    # ----------------------------------
    # ADD YOUR PID CONTROLLER HERE:
    #   - Your D conroller should get rid of a lot of oscillations

    while (True):

        # include bot.wait(50) INSIDE YOUR WHILE LOOP to get better I and D values
        bot.wait(50) # No need to run this more than 20 times per second
    # ----------------------------------

    # Question 6: Why does the D controller limit oscillations.


MainRun(go)