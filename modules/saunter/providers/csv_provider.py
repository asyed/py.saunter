# Copyright 2011 Element 34
# 
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# 
#     http://www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""
============
CSV Provider
============
"""
import csv
import os.path
import random

class CSVProvider(object):
    """
    Provides data for either data driven scripting or as oracles from a csv file

    :params c: name of csv file locates in support/csv directory
    """
    def __init__(self, c):
        """
        :params c: name of csv file locates in support/csv directory
        """
        f = os.path.join(os.path.dirname(__file__), '..', '..', '..', 'support', 'csv', c)
        self.data = csv.DictReader(open(f, 'r'))
        
    def randomRow(self):
        """
        Gets a random row from the provider

        :returns: List
        """
        l = []
        for row in self.data:
            l.append(row)
        return random.choice(l)