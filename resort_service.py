class ResortService:

    def __init__(self, resorts):
        self.resorts = resorts

    # return a list of all available resorts
    def get_all_resorts(self):
        if len(self.resorts) > 0:
            return self.resorts
        else:
            return None

    # filters the resorts and return a list of resorts with the passed category
    def get_resorts_by_category(self, category):
        result = [x for x in self.resorts if x.category == category]
        return result

    # return a string list of all categories
    def get_all_categories(self):
        result = []
        for resort in self.resorts:
            if resort.category not in result:
                result.append(resort.category)
        return result

    # filters the resorts and return a list of resorts with the passed category
    # sort_order: asc, dec
    # sort_by: price, ranking
    def get_sorted_resorts_by_category(self, category, sort_order, sort_by):
        resorts = self.get_resorts_by_category(category)
        if sort_by == 'price':
            resorts.sort(key=lambda x: x.get_price(), reverse=sort_order == 'des')
        else:
            resorts.sort(key=lambda x: x.ranking, reverse=sort_order == 'des')
        return resorts
