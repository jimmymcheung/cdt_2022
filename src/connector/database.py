#!/usr/bin/env python
#
# Server database connector
# Copyright © 2022 CDT project
# Author: Jiaming Zhang
import getopt
import sys
import psycopg2
from configparser import ConfigParser
# pre-request: create database in PostGreSQL
# CREATE DATABASE db_name;
#
# Functions
#
# Read database configuration


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


def connect(filename='database.ini', section='postgresql'):
    """ Connect to the PostgreSQL database server

    :param: filename - str, section - str
    """
    conn = None
    try:
        # read connection parameters
        params = config(filename=filename, section=section)

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
def pg_read(select, conf='database.ini', sec='postgresql', quite=False):
    """ read from the PostgreSQL database

    :param: select - str, conf - str, sec - str, quite - boolean
    :return: reads
    """
    conn = None
    status = 0
    try:
        # read connection parameters
        params = config(filename=conf, section=sec)

        # connect to the PostgreSQL server
        if quite is False:
            print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(**params)

        # create a cursor
        cur = conn.cursor()

        # read from database
        cur.execute('SELECT ' + select + ';')
        reads = cur.fetchone()

        # close the communication with the PostgreSQL
        cur.close()
        return reads
    except (Exception, psycopg2.DatabaseError) as error:
        status = 1
        if quite is False:
            print(error)
    finally:
        if conn is not None:
            conn.close()
            if quite is False:
                print('Database connection closed.')

        if status != 0:
            import sys
            sys.exit(status)


# write to postgres
def pg_write(insert, conf='database.ini', sec='postgresql', quite=False, out=False):
    """ writes to the PostgreSQL database server

    :param: insert - str, conf - str, sec - str, quite - boolean, out - boolean
    """
    conn = None
    status = 0
    try:
        # read connection parameters
        params = config(filename=conf, section=sec)

        # connect to the PostgreSQL server
        if quite is False:
            print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(**params)

        # create a cursor
        cur = conn.cursor()

        # write to database
        cur.execute('INSERT INTO ' + insert + ';')
        w = cur.fetchone()
        # close the communication with the PostgreSQL
        cur.close()

        if (quite is False) or (out is True):
            print(str(w))

    except (Exception, psycopg2.DatabaseError) as error:
        status = 1
        if quite is False:
            print(error)
    finally:
        if conn is not None:
            conn.close()
            if quite is False:
                print('Database connection closed.')
        if status != 0:
            import sys
            sys.exit(status)


# other operation
def pg_handle(opr, conf='database.ini', sec='postgresql', quite=False, out=True):
    """ other operation with the PostgreSQL database

    :param: opr - str, conf - str, sec - str, quite - boolean, out - boolean
    :return: reads
    """
    status = 0
    conn = None
    if not opr:
        import sys
        print('\033[1mERROR: \'opr\' is required and must be valid SQL operation.\033[0m')
        sys.exit(1)

    try:
        # read connection parameters
        params = config(filename=conf, section=sec)

        # connect to the PostgreSQL server
        if quite is False:
            print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(**params)

        # create a cursor
        cur = conn.cursor()

        # operation with database
        cur.execute(opr)
        o = cur.fetchone()
        # close the communication with the PostgreSQL
        cur.close()

        if (quite is False) or (out is True):
            print(str(o))

    except (Exception, psycopg2.DatabaseError) as error:
        status = 1
        if quite is False:
            print(error)
    finally:
        if conn is not None:
            conn.close()
            if quite is False:
                print('Database connection closed.')
        if status != 0:
            import sys
            sys.exit(status)


# get option and input
def main(argv):
    operation = ''
    conf = 'database.ini'
    database = 'postgresql'
    quite = False
    out = 'default'
    read = ''
    write = ''
    usage = '\033[5mUsage:\033[0m\n   \033[1mdatabase.py\033[0m [-o|--opr'\
            ' \033[4mSQL operation\033[0m] [-c|--conf \033[4mconfig file'\
            '\033[0m] [-d|--db \033[4mdatabase section\033[0m] [-q|--quite]'\
            ' [-Q|--Quite] [-r \033[4mSELECT operation\033[0m] [-w \033[4m'\
            'INSERT INTO operation\033[0m]'
    try:
        opts, args = getopt.getopt(argv, "ho:c:d:qQr:w:", ["help", "opr=", "conf=", "db=", "quite", "Quite"])
    except getopt.GetoptError:
        print(usage)
        sys.exit(2)
    for opt, arg in opts:
        if opt in ('-h', "--help"):
            print(usage)
            sys.exit(0)
        elif opt in ("-o", "--opr"):
            operation = arg
        elif opt in ("-c", "--conf"):
            conf = arg
        elif opt in ("-d", "--db"):
            database = arg
        elif opt in ("-q", "--quite"):
            quite = True
        elif opt in ("-Q", "--Quite"):
            quite = True
            out = False
        elif opt == '-r':
            read = arg
        elif opt == '-w':
            write = arg
    # operation call
    if read:
        readout = pg_read(select=read, conf=conf, sec=database)
        return readout
    if write:
        if out == 'default':
            pg_write(insert=write, conf=conf, sec=database, quite=quite)
        else:
            pg_write(insert=write, conf=conf, sec=database, quite=quite, out=out)
    if operation != '':
        if out == 'default':
            pg_handle(operation, conf=conf, sec=database, quite=quite)
        else:
            pg_handle(operation, conf=conf, sec=database, quite=quite, out=out)
    else:
        connect(filename=conf, section=database)


# test
if __name__ == '__main__':
    main(sys.argv[1:])
