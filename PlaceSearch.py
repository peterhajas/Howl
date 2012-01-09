#!/usr/bin/env python

# Copyright (c) 2011, Peter Hajas
# All rights reserved.

# Redistribution and use in source and binary forms, with or without modification, are permitted
# provided that the following conditions are met:

# Redistributions of source code must retain the above copyright notice, this list of conditions and
# the following disclaimer.
# Redistributions in binary form must reproduce the above copyright notice, this list of conditions
# and the following disclaimer in the documentation and/or other materials provided with the
# distribution.
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR
# IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND
# FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR
# CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
# DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
# DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER
# IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT
# OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

# A very rudimentary tool for searching the Yelp! academic 
# dataset for places matching a query

import json
import os, sys

if len(sys.argv) < 3:
    print "Usage: PlaceSearch.py [Query] [Yelp! Dataset Path]"
    quit()
    
query = sys.argv[1]
datasetLocation = sys.argv[2]
cities = [ ]

yelpFile = open(datasetLocation)

matchingFile = open("matchesQuery", 'w')

count = 0

for line in yelpFile:
    data = json.loads(line)
    if data["type"] == "business":
        if data["city"].find(query) != -1:
            # This is the city / state they're interested in, keep track of
            # this business id:
            
            id = data["business_id"]
            lat = data["latitude"]
            lon = data["longitude"]
            
            count += 1
            
            matchingFile.write("{} {} {}\n".format(id, lat, lon))
            
print "Found {} businesses matching place query {}".format(count, query)