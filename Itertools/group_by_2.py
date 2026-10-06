from itertools import groupby
persons = [{"name": "atul", "age":20 }, {"name": "rashi", "age":17 }, {"name": "saloni", "age":19 }]

group_obj = groupby(persons, key = lambda x: x["age"])

for key, value in group_obj:
    print(key, list(value))