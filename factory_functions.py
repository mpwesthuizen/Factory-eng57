# follow some TDD

def make_dough(ingredient1, ingredient2):
    # when given water in ingredient1 and flour in ingredient 2
        # return dough
    if ingredient1 == 'water' and ingredient2 == 'flour' or ingredient1 == 'flour' or ingredient2 == 'water':
        return "dough"
    else:
        return 'not dough'

def make_bread(dough_prep):
    if dough_prep == "dough":
        return "bread"
    else:
        return "not bread"

def make_ww_dough(ingredient1, ingredient2):
    # when given water in ingredient1 and flour in ingredient 2
        # return dough
    if ingredient1 == 'water' and ingredient2 == 'wholewheat flour' or ingredient1 == 'wholewheat flour' or ingredient2 == 'water':
        return "wholewheat dough"
    else:
        return 'not wholewheat dough'

def bake_ww_bread(ww_dough_prep):
    if ww_dough_prep == "wholewheat dough":
        return "wholewheat bread"
    else:
        return "not wholewheat bread"