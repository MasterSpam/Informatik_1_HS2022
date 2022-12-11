class ItemConfirm:
    _actives = {}

    def __init__(self, text):
        self.text = text
        self.active = False

    def __str__(self):
        return f"'{self.text}'"

    def __repr__(self):
        return str(self)

    def select(self):
        """ select this instance """
        self.active = True
        ItemConfirm.set_icon(self, self.text)  # will add to class variable of all actives

    @classmethod
    def set_icon(cls, instance_check, self_text):
        """ select or deselect item """

        if instance_check.active:
            # case select: add to dict
            ItemConfirm._actives[instance_check] = self_text
        else:
            # case deselect: remove from dict
            if instance_check in ItemConfirm._actives:
                del ItemConfirm._actives[instance_check]
            else:
                print(f"WARNING: {self_text} not in ItemConfirm.actives")

    @classmethod
    def get_actives(cls):
        """ return copy of all activated list item texts"""
        return list(cls._actives.values())

    @classmethod
    def reset_actives(cls):
        """ reset every activated list item"""

        items = list(cls._actives.items())  # get copy of items; avoid runtime error
        for instance_check, text in items:
            instance_check.active = False  # deactivate item
            ItemConfirm.set_icon(instance_check, text)  # simulate deactivation click


if __name__ == '__main__':
    item_1 = ItemConfirm('item 1')
    item_2 = ItemConfirm('item 2')
    items = [
        item_1,
        item_2
    ]

    print(f"Items: {items}\n")

    # select item
    print(f'select {item_1}')
    item_1.select()

    print(f"Get all selected items: {ItemConfirm.get_actives()}\n")

    print(f"Deselect all")
    ItemConfirm.reset_actives()
    print(f"Get all selected items: {ItemConfirm.get_actives()}")
