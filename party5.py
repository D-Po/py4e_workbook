# 12.06.2021
# PY4E
# Section 14.9 - Multiple Instances
# However, the real power in object-oriented programming happens
# when we construct multiple instances of our class. When we
# construct multiple objects from our class, we might want to set
# up different initial values for each of the objects. We can pass
# data to the constructors to give each object a different initial
# value

class PartyAnimal:
    x = 0
    name = ''
    def __init__(self, nam):
        self.name = nam
        print(self.name, 'constructed')

    def party(self) :
        self.x = self.x + 1
        print(self.name,'party count',self.x)

s = PartyAnimal('Sally')
j = PartyAnimal('Jim')

s.party()
j.party()
s.party()
