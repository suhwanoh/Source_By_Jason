class Mario():

    def move(self):
        print("I'm moving")

class Shroom():

    def eat_shroom(self):
        print("I'm eating shroom!")


class Bigmario(Mario, Shroom):
    pass

# if you want to write nothing in class, just type in 'pass' instead of emptying lines!!!!!!!

bm = Bigmario()

bm.move()
bm.eat_shroom()