#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import functools 
from types import GeneratorType
from Fight import *
from operator import *

class TestFights(unittest.TestCase):
    def test_random_age_returns_int_iterable(self):
        ages = random_ages()
        self.assertEqual(type(ages), GeneratorType, 'random_age() should return an iterable')
        self.assertEqual(type(next(ages)), int, 'random_age() should return an iterable that spits out ints')

    def test_random_age_returns_random_int_by_default(self):
        ages = random_ages()
        age1 = next(ages)
        age2 = next(ages)
        self.assertNotEqual(age1, age2, 'random_ages() iterable should return random ages')

    def test_get_age_returns_random_int_between_range(self):
        min_age = 1
        max_age = 5
        ages = random_ages(min_age,max_age)
        for n in range(1,10):
            age = next(ages)
            self.assertTrue(and_(ge(age,min_age),le(age, max_age)), 'get_age() should return a random number in the range')

    def test_random_fighters_returns_fighter_from_iterable(self):
        mock_fighters = ['a', 'b', 'c']
        fighters = random_fighters(mock_fighters)
        for n in range(1,10):
            fighter = next(fighters)
            self.assertTrue(contains(mock_fighters, fighter), 'random fighter should be from list')

    def test_random_contest_returns_contest_from_iterable(self):
        mock_contests = ['a', 'b', 'c']
        contests = random_contests(mock_contests)
        for n in range(1,10):
            contest = next(contests)
            self.assertTrue(contains(mock_contests, contest), 'random contest should be from list')

if __name__ == '__main__':
    unittest.main()
