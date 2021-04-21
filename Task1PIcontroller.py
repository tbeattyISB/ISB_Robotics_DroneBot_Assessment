from robot import MainRun
import time

def go(bot):
    bot.wait(2000)
    # ----------------------------------
    # ADD YOUR P CONTROLLER HERE:
    #   - This is a special drone, it's motors only spin one way! UP.
    #   - Find the lowest kp value so that the drone doesn't oscilate (but still flies)
    #   - Fine the best kp value so that the robot oscilates at the goal
    #   - Try to match the blue line at 400 altitude


    while (True):

        # include bot.wait(50) INSIDE YOUR WHILE LOOP to get better I and D values
        bot.wait(50) # No need to run this more than 20 times per second
    # ----------------------------------
  # Question 1: Why does the drone oscilate when it passes the desired altitude (what does the motor do)?
  #
  #
  # Question 2: What happens to the motors when the kp is very low?
  #
  #



MainRun(go)