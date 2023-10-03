import pymysql

# Define the database connection parameters
db_host = 'localhost'
db_user = 'root'
db_password = ''
db_name = 'indolens_db'

# SQL statements to create all the tables
sql_queries = [
    """
    CREATE TABLE IF NOT EXISTS accountant (
        accountant_id INT(11) NOT NULL AUTO_INCREMENT,
        name VARCHAR(255) NOT NULL,
        email VARCHAR(255) NOT NULL,
        phone INT(12) NOT NULL,
        password VARCHAR(255) NOT NULL,
        profile_pic VARCHAR(255) NOT NULL,
        address VARCHAR(255) NOT NULL,
        document_1_type VARCHAR(255) NOT NULL,
        document_1_url VARCHAR(255) NOT NULL,
        document_2_type VARCHAR(255) NOT NULL,
        document_2_url VARCHAR(255) NOT NULL,
        status INT(11) NOT NULL,
        created_by INT(11) NOT NULL,
        created_on DATETIME NOT NULL,
        last_updated_by INT(11) NOT NULL,
        last_updated_on DATETIME NOT NULL,
        PRIMARY KEY (accountant_id)
    );
    """,
    """
    CREATE TABLE IF NOT EXISTS admin (
        admin_id INT(11) NOT NULL AUTO_INCREMENT,
        name VARCHAR(255) NOT NULL,
        email VARCHAR(255) NOT NULL,
        phone INT(12) NOT NULL,
        password VARCHAR(255) NOT NULL,
        role INT(12) NOT NULL,
        profile_pic VARCHAR(255) NOT NULL,
        address VARCHAR(255) NOT NULL,
        document_1_type VARCHAR(255) NOT NULL,
        document_1_url VARCHAR(255) NOT NULL,
        document_2_type VARCHAR(255) NOT NULL,
        document_2_url VARCHAR(255) NOT NULL,
        status INT(11) NOT NULL,
        created_by INT(11) NOT NULL,
        created_on DATETIME NOT NULL,
        last_updated_by INT(11) NOT NULL,
        last_updated_on DATETIME NOT NULL,
        PRIMARY KEY (admin_id)
    );
    """,
    """
    CREATE TABLE IF NOT EXISTS area_head (
        area_head_id INT(11) NOT NULL AUTO_INCREMENT,
        name VARCHAR(255) NOT NULL,
        email VARCHAR(255) NOT NULL,
        phone INT(12) NOT NULL,
        password VARCHAR(255) NOT NULL,
        profile_pic VARCHAR(255) NOT NULL,
        assigned_stores LONGTEXT CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NOT NULL,
        address VARCHAR(255) NOT NULL,
        document_1_type VARCHAR(255) NOT NULL,
        document_1_url VARCHAR(255) NOT NULL,
        document_2_type VARCHAR(255) NOT NULL,
        document_2_url VARCHAR(255) NOT NULL,
        status INT(11) NOT NULL,
        created_by INT(11) NOT NULL,
        created_on DATETIME NOT NULL,
        last_updated_by INT(11) NOT NULL,
        last_updated_on DATETIME NOT NULL,
        PRIMARY KEY (area_head_id)
    );
    """,
    """
    CREATE TABLE IF NOT EXISTS franchise_owner (
        franchise_owner_id INT(11) NOT NULL AUTO_INCREMENT,
        name VARCHAR(255) NOT NULL,
        email VARCHAR(255) NOT NULL,
        phone INT(12) NOT NULL,
        password VARCHAR(255) NOT NULL,
        profile_pic VARCHAR(255) NOT NULL,
        franchise_store_id INT(11) NOT NULL,
        address VARCHAR(255) NOT NULL,
        document_1_type VARCHAR(255) NOT NULL,
        document_1_url VARCHAR(255) NOT NULL,
        document_2_type VARCHAR(255) NOT NULL,
        document_2_url VARCHAR(255) NOT NULL,
        status INT(11) NOT NULL,
        created_by INT(11) NOT NULL,
        created_on DATETIME NOT NULL,
        last_updated_by INT(11) NOT NULL,
        last_updated_on DATETIME NOT NULL,
        PRIMARY KEY (franchise_owner_id)
    );
    """,
    """
    CREATE TABLE IF NOT EXISTS franchise_store (
        store_id INT(11) NOT NULL AUTO_INCREMENT,
        store_name VARCHAR(255) NOT NULL,
        store_display_name VARCHAR(255) NOT NULL,
        store_phone INT(11) NOT NULL,
        store_gst VARCHAR(255) NOT NULL,
        store_email VARCHAR(255) NOT NULL,
        store_city VARCHAR(255) NOT NULL,
        store_state VARCHAR(255) NOT NULL,
        store_zip VARCHAR(255) NOT NULL,
        store_lat DOUBLE NOT NULL,
        store_lng DOUBLE NOT NULL,
        store_address VARCHAR(255) NOT NULL,
        status INT(11) NOT NULL,
        created_by INT(11) NOT NULL,
        created_on DATETIME NOT NULL,
        last_updated_by INT(11) NOT NULL,
        last_updated_on DATETIME NOT NULL,
        PRIMARY KEY (store_id)
    );
    """,
    """
    CREATE TABLE IF NOT EXISTS lab (
        lab_id INT(11) NOT NULL AUTO_INCREMENT,
        lab_name VARCHAR(255) NOT NULL,
        lab_display_name VARCHAR(255) NOT NULL,
        lab_phone INT(11) NOT NULL,
        lab_gst VARCHAR(255) NOT NULL,
        lab_email VARCHAR(255) NOT NULL,
        lab_city VARCHAR(255) NOT NULL,
        lab_state VARCHAR(255) NOT NULL,
        lab_zip VARCHAR(255) NOT NULL,
        lab_lat DOUBLE NOT NULL,
        lab_lng DOUBLE NOT NULL,
        lab_address VARCHAR(255) NOT NULL,
        status INT(11) NOT NULL,
        created_by INT(11) NOT NULL,
        created_on DATETIME NOT NULL,
        last_updated_by INT(11) NOT NULL,
        last_updated_on DATETIME NOT NULL,
        PRIMARY KEY (lab_id)
    );
    """,
    """
    CREATE TABLE IF NOT EXISTS lab_technician (
        lab_technician_id INT(11) NOT NULL AUTO_INCREMENT,
        name VARCHAR(255) NOT NULL,
        email VARCHAR(255) NOT NULL,
        phone INT(12) NOT NULL,
        password VARCHAR(255) NOT NULL,
        profile_pic VARCHAR(255) NOT NULL,
        assigned_lab_id INT(11) NOT NULL,
        address VARCHAR(255) NOT NULL,
        document_1_type VARCHAR(255) NOT NULL,
        document_1_url VARCHAR(255) NOT NULL,
        document_2_type VARCHAR(255) NOT NULL,
        document_2_url VARCHAR(255) NOT NULL,
        status INT(11) NOT NULL,
        created_by INT(11) NOT NULL,
        created_on DATETIME NOT NULL,
        last_updated_by INT(11) NOT NULL,
        last_updated_on DATETIME NOT NULL,
        PRIMARY KEY (lab_technician_id)
    );
    """,
    """
    CREATE TABLE IF NOT EXISTS marketing_head (
        marketing_head_id INT(11) NOT NULL AUTO_INCREMENT,
        name VARCHAR(255) NOT NULL,
        email VARCHAR(255) NOT NULL,
        phone INT(12) NOT NULL,
        password VARCHAR(255) NOT NULL,
        profile_pic VARCHAR(255) NOT NULL,
        assigned_area_head INT(11) NOT NULL,
        address VARCHAR(255) NOT NULL,
        document_1_type VARCHAR(255) NOT NULL,
        document_1_url VARCHAR(255) NOT NULL,
        document_2_type VARCHAR(255) NOT NULL,
        document_2_url VARCHAR(255) NOT NULL,
        status INT(11) NOT NULL,
        created_by INT(11) NOT NULL,
        created_on DATETIME NOT NULL,
        last_updated_by INT(11) NOT NULL,
        last_updated_on DATETIME NOT NULL,
        PRIMARY KEY (marketing_head_id)
    );
    """,
    """
    CREATE TABLE IF NOT EXISTS optimetry (
        optimetry_id INT(11) NOT NULL AUTO_INCREMENT,
        name VARCHAR(255) NOT NULL,
        email VARCHAR(255) NOT NULL,
        phone INT(12) NOT NULL,
        password VARCHAR(255) NOT NULL,
        profile_pic VARCHAR(255) NOT NULL,
        assigned_store_id INT(11) NOT NULL,
        address VARCHAR(255) NOT NULL,
        document_1_type VARCHAR(255) NOT NULL,
        document_1_url VARCHAR(255) NOT NULL,
        document_2_type VARCHAR(255) NOT NULL,
        document_2_url VARCHAR(255) NOT NULL,
        status INT(11) NOT NULL,
        created_by INT(11) NOT NULL,
        created_on DATETIME NOT NULL,
        last_updated_by INT(11) NOT NULL,
        last_updated_on DATETIME NOT NULL,
        PRIMARY KEY (optimetry_id)
    );
    """,
    """
    CREATE TABLE IF NOT EXISTS other_employees (
        other_employee_id INT(11) NOT NULL AUTO_INCREMENT,
        name VARCHAR(255) NOT NULL,
        email VARCHAR(255) NOT NULL,
        phone INT(12) NOT NULL,
        password VARCHAR(255) NOT NULL,
        profile_pic VARCHAR(255) NOT NULL,
        assigned_store_id INT(11) NOT NULL,
        address VARCHAR(255) NOT NULL,
        document_1_type VARCHAR(255) NOT NULL,
        document_1_url VARCHAR(255) NOT NULL,
        document_2_type VARCHAR(255) NOT NULL,
        document_2_url VARCHAR(255) NOT NULL,
        status INT(11) NOT NULL,
        created_by INT(11) NOT NULL,
        created_on DATETIME NOT NULL,
        last_updated_by INT(11) NOT NULL,
        last_updated_on DATETIME NOT NULL,
        PRIMARY KEY (other_employee_id)
    );
    """,
    """
    CREATE TABLE IF NOT EXISTS own_store (
        store_id INT(11) NOT NULL AUTO_INCREMENT,
        store_name VARCHAR(255) NOT NULL,
        store_display_name VARCHAR(255) NOT NULL,
        store_phone INT(11) NOT NULL,
        store_gst VARCHAR(255) NOT NULL,
        store_email VARCHAR(255) NOT NULL,
        store_city VARCHAR(255) NOT NULL,
        store_state VARCHAR(255) NOT NULL,
        store_zip VARCHAR(255) NOT NULL,
        store_lat DOUBLE NOT NULL,
        store_lng DOUBLE NOT NULL,
        store_address VARCHAR(255) NOT NULL,
        status INT(11) NOT NULL,
        created_by INT(11) NOT NULL,
        created_on DATETIME NOT NULL,
        last_updated_by INT(11) NOT NULL,
        last_updated_on DATETIME NOT NULL,
        PRIMARY KEY (store_id)
    );
    """,
    """
    CREATE TABLE IF NOT EXISTS sales_executive (
        sales_executive_id INT(11) NOT NULL AUTO_INCREMENT,
        name VARCHAR(255) NOT NULL,
        email VARCHAR(255) NOT NULL,
        phone INT(12) NOT NULL,
        password VARCHAR(255) NOT NULL,
        profile_pic VARCHAR(255) NOT NULL,
        assigned_store_id INT(11) NOT NULL,
        address VARCHAR(255) NOT NULL,
        document_1_type VARCHAR(255) NOT NULL,
        document_1_url VARCHAR(255) NOT NULL,
        document_2_type VARCHAR(255) NOT NULL,
        document_2_url VARCHAR(255) NOT NULL,
        status INT(11) NOT NULL,
        created_by INT(11) NOT NULL,
        created_on DATETIME NOT NULL,
        last_updated_by INT(11) NOT NULL,
        last_updated_on DATETIME NOT NULL,
        PRIMARY KEY (sales_executive_id)
    );
    """,
    """
    CREATE TABLE IF NOT EXISTS store_manager (
        store_manager_id INT(11) NOT NULL AUTO_INCREMENT,
        name VARCHAR(255) NOT NULL,
        email VARCHAR(255) NOT NULL,
        phone INT(12) NOT NULL,
        password VARCHAR(255) NOT NULL,
        profile_pic VARCHAR(255) NOT NULL,
        assigned_store_id INT(11) NOT NULL,
        address VARCHAR(255) NOT NULL,
        document_1_type VARCHAR(255) NOT NULL,
        document_1_url VARCHAR(255) NOT NULL,
        document_2_type VARCHAR(255) NOT NULL,
        document_2_url VARCHAR(255) NOT NULL,
        status INT(11) NOT NULL,
        created_by INT(11) NOT NULL,
        created_on DATETIME NOT NULL,
        last_updated_by INT(11) NOT NULL,
        last_updated_on DATETIME NOT NULL,
        PRIMARY KEY (store_manager_id)
    );
    """,
    """
    CREATE TABLE `django_session` (
     `session_key` varchar(40) NOT NULL,
     `session_data` longtext NOT NULL,
     `expire_date` datetime(6) NOT NULL,
     PRIMARY KEY (`session_key`),
     KEY `django_session_expire_date_a5c62663` (`expire_date`)
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci
    """
]

# Create a database connection
connection = pymysql.connect(host=db_host, user=db_user, password=db_password, database=db_name)

try:
    # Create a cursor object
    with connection.cursor() as cursor:
        # Execute each SQL query to create the tables
        for sql_query in sql_queries:
            cursor.execute(sql_query)

    # Commit the changes to the database
    connection.commit()
    print("Tables created successfully!")

except Exception as e:
    print(f"Error: {str(e)}")

finally:
    # Close the database connection
    connection.close()
