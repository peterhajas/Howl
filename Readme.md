Howl, a series of tools for the Yelp! academic dataset
======================================================

by Peter Hajas

![Troy, NY as visualized by Howl.py](http://i.imgur.com/CTOmS.png "Troy, NY")

(Troy, NY as visualized by Howl.py)

About
-----

Howl is a series of simple Python scripts for analyzing the Yelp! Academic Dataset, used for my research with [Dr. Krishnamoorthy](http://cs.rpi.edu/~moorthy)

Source files have explanations in them after the license header.

Howl.py is a simple python tool for visualizing location reviews around your town.

The more red/white a point is, the better the reviews.

Howl requires Heatmap.py, the Python Image Library and a recent Python version.

Howl was designed for use with the [Yelp! Academic Dataset](http://www.yelp.com/academic_dataset)

Howl.py Usage
-------------

Simply run Howl with a city, state and an image width

`./Howl.py Troy,NY 1024 yelp_academic_dataset.json`

or with ALL as a location, to generate an image for the entire dataset:

`./Howl.py ALL 1024 yelp_academic_dataset.json`
(this will probably take a while)

and Howl will generate an image and KML file for your location.

It'll save them in the current working directory, like this:

`Troy,NY.png`, `Troy,NY.kml` or `ALL.png`

Open Howl KML files in a tool like Google Earth to visualize reviews.

It's really neat!

Legal
-----

All of Howl is Copyright 2011 Peter Hajas. It's BSD licensed. The full text of the
license can be found in Howl.py.

The work in Howl does not imply endorsement by past, current or future
employers.
