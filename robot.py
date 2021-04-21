import pygame
import math
import random
from threading import Thread, Timer

displayw = 800
displayh = 600
wallPos = 0
simSpeed = 30


class Graph(object):
    def __init__(self, window):
        self.window = window
        self.data = [wallPos];
        self.xScale = 0.0004 * math.pow(simSpeed, 2) - 0.0637 * simSpeed + 3.15
        self.yScale = 0.1
        self.timeScale = 0.047

    def showGraph(self):
        myfont = pygame.font.SysFont('Aerial', 20)
        pygame.draw.line(self.window, (100, 100, 100), (30, 500), (750, 500))
        textsurface = myfont.render('Sensor', True, (0, 0, 0))
        textsurface = pygame.transform.rotate(textsurface, 90)
        self.window.blit(textsurface, (30, 400))
        pygame.draw.line(self.window, (100, 100, 100), (50, 400), (50, 520))
        textsurface = myfont.render('Time', True, (0, 0, 0))
        self.window.blit(textsurface, (600, 510))
        pygame.draw.line(self.window, (150, 150, 255), (50, 500 - 0 * self.yScale),
                         (2000 * self.timeScale, 500 - 0 * self.yScale), 3)
        pygame.draw.line(self.window, (150, 150, 255), (2000 * self.timeScale, 500 - 0 * self.yScale),
                         (2000 * self.timeScale, 500 - 400 * self.yScale),
                         3)
        pygame.draw.line(self.window, (200, 255, 200), (5000 * self.timeScale, 500 - 400 * self.yScale),
                         (5000 * self.timeScale, 500 - 800 * self.yScale),
                         3)
        pygame.draw.line(self.window, (200, 255, 200), (5000 * self.timeScale, 500 - 800 * self.yScale),
                         (8000 * self.timeScale, 500 - 800 * self.yScale),
                         3)
        pygame.draw.line(self.window, (200, 255, 200), (8000 * self.timeScale, 500 - 800 * self.yScale),
                         (8000 * self.timeScale, 500 - 200 * self.yScale),
                         3)
        pygame.draw.line(self.window, (200, 255, 200), (8000 * self.timeScale, 500 - 200 * self.yScale),
                         (10000 * self.timeScale, 500 - 200 * self.yScale),
                         3)
        pygame.draw.line(self.window, (150, 150, 255), (2000 * self.timeScale, 500 - 400 * self.yScale),
                         (10000 * self.timeScale, 500 - 400 * self.yScale),
                         3)

    def update(self):
        self.showGraph();
        length = len(self.data) - 1
        for i in range(0, length):
            pygame.draw.line(self.window, (255, 150, 150),
                             (50 + self.xScale * (i), 500 - self.yScale * self.data[i]),
                             (50 + self.xScale * i + 1, 500 - self.yScale * self.data[i + 1]), 3)

    def addData(self, value):
        self.data.append(value)


# Simple player object
class Player(object):
    def __init__(self, x, y, window):
        self.__x = x
        self.__y = y
        self.mass = 200
        self.__v = 0
        self.power = 0
        self.error = 0
        self.sensorSampleRate = 0.2
        self.random_noise = 0
        self.delay = 0
        self.sensor = 800
        self.image = pygame.image.load("dronered.png")
        # Robot icon made by Turkkub fro www.flaticon.com:  <a href="https://www.flaticon.com/authors/turkkub"        # self.image = pygame.transform.rotate(self.image, 270)
        self.window = window
        self.update_altitude()
        self.stopped = True
        self.start = 0

    def draw(self):
        # Force = motor - friction - resistance
        if (self.power < 0):
            self.power = 0
        totalAccel = (0.5 * math.copysign(math.pow(self.power, 2), self.power) - 1000 - 1 * math.copysign(
            math.pow(self.__v, 2), self.__v)) / self.mass

        self.__v = self.__v + totalAccel
        self.__y -= self.__v
        if (self.__y > displayh - 60):
            self.__y = displayh - 60
        self.window.blit(self.image, (self.__x, self.__y))

    # Method to move object (special input of speedx and speedy)
    def run(self, power):
        if power > 100:
            power = 100
        if power < -100:
            power = -100
        self.power = power

    def wait(self, time):
        if (self.start == 0):
            self.start = pygame.time.get_ticks()
        pygame.time.wait(time)
        print(f'{round(self.altitudeSensor())}px at {(pygame.time.get_ticks() - self.start) / 1000:.2f} seconds')

    def runTime(self):
        return pygame.time.get_ticks() - self.start

    def setPayload(self, mass):
        if (mass < 0):
            mass = 0
        if (mass > 500):
            mass = 500
        self.mass = 200 + mass * 50

    def setNoise(self, noise):
        self.random_noise = noise;

    def setDelay(self, delay):
        self.delay = delay

    def altitudeSensor(self):
        return self.sensor

    def drawBarGraph(self, error):
        self.error = - error / 7

    def set_timeout(self, func, sec):
        t = None

        def func_wrapper():
            func()
            t.cancel()

        t = Timer(sec, func_wrapper)
        t.start()

    def update_altitude(self):
        global wallPos
        self.sensor = - (self.__y) + (displayh - 60) + self.random_noise * (random.random() - 0.5)
        if (self.delay > 0.002 and self.delay < 2.001):
            self.set_timeout(self.update_altitude, self.delay)
        elif (self.delay > 2):
            self.set_timeout(self.update_altitude, 2)
        else:
            self.set_timeout(self.update_altitude, 0.02)


# Main Class
class MainRun(object):
    def __init__(self, program):
        pygame.init()
        pygame.font.init()

        global displayw
        global displayh
        self.window = pygame.display.set_mode((displayw, displayh))
        self.windowclock = pygame.time.Clock()
        self.program = program
        self.Main()

    def Main(self):
        global wallPos
        stopped = False

        # Creating the player objects
        player = Player(30, displayh - 60, self.window)
        graph = Graph(self.window)

        cont = Thread(target=self.program, args=(player,))
        cont.setDaemon(True)

        # When you want to draw the player object use its draw() method
        self.window.fill((255, 255, 255))
        player.draw()
        graph.showGraph()
        pygame.display.update()
        cont.start()

        while stopped == False:
            self.window.fill((255, 255, 255),
                             (0, 0, displayw, displayh))  # Tuple for filling display... Current is white

            # Event Tasking
            # Add all your event tasking things here
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            # And be sure to redraw your player

            graph.addData(player.altitudeSensor())
            graph.update()
            player.draw()

            # Remember to update your clock and display at the end
            pygame.display.update()
            self.windowclock.tick(simSpeed)

