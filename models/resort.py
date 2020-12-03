class Resort:
    def get_price(self):
        self.rooms.sort(key=lambda x: x.current_price)
        return self.rooms[0].current_price

    def set_ranking(self, ranking):
        if (ranking >= 1) and (ranking <= 5):
            self.ranking = ranking
            return True
        else:
            return False

    def set_restaurants(self, restaurants):
        if len(restaurants) > 0:
            self.restaurants = restaurants
            return True
        else:
            return False

    def set_swimming_pools(self, swimming_pools):
        if len(swimming_pools) > 0:
            self.swimming_pools = swimming_pools
            return True
        else:
            return False

    def set_internet_access(self, internet_access):
        if internet_access in ['no_access', 'lobby', 'lobby_room']:
            self.internet_access = internet_access
            return True
        else:
            return False

    def __init__(self, name, category, summary, ranking, rooms, restaurants, swimming_pools, internet_access):
        self.name = name
        self.category = category
        self.summary = summary
        self.ranking = ranking
        self.rooms = rooms
        self.restaurants = restaurants
        self.swimming_pools = swimming_pools
        self.internet_access = internet_access
