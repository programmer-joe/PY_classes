class SuperHeroes:
    def __init__(self, name):
           self.full_name = name
    def convert_superhero_name(self):
        proper_case = self.full_name.title()
        return proper_case
