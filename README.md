# Random Quote

A simple pelican plugin used to populate a variable `{{ QUOTE }}` selecting randomly lines from a text file at every generation of the pelican output. Useful to show variable quotes and fortunes.

## Usage

Put in your `pelicanconf.py` the variable `RANDOM_QUOTE` configured pointing to a text file with a line for every quote and put in your template the variable `{{ QUOTE }}` where you want to show the line selected.
