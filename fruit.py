#!/usr/bin/env python
prices = {'apple':0.4, 'pear':0.5}
purchase = {'apple':4, 'pear':3}
total = sum(prices[fruit] * purchase[fruit]
        for fruit in purchase)
print total
