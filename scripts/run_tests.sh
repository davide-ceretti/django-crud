#!/bin/bash

# This should be run from the folder where manage.py is.
# The virtual env should have also been activate

python manage.py test core items
