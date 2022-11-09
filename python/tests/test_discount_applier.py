from discount_applier import DiscountApplier

class Notifier:
    def __init__(self):
        self.messages = {}

    def notify(self, name, message):
        self.messages[str(name)]= message
    
def test_apply_v1():
    # TODO: write a test that fails due to the bug in
    # DiscountApplier.apply_v1
    discount = 30
    users = ['Denis', 'Michel']
    notifier = Notifier()
    discount_applier = DiscountApplier(notifier)
    discount_applier.apply_v1(discount, users)
    assert len(users) == len(notifier.messages.values()), "Number of messages isn't correct"


def test_apply_v2():
    # TODO: write a test that fails due to the bug in
    # DiscountApplier.apply_v2
    discount = 30
    users = ['Denis', 'Michel']
    notifier = Notifier()
    discount_applier = DiscountApplier(notifier)
    discount_applier.apply_v2(discount, users)
    # How to get notification of the user to assert equals ?
    # assert discount for 'Michel'
    assert notifier.messages.get('Michel') == f"You've got a new discount of {discount}", "User not correspond to notification"

