Howl, a visualizer for the Yelp! academic dataset
=================================================

by Peter Hajas

![Troy, NY as visualized by Howl](http://i.imgur.com/CTOmS.png "Troy, NY")

About
-----

Howl is a simple python tool for visualizing location reviews around your town.

The more red/white a point is, the better the reviews.

Howl requires Heatmap.py, the Python Image Library and a recent Python version.

Howl was designed for use with the [Yelp! Academic Dataset](http://www.yelp.com/academic_dataset)

Usage
-----

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

Howl is Copyright 2011 Peter Hajas. It's BSD licensed. The full text of the
license can be found in Howl.py.

The work in Howl does not imply endorsement by past, current or future
employers.
