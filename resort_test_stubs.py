from resort_service import ResortService
from db import DB

db = DB()


# Requirement 4.1: system shall allow the users to browse resorts
# getting list of all resorts
def test_get_all_resorts():
    resort = ResortService(db.resorts)
    all_resorts = resort.get_all_resorts()

    assert len(all_resorts) == len(db.resorts), "all resorts should be returned!"


# Requirement: 4.1.1 system shall allow the users to narrow down their targeted resorts using categories
# getting list of categories
def test_get_all_categories():
    resort = ResortService(db.resorts)
    categories = resort.get_all_categories()
    l = len(categories)
    assert len(categories) > 0, "category list cannot be empty"


# Requirement: 4.1.1 system shall allow the users to narrow down their targeted resorts using categories
# getting list of resorts for a specific category
def test_get_resorts_by_category():
    resort = ResortService(db.resorts)
    categories = resort.get_all_categories()
    # get the last item as an example
    category = categories.pop()
    resorts = resort.get_resorts_by_category(category)

    assert len(resorts) > 0, "resort list cannot be empty for the passed category"


# Requirement: 4.1.3 system shall give sorting functionality for the results displayed for the selected category
# getting list of resorts for a specific category, sorted by price in ascending order
def test_get_sorted_resorts_by_category_price_asc():
    resort = ResortService(db.resorts)

    # choosing 'Winter' from sample db as we know it has 3 resorts with different prices
    category = 'Winter'
    resorts = resort.get_sorted_resorts_by_category(category, 'asc', 'price')

    assert resorts[0].get_price() < resorts[-1].get_price(), "resort list not sorted by price in ascending order!"


# Requirement: 4.1.3 system shall give sorting functionality for the results displayed for the selected category
# getting list of resorts for a specific category, sorted by price in descending order
def test_get_sorted_resorts_by_category_price_des():
    resort = ResortService(db.resorts)

    # choosing 'Winter' from sample db as we know it has 3 resorts with different prices
    category = 'Winter'
    resorts = resort.get_sorted_resorts_by_category(category, 'des', 'price')

    assert resorts[0].get_price() > resorts[-1].get_price(), "resort list not sorted by price in descending order!"


# Requirement: 4.1.3 system shall give sorting functionality for the results displayed for the selected category
# getting list of resorts for a specific category, sorted by price in descending order
def test_get_sorted_resorts_by_category_ranking_asc():
    resort = ResortService(db.resorts)

    # choosing 'Caribbean' from sample db as we know it has 3 resorts with different rankings
    category = 'Caribbean'
    resorts = resort.get_sorted_resorts_by_category(category, 'asc', 'ranking')

    assert resorts[0].ranking < resorts[-1].ranking, "resort list not sorted by ranking in ascending order!"


# Requirement: 4.1.3 system shall give sorting functionality for the results displayed for the selected category
# getting list of resorts for a specific category, sorted by price in descending order
def test_get_sorted_resorts_by_category_ranking_des():
    resort = ResortService(db.resorts)

    # choosing 'Caribbean' from sample db as we know it has 3 resorts with different rankings
    category = 'Caribbean'
    resorts = resort.get_sorted_resorts_by_category(category, 'des', 'ranking')

    assert resorts[0].ranking > resorts[-1].ranking, "resort list not sorted by ranking in descending order!"


# Requirement: 4.2.3.1 Resort’s ranking in the scale of 1 to 5
def test_resort_ranking():
    resort = ResortService(db.resorts)
    all_resorts = resort.get_all_resorts()
    sample_resort = all_resorts.pop()
    assert sample_resort.set_ranking(6) is False, 'cannot have ranking less than 1 or greater than 5!'


# Requirement: 4.2.3.2 Number of restaurants in a resort
def test_number_of_restaurants():
    resort = ResortService(db.resorts)
    all_resorts = resort.get_all_resorts()
    sample_resort = all_resorts.pop()
    assert sample_resort.set_restaurants([]) is False, 'number of restaurants should be greater than 0'


# Requirement: 4.2.3.3 internet accessibility should be: 'no_access' or 'lobby' or 'lobby_room'
def test_check_internet_accessibility():
    resort = ResortService(db.resorts)
    all_resorts = resort.get_all_resorts()
    sample_resort = all_resorts.pop()
    assert sample_resort.set_internet_access(None) is False, \
        "Internet Access should be 'no_access' or 'lobby' or 'lobby_room'"


# Requirement: 4.2.3.4 Number of swimming pools in a resort
def test_number_of_swimming_pools():
    resort = ResortService(db.resorts)
    all_resorts = resort.get_all_resorts()
    sample_resort = all_resorts.pop()
    assert sample_resort.set_swimming_pools([]) is False, 'number of swimming pools should be greater than 0'


if __name__ == '__main__':
    test_get_all_resorts()
    test_get_all_categories()
    test_get_resorts_by_category()
    test_get_sorted_resorts_by_category_price_asc()
    test_get_sorted_resorts_by_category_price_des()
    test_get_sorted_resorts_by_category_ranking_asc()
    test_get_sorted_resorts_by_category_ranking_des()
    test_resort_ranking()
    test_number_of_restaurants()
    test_check_internet_accessibility()
    test_number_of_swimming_pools()
