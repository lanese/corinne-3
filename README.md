# corinne-3

## Installation

The following prerequisites should be fulfilled:

- python3
- python3-pip
- antlr4

Corinne relies on, antlr4, the DOT format, and python's Tkinter (for its GUI);
therefore the following packages are required:

- install python3-tk
- python3-pil.imagetk
- graphviz

In debian-based distros execute the following commands from a shell.

- sudo apt install antlr4
- sudo apt install graphviz
- sudo apt install python3-graphviz
- sudo apt install python3-tk
- sudo apt install python3-pil.imagetk
- sudo pip install antlr4-python3-runtime

1. execute the 'makeParser.sh' script in the subdirectory 'global_graph_parser'
2. execute the 'makeParser.sh' script in the subdirectory 'dot_parser'

You can now execute the script 'corinne.sh' from the root directory.
Have fun!
