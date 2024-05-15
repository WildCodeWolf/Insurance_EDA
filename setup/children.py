class Children(int):
    """Extends integers used to count the number of children with categorical capabilities."""
    categories = ['no children', 'less than 3 children', '3 or more children']

    def category(self) -> str:
        match self:
            case 0:
                return Children.categories[0]
            case 1 | 2:
                return Children.categories[1]
            case _:
                return Children.categories[2]