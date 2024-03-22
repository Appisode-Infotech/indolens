import datetime
import pytz

from indolens_admin.admin_controllers.admin_setting_controller import get_base_url, get_support_data

base_url = get_base_url()

ist = pytz.timezone('Asia/Kolkata')


def getIndianTime():
    today = datetime.datetime.now(ist)
    formatted_date = today.strftime('%d/%m/%Y %I:%M %p')
    return formatted_date


support_data = get_support_data()


# EMPLOYEE CREATION EMAIL
def get_employee_creation_email_subject(name):
    return f""" INDOLENS Account Created - {name} """


def get_employee_creation_email_body(name, role, email, password):
    return f""" Dear {name},
            
We are pleased to inform you that your user {role} profile has been successfully created in Indolens, and you are now ready to access our platform. Below are your login credentials:
                        
Username/Email: {email}
Password: {password}

For security reasons, we recommend that you log in to your account as soon as possible and change your password. 
Here are the steps to access your account:

Visit the Indolens: {base_url}/own_store/own_store_login/
Enter your email and the temporary password provided above.
Click on the "Login" button.

If you encounter any issues during the login process or have any questions about your account, please contact our support team. We are here to assist you.
                        
Best regards,
INDOLENS 
Email: {support_data.get('support_email')}
Phone: {support_data.get('support_phone')}
Working Hours: {support_data.get('support_hour')}
"""


# EMPLOYEE CREATION EMAIL
def get_franchise_employee_creation_email_subject(name):
    return f""" INDOLENS Account Created - {name} """


def get_franchise_employee_creation_email_body(name, role, email, password):
    return f""" Dear {name},

We are pleased to inform you that your user {role} profile has been successfully created in Indolens, and you are now ready to access our platform. Below are your login credentials:

Username/Email: {email}
Password: {password}

For security reasons, we recommend that you log in to your account as soon as possible and change your password. 
Here are the steps to access your account:

Visit the Indolens: {base_url}/franchise_store/franchise_store_login/
Enter your email and the temporary password provided above.
Click on the "Login" button.

If you encounter any issues during the login process or have any questions about your account, please contact our support team. We are here to assist you.

Best regards,
INDOLENS 
Email: {support_data.get('support_email')}
Phone: {support_data.get('support_phone')}
Working Hours: {support_data.get('support_hour')}
"""

# EMPLOYEE CREATION EMAIL
def get_lab_tech_creation_email_subject(name):
    return f""" INDOLENS Account Created - {name} """


def get_lab_tech_creation_email_body(name, role, email, password):
    return f""" Dear {name},

We are pleased to inform you that your user {role} profile has been successfully created in Indolens, and you are now ready to access our platform. Below are your login credentials:

Username/Email: {email}
Password: {password}

For security reasons, we recommend that you log in to your account as soon as possible and change your password. 
Here are the steps to access your account:

Visit the Indolens: {base_url}/lab/lab_login/
Enter your email and the temporary password provided above.
Click on the "Login" button.

If you encounter any issues during the login process or have any questions about your account, please contact our support team. We are here to assist you.

Best regards,
INDOLENS 
Email: {support_data.get('support_email')}
Phone: {support_data.get('support_phone')}
Working Hours: {support_data.get('support_hour')}
"""

def get_store_employee_creation_email_body(name, role, email):
    return f""" Dear {name},
            
We are pleased to inform you that your user {role} profile has been successfully created in Indolens.
                        
Username/Email: {email}
                 
Best regards,
INDOLENS 
Email: {support_data.get('support_email')}
Phone: {support_data.get('support_phone')}
Working Hours: {support_data.get('support_hour')}
"""


# EMPLOYEE UPDATE EMAIL
def get_employee_update_email_body(name, role, email, phone, address):
    return f""" Dear {name},

We are pleased to inform you that your user {role} profile has been successfully updated in Indolens.

Username/Email: {email}
Phone: {phone}
Address: {address}
Date: {getIndianTime()}

Best regards,
INDOLENS 
Email: {support_data.get('support_email')}
Phone: {support_data.get('support_phone')}
Working Hours: {support_data.get('support_hour')}"""


