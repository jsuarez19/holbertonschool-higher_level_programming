#!/usr/bin/python3
"""

"""

import sys
from sqlalchemy import (create_engine)
from sqlalchemy.orm import Session
from sqlalchemy.engine.url import URL
from model_state import Base, State

""" To not execute when imported """
if __name__ == '__main__':
    host="localhost"
    port=3306
    user=sys.argv[1]
    passwd=sys.argv[2]
    db=sys.argv[3]

    