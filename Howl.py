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

# Howl, a parser for Yelp! JSON datasets!

# Howl was designed to run with the Yelp! Academic Dataset: http://www.yelp.com/academic_dataset

# When run, Howl will generate an image and a KML file for a city and state of your choice.
# Or, pass "ALL" as the location, and generate a map of the entire dataset.
#
# $ python Howl.py Troy,NY 1024

# or

# $ python Howl.py ALL 2048

import json
import heatmap
import os, sys

if len(sys.argv) < 4:
    print "Howl, a parser for Yelp! JSON datasets!\nHowl will generate an image and a KML file for a city of your choice.\nAlternatively, pass \"ALL\" as the location for a map of all points.\n\nUsage: howl.py [City,State] [Output Image Width] [Yelp! Dataset Path]"
    quit()

city = state = None

# If they passed us a city and state (and not ALL), parse them out

location = sys.argv[1]
locationTuple = location.split(",")

if len(locationTuple) == 2:
    city = locationTuple[0]
    state = locationTuple[1]

# Cast the width to an integer

width = sys.argv[2]
width = int(width)

datasetLocation = sys.argv[3]

# Grab the academic dataset

yelpFile = open(datasetLocation)

points = [ ]

# Keep track of minimum and maximum latitude / longitude for scaling

minLatitude = 91
maxLatitude = -91

minLongitude = 181
maxLongitude = -181

for line in yelpFile:
    data = json.loads(line)
    if data["type"] == "business":
        if location == "ALL" or (data["city"] == city and data["state"] == state):
            # Save the point
            latitude = data["latitude"]
            longitude = data["longitude"]
            
            point = (longitude, latitude)
            
            # Append it to our points list for how many star ratings the place has
            stars = data["stars"]
            
            for i in range(0, int(stars)):
                points.append(point)
            
            # Calculate minimum/maximum latitude/longitude
            
            if latitude < minLatitude:
                minLatitude = latitude
            if latitude > maxLatitude:
                maxLatitude = latitude
            
            if longitude < minLongitude:
                minLongitude = longitude
            if longitude > maxLongitude:
                maxLongitude = longitude

# If we didn't find any points, let's let them know

if len(points) == 0:
    print "No points for {0}, {1}".format(city, state)
    quit()

# Compute dimensions such that we can have an image with the right aspect ratio

longitudeDifference = maxLongitude - minLongitude
latitudeDifference = maxLatitude - minLatitude

scaleFactor = width / longitudeDifference

height = int(scaleFactor * latitudeDifference)

# Now, ask heatmap to create a heatmap

hm = heatmap.Heatmap()

# Save the heatmap as a PNG and KML file

outputName = location

hm.heatmap(points, outputName + ".png", 30, 200, (width,height), scheme='classic')
hm.saveKML(outputName + ".kml")