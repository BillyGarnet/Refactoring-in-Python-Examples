import unittest

from TheGildedRose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):
    def test_sulfuras_maintains_quality(self):
        items = [Item("Sulfuras, Hand of Ragnaros", 10, 80)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(items[0].quality, 80)

    def test_brie_at_50_quality(self):
        items = [Item("Aged Brie", 5, 50)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(items[0].quality, 50)

    def test_brie_at_25_quality(self):
        items = [Item("Aged Brie", 5, 25)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(items[0].quality, 26)

    def test_mead_degrading(self):
        items = [Item("Mead", 5, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(items[0].quality, 19)

    def test_mead_degrading_after_date(self):
        items = [Item("Mead", 0, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(items[0].quality, 18)

    def test_mead_spoiled(self):
        items = [Item("Mead", 0, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(items[0].quality, 0)

    def test_concert_ticket(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 25, 30)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(items[0].quality, 31)

    def test_concert_ticket_less_then_10_days(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 8, 40)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(items[0].quality, 42)

    def test_concert_ticket_less_then_5_days(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 4, 40)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(items[0].quality, 43)

    def test_concert_ticket_less_then_0_days(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 0, 45)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(items[0].quality, 0)

    def test_concert_ticket_at_49_quality_with_4_days(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 4, 49)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(items[0].quality, 50)

    def test_concert_ticket_at_90_quality_with_4_days(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 4, 90)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(items[0].quality, 50)

    def test_conjured_degrades_twice_as_fast(self):
        items = [Item("Conjured Mana Potion", 10, 28)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(items[0].quality, 26)

    def test_conjured_degrades_twice_as_fast(self):
        items = [Item("Conjured Mana Potion", 10, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(items[0].quality, 0)

    def test_conjured_after_due_date(self):
        items = [Item("Conjured Mana Potion", 0, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(items[0].quality, 16)


if __name__ == '__main__':
    unittest.main()
