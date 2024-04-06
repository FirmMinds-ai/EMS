import json
import pymysql
import rds_config
import sys
from datetime import datetime
import uuid
import boto3
from botocore.exceptions import ClientError

##RDS##insert_data

rds_host = rds_config.db_endpoint
name = rds_config.db_username
password = rds_config.db_password
db_name = rds_config.db_name
port = 3306
import logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)

try:
    conn = pymysql.connect(host=rds_host,user=name,
                           passwd=password,db=db_name,
                           connect_timeout=5,
                           cursorclass=pymysql.cursors.DictCursor)
    print(conn)                       
except:
    logger.error("ERROR: Unexpected error: Could not connect to MySql instance.")
    sys.exit()


cur = conn.cursor() 

def insert_data(name,contact,email,subject,message):
    with conn.cursor() as cur:
        query = "INSERT INTO employeemanagement.contactus (name, contact, email, subject, message) VALUES(%s,%s,%s,%s,%s);"
        data = (name,contact,email,subject,message)
        cur.execute(query,data)
        conn.commit()
        cur.close()

##RDS##insert_data

##EMAIL NOTIFICATION
SENDER = 'librarymanagmenta3s@gmail.com'
RECIPIENT = 'librarymanagmenta3s@gmail.com'
AWS_REGION = "us-east-1"

# Create a new SES resource and specify a region.
client = boto3.client('ses',region_name=AWS_REGION )


def lambda_handler(event, context):
    http_method = event.get('httpMethod')
    if http_method == 'GET':
      
        with conn.cursor() as cur:
            qry = "select * from contactus;"
            cur.execute(qry)
            conn.commit()
            cur.close()
            res_items=cur.fetchall()
            statusCode = 200
    elif http_method == 'POST':
        body = event.get('body')
        name = ''
        contact = ''
        email = ''
        subject = ''
        message = ''
        if body is not None:
            name = json.loads(body).get('name', name)
            contact = json.loads(body).get('contact', contact)
            email = json.loads(body).get('email', email)
            subject = json.loads(body).get('subject', subject)
            message = json.loads(body).get('message', message)
        try:
            ##RDS##insert_data
            insert_data(name,contact,email,subject,message)
            ##email notification
            # The character encoding for the email.
            CHARSET = "utf-8"
            SUBJECT = subject
            CONTACT = contact
            BODY_TEXT = message
            BODY_HTML = """\
        <!DOCTYPE html>
<html>
<style>
body {font-family: Arial, Helvetica, sans-serif;}
</style>
<body>
<p>Customer :"""+name+"""</p>
<p>Contact Details : """+contact+"""</p>
<p>Email : """+email+"""</p>
<p>Subject: """+subject+"""</p>
<p>Message: """+message+"""</p>
</body>
</html>
"""
            
            response = client.send_email(
                Destination={'ToAddresses': [RECIPIENT,],},
                Message={'Body': {'Html': {'Charset': CHARSET,'Data': BODY_HTML,},'Text': {'Charset': CHARSET,'Data': BODY_TEXT,},},
                                'Subject': {'Charset': CHARSET,'Data': SUBJECT,},},
                Source=SENDER,)
            # logger.info("Email sent! Message ID:" +response['MessageId'])
            statusCode = 200
            res_items = {"msg":"Thank you for filling out your information!  : "+email}
        except Exception as e:
            logger.info(e)
            statusCode = 400
            res_items = {"msg":"Sorry, Unable to submit your request, if urgent please call me."}
      
    else:
        statusCode = 405
        res_items = 'httpMethod: '+http_method+ ' not supported for request'       
    return {
        "statusCode": statusCode,
        "body": json.dumps(res_items),  
        "headers": {
            'Content-Type' : 'application/json',
            'Access-Control-Allow-Origin' : '*',
            'Access-Control-Allow-Headers' : '*'
            }
        } 