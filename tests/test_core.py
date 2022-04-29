from beerlog.core import get_beers_from_database, add_beer_to_database, delete_beers_from_database

def test_add_beer_to_database():
    assert add_beer_to_database('Blue Moon', 'Witbier', 10, 3, 6)

def test_get_beers_to_database():
    add_beer_to_database('Blue Moon', 'Witbier', 10, 3, 6)
    results = get_beers_from_database()
    assert len(results) > 0

def test_get_beers_from_style_to_database():
    add_beer_to_database('Cacildis', 'Lager', 10, 3, 6)
    results = get_beers_from_database('Lager')
    assert len(results) > 0

def test_delete_beer_to_database():
    add_beer_to_database('Cacildis', 'Lager', 10, 3, 6)
    assert delete_beers_from_database(1)
