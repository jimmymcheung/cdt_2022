#!/usr/bin/env python
#
# Server database connector
# Copyright © 2022 CDT project
# Author: Jiaming Zhang

import psycopg2
from configparser import ConfigParser
import config
# pre-request: create database in PostGreSQL
# CREATE DATABASE db_name;

# Functions
# Read database configuration
# example file database.ini
# [postgresql]
# host=localhost
# database=db1
# user=postgres
# password=SecurePas$1
# port=5432


def config(filename='database.ini', section='postgresql'):
    # create a parser
    parser = ConfigParser()
    # read config file
    parser.read(filename)

    # get section, default to postgresql
    db = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            db[param[0]] = param[1]
    else:
        raise Exception('Section {0} not found in the {1} file'.format(section, filename))

    return db


def connect():
    """ Connect to the PostgreSQL database server """
    conn = None
    try:
        # read connection parameters
        params = config()

        # connect to the PostgreSQL server
        print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(**params)

        # create a cursor
        cur = conn.cursor()

    # execute a statement
        print('PostgreSQL database version:')
        cur.execute('SELECT version()')

        # display the PostgreSQL database server version
        db_version = cur.fetchone()
        print(db_version)

    # close the communication with the PostgreSQL
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')


# read from postgres
def pg_read(conf='database.ini', sec='postgresql'):
    """ read from the PostgreSQL database server """
    conn = None
    try:
        # read connection parameters
        params = config(filename=conf, section=sec)

        # connect to the PostgreSQL server
        print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(**params)

        # create a cursor
        cur = conn.cursor()

        # read from database
        # needs to be changed
        reads = cur.execute('SELECT version()')
        return reads

    # close the communication with the PostgreSQL
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')


# write to postgres
def pg_write(conf='database.ini', sec='postgresql', quite=False):
    """ writes to the PostgreSQL database server """
    conn = None
    try:
        # read connection parameters
        params = config(filename=conf, section=sec)

        # connect to the PostgreSQL server
        print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(**params)

        # create a cursor
        cur = conn.cursor()

        # write to database
        # needs to be changed
        cur.execute('SELECT version()')

        # check if written successfully
        w = cur.execute('')
        if w and (quite is False):
            print('\033[0mINFO: Successfully written to database.')
        elif w and (quite is True):
            status = 0
            return status
        elif (not w) and (quite is False):
            import sys
            print('\033[1mERROR: The write action was failed. \033[0m')
            sys.exit(1)
        else:
            status = 1
            return status

    # close the communication with the PostgreSQL
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')


if __name__ == '__main__':
    # test connection PostGreSQL
    connect()
