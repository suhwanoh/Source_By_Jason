class Enemy:
    life = 3


    def attack(self):
        print("ouch!")

        self.life -= 1

    def check_life(self):

        if self.life <= 0:
            print("I'm dead!")
        else:
            print("Oops! I'm still Alive.  " + str(self.life) + " life left.")




enemy1 = Enemy()

enemy1.attack()

enemy1.attack()

enemy1.check_life()


enemy1.attack()


enemy1.check_life()