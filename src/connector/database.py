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
    """ Connect to the PostgreSQL database server """
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
def pg_read(select, conf='database.ini', sec='postgresql'):
    """ read from the PostgreSQL database server """
    conn = None
    err_code = 0
    try:
        # read connection parameters
        params = config(filename=conf, section=sec)

        # connect to the PostgreSQL server
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
        print(error)
        err_code = 1
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')

        if err_code != 0:
            import sys
            sys.exit(err_code)


# write to postgres
def pg_write(insert, conf='database.ini', sec='postgresql', quite=False):
    """ writes to the PostgreSQL database server """
    conn = None
    err_code = 0
    try:
        # read connection parameters
        params = config(filename=conf, section=sec)

        # connect to the PostgreSQL server
        print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(**params)

        # create a cursor
        cur = conn.cursor()

        # write to database
        cur.execute('INSERT INTO ' + insert + ';')
        w = cur.fetchone()

        # close the communication with the PostgreSQL
        cur.close()

        # check if written successfully
        if w and (quite is False):
            print('\033[0mINFO: Successfully written to database.')
        elif w and (quite is True):
            status = 0
            return status
        elif (not w) and (quite is False):
            print('\033[1mERROR: The write action was failed. \033[0m')
            sys.exit(1)
        else:
            status = 1
            return status
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        err_code = 1
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')
        if err_code != 0:
            import sys
            sys.exit(err_code)


# other operation
def pg_handle(opr, conf='database.ini', sec='postgresql', quite=False):
    """ other operation with the PostgreSQL database server """
    err_code = 0
    conn = None
    if not opr:
        import sys
        print('\033[1mERROR: \'opr\' is required and must be valid SQL operation.\033[0m')
        sys.exit(1)

    try:
        # read connection parameters
        params = config(filename=conf, section=sec)

        # connect to the PostgreSQL server
        print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(**params)

        # create a cursor
        cur = conn.cursor()

        # operation with database
        cur.execute(opr)
        o = cur.fetchone()
        # close the communication with the PostgreSQL
        cur.close()

        if quite is True:
            print(str(o))
        # if o and (quite is False):
        #     print('\033[0m' + str(o))
        # elif o and (quite is True):
        #     status = 0
        #     return status
        # elif (not o) and (quite is False):
        #     import sys
        #     print('\033[1mERROR: The given operation was failed. \033[0m')
        #     sys.exit(1)
        # else:
        #     status = 1
        #     return status

    except (Exception, psycopg2.DatabaseError) as error:
        err_code = 1
        if quite is False:
            print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')
        if err_code != 0:
            import sys
            sys.exit(err_code)


# get option and input
def main(argv):
    operation = ''
    conf = 'database.ini'
    database = 'postgresql'
    quite = False
    read = ''
    write = ''
    usage = '\033[5mUsage:\033[0m\n   \033[1mdatabase.py\033[0m -o <SQL operation> -c <config file> -d <database section> -q -r <READ operation> -w <WRITE operation>'
    try:
        opts, args = getopt.getopt(argv, "ho:c:d:qr:w:", ["help", "opr=", "conf=", "db=", "quite"])
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
        elif opt == '-r':
            read = arg
        elif opt == '-w':
            write = arg
    # operation call
    if read:
        readout = pg_read(select=read, conf=conf, sec=database)
        return readout
    if write:
        write_out = pg_write(insert=write, conf=conf, sec=database, quite=quite)
        return write_out
    if operation != '':
        pg_handle(operation, conf=conf, sec=database, quite=quite)
    else:
        connect(filename=conf, section=database)


# test
if __name__ == '__main__':
    main(sys.argv[1:])
