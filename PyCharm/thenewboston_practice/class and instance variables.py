class Girl:

# class variable is for global
     gender = 'female'


#instance variable is for the unique usage
     def __init__(self, name):
        self.name = name

a = Girl('Rachel')
b = Girl('Gina')

print a.gender, a.name
print b.gender, b.name