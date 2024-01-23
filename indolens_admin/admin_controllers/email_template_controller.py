
def get_order_creation_email_subject(order_number):
    return f""" INDOLENS Order Created - {order_number} """

def get_employee_creation_email_body(name, role, email, password):
    return f""" Dear {name},
            
We are pleased to inform you that your user {role} profile has been successfully created in Indolens, and you are now ready to access our platform. Below are your login credentials:
                        
Username/Email: {email}
Password: {password}

For security reasons, we recommend that you log in to your account as soon as possible and change your password. 
Here are the steps to access your account:

Visit the Indolens: http://127.0.0.1:8000/own_store/own_store_login/
Enter your email and the temporary password provided above.
Click on the "Login" button.

If you encounter any issues during the login process or have any questions about your account, please contact our support team at support@indolens.in. We are here to assist you.
                        
Best regards,
INDOLENS """


def get_order_status_change_email_subject(order_number):
    return f""" INDOLENS Order status changed - {order_number} """

def get_employee_update_email_body(name, role, email, phone, address):
    return f""" Dear {name},

We are pleased to inform you that your user {role} profile has been successfully updated in Indolens.

Username/Email: {email}
Phone: {phone}
Address: {address}

Best regards,
INDOLENS """


def get_employee_assigned_store_email_subject(order_number):
    return f""" INDOLENS Store Assigned - {order_number} """

def get_employee_assigned_store_email_body(name, role, email, phone, store_name, store_phone, store_address):
    return f""" Hello {name},

We are pleased to inform you of your recent store assignment at Indolens. We are confident that you will make valuable contributions to the success of the assigned store.

Store Assignment Details:
- Store Name: {store_name}
- Location: {store_address}
- Store Phone: {store_phone}

As a team member of this store, your responsibilities will include {role}. Your role is crucial to the store's success, and we believe your expertise will enhance the overall performance of the team.

Thank you for your continued dedication to Indolens. We look forward to witnessing your positive impact on the assigned store.

Best regards,
INDOLENS
"""


def get_employee_unassigned_store_email_body(name, storeName, storeId, address):
    return f""" Dear {name},

    We wanted to inform you of a recent change in your store assignment at Imdolens.
    It has been decided to unassign you from the following store:

    Store Assignment Details:
    - Store Name: {storeName}
    - Location: {address}
    - Store ID: {storeId}
    We look forward to your continued success in your future assignments.

    Best regards,
    INDOLENS
    """


def get_order_payment_status_change_email_subject(order_number):
    return f""" INDOLENS Order payment status changed - {order_number} """


def get_order_placed_email_body(customer_name, order_number, order_date, estimated_delivery_date):
    return f""" 
Dear {customer_name},

Thank you for choosing INDOLENS! We are excited to confirm that your order has been successfully created. 
Below are the details of your recent purchase:

Order Number: {order_number}
Order Date: {order_date}
Estimated Delivery Date: {estimated_delivery_date}
Track Order on: http://127.0.0.1:8000/customer_order_tracking/orderId={order_number}

Best regards,
INDOLENS
09980557575
"""


def get_order_status_change_email_body(customer_name, order_number, status, date):
    return f""" Dear {customer_name},

Kindly be informed that the status of your order has been updated. Below are the details of the recent change:

Order Number: {order_number}
Order Status: {status}
Date of Change: {date}
Track Order on: http://127.0.0.1:8000/customer_order_tracking/orderId={order_number}

Best regards,
INDOLENS
09980557575
"""

def get_order_payment_status_change_email_body(customer_name, order_number, status, date):
    return f""" Dear {customer_name},

Kindly be informed that the payment status of your order has been updated. Below are the details of the recent change:

Order Number: {order_number}
Payment Status: {status}
Date of Change: {date}
Track Order on: http://127.0.0.1:8000/customer_order_tracking/orderId={order_number}

Best regards,
INDOLENS
09980557575
"""