#!/usr/bin/python3

# Copyright © 2021 Camptocamp.
#
# This file is part of Meeting-Randomizer.
#
# Meeting-Randomizer is free software; you can redistribute it and/or modify it
# under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or (at
# your option) any later version.
#
# Meeting-Randomizer is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Meeting-Randomizer.  If not, see <http://www.gnu.org/licenses/>.

import data
import random

lans = list(data.languages.keys())
weights = list(data.languages.values())

lan_choise = random.choices(population=lans, weights=weights,k=1)[0]
person_order=random.sample(population=data.persons,k=len(data.persons))

print("Language of the day:")
print("====================")
print(lan_choise)
print()
print("Order of the day:")
print("=================")
for person in person_order:
    print(person)
