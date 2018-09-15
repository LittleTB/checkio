past_gifts = {}


def choose_good_gift(current_gift, gifts_in_bag, gift_number):
    past_gifts.setdefault(gifts_in_bag, [0])
    if ((2.712 * gift_number < gifts_in_bag or current_gift < max(past_gifts[gifts_in_bag]))
            and gift_number < gifts_in_bag):
        past_gifts[gifts_in_bag].append(current_gift)
        return False
    else:
        past_gifts[gifts_in_bag] = [0]
        return True

print(choose_good_gift(1.5,60,60))