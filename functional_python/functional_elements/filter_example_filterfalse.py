from itertools import filterfalse 
little_horrors_shop = [('fake_blood', 120), ('horns', 500), ('claws', 95)]
print(list(filterfalse(lambda item: item[1] < 100, little_horrors_shop)))
