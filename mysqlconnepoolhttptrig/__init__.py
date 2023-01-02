import logging

import azure.functions as func
import mysql.connector
from mysql.connector import Error
from mysql.connector import pooling

# Create a connection pool
connection_pool = pooling.MySQLConnectionPool(
    pool_name="pynative_pool",
    pool_size=5,
    host='mysqlfexibleserver.mysql.database.azure.com',
    user='userId',
    password='password',
    database='python_db',
    ssl_ca="DigiCertGlobalRootCA.crt.pem"
)


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    try:
        logging.info("Printing connection pool properties ")
        logging.info("Connection Pool Name - "+ connection_pool.pool_name)
        logging.info("Connection Pool Size - ")
        logging.info( connection_pool.pool_size)

        # Get connection object from a pool
        connection_object = connection_pool.get_connection()

        if connection_object.is_connected():
            db_Info = connection_object.get_server_info()
            logging.info("Connected to MySQL database using connection pool ... MySQL Server version on " + db_Info)
            connection_id = connection_object.connection_id; 

            logging.info("Connected to MySQL database using connection pool ... MySQL connection_id " )
            logging.info(connection_id) 

            cursor = connection_object.cursor()
            cursor.execute("select database();")
            record = cursor.fetchone()
            logging.info("Your connected to - " )
            logging.info(record )
            

    except Error as e:
        logging.info("Error while connecting to MySQL using Connection pool ", e)
    finally:
        # closing database connection.
        if connection_object.is_connected():
            cursor.close()
            connection_object.close()
            logging.info("MySQL connection is closed")

   
    return func.HttpResponse(
            "This HTTP triggered function executed successfully.",
            status_code=200
    )
