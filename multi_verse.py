class Superpower:
    def __init__(self, name, code, rating):
        self.full_name = name
        self.superhero_code = code
        self.superhero_rating = rating

    def convert_superhero_name(self):
        proper_case = self.full_name.title()
        return proper_case

    def abilities(self):
        superpower = "No super power"
        if self.superhero_code is "SS":
            superpower = "Super Strength"
        elif self.superhero_code is "BP":
            superpower = "Bullet Proof"
        elif self.superhero_code is "SF":
            superpower = "Super Fast"
        elif self.superhero_code is "TP":
            superpower = "Telepathy"
        return superpower

    def get_rating(self):
        self.__convert_score()
        return self.__convert_score()

    def __convert_score(self):  # double underscore for encapsulation
        if self.superhero_rating is 5:
            star_rating = "Rating : Five star"
        elif self.superhero_rating is 4:
            star_rating = 'Rating : Four star'
        elif self.superhero_rating is 3:
            star_rating = 'Rating : Three star'
        elif self.superhero_rating is 2:
            star_rating = 'Rating : Two star'
        elif self.superhero_rating is 1:
            star_rating = 'Rating : One star'

        else:
            star_rating = 'You must be Batman'
        return star_rating