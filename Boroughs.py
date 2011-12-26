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

# Sort a list of businesses with latitude/longitude points into boroughs
# from a passed-in geometry file

import sys
import planar
from elementtree import ElementTree

# We should later parse this out of the XML

def borough_for_line(lineNum):
    if lineNum == 1:
        return "Manhattan"
    elif lineNum == 2:
        return "The Bronx"
    elif lineNum == 3:
        return "Staten Island"
    elif lineNum == 4:
        return "Brooklyn"
    elif lineNum == 5:
        return "Queens"
    
# Argument checking

if len(sys.argv) < 3:
    print "Please pass a path to a polygon CSV file and a path to a list of"
    print "businesses with latitude/longitude points, space-delimited."
    quit()

geometryFile = open(sys.argv[1])
businessFile = open(sys.argv[2])

count = 0

boroughs = { }

for line in geometryFile:
    pointList = [ ]
    
    if count == 0:
        count+=1
        continue
    
    boroughs[borough_for_line(count)] = [ ]
    
    # Split by quotes for Google fusion table CSV/XML data
    
    elements = line.split("\"")
    root = ElementTree.XML(elements[1])
    
    for child in root.getchildren():
        # Each of these children is a polygon, make a new point list
        
        pointList = [ ]
        
        allCoordinates = child[0][0].getchildren()[0].text.split(",0 ")
        for coordinate in allCoordinates:
            coordinateComponents = coordinate.split(",")
            latitude = float(coordinateComponents[0])
            longitude = float(coordinateComponents[1])
            
            pointList.append(planar.Vec2(latitude,longitude))
        
        # Create the polygon
        
        polygon = planar.Polygon.convex_hull(pointList)
        
        # Add it to the list in our dictinary
        
        boroughs[borough_for_line(count)].append(polygon)
        
    count+=1


# Sort all the business id's by borough

borough_cities = { }

for key in boroughs.keys():
    borough_cities[key] = [ ]

# Some businesses will not be in a borough

borough_cities["None"] = [ ]

for line in businessFile:
    lineElements = line.split()
    id = lineElements[0]
    location = planar.Vec2(float(lineElements[1]), float(lineElements[2]))
    
    # Find which borough this point belongs in
    
    found_borough = False
    
    for borough in boroughs.keys():
        for polygon in boroughs[borough]:
            if polygon.contains_point(location):
                found_borough = True
                borough_cities[borough].append(id)
    
    if not found_borough:
        borough_cities["None"].append(id)

# Save these businesses sorted by boroughs into a file

sorted_businesses = open("sorted", 'w')

for borough in borough_cities.keys():
    sorted_businesses.write("{}\n".format(borough))
    for business_id in borough_cities[borough]:
        sorted_businesses.write("{}\n".format(business_id))
    sorted_businesses.write("\n")
    