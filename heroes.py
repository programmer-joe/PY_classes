from multi_verse import Superpower
class SuperHeroes(Superpower):
    def likability(self,score):
        if score is 1:
            niceness = '1 out of 5'
        else:
            niceness = str(score) + 'out of 5'
        return niceness

class SuperVillian(Superpower):
    def dislike(self,score):
        if score is 1:
            evil_ranking = "1 out of 5"

        else:
            evil_ranking = str(score) + "out of 5"
        return evil_ranking