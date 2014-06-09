superpaste
==========

Upgrade for standard unix paste command.

Basically written because I was sick and tired of standard paste making files where each line has a different length look like wobbly crap when displayed side by side.  Superpaste pads each line in a file out to the width of the longest line before printing the matching line from the second file, so everything lines up neatly.

TODO:

* Print help / error messages when appropriate
* Handle more than 2 input files
* Handle input from stdin
* Improve compatibiltiy with standard paste to facilitate aliasing 'superpaste' to 'paste' without headaches
* Restructure to avoid reading entire files into memory if possible
