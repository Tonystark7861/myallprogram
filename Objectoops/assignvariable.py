

class Superheroes:
      def __init__(self, Full_name, PowerLevel, Superheroname):
          self.name = Full_name
          self.level = PowerLevel
          self.identity = Superheroname


      def Superhero_details(self):
           print(f"{self.name} is of powerlevel {self.level} and is famous as {self.identity}")


Superhero1 = Superheroes("TonyStrark",  5,   "IRONMAN")
Superhero2 = Superheroes("DonaldBlake", 1,      "THOR")
Superhero3 = Superheroes("PeterParker", 4, "SPIDERMAN")
Superhero4 = Superheroes("SteveRogers", 4, "CaptainAmerica")
Superhero5 = Superheroes("Tchalla", 3, "Blackpanther")
Superhero6 = Superheroes("Stephanstrange", 1, "DoctorStrange")


Superhero1.Superhero_details()
Superhero2.Superhero_details()
Superhero3.Superhero_details()
Superhero4.Superhero_details()
Superhero5.Superhero_details()
Superhero6.Superhero_details()


        