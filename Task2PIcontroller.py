from robot import MainRun
import time

def go(bot):
    bot.wait(2000)
    # ----------------------------------
    # ADD YOUR PI CONTROLLER HERE:
    #   - Start with an I controller (trust me) then add the P
    #   - Note you will have oscillations!

    while (True):

        # include bot.wait(50) INSIDE YOUR WHILE LOOP to get better I and D values
        bot.wait(50) # No need to run this more than 20 times per second
    # ----------------------------------


    # Question 4: Try removing any code that deletes the integral when it passes the desired goal.
    #              What effect does this have?
    #
    # Question 5: Why do you want some integral amount while at the desired altitude?
    #

MainRun(go)