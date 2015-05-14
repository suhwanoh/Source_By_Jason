class Enemy():
    def __init__(self, given_energy):
        self.energy = given_energy

    def get_energy(self):
        print(self.energy)


jason = Enemy(10)
sandy = Enemy(50)

jason.get_energy()
sandy.get_energy()
