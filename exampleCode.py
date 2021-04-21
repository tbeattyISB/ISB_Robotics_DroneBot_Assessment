from robot import MainRun
import time

desired_position = 0


def go(bot):
    bot.wait(2000)
    # This example simply shows many of the robot functions, including
    # .run   .runTime  and  .altitudeSensor
    # you should DELETE this when you get started
    bot.run(100)  # This is the fastest the drone can fly
    while (True):
        if (bot.runTime() > 3000):
            print(bot.altitudeSensor())
            bot.run(-100)
            break
        # include bot.weit(50) INSIDE YOUR WHILE LOOP to get better I and D values
        bot.wait(50) # No need to run this more than 20 times per second
    # ----------------------------------


MainRun(go)