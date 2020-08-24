class GildedRose(object):
    def __init__(self, items):
        self.items = items

    def update_quality(self):

        for item in self.items:
            if item.name == "Sulfuras, Hand of Ragnaros":
                item.quality = 80
                continue

            if item.name == "Aged Brie":
                item.quality = item.quality + 1
                self.dont_exceed_50(item)
                continue

            if item.name == "Backstage passes to a TAFKAL80ETC concert":
                item.quality = self.get_ticket_quality(item)
                continue

            if "Conjured" in item.name:
                item.quality -= 2
                if item.sell_in <= 0:
                    item.quality -= 2
                self.dont_drop_below_0(item)
                continue

            self.handle_normal_items(item)

    def get_ticket_quality(self, item):
        if item.sell_in <= 0:
            item.quality = 0
        elif item.sell_in < 6:
            item.quality += 3
        elif item.sell_in < 11:
            item.quality += 2
        else:
            item.quality += 1
        self.dont_exceed_50(item)
        return item.quality

    def handle_normal_items(self, item):
        item.sell_in -= 1

        item.quality -= 1

        if item.sell_in < 0:
            item.quality -= 1

        self.dont_drop_below_0(item)

    def dont_drop_below_0(self, item):
        if item.quality < 0:
            item.quality = 0

    def dont_exceed_50(self, item):
        if item.quality > 50:
            item.quality = 50


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