# EMPLOYEE STORE ASSIGNED
def get_employee_assigned_store_email_subject(name):
    return f""" INDOLENS Store Assigned - {name} """


def get_employee_assigned_store_email_body(name, role, email, store_name, store_phone, store_address):
    return f""" Hello {name},

We are pleased to inform you of your recent store assignment at Indolens. We are confident that you will make valuable contributions to the success of the assigned store.

Store Assignment Details:
- Store Name: {store_name}
- Assigned Date: {getIndianTime()}
- Location: {store_address}
- Store Phone: {store_phone}

As a team member of this store, your responsibilities will include {role} for employee: {email}. Your role is crucial to the store's success, and we believe your expertise will enhance the overall performance of the team.

Thank you for your continued dedication to Indolens. We look forward to witnessing your positive impact on the assigned store.

Best regards,
INDOLENS
Email: {support_data.get('support_email')}
Phone: {support_data.get('support_phone')}
Working Hours: {support_data.get('support_hour')}
"""


# AREA HEAD STORE ASSIGNED
def get_area_head_assigned_store_email_subject(name):
    return f""" INDOLENS Store Assigned - {name} """


def get_area_head_assigned_store_email_body(name, role, email, store_data):
    stores_info = ""
    for store_name, store_phone, store_address in store_data:
        stores_info += f"  Store Name: {store_name}\n"
        stores_info += f"  Assigned Date: {getIndianTime()}\n"
        stores_info += f"  Location: {store_address}\n"
        stores_info += f"  Store Phone: {store_phone}\n\n"
    return f""" Hello {name},

We are pleased to inform you of your recent store assignment at Indolens. We are confident that you will make valuable contributions to the success of the assigned store.

Store Assignment Details:
{stores_info}

As a team member of this store, your responsibilities will include {role} for employee: {email}. Your role is crucial to the store's success, and we believe your expertise will enhance the overall performance of the team.

Thank you for your continued dedication to Indolens. We look forward to witnessing your positive impact on the assigned store.

Best regards,
INDOLENS
Email: {support_data.get('support_email')}
Phone: {support_data.get('support_phone')}
Working Hours: {support_data.get('support_hour')}
"""


# EMPLOYEE STORE ASSIGNED
def get_password_reset_email_subject(name):
    return f""" Password Reset for Your Indolens Account - {name} """


def get_password_reset_email_body(name, pwd_link, email):
    return f""" Hello {name},

We received a request to reset the password for your account: {email} . 

To reset your password, please click on the following link:

{pwd_link}

Please note that this link is time-sensitive, so we recommend completing the reset process within 15 minutes.

If you have any issues or need further assistance, feel free to contact our support team.

Best regards,
INDOLENS
Email: {support_data.get('support_email')}
Phone: {support_data.get('support_phone')}
Working Hours: {support_data.get('support_hour')}
"""


# EMPLOYEE STORE UNASSIGNED
def get_employee_unassigned_store_email_subject(order_number):
    return f""" INDOLENS Store Unassigned - {order_number} """


def get_employee_unassigned_store_email_body(name, role, email, store_name, store_phone, store_address):
    return f""" Dear {name},

    We wanted to inform you of a recent change in your store assignment at Indolens.
    It has been decided to unassign your {role} role for user: {email} from the following store:

    Store Unassignment Details:
    - Store Name: {store_name}
    - Unassigned Date: {getIndianTime()}
    - Location: {store_address}
    - Store Phone: {store_phone}
    
    We anticipate your ongoing success in your future assignments.

    Best regards,
    INDOLENS
    Email: {support_data.get('support_email')}
    Phone: {support_data.get('support_phone')}
    Working Hours: {support_data.get('support_hour')}
    """


# ORDER CREATE EMAIL
def get_order_creation_email_subject(order_number):
    return f""" INDOLENS Order Created - {order_number} """


