from datetime import datetime

import bcrypt
import pymysql

db_host = 'localhost'
db_user = 'indolensadmin'
db_password = 'Indolens@#1234'
db_name = 'indolens_db'

# db_host = 'localhost'
# db_user = 'root'
# db_password = ''
# db_name = 'indolens_db'

super_name = input("Enter name for super admin : ")
super_email = input("Enter email for super admin : ")
super_phone = input("Enter phone for super admin : ")
super_password = input("Enter password for super admin : ")

password_hash = bcrypt.hashpw(super_password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
print(password_hash)

sql_queries = [
    """CREATE TABLE `accountant` (
 `accountant_id` int(11) NOT NULL AUTO_INCREMENT,
 `name` varchar(255),
 `email` varchar(255),
 `phone` varchar(255),
 `password` varchar(255),
 `profile_pic` varchar(255),
 `address` varchar(255),
 `document_1_type` varchar(255),
 `document_1_url` varchar(255),
 `document_2_type` varchar(255),
 `document_2_url` varchar(255),
 `status` int(11),
 `created_by` int(11),
 `created_on` datetime,
 `last_updated_by` int(11),
 `last_updated_on` datetime,
 PRIMARY KEY (`accountant_id`),
 UNIQUE KEY `unique_email_accountant` (`email`)
)""",
    """CREATE TABLE `admin` (
 `admin_id` int(11) NOT NULL AUTO_INCREMENT,
 `name` varchar(255),
 `email` varchar(255),
 `phone` varchar(12),
 `password` varchar(255),
 `role` int(12),
 `profile_pic` varchar(255),
 `address` varchar(255),
 `document_1_type` varchar(255),
 `document_1_url` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_bin CHECK (json_valid(`document_1_url`)),
 `document_2_type` varchar(255),
 `document_2_url` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_bin CHECK (json_valid(`document_2_url`)),
 `status` int(11),
 `created_by` int(11),
 `created_on` datetime,
 `last_updated_by` int(11),
 `last_updated_on` datetime,
 PRIMARY KEY (`admin_id`),
 UNIQUE KEY `unique_email_admin` (`email`)
)""",
    """CREATE TABLE `admin_setting` (
 `setting_id` int(11) NOT NULL AUTO_INCREMENT,
 `emailjs_attribute` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NOT NULL CHECK (json_valid(`emailjs_attribute`)),
 `base_url` varchar(255),
 `created_by` int(11),
 `created_on` datetime,
 `updated_by` int(11),
 `updated_on` datetime,
 PRIMARY KEY (`setting_id`)
)""",
    """CREATE TABLE `area_head` (
 `area_head_id` int(11) NOT NULL AUTO_INCREMENT,
 `name` varchar(255),
 `email` varchar(255),
 `phone` varchar(255),
 `password` varchar(255),
 `profile_pic` varchar(255),
 `assigned_stores` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_bin,
 `address` varchar(255),
 `document_1_type` varchar(255),
 `document_1_url` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_bin CHECK (json_valid(`document_1_url`)),
 `document_2_type` varchar(255),
 `document_2_url` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_bin CHECK (json_valid(`document_2_url`)),
 `status` int(11),
 `created_by` int(11),
 `created_on` datetime,
 `last_updated_by` int(11),
 `last_updated_on` datetime,
 PRIMARY KEY (`area_head_id`),
 UNIQUE KEY `unique_email_area_head` (`email`)
)""",
    """CREATE TABLE `brands` (
 `brand_id` int(11) NOT NULL AUTO_INCREMENT,
 `brand_name` varchar(255),
 `category_id` int(11),
 `brand_description` varchar(255),
 `status` tinyint(1),
 `created_on` datetime,
 `created_by` int(11),
 `last_updated_on` datetime,
 `last_updated_by` int(11),
 PRIMARY KEY (`brand_id`)
)""",
    """CREATE TABLE `central_inventory` (
 `product_id` int(11) NOT NULL AUTO_INCREMENT,
 `product_name` varchar(255),
 `product_description` longtext,
 `product_images` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_bin CHECK (json_valid(`product_images`)),
 `product_qr_code` varchar(255),
 `category_id` int(11),
 `brand_id` int(11),
 `material_id` int(11),
 `frame_type_id` int(11),
 `frame_shape_id` int(11),
 `color_id` int(11),
 `unit_id` int(11),
 `origin` varchar(255),
 `cost_price` int(11),
 `sale_price` int(11),
 `model_number` varchar(255),
 `hsn` varchar(255),
 `power_attribute` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_bin CHECK (json_valid(`power_attribute`)),
 `franchise_sale_price` int(11),
 `product_quantity` int(11),
 `product_gst` int(11),
 `status` tinyint(1),
 `discount` int(11),
 `created_on` datetime,
 `created_by` int(11),
 `last_updated_on` datetime,
 `last_updated_by` int(11),
 PRIMARY KEY (`product_id`)
)""",
    """CREATE TABLE `central_inventory_restock_log` (
 `restock_id` int(11) NOT NULL AUTO_INCREMENT,
 `product_id` int(11),
 `quantity` int(11),
 `created_by` int(11),
 `created_on` datetime,
 PRIMARY KEY (`restock_id`)
)""",
    """CREATE TABLE `customers` (
 `customer_id` int(11) NOT NULL AUTO_INCREMENT,
 `name` varchar(255),
 `gender` varchar(255),
 `age` int(11),
 `phone` varchar(255),
 `email` varchar(255),
 `language` varchar(255),
 `city` varchar(255),
 `address` varchar(255),
 `created_by_employee_id` int(11),
 `created_by_store_id` int(11),
 `created_by_store_type` int(11),
 `created_on` datetime,
 `updated_by_employee_id` int(11),
 `updated_by_store_id` int(11),
 `updated_by_store_type` int(11),
 `updated_on` datetime,
 PRIMARY KEY (`customer_id`),
 UNIQUE KEY `unique_phone` (`phone`)
)""",
    """CREATE TABLE `django_session` (
 `session_key` varchar(40),
 `session_data` longtext,
 `expire_date` datetime(6),
 PRIMARY KEY (`session_key`),
 KEY `django_session_expire_date_a5c62663` (`expire_date`)
)""",
    """CREATE TABLE `eye_test` (
 `eye_test_id` int(11) NOT NULL AUTO_INCREMENT,
 `customer_id` int(11),
 `power_attributes` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NOT NULL CHECK (json_valid(`power_attributes`)),
 `created_by_store_id` int(11),
 `created_by_store_type` int(11),
 `created_by` int(11),
 `created_on` datetime,
 `updated_by` int(11),
 `updated_on` datetime,
 PRIMARY KEY (`eye_test_id`)
)""",
    """CREATE TABLE `frame_shapes` (
 `shape_id` int(11) NOT NULL AUTO_INCREMENT,
 `shape_name` varchar(255),
 `shape_description` varchar(255),
 `status` int(11),
 `created_on` datetime,
 `created_by` int(11),
 `last_updated_on` datetime,
 `last_updated_by` int(11),
 PRIMARY KEY (`shape_id`)
)""",
    """CREATE TABLE `frame_types` (
 `frame_id` int(11) NOT NULL AUTO_INCREMENT,
 `frame_type_name` varchar(255),
 `frame_type_description` varchar(255),
 `status` int(11),
 `created_on` datetime,
 `created_by` int(11),
 `last_updated_on` datetime,
 `last_updated_by` int(11),
 PRIMARY KEY (`frame_id`)
)""",
    """CREATE TABLE `franchise_owner` (
 `franchise_owner_id` int(11) NOT NULL AUTO_INCREMENT,
 `name` varchar(255),
 `email` varchar(255),
 `phone` varchar(255),
 `password` varchar(255),
 `profile_pic` varchar(255),
 `franchise_store_id` int(11),
 `address` varchar(255),
 `document_1_type` varchar(255),
 `document_1_url` varchar(255),
 `document_2_type` varchar(255),
 `document_2_url` varchar(255),
 `status` int(11),
 `created_by` int(11),
 `created_on` datetime,
 `last_updated_by` int(11),
 `last_updated_on` datetime,
 PRIMARY KEY (`franchise_owner_id`)
)""",
    """CREATE TABLE `franchise_store` (
 `store_id` int(11) NOT NULL AUTO_INCREMENT,
 `store_name` varchar(255),
 `store_display_name` varchar(255),
 `store_phone` varchar(255),
 `store_gst` varchar(255),
 `store_email` varchar(255),
 `store_city` varchar(255),
 `store_state` varchar(255),
 `store_zip` varchar(255),
 `store_lat` double,
 `store_lng` double,
 `store_address` varchar(255),
 `status` int(11),
 `created_by` int(11),
 `created_on` datetime,
 `last_updated_by` int(11),
 `last_updated_on` datetime,
 PRIMARY KEY (`store_id`)
)""",
    """CREATE TABLE `franchise_store_employees` (
 `employee_id` int(11) NOT NULL AUTO_INCREMENT,
 `name` varchar(255),
 `email` varchar(255),
 `phone` varchar(255),
 `password` varchar(255),
 `profile_pic` varchar(255),
 `assigned_store_id` int(11),
 `address` varchar(255),
 `document_1_type` varchar(255),
 `document_1_url` varchar(255),
 `document_2_type` varchar(255),
 `document_2_url` varchar(255),
 `status` int(11),
 `role` int(11),
 `created_by` int(11),
 `created_on` datetime,
 `last_updated_by` int(11),
 `last_updated_on` datetime,
 `certificates` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_bin,
 PRIMARY KEY (`employee_id`),
 UNIQUE KEY `unique_email` (`email`),
 UNIQUE KEY `unique_email_franchise` (`email`)
)""",
    """CREATE TABLE `invoice` (
 `invoice_id` int(11) NOT NULL AUTO_INCREMENT,
 `invoice_number` varchar(255),
 `order_id` varchar(255),
 `store_id` int(11),
 `store_type` int(11),
 `invoice_status` int(11),
 `invoice_date` date,
 PRIMARY KEY (`invoice_id`),
 UNIQUE KEY `unique_order_id` (`order_id`)
)""",
    """CREATE TABLE `lab` (
 `lab_id` int(11) NOT NULL AUTO_INCREMENT,
 `lab_name` varchar(255),
 `lab_display_name` varchar(255),
 `lab_phone` varchar(255),
 `lab_gst` varchar(255),
 `lab_email` varchar(255),
 `lab_city` varchar(255),
 `lab_state` varchar(255),
 `lab_zip` varchar(255),
 `lab_lat` double,
 `lab_lng` double,
 `lab_address` varchar(255),
 `status` int(11),
 `created_by` int(11),
 `created_on` datetime,
 `last_updated_by` int(11),
 `last_updated_on` datetime,
 PRIMARY KEY (`lab_id`)
)""",
    """CREATE TABLE `lab_technician` (
 `lab_technician_id` int(11) NOT NULL AUTO_INCREMENT,
 `name` varchar(255),
 `email` varchar(255),
 `phone` varchar(255),
 `password` varchar(255),
 `profile_pic` varchar(255),
 `assigned_lab_id` int(11),
 `address` varchar(255),
 `document_1_type` varchar(255),
 `document_1_url` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_bin CHECK (json_valid(`document_1_url`)),
 `document_2_type` varchar(255),
 `document_2_url` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_bin CHECK (json_valid(`document_2_url`)),
 `status` int(11),
 `created_by` int(11),
 `created_on` datetime,
 `last_updated_by` int(11),
 `last_updated_on` datetime,
 PRIMARY KEY (`lab_technician_id`),
 UNIQUE KEY `unique_email_lab_technician` (`email`)
)""",
    """CREATE TABLE `marketing_head` (
 `marketing_head_id` int(11) NOT NULL AUTO_INCREMENT,
 `name` varchar(255),
 `email` varchar(255),
 `phone` varchar(255),
 `password` varchar(255),
 `profile_pic` varchar(255),
 `assigned_area_head` int(11),
 `address` varchar(255),
 `document_1_type` varchar(255),
 `document_1_url` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_bin CHECK (json_valid(`document_1_url`)),
 `document_2_type` varchar(255),
 `document_2_url` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_bin CHECK (json_valid(`document_2_url`)),
 `status` int(11),
 `created_by` int(11),
 `created_on` datetime,
 `last_updated_by` int(11),
 `last_updated_on` datetime,
 PRIMARY KEY (`marketing_head_id`),
 UNIQUE KEY `unique_email_marketing_head` (`email`)
)""",
    """CREATE TABLE `optimetry` (
 `optimetry_id` int(11) NOT NULL AUTO_INCREMENT,
 `name` varchar(255),
 `email` varchar(255),
 `phone` varchar(255),
 `password` varchar(255),
 `profile_pic` varchar(255),
 `assigned_store_id` int(11),
 `address` varchar(255),
 `document_1_type` varchar(255),
 `document_1_url` varchar(255),
 `document_2_type` varchar(255),
 `document_2_url` varchar(255),
 `status` int(11),
 `created_by` int(11),
 `created_on` datetime,
 `last_updated_by` int(11),
 `last_updated_on` datetime,
 PRIMARY KEY (`optimetry_id`)
)""",
    """CREATE TABLE `order_track` (
 `track_id` int(11) NOT NULL AUTO_INCREMENT,
 `order_id` varchar(255),
 `status` int(11),
 `created_on` datetime,
 PRIMARY KEY (`track_id`)
)""",
    """CREATE TABLE `other_employees` (
 `other_employee_id` int(11) NOT NULL AUTO_INCREMENT,
 `name` varchar(255),
 `email` varchar(255),
 `phone` varchar(255),
 `password` varchar(255),
 `profile_pic` varchar(255),
 `assigned_store_id` int(11),
 `address` varchar(255),
 `document_1_type` varchar(255),
 `document_1_url` varchar(255),
 `document_2_type` varchar(255),
 `document_2_url` varchar(255),
 `status` int(11),
 `created_by` int(11),
 `created_on` datetime,
 `last_updated_by` int(11),
 `last_updated_on` datetime,
 PRIMARY KEY (`other_employee_id`)
)""",
    """CREATE TABLE `own_store` (
 `store_id` int(11) NOT NULL AUTO_INCREMENT,
 `store_name` varchar(255),
 `store_display_name` varchar(255),
 `store_phone` varchar(255),
 `store_gst` varchar(255),
 `store_email` varchar(255),
 `store_city` varchar(255),
 `store_state` varchar(255),
 `store_zip` varchar(255),
 `store_lat` double,
 `store_lng` double,
 `store_address` varchar(255),
 `status` int(11),
 `created_by` int(11),
 `created_on` datetime,
 `last_updated_by` int(11),
 `last_updated_on` datetime,
 PRIMARY KEY (`store_id`)
)""",
    """CREATE TABLE `own_store_employees` (
 `employee_id` int(11) NOT NULL AUTO_INCREMENT,
 `name` varchar(255),
 `email` varchar(255),
 `phone` varchar(255),
 `password` varchar(255),
 `profile_pic` varchar(255),
 `assigned_store_id` int(11),
 `address` varchar(255),
 `document_1_type` varchar(255),
 `document_1_url` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_bin CHECK (json_valid(`document_1_url`)),
 `document_2_type` varchar(255),
 `document_2_url` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_bin CHECK (json_valid(`document_2_url`)),
 `status` int(11),
 `role` int(11),
 `created_by` int(11),
 `created_on` datetime,
 `last_updated_by` int(11),
 `last_updated_on` datetime,
 `certificates` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_bin,
 PRIMARY KEY (`employee_id`),
 UNIQUE KEY `unique_email` (`email`)
)""",
    """CREATE TABLE `product_categories` (
 `category_id` int(11) NOT NULL AUTO_INCREMENT,
 `category_name` varchar(255),
 `category_prefix` varchar(255),
 `category_description` varchar(255),
 `status` tinyint(1),
 `created_on` datetime,
 `created_by` int(11),
 `last_updated_on` datetime,
 `last_updated_by` int(11),
 PRIMARY KEY (`category_id`)
)""",
    """CREATE TABLE `product_colors` (
 `color_id` int(11) NOT NULL AUTO_INCREMENT,
 `color_code` varchar(255),
 `color_name` varchar(255),
 `color_description` varchar(255),
 `status` int(11),
 `created_on` datetime,
 `created_by` int(11),
 `last_updated_on` datetime,
 `last_updated_by` int(11),
 PRIMARY KEY (`color_id`)
)""",
    """CREATE TABLE `product_materials` (
 `material_id` int(11) NOT NULL AUTO_INCREMENT,
 `material_name` varchar(255),
 `material_description` varchar(255),
 `status` int(11),
 `created_on` datetime,
 `created_by` int(11),
 `last_updated_on` datetime,
 `last_updated_by` int(11),
 PRIMARY KEY (`material_id`)
)""",
    """CREATE TABLE `request_products` (
 `request_products_id` int(11) NOT NULL AUTO_INCREMENT,
 `store_id` int(11),
 `store_type` int(11),
 `product_id` int(11),
 `product_quantity` int(11),
 `unit_cost` int(11),
 `request_status` int(11),
 `delivery_status` int(11),
 `is_requested` tinyint(1),
 `request_to_store_id` int(11),
 `payment_status` int(11),
 `comment` varchar(255),
 `created_on` datetime,
 `created_by` int(11),
 `last_updated_on` datetime,
 `last_updated_by` int(11),
 PRIMARY KEY (`request_products_id`)
)""",
    """CREATE TABLE `reset_password` (
 `reset_password_id` int(11) NOT NULL AUTO_INCREMENT,
 `email` varchar(255),
 `code` varchar(255),
 `status` int(11),
 `created_on` datetime,
 PRIMARY KEY (`reset_password_id`)
)""",
    """CREATE TABLE `sales_executive` (
 `sales_executive_id` int(11) NOT NULL AUTO_INCREMENT,
 `name` varchar(255),
 `email` varchar(255),
 `phone` varchar(255),
 `password` varchar(255),
 `profile_pic` varchar(255),
 `assigned_store_id` int(11),
 `address` varchar(255),
 `document_1_type` varchar(255),
 `document_1_url` varchar(255),
 `document_2_type` varchar(255),
 `document_2_url` varchar(255),
 `status` int(11),
 `created_by` int(11),
 `created_on` datetime,
 `last_updated_by` int(11),
 `last_updated_on` datetime,
 PRIMARY KEY (`sales_executive_id`)
)""",
    """CREATE TABLE `sales_order` (
 `sale_item_id` int(11) NOT NULL AUTO_INCREMENT,
 `order_id` varchar(255),
 `product_id` int(11),
 `hsn` varchar(255),
 `unit_sale_price` int(11),
 `unit_type` varchar(255),
 `purchase_quantity` int(11),
 `product_total_cost` int(11),
 `discount_percentage` int(11),
 `is_discount_applied` int(11),
 `power_attribute` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_bin CHECK (json_valid(`power_attribute`)),
 `assigned_lab` int(11),
 `customer_id` int(11),
 `order_status` int(11),
 `payment_status` int(11),
 `delivery_status` int(11),
 `payment_mode` int(11),
 `amount_paid` int(11),
 `estimated_delivery_date` date,
 `linked_item` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_bin CHECK (json_valid(`linked_item`)),
 `sales_note` longtext,
 `created_by_store` int(11),
 `created_by_store_type` int(11),
 `created_by` int(11),
 `created_on` datetime,
 `updated_by` int(11),
 `updated_on` datetime,
 PRIMARY KEY (`sale_item_id`)
)""",
    """
    CREATE TABLE `sales_order_payment_track` (
 `id` int(11) NOT NULL AUTO_INCREMENT,
 `order_id` varchar(255),
 `payment_amount` int(11),
 `payment_mode` int(11),
 `payment_type` int(11),
 `created_by_store` int(11),
 `created_by_store_type` int(11),
 `created_by_id` int(11),
 `created_on` datetime,
 PRIMARY KEY (`id`))
    """,
    """CREATE TABLE `store_expense` (
 `store_expense_id` int(11) NOT NULL AUTO_INCREMENT,
 `store_id` int(11),
 `store_type` int(11),
 `expense_amount` int(11),
 `expense_reason` varchar(255),
 `expense_date` datetime,
 `created_on` datetime,
 `created_by` int(11),
 PRIMARY KEY (`store_expense_id`)
)""",
    """CREATE TABLE `store_inventory` (
 `store_inventory_id` int(11) NOT NULL AUTO_INCREMENT,
 `store_id` int(11),
 `store_type` int(11),
 `product_id` int(11),
 `product_quantity` int(11),
 `created_on` datetime,
 `created_by` int(11),
 `last_updated_on` datetime,
 `last_updated_by` int(11),
 PRIMARY KEY (`store_inventory_id`),
 UNIQUE KEY `store_product_unique` (`store_id`,`store_type`,`product_id`)
)""",
    """CREATE TABLE `store_manager` (
 `store_manager_id` int(11) NOT NULL AUTO_INCREMENT,
 `name` varchar(255),
 `email` varchar(255),
 `phone` varchar(255),
 `password` varchar(255),
 `profile_pic` varchar(255),
 `assigned_store_id` int(11),
 `address` varchar(255),
 `document_1_type` varchar(255),
 `document_1_url` varchar(255),
 `document_2_type` varchar(255),
 `document_2_url` varchar(255),
 `status` int(11),
 `created_by` int(11),
 `created_on` datetime,
 `last_updated_by` int(11),
 `last_updated_on` datetime,
 PRIMARY KEY (`store_manager_id`),
 UNIQUE KEY `email` (`email`)
)""",
    """CREATE TABLE `units` (
 `unit_id` int(11) NOT NULL AUTO_INCREMENT,
 `unit_name` varchar(255),
 `status` int(11),
 `created_on` datetime,
 `created_by` int(11),
 `last_updated_on` datetime,
 `last_updated_by` int(11),
 PRIMARY KEY (`unit_id`)
)"""
]

connection = pymysql.connect(host=db_host, user=db_user, password=db_password, database=db_name)

create_admin_query = """
    INSERT INTO admin (
        name, 
        email, 
        phone, 
        password, 
        role, 
        profile_pic, 
        address, 
        document_1_type, 
        document_1_url, 
        document_2_type, 
        document_2_url, 
        status, 
        created_by, 
        created_on, 
        last_updated_by, 
        last_updated_on
    ) VALUES (
        %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s
    )
"""

try:
    with connection.cursor() as cursor:
        for sql_query in sql_queries:
            cursor.execute(sql_query)
        cursor.execute(create_admin_query, (
            super_name,
            super_email,
            super_phone,
            password_hash,
            1,
            'logo/admin.png',
            '123 Main St, City',
            'Aadhar Card',
            None,
            'Pan Card',
            None,
            1,
            1,
            datetime.now(),
            1,
            datetime.now()
        ))
        cursor.execute(
            """INSERT INTO product_categories 
                 (category_name, category_prefix, category_description, status, created_on, created_by, last_updated_on, last_updated_by) 
                 VALUES 
                 ('Frames', 'IND-FR', 'description for frames goes here', 1, NOW(), 1, NOW(), 1)""")

        cursor.execute(
            """INSERT INTO product_categories 
                 (category_name, category_prefix, category_description, status, created_on, created_by, last_updated_on, last_updated_by) 
                 VALUES 
                 ('Lens', 'IND-LENS', 'description for lens goes here', 1, NOW(), 1, NOW(), 1)""")

        cursor.execute(
            """INSERT INTO product_categories 
                 (category_name, category_prefix, category_description, status, created_on, created_by, last_updated_on, last_updated_by) 
                 VALUES 
                 ('Contact Lens', 'IND-CL', 'description for lens goes here', 1, NOW(), 1, NOW(), 1)""")
    connection.commit()
    print("Tables created successfully!")

except Exception as e:
    print(f"Error: {str(e)}")

finally:
    connection.close()
