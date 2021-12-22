#!/usr/bin/python3
"""DB Storage Module for AirBnb Project"""
import MySQLdb


class DBStorage:
    __engine = None
    __session = None

    def __init__(self):
        self.__engine = MySQLdb.connect(
            host="localhost",
            user="hbnb_dev",
            passwd="hbnb_dev_pwd",
            db="hbnb_dev_db")