def get_order_placed_email_body(customer_name, order_number, order_date, estimated_delivery_date):
    return f""" 
Dear {customer_name},

Thank you for choosing INDOLENS! We are excited to confirm that your order has been successfully created. 
Below are the details of your recent purchase:

Order Number: {order_number}
Date: {getIndianTime()}
Estimated Delivery Date: {estimated_delivery_date}
Track Order on: {base_url}/customer_order_tracking/orderId={order_number}

Best regards,
INDOLENS
Email: {support_data.get('support_email')}
Phone: {support_data.get('support_phone')}
Working Hours: {support_data.get('support_hour')}
"""


# ORDER STATUS CHANGE
def get_order_status_change_email_subject(order_number):
    return f""" INDOLENS Order status changed - {order_number} """


def get_order_status_change_email_body(customer_name, order_number, status, date):
    return f""" Dear {customer_name},

Kindly be informed that the status of your order has been updated. Below are the details of the recent change:

Order Number: {order_number}
Order Status: {status}
Date of Change: {getIndianTime()}
Track Order on: {base_url}/customer_order_tracking/orderId={order_number}

Best regards,
INDOLENS
Email: {support_data.get('support_email')}
Phone: {support_data.get('support_phone')}
Working Hours: {support_data.get('support_hour')}
"""


def get_order_completion_email_subject(order_number):
    return f""" INDOLENS Order Completed - {order_number} """


def get_order_completion_email_body(customer_name, order_number, status, date):
    return f""" Dear {customer_name},

Kindly be informed that your order has been completed. Below are the completed order details details:

Order Number: {order_number}
Order Status: {status}
Date of Change: {getIndianTime()}
Invoice: {base_url}/customer_order_invoice/orderId={order_number}

Best regards,
INDOLENS
Email: {support_data.get('support_email')}
Phone: {support_data.get('support_phone')}
Working Hours: {support_data.get('support_hour')}
"""


def get_order_cancelled_email_subject(order_number):
    return f""" INDOLENS Order Cancelled - {order_number} """


def get_order_cancelled_email_body(customer_name, order_number, status, date):
    return f""" Dear {customer_name},

Kindly be informed that your order has been cancelled. Below are the cancelled order details details:

Order Number: {order_number}
Order Status: {status}
Date of Change: {getIndianTime()}

Best regards,
INDOLENS
Email: {support_data.get('support_email')}
Phone: {support_data.get('support_phone')}
Working Hours: {support_data.get('support_hour')}
"""


# ORDER PAYMENT STATUS CHANGE
def get_order_payment_status_change_email_subject(order_number):
    return f""" INDOLENS Order payment status changed - {order_number} """


def get_order_payment_status_change_email_body(customer_name, order_number, status, date):
    return f""" Dear {customer_name},

Kindly be informed that the payment status of your order has been updated. Below are the details of the recent change:

Order Number: {order_number}
Payment Status: {status}
Date of Change: {date}
Track Order on: {base_url}/customer_order_tracking/orderId={order_number}

Best regards,
INDOLENS
Email: {support_data.get('support_email')}
Phone: {support_data.get('support_phone')}
Working Hours: {support_data.get('support_hour')}
"""


# EMPLOYEE CREATION EMAIL
def get_customer_eye_test_email_subject(name):
    return f""" INDOLENS Eye Test Summary - {name} """


def get_customer_eye_test_email_body(name, test_id):
    return f""" Dear {name},

Thank you for choosing INDOLENS for your recent eye test. We are pleased to inform you that your eye test report is now available.

Your eye test was conducted on {getIndianTime()}. 
To access your eye test report, please click on the following secure link: {base_url}/customer_eye_test/testId={test_id}

Please note that the link is unique to you and should not be shared with others to maintain the privacy of your eye health information.
If you have any questions or concerns regarding your eye test report, our team is here to assist you.

Thank you once again for choosing INDOLENS. We value your trust in us and look forward to serving you in the future.

Best regards,
INDOLENS 
Email: {support_data.get('support_email')}
Phone: {support_data.get('support_phone')}
Working Hours: {support_data.get('support_hour')}"""
