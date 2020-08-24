import unittest

from session_TheGildedRose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):
    def test_foo(self):
        items = [Item("foo", 0, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals("foo", items[0].name)

    def test_sulfuras(self):
        items = [Item("Sulfuras, Hand of Ragnaros", 20, 80)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(80, items[0].quality)

    def test_sulfuras_past_date(self):
        items = [Item("Sulfuras, Hand of Ragnaros", 0, 80)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(80, items[0].quality)

    def test_aged_brie_increases_in_quality(self):
        items = [Item("Aged Brie", 20, 30)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(19, items[0].sell_in)
        self.assertEquals(31, items[0].quality)

    def test_aged_brie_hit_50_quality(self):
        items = [Item("Aged Brie", 20, 50)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(50, items[0].quality)

    def test_aged_brie_increases_by_2_after_date(self):
        items = [Item("Aged Brie", 0, 37)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(39, items[0].quality)

    def test_normal_item_quality(self):
        items = [Item("Rat Soup", 20, 11)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(10, items[0].quality)

    def test_normal_item_degrades_twice_as_fast(self):
        items = [Item("Rat Soup", 0, 11)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(9, items[0].quality)

    def test_normal_item_stops_at_0(self):
        items = [Item("Rat Soup", 10, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(0, items[0].quality)

    def test_backstage_pass_increases_quality(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 20, 25)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(26, items[0].quality)

    def test_backstage_pass_stops_at_50_quality(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 20, 50)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(50, items[0].quality)

    def test_backstage_pass_less_then_10_days(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 8, 25)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(27, items[0].quality)

    def test_backstage_pass_less_then_5_days(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 3, 25)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(28, items[0].quality)

    def test_backstage_pass_less_then_0_days(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 0, 25)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(0, items[0].quality)

    def test_conjured_item_degrading(self):
        items = [Item("Conjured Mana Potion", 15, 40)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(38, items[0].quality)

    def test_conjured_item_pass_degrades_twice_as_fast(self):
        items = [Item("Conjured Mana Potion", 0, 40)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(36, items[0].quality)

    def test_conjured_item_at_0_quality(self):
        items = [Item("Conjured Mana Potion", 10, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(0, items[0].quality)


if __name__ == '__main__':
    unittest.main()
