from pygame import *
import random

FPS = 60

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

class Molecule(sprite.Sprite):
    def __init__(self, x, y):
        sprite.Sprite.__init__(self)
        self.img_load('assets/WaterMolecule.gif')
        self.rect.centerx = x
        self.rect.centery = y

        random1 = random.randint(0,1)
        random2 = random.randint(0,1)

        if random1 == 1:
            self.xmove = 10
        else:
            self.xmove = -10
        if random2 == 1:
            self.ymove = 10
        else:
            self.ymove = -10

    def update(self):
        self.move()
        self.ballBarrier()

    def move(self):
        self.rect.x += self.xmove
        self.rect.y += self.ymove

    def img_load(self, filename):
        self.image = image.load(filename)
        self.rect = self.image.get_rect()

    def speed_up(self):
        if self.xmove > 0:
            self.xmove = self.xmove+1
        else:
            self.xmove = self.xmove-1
        if self.ymove > 0:
            self.ymove = self.ymove+1
        else:
            self.ymove = self.ymove-1

    def slow_down(self):
        if self.xmove > 0:
            self.xmove = self.xmove-1
        else:
            self.xmove = self.xmove+1
        if self.ymove > 0:
            self.ymove = self.ymove-1
        else:
            self.ymove = self.ymove+1

    def ballBarrier(self):
        """
        Checks to make sure the molecule on the screen
        """
        if self.rect.right > SCREEN_WIDTH:
            self.xmove = self.xmove*-1
        if self.rect.left < 0:
            self.xmove = self.xmove*-1
        if self.rect.bottom > SCREEN_HEIGHT:
            self.ymove = self.ymove*-1
        if self.rect.top < 0:
            self.ymove = self.ymove*-1


class Simulation(object):
    def __init__(self):
        init()
        self.myfont = font.Font('assets/Calibri.ttf', 48)

        self.screen = display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = time.Clock()
        display.set_caption('Temperature Simulation')

        self.background = Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.background.fill((0,0,0))

        self.sprites = sprite.RenderUpdates()

        self.temperatureValue = 200

        self.waterMoleculesList = []
        for x in range(10):
            self.waterMoleculesList.append(Molecule(random.randint(100,700),random.randint(100,500)))

        self.sprites = sprite.RenderUpdates()

        for waterMolecule in self.waterMoleculesList:
            self.sprites.add(waterMolecule)

    def run(self):
        running = True
        while running == True:
            self.clock.tick(FPS)
            running = self.handleEvents(self.waterMoleculesList)
            display.set_caption('game %d fps' % self.clock.get_fps())

            self.sprites.clear(self.screen, self.background)

            label = self.myfont.render(str(self.temperatureValue)+" Kelvin", 1, (255,255,0))
            self.screen.fill((0,0,0))
            self.screen.blit(label, (50, 5))

            for sprite in self.sprites:
                sprite.update()

            dirty = self.sprites.draw(self.screen)
            display.update(dirty)

    def handleEvents(self, waterMoleculesList):
        for e in event.get():
            if e.type == QUIT:
                return False

            elif e.type == KEYDOWN:
                if e.key == K_ESCAPE:
                    return False
                if e.key == K_UP:
                    if self.temperatureValue < 320:
                        self.temperatureValue = self.temperatureValue + 20
                        for x in self.waterMoleculesList:
                            x.speed_up()
                if e.key == K_DOWN:
                    if self.temperatureValue != 0:
                        self.temperatureValue = self.temperatureValue - 20
                        for x in self.waterMoleculesList:
                            x.slow_down()

        return True

def main():
    simulation = Simulation()
    simulation.run()
    quit()

main()
exit()
