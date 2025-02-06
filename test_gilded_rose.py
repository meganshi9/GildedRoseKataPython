# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):
    # example of test that checks for logical errors
    def test_sulfuras_should_not_decrease_quality(self):
        items = [Item("Sulfuras", 5, 80)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        sulfuras_item = items[0]
        self.assertEquals(80, sulfuras_item.quality)
        self.assertEquals(4, sulfuras_item.sell_in)
        self.assertEquals("Sulfuras", sulfuras_item.name)
    
    # failed test for business logic errors
    def test_aged_brie_quality_should_not_exceed_50(self):
        items = [Item("Aged Brie", 2, 50)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        aged_brie_item = items[0]
        self.assertEquals(50, aged_brie_item.quality)
        self.assertEquals(1, aged_brie_item.sell_in)
        self.assertEquals("Aged Brie", aged_brie_item.name)

    def test_quality_degrades_twice_as_fast_after_sell_by_date(self):
            items = [Item("Elixir of the Mongoose", 0, 10)]  
            gilded_rose = GildedRose(items)
            gilded_rose.update_quality()
            elixir_item = items[0]
            self.assertEquals(8, elixir_item.quality)  
            self.assertEquals(-1, elixir_item.sell_in)
            self.assertEquals("Elixir of the Mongoose", elixir_item.name)

    def test_conjured_items_should_degrade_twice_as_fast(self):
        items = [Item("Conjured Mana Cake", 3, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        conjured_item = items[0]
        self.assertEquals(8, conjured_item.quality)  
        self.assertEquals(2, conjured_item.sell_in)
        self.assertEquals("Conjured Mana Cake", conjured_item.name)


    # example of test that checks for syntax errors
    def test_gilded_rose_list_all_items(self):
        items = [Item("Sulfuras", 5, 80)]
        gilded_rose = GildedRose(items)
        all_items = gilded_rose.get_items()
        self.assertEquals(["Sulfuras"], all_items)

    #failed test for Syntax error 
    def test_gilded_rose_get_item_quality(self):
        items = [Item("Aged Brie", 2, 0)]
        gilded_rose = GildedRose(items)
        item_quality = gilded_rose.get_item_quality("Aged Brie") 
        self.assertEquals(0, item_quality)



if __name__ == '__main__':
    unittest.main()