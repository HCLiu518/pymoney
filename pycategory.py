class Categories:
    """Maintain the category list and provide some methods."""

    """ 
    initialize the categories
    """
    def __init__(self):
        self._categories = ['expense', ['food', ['meal', 'snack', 'drink'], 'transportation', ['bus', 'railway']], 'income', ['salary', 'bonus']]

    """
    View categories
    """
    def view(self, categories = None, n = 0):

        if categories == None:
            categories = self._categories

        for item in categories:
            if type(item) is list:
                self.view(item, n + 2)
            else:
                print(' '*n+f'- {item}')

    """
    Check if the category is valid
    """
    def is_category_valid(self, category):
        def recurse_check(category, categories = self._categories):
            if type(categories) is list:
                for child in categories:
                    if recurse_check(category, child):
                        return True
                return False
            else:
                return category == categories
        
        return recurse_check(category)

    """
    Find subcategories
    """
    def find_subcategories(self, category):
        def find_subcategories_gen(category, categories, found = False):
            if type(categories) is list:
                for index, child in enumerate(categories):
                    yield from find_subcategories_gen(category, child, found)
                    if child == category and index + 1 <= len(categories) and type(categories[index + 1]) == list:
                        yield from find_subcategories_gen(category, categories[index+1:index+2], True)
            else:
                if category == categories or found:
                    yield categories

        return list(find_subcategories_gen(category, self._categories))