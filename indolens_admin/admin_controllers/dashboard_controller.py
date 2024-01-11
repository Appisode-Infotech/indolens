import datetime
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import pymysql
import pytz
from django.db import connection

ist = pytz.timezone('Asia/Kolkata')
today = datetime.datetime.now(ist)


def get_order_stats(status, store_type):
    status_conditions = {
        "New": "= 1",
        "Completed": "= 5",
    }
    status_condition = status_conditions[status]
    try:
        with connection.cursor() as cursor:
            get_order_query = f"""
                    SELECT *
                    FROM sales_order
                    WHERE order_status {status_condition} AND created_by_store_type = {store_type} 
                    GROUP BY order_id          
                    """
            cursor.execute(get_order_query)
            orders_list = cursor.fetchall()

            return {
                       "status": True,
                       "count": len(orders_list)
                   }, 200

    except pymysql.Error as e:
        return {"status": False, "message": str(e)}, 301
    except Exception as e:
        return {"status": False, "message": str(e)}, 301


def get_sales_stats(store):
    try:
        with connection.cursor() as cursor:
            get_order_query = f"""
                                SELECT IFNULL(SUM(product_total_cost), 0) AS total_sale
                                FROM sales_order
                                WHERE created_by_store_type = {store} 
                                """
            cursor.execute(get_order_query)
            orders_list = cursor.fetchone()
            total_sale = orders_list[0] if orders_list[0] is not None else 0

            return {
                       "status": True,
                       "sale": total_sale
                   }, 200


    except pymysql.Error as e:
        return {"status": False, "message": str(e)}, 301
    except Exception as e:
        return {"status": False, "message": str(e)}, 301


def send_email(subject, body, to_email, smtp_server, smtp_port, smtp_username, smtp_password):
    # Create the MIME object
    msg = MIMEMultipart()
    msg['From'] = smtp_username
    msg['To'] = to_email
    msg['Subject'] = subject

    # Attach the email body as plain text
    msg.attach(MIMEText(body, 'plain'))

    # Connect to the SMTP server
    with smtplib.SMTP_SSL(smtp_server, smtp_port) as server:
        # Login to the SMTP server
        a = server.login(smtp_username, smtp_password)
        print(a)
        # Send the email
        b = server.sendmail(smtp_username, to_email, msg.as_string())
        print(b)

    print("Email sent successfully.")
