class Parent:
    def print_last_name(self):
        print 'Oh'

class Child(Parent):
    def print_first_name(self):
        print 'Jason'

#in python, you can overide function from inherited class
    def print_last_name(self):
        print "Snitzlberg"



suhwan = Child()
suhwan.print_first_name()
suhwan.print_last_name()
