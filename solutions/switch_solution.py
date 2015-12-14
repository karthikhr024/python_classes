from help_csv import *
from os.path import basename
import pandas as pd
import json
import boto3
from botocore.exceptions import ClientError
import mysql
from mysql.connector import MySQLConnection, Error, errorcode

DEBUG = 0

class Controller(object):
    def __init__(self, cnx):
        self.cnx = cnx
        self.cursor = self.cnx.cursor()
        self.tables = []

    def get_db(self, name):
        # Get an existing database named db_name.
        # If it doesn't exist, create a new database db_name.
        # Also get all tables in database.
        cursor = cnx.cursor()
        print "[INFO]  Fetching database %s ..." % name
        try:
            cnx.database = name
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_BAD_DB_ERROR:
                print "[ERROR] Database %s does not exist! Creating database..." % name
                self.create_db(name)
                cnx.database = name
            else:
                print(err)
                exit(1)
        print "[INFO]  Database %s selected." % name

    def create_db(self, name):
        # Create a new database on the MySQL server
        query = "CREATE DATABASE %s" % name
        self.exec_query(query)

    def delete_db(self, name):
        # Delete an existing database.
        query = "DROP DATABASE %s" % name
        self.exec_query(query)

    def delete_table(self, name):
        # Delete a table from the database
        query = "DROP TABLE %s" % name
        self.exec_query(query)

    def create_table(self, name, args):
        # Create a new table in the database.
        args_str = ','.join(args)
        query = "CREATE TABLE IF NOT EXISTS %s" % name + "(" + args_str + ")"
        self.exec_query(query)

    def describe_table(self, name):
        query = "DESCRIBE %s" % name
        self.exec_query(query)
        try:
            import pandas
            df = pandas.DataFrame(self.cursor.fetchall())
            print df
            print
        except ImportError:
            print self.cursor.fetchall()
            print

    def exec_query(self, query, query_args=None):
        try:
            if query_args is not None:
                print "[INFO]  Executing SQL: \"%s\"..." % (query % query_args),
                self.cursor.execute(query, query_args)
            else:
                print "[INFO]  Executing SQL: \"%s\"..." % query,
                self.cursor.execute(query)
            print " SUCCESS"
        except mysql.connector.Error as err:
            print
            print "[ERROR] " + err.msg

if __name__ == '__main__':
    table_names = ["Inventory", "HP BladeSystem Rack", "Network Interface"]
    paths = split_csv("../files/switch_records.csv", table_names)

    # Construct dataframes from each csv file (one per table)
    dataframes = []
    for p in paths:
        with open(p, 'r') as f:
            df = pd.read_csv(f, skiprows=1)
            df.name = basename(p).replace('.csv','')
            dataframes.append(df)

    for df in dataframes:
        if DEBUG:
            print df.name
            print df.columns
            print

    # Create json files for each table
    files = []
    for df in dataframes:
        fname = "../files/" + df.name + "_output.json"
        files.append(fname)
        df.to_json(fname)

    print "Files written:"
    for f in files:
        print f

    # Load the json files
    jsons = []
    for f in files:
        j = json.load(open(f, 'r'))
        jsons.append(j)

    #############
    ### MYSQL ###
    #############

    # Connection
    config = {
        'user': 'root',
        'password': 'password',
        'host': 'localhost',
        'raise_on_warnings': True,
    }
    try:
        cnx = MySQLConnection(**config)
    except Error as e:
        print "[ERROR] Could not connect to MySQL database."
        exit(1)

    ctrl = Controller(cnx) # Instantiate controller

    # Create database
    ctrl.get_db('ocervell')

    # Create and populate table with each json file
    for f in files:
        name = basename(f).lower().replace('.json','')
        args = ("`doc` json DEFAULT NULL",
                "`updated` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"
                )
        ctrl.create_table(name, args)
        content = json.load(open(f, 'r'))
        insert = "INSERT INTO %s (doc) " % name
        insert += "VALUES(%s)"

        ctrl.exec_query(insert, (json.dumps(content),))
    cnx.close()


    #################
    ### DYNAMO DB ###
    #################

    # Connection
    dynamodb_resource = boto3.resource('dynamodb', endpoint_url="http://localhost:9090")

    # Create tables
    for f in files:
        name = basename(f).lower().replace('.json','')
        j = json.load(open(f, 'r'))
        KeySchema = {'AttributeName': ', 'KeyType': 'HASH'}
        AttributeDefinitions = {'AttributeName': key.encode(), 'AttributeType': 'S'}
        print KeySchema
        print AttributeDefinitions
        try:
            table = dynamodb_resource.create_table(
                TableName=name,
                KeySchema=[KeySchema,]
                AttributeDefinitions=AttributeDefinitions,
                ProvisionedThroughput={'ReadCapacityUnits': 10, 'WriteCapacityUnits': 10}
            )
        except ClientError as e:
            print e





