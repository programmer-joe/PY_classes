from heroes import SuperHeroes,SuperVillian
hero_object = SuperHeroes("iron man",'BP',4)#instanciating a class

good_name = hero_object.convert_superhero_name()
print(good_name)

powers = hero_object.abilities()
# rating = hero_object.convert_score()
rating = hero_object.get_rating()

print(good_name+' has '+powers +' ' ,rating)


hero_object2 = SuperHeroes("ant man",'TK','2')
print(hero_object2.convert_superhero_name())

