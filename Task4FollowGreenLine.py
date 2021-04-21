from robot import MainRun
import time

def go(bot):
    bot.wait(2000)
    # ----------------------------------
    # Follow the green line (it is hidden behind the blue line for the first 10 seconds
    # @ 2 sec -> 400 pixels altitude
    # @ 10 sec -> 800 pixels altitude
    # @ 18 sec -> 200 pixels altitude
    # Tune your drone as best you can
    # Take a screenshot of the result and add it to this folder before submitting.
    # Keep notes of good kp,ki & kd values, but experiment a little bit

    while (True):


        # include bot.wait(50) INSIDE YOUR WHILE LOOP to get better I and D values
        bot.wait(50) # No need to run this more than 20 times per second
    # ----------------------------------
    # Choose two sets of kp,ki & kd values, one with overshoot one without. How do they compare?
MainRun(go)