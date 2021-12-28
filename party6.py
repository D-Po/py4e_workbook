# 12.06.2021
# PY4E
# Section 14.10 - Inheritance
#  When extending a class, we call the original class the parent class
# and the new class the child class. For this example, we move our
# PartyAnimal class into its own file. Then, we can ‘import’ the
# PartyAnimal class in a new file and extend it, as follows:

from party import PartyAnimal

class CricketFan(PartyAnimal):
    points = 0
    def six(self):
        self.points = self.points + 6
        self.party()
        print(self.name,"points",self.points)

s = PartyAnimal("Sally")
s.party()
j = CricketFan("Jim")
j.party()
j.six()
print(dir(j))
