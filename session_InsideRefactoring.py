class GildedRose(object):
    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:

            item.sell_in -= 1
            if item.name == "Sulfuras, Hand of Ragnaros":
                item.quality = 80
                continue

            elif item.name == "Aged Brie":
                item.quality += 1
                if item.sell_in < 0:
                    item.quality += 1
                item.quality = min(item.quality, 50)
                continue

            elif "Conjured" in item.name:
                item.quality -= 2
                if item.sell_in < 0:
                    item.quality -= 2
                continue

            elif item.name == "Backstage passes to a TAFKAL80ETC concert":
                if item.sell_in < 0:
                    item.quality = 0
                elif item.sell_in < 6:
                    item.quality += 3
                elif item.sell_in < 11:
                    item.quality += 2
                else:
                    item.quality += 1
                item.quality = min(item.quality, 50)
                continue
            else:
                item.quality -= 1
                item.quality = max(item.quality, 0)
                if item.sell_in < 0:
                    item.quality -= 1
                    item.quality = max(item.quality, 0)


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
