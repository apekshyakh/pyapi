#!/usr/bin/env python3

vendors = ['cisco', 'juniper', 'big_ip', 'f5', 'arista', 'hp']

print("Currently the value of vendor:", vendors)

print("\nThe results of sorted() function:", sorted(vendors))

print("\nThe results of sorted() function:", sorted(vendors))

sortedvendors = sorted(vendors)

baksortvendors = sorted(vendors, reverse=True)

print('Our sorted vendor list looks like this: ', baksortvendors)

vendorsdeux = ['CISCO', 'JUNIPER', 'cisco', 'juniper', 'BIG_IP', 'big_ip', \
'f5', 'arista', 'HP', 'F5', 'hp', 'ARISTA']

print('Our sorted vendor list looks like this: ', sorted(vendorsdeux))

