"""
Package providing remote access to and local persistant storage of GRB data
from the BATSE 5Bp ("Current") catalog hosted by the Compton Observatory
Science Support Center (COSSC) at Goddard Space Flight Center.

Created 2012-05-07 by Tom Loredo
"""

# Import modules that deserve easy top-level access if "import *" is used.
from batse5bp import locations
from batse5bp import catalog
from batse5bp import docn
from batse5bp import grb

# Import objects that deserve easy top-level access.
from batse5bp.catalog import load_catalog
from batse5bp.docn import *  # just imports 'show_' functions
