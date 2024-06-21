from indolens.db_connection import getConnection

sql_queries = [
    """
  ALTER TABLE `admin_setting`
  ADD COLUMN `support_attributes` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_bin,
  ADD COLUMN `central_inventory_details` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_bin;""",

    """ALTER TABLE admin
    CHANGE COLUMN admin_id admin_admin_id INT(11) NOT NULL AUTO_INCREMENT,
    CHANGE COLUMN name admin_name VARCHAR(255),
    CHANGE COLUMN email admin_email VARCHAR(255),
    CHANGE COLUMN phone admin_phone VARCHAR(12),
    CHANGE COLUMN password admin_password VARCHAR(255),
    CHANGE COLUMN role admin_role INT(12),
    CHANGE COLUMN profile_pic admin_profile_pic VARCHAR(255),
    CHANGE COLUMN address admin_address VARCHAR(255),
    CHANGE COLUMN document_1_type admin_document_1_type VARCHAR(255),
    CHANGE COLUMN document_1_url admin_document_1_url longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_bin,
    CHANGE COLUMN document_2_type admin_document_2_type VARCHAR(255),
    CHANGE COLUMN document_2_url admin_document_2_url longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_bin,
    CHANGE COLUMN status admin_status INT(11),
    CHANGE COLUMN created_by admin_created_by INT(11),
    CHANGE COLUMN created_on admin_created_on DATETIME,
    CHANGE COLUMN last_updated_by admin_last_updated_by INT(11),
    CHANGE COLUMN last_updated_on admin_last_updated_on DATETIME;""",

    """ALTER TABLE area_head
    CHANGE COLUMN area_head_id ah_area_head_id INT(11) NOT NULL AUTO_INCREMENT,
    CHANGE COLUMN name ah_name VARCHAR(255),
    CHANGE COLUMN email ah_email VARCHAR(255),
    CHANGE COLUMN phone ah_phone VARCHAR(255),
    CHANGE COLUMN password ah_password VARCHAR(255),
    CHANGE COLUMN profile_pic ah_profile_pic VARCHAR(255),
    CHANGE COLUMN assigned_stores ah_assigned_stores longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_bin,
    CHANGE COLUMN address ah_address VARCHAR(255),
    CHANGE COLUMN document_1_type ah_document_1_type VARCHAR(255),
    CHANGE COLUMN document_1_url ah_document_1_url longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_bin,
    CHANGE COLUMN document_2_type ah_document_2_type VARCHAR(255),
    CHANGE COLUMN document_2_url ah_document_2_url longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_bin,
    CHANGE COLUMN status ah_status INT(11),
    CHANGE COLUMN created_by ah_created_by INT(11),
    CHANGE COLUMN created_on ah_created_on DATETIME,
    CHANGE COLUMN last_updated_by ah_last_updated_by INT(11),
    CHANGE COLUMN last_updated_on ah_last_updated_on DATETIME;""",

    """ALTER TABLE brands
    CHANGE COLUMN brand_id brand_brand_id INT(11) NOT NULL AUTO_INCREMENT,
    CHANGE COLUMN brand_name brand_name VARCHAR(255),
    CHANGE COLUMN category_id brand_category_id INT(11),
    CHANGE COLUMN brand_description brand_description VARCHAR(255),
    CHANGE COLUMN status brand_status TINYINT(1),
    CHANGE COLUMN created_on brand_created_on DATETIME,
    CHANGE COLUMN created_by brand_created_by INT(11),
    CHANGE COLUMN last_updated_on brand_last_updated_on DATETIME,
    CHANGE COLUMN last_updated_by brand_last_updated_by INT(11);""",

    """
    ALTER TABLE central_inventory
  CHANGE COLUMN product_id ci_product_id INT(11) NOT NULL AUTO_INCREMENT,
  CHANGE COLUMN product_name ci_product_name VARCHAR(255),
  CHANGE COLUMN product_description ci_product_description LONGTEXT,
  CHANGE COLUMN product_images ci_product_images longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_bin,
  CHANGE COLUMN product_qr_code ci_product_qr_code VARCHAR(255),
  CHANGE COLUMN category_id ci_category_id INT(11),
  CHANGE COLUMN brand_id ci_brand_id INT(11),
  CHANGE COLUMN material_id ci_material_id INT(11),
  CHANGE COLUMN frame_type_id ci_frame_type_id INT(11),
  CHANGE COLUMN frame_shape_id ci_frame_shape_id INT(11),
  CHANGE COLUMN color_id ci_color_id INT(11),
  CHANGE COLUMN unit_id ci_unit_id INT(11),
  CHANGE COLUMN origin ci_origin VARCHAR(255),
  CHANGE COLUMN cost_price ci_cost_price INT(11),
  CHANGE COLUMN sale_price ci_sale_price INT(11),
  CHANGE COLUMN model_number ci_model_number VARCHAR(255),
  CHANGE COLUMN hsn ci_hsn VARCHAR(255),
  CHANGE COLUMN power_attribute ci_power_attribute longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_bin,
  CHANGE COLUMN franchise_sale_price ci_franchise_sale_price INT(11),
  CHANGE COLUMN product_quantity ci_product_quantity INT(11),
  CHANGE COLUMN product_gst ci_product_gst FLOAT,
  CHANGE COLUMN status ci_status TINYINT(1),
  CHANGE COLUMN discount ci_discount FLOAT,
  CHANGE COLUMN created_on ci_created_on DATETIME,
  CHANGE COLUMN created_by ci_created_by INT(11),
  CHANGE COLUMN last_updated_on ci_last_updated_on DATETIME,
  CHANGE COLUMN last_updated_by ci_last_updated_by INT(11);
    """,

    """ALTER TABLE central_inventory_restock_log
    CHANGE COLUMN restock_id cirl_restock_id INT(11) NOT NULL AUTO_INCREMENT,
    CHANGE COLUMN product_id cirl_product_id INT(11),
    CHANGE COLUMN quantity cirl_quantity INT(11),
    CHANGE COLUMN created_by cirl_created_by INT(11),
    CHANGE COLUMN created_on cirl_created_on DATETIME;""",

    """ALTER TABLE customers
    CHANGE COLUMN customer_id customer_customer_id INT(11) NOT NULL AUTO_INCREMENT,
    CHANGE COLUMN name customer_name VARCHAR(255),
    CHANGE COLUMN gender customer_gender VARCHAR(255),
    CHANGE COLUMN age customer_age INT(11),
    CHANGE COLUMN phone customer_phone VARCHAR(255),
    CHANGE COLUMN email customer_email VARCHAR(255),
    CHANGE COLUMN language customer_language VARCHAR(255),
    CHANGE COLUMN city customer_city VARCHAR(255),
    CHANGE COLUMN address customer_address VARCHAR(255),
    CHANGE COLUMN created_by_employee_id customer_created_by_employee_id INT(11),
    CHANGE COLUMN created_by_store_id customer_created_by_store_id INT(11),
    CHANGE COLUMN created_by_store_type customer_created_by_store_type INT(11),
    CHANGE COLUMN created_on customer_created_on DATETIME,
    CHANGE COLUMN updated_by_employee_id customer_updated_by_employee_id INT(11),
    CHANGE COLUMN updated_by_store_id customer_updated_by_store_id INT(11),
    CHANGE COLUMN updated_by_store_type customer_updated_by_store_type INT(11),
    CHANGE COLUMN updated_on customer_updated_on DATETIME;""",

    """
    ALTER TABLE eye_test
    CHANGE COLUMN eye_test_id et_eye_test_id INT(11) NOT NULL AUTO_INCREMENT,
    CHANGE COLUMN customer_id et_customer_id INT(11),
    CHANGE COLUMN power_attributes et_power_attributes longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_bin,
    CHANGE COLUMN created_by_store_id et_created_by_store_id INT(11),
    CHANGE COLUMN created_by_store_type et_created_by_store_type INT(11),
    CHANGE COLUMN created_by et_created_by INT(11),
    CHANGE COLUMN created_on et_created_on DATETIME,
    CHANGE COLUMN updated_by et_updated_by INT(11),
    CHANGE COLUMN updated_on et_updated_on DATETIME,
    ADD COLUMN et_optometry_id INT(11);
    """,
    
    """
    UPDATE eye_test SET et_optometry_id = et_created_by;
    """,

    """ALTER TABLE frame_shapes
    CHANGE COLUMN shape_id fshape_shape_id INT(11) NOT NULL AUTO_INCREMENT,
    CHANGE COLUMN shape_name fshape_name VARCHAR(255),
    CHANGE COLUMN shape_description fshape_description VARCHAR(255),
    CHANGE COLUMN status fshape_status INT(11),
    CHANGE COLUMN created_on fshape_created_on DATETIME,
    CHANGE COLUMN created_by fshape_created_by INT(11),
    CHANGE COLUMN last_updated_on fshape_last_updated_on DATETIME,
    CHANGE COLUMN last_updated_by fshape_last_updated_by INT(11);""",

    """ALTER TABLE frame_types
    CHANGE COLUMN frame_id ftype_frame_id INT(11) NOT NULL AUTO_INCREMENT,
    CHANGE COLUMN frame_type_name ftype_name VARCHAR(255),
    CHANGE COLUMN frame_type_description ftype_description VARCHAR(255),
    CHANGE COLUMN status ftype_status INT(11),
    CHANGE COLUMN created_on ftype_created_on DATETIME,
    CHANGE COLUMN created_by ftype_created_by INT(11),
    CHANGE COLUMN last_updated_on ftype_last_updated_on DATETIME,
    CHANGE COLUMN last_updated_by ftype_last_updated_by INT(11);""",


    """
    ALTER TABLE franchise_store
CHANGE COLUMN store_id fs_store_id INT(11) NOT NULL AUTO_INCREMENT,
CHANGE COLUMN store_name fs_store_name VARCHAR(255),
CHANGE COLUMN store_display_name fs_store_display_name VARCHAR(255),
CHANGE COLUMN store_phone fs_store_phone VARCHAR(255),
CHANGE COLUMN store_gst fs_store_gst VARCHAR(255),
CHANGE COLUMN store_email fs_store_email VARCHAR(255),
CHANGE COLUMN store_city fs_store_city VARCHAR(255),
CHANGE COLUMN store_state fs_store_state VARCHAR(255),
CHANGE COLUMN store_zip fs_store_zip VARCHAR(255),
CHANGE COLUMN store_lat fs_store_lat DOUBLE,
CHANGE COLUMN store_lng fs_store_lng DOUBLE,
CHANGE COLUMN store_address fs_store_address VARCHAR(255),
CHANGE COLUMN status fs_status INT(11),
CHANGE COLUMN created_by fs_created_by INT(11),
CHANGE COLUMN created_on fs_created_on DATETIME,
CHANGE COLUMN last_updated_by fs_last_updated_by INT(11),
CHANGE COLUMN last_updated_on fs_last_updated_on DATETIME;
    """,

   
   """
   ALTER TABLE franchise_store_employees
CHANGE COLUMN employee_id fse_employee_id INT(11) NOT NULL AUTO_INCREMENT,
CHANGE COLUMN name fse_name VARCHAR(255),
CHANGE COLUMN email fse_email VARCHAR(255),
CHANGE COLUMN phone fse_phone VARCHAR(255),
CHANGE COLUMN password fse_password VARCHAR(255),
CHANGE COLUMN profile_pic fse_profile_pic VARCHAR(255),
CHANGE COLUMN assigned_store_id fse_assigned_store_id INT(11),
CHANGE COLUMN address fse_address VARCHAR(255),
CHANGE COLUMN document_1_type fse_document_1_type VARCHAR(255),
CHANGE COLUMN document_1_url fse_document_1_url longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_bin,
CHANGE COLUMN document_2_type fse_document_2_type VARCHAR(255),
CHANGE COLUMN document_2_url fse_document_2_url longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_bin,
CHANGE COLUMN status fse_status INT(11),
CHANGE COLUMN role fse_role INT(11),
CHANGE COLUMN created_by fse_created_by INT(11),
CHANGE COLUMN created_on fse_created_on DATETIME,
CHANGE COLUMN last_updated_by fse_last_updated_by INT(11),
CHANGE COLUMN last_updated_on fse_last_updated_on DATETIME,
CHANGE COLUMN certificates fse_certificates longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_bin;
   """,

    """ ALTER TABLE invoice
    CHANGE COLUMN invoice_id invoice_invoice_id INT(11) NOT NULL AUTO_INCREMENT,
    CHANGE COLUMN invoice_number invoice_invoice_number VARCHAR(255),
    CHANGE COLUMN order_id invoice_order_id VARCHAR(255),
    CHANGE COLUMN store_id invoice_store_id INT(11),
    CHANGE COLUMN store_type invoice_store_type INT(11),
    CHANGE COLUMN invoice_status invoice_invoice_status INT(11),
    CHANGE COLUMN invoice_date invoice_invoice_date DATE;""",

    """ALTER TABLE lab
    CHANGE COLUMN lab_id lab_lab_id INT(11) NOT NULL AUTO_INCREMENT,
    CHANGE COLUMN lab_name lab_name VARCHAR(255),
    CHANGE COLUMN lab_display_name lab_display_name VARCHAR(255),
    CHANGE COLUMN lab_phone lab_phone VARCHAR(255),
    CHANGE COLUMN lab_gst lab_gst VARCHAR(255),
    CHANGE COLUMN lab_email lab_email VARCHAR(255),
    CHANGE COLUMN lab_city lab_city VARCHAR(255),
    CHANGE COLUMN lab_state lab_state VARCHAR(255),
    CHANGE COLUMN lab_zip lab_zip VARCHAR(255),
    CHANGE COLUMN lab_lat lab_lat DOUBLE,
    CHANGE COLUMN lab_lng lab_lng DOUBLE,
    CHANGE COLUMN lab_address lab_address VARCHAR(255),
    CHANGE COLUMN status lab_status INT(11),
    CHANGE COLUMN created_by lab_created_by INT(11),
    CHANGE COLUMN created_on lab_created_on DATETIME,
    CHANGE COLUMN last_updated_by lab_last_updated_by INT(11),
    CHANGE COLUMN last_updated_on lab_last_updated_on DATETIME;""",

    """ALTER TABLE lab_technician
    CHANGE COLUMN lab_technician_id lt_lab_technician_id INT(11) NOT NULL AUTO_INCREMENT,
    CHANGE COLUMN name lt_name VARCHAR(255),
    CHANGE COLUMN email lt_email VARCHAR(255),
    CHANGE COLUMN phone lt_phone VARCHAR(255),
    CHANGE COLUMN password lt_password VARCHAR(255),
    CHANGE COLUMN profile_pic lt_profile_pic VARCHAR(255),
    CHANGE COLUMN assigned_lab_id lt_assigned_lab_id INT(11),
    CHANGE COLUMN address lt_address VARCHAR(255),
    CHANGE COLUMN document_1_type lt_document_1_type VARCHAR(255),
    CHANGE COLUMN document_1_url lt_document_1_url longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_bin,
    CHANGE COLUMN document_2_type lt_document_2_type VARCHAR(255),
    CHANGE COLUMN document_2_url lt_document_2_url longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_bin,
    CHANGE COLUMN status lt_status INT(11),
    CHANGE COLUMN created_by lt_created_by INT(11),
    CHANGE COLUMN created_on lt_created_on DATETIME,
    CHANGE COLUMN last_updated_by lt_last_updated_by INT(11),
    CHANGE COLUMN last_updated_on lt_last_updated_on DATETIME;""",

    """ALTER TABLE marketing_head
    CHANGE COLUMN marketing_head_id mh_marketing_head_id INT(11) NOT NULL AUTO_INCREMENT,
    CHANGE COLUMN name mh_name VARCHAR(255),
    CHANGE COLUMN email mh_email VARCHAR(255),
    CHANGE COLUMN phone mh_phone VARCHAR(255),
    CHANGE COLUMN password mh_password VARCHAR(255),
    CHANGE COLUMN profile_pic mh_profile_pic VARCHAR(255),
    CHANGE COLUMN assigned_area_head mh_assigned_area_head INT(11),
    CHANGE COLUMN address mh_address VARCHAR(255),
    CHANGE COLUMN document_1_type mh_document_1_type VARCHAR(255),
    CHANGE COLUMN document_1_url mh_document_1_url longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_bin,
    CHANGE COLUMN document_2_type mh_document_2_type VARCHAR(255),
    CHANGE COLUMN document_2_url mh_document_2_url longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_bin,
    CHANGE COLUMN status mh_status INT(11),
    CHANGE COLUMN created_by mh_created_by INT(11),
    CHANGE COLUMN created_on mh_created_on DATETIME,
    CHANGE COLUMN last_updated_by mh_last_updated_by INT(11),
    CHANGE COLUMN last_updated_on mh_last_updated_on DATETIME;""",

    """ALTER TABLE own_store
    CHANGE COLUMN store_id os_store_id INT(11) NOT NULL AUTO_INCREMENT,
    CHANGE COLUMN store_name os_store_name VARCHAR(255),
    CHANGE COLUMN store_display_name os_store_display_name VARCHAR(255),
    CHANGE COLUMN store_phone os_store_phone VARCHAR(255),
    CHANGE COLUMN store_gst os_store_gst VARCHAR(255),
    CHANGE COLUMN store_email os_store_email VARCHAR(255),
    CHANGE COLUMN store_city os_store_city VARCHAR(255),
    CHANGE COLUMN store_state os_store_state VARCHAR(255),
    CHANGE COLUMN store_zip os_store_zip VARCHAR(255),
    CHANGE COLUMN store_lat os_store_lat DOUBLE,
    CHANGE COLUMN store_lng os_store_lng DOUBLE,
    CHANGE COLUMN store_address os_store_address VARCHAR(255),
    CHANGE COLUMN status os_status INT(11),
    CHANGE COLUMN created_by os_created_by INT(11),
    CHANGE COLUMN created_on os_created_on DATETIME,
    CHANGE COLUMN last_updated_by os_last_updated_by INT(11),
    CHANGE COLUMN last_updated_on os_last_updated_on DATETIME;""",

    """ALTER TABLE own_store_employees
    CHANGE COLUMN employee_id ose_employee_id INT(11) NOT NULL AUTO_INCREMENT,
    CHANGE COLUMN name ose_name VARCHAR(255),
    CHANGE COLUMN email ose_email VARCHAR(255),
    CHANGE COLUMN phone ose_phone VARCHAR(255),
    CHANGE COLUMN password ose_password VARCHAR(255),
    CHANGE COLUMN profile_pic ose_profile_pic VARCHAR(255),
    CHANGE COLUMN assigned_store_id ose_assigned_store_id INT(11),
    CHANGE COLUMN address ose_address VARCHAR(255),
    CHANGE COLUMN document_1_type ose_document_1_type VARCHAR(255),
    CHANGE COLUMN document_1_url ose_document_1_url longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_bin,
    CHANGE COLUMN document_2_type ose_document_2_type VARCHAR(255),
    CHANGE COLUMN document_2_url ose_document_2_url longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_bin,
    CHANGE COLUMN status ose_status INT(11),
    CHANGE COLUMN role ose_role INT(11),
    CHANGE COLUMN created_by ose_created_by INT(11),
    CHANGE COLUMN created_on ose_created_on DATETIME,
    CHANGE COLUMN last_updated_by ose_last_updated_by INT(11),
    CHANGE COLUMN last_updated_on ose_last_updated_on DATETIME,
    CHANGE COLUMN certificates ose_certificates longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_bin;""",

    """ALTER TABLE product_categories
    CHANGE COLUMN category_id pc_category_id INT(11) NOT NULL AUTO_INCREMENT,
    CHANGE COLUMN category_name pc_category_name VARCHAR(255),
    CHANGE COLUMN category_prefix pc_category_prefix VARCHAR(255),
    CHANGE COLUMN category_description pc_category_description VARCHAR(255),
    CHANGE COLUMN status pc_status TINYINT(1),
    CHANGE COLUMN created_on pc_created_on DATETIME,
    CHANGE COLUMN created_by pc_created_by INT(11),
    CHANGE COLUMN last_updated_on pc_last_updated_on DATETIME,
    CHANGE COLUMN last_updated_by pc_last_updated_by INT(11);""",

    """ALTER TABLE product_colors
    CHANGE COLUMN color_id pcol_color_id INT(11) NOT NULL AUTO_INCREMENT,
    CHANGE COLUMN color_code pcol_color_code VARCHAR(255),
    CHANGE COLUMN color_name pcol_color_name VARCHAR(255),
    CHANGE COLUMN color_description pcol_color_description VARCHAR(255),
    CHANGE COLUMN status pcol_status INT(11),
    CHANGE COLUMN created_on pcol_created_on DATETIME,
    CHANGE COLUMN created_by pcol_created_by INT(11),
    CHANGE COLUMN last_updated_on pcol_last_updated_on DATETIME,
    CHANGE COLUMN last_updated_by pcol_last_updated_by INT(11);""",

    """ALTER TABLE product_materials
    CHANGE COLUMN material_id pm_material_id INT(11) NOT NULL AUTO_INCREMENT,
    CHANGE COLUMN material_name pm_material_name VARCHAR(255),
    CHANGE COLUMN material_description pm_material_description VARCHAR(255),
    CHANGE COLUMN status pm_status INT(11),
    CHANGE COLUMN created_on pm_created_on DATETIME,
    CHANGE COLUMN created_by pm_created_by INT(11),
    CHANGE COLUMN last_updated_on pm_last_updated_on DATETIME,
    CHANGE COLUMN last_updated_by pm_last_updated_by INT(11);""",

    """ALTER TABLE request_products
    CHANGE COLUMN request_products_id pr_request_products_id INT(11) NOT NULL AUTO_INCREMENT,
    CHANGE COLUMN store_id pr_store_id INT(11),
    CHANGE COLUMN store_type pr_store_type INT(11),
    CHANGE COLUMN product_id pr_product_id INT(11),
    CHANGE COLUMN product_quantity pr_product_quantity INT(11),
    CHANGE COLUMN unit_cost pr_unit_cost INT(11),
    CHANGE COLUMN request_status pr_request_status INT(11),
    CHANGE COLUMN delivery_status pr_delivery_status INT(11),
    CHANGE COLUMN is_requested pr_is_requested TINYINT(1),
    CHANGE COLUMN request_to_store_id pr_request_to_store_id INT(11),
    CHANGE COLUMN payment_status pr_payment_status INT(11),
    CHANGE COLUMN comment pr_comment VARCHAR(255),
    CHANGE COLUMN created_on pr_created_on DATETIME,
    CHANGE COLUMN created_by pr_created_by INT(11),
    CHANGE COLUMN last_updated_on pr_last_updated_on DATETIME,
    CHANGE COLUMN last_updated_by pr_last_updated_by INT(11);""",

    """ALTER TABLE reset_password
    CHANGE COLUMN reset_password_id rpwd_reset_password_id INT(11) NOT NULL AUTO_INCREMENT,
    CHANGE COLUMN email rpwd_email VARCHAR(255),
    CHANGE COLUMN code rpwd_code VARCHAR(255),
    CHANGE COLUMN status rpwd_status INT(11),
    CHANGE COLUMN created_on rpwd_created_on DATETIME;""",

    """ALTER TABLE sales_order_payment_track
    CHANGE COLUMN id sopt_id INT(11) NOT NULL AUTO_INCREMENT,
    CHANGE COLUMN order_id sopt_order_id VARCHAR(255),
    CHANGE COLUMN payment_amount sopt_payment_amount INT(11),
    CHANGE COLUMN payment_mode sopt_payment_mode INT(11),
    CHANGE COLUMN payment_type sopt_payment_type INT(11),
    CHANGE COLUMN created_by_store sopt_created_by_store INT(11),
    CHANGE COLUMN created_by_store_type sopt_created_by_store_type INT(11),
    CHANGE COLUMN created_by_id sopt_created_by_id INT(11),
    CHANGE COLUMN created_on sopt_created_on DATETIME;""",

    """ALTER TABLE sales_order
    CHANGE COLUMN sale_item_id so_sale_item_id INT(11) NOT NULL AUTO_INCREMENT,
    CHANGE COLUMN order_id so_order_id VARCHAR(255),
    CHANGE COLUMN product_id so_product_id INT(11),
    CHANGE COLUMN hsn so_hsn VARCHAR(255),
    CHANGE COLUMN unit_sale_price so_unit_sale_price INT(11),
    CHANGE COLUMN unit_type so_unit_type VARCHAR(255),
    CHANGE COLUMN purchase_quantity so_purchase_quantity INT(11),
    CHANGE COLUMN product_total_cost so_product_total_cost INT(11),
    CHANGE COLUMN discount_percentage so_discount_percentage INT(11),
    CHANGE COLUMN is_discount_applied so_is_discount_applied INT(11),
    CHANGE COLUMN power_attribute so_power_attribute longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_bin,
    CHANGE COLUMN assigned_lab so_assigned_lab INT(11),
    CHANGE COLUMN customer_id so_customer_id INT(11),
    CHANGE COLUMN order_status so_order_status INT(11),
    CHANGE COLUMN payment_status so_payment_status INT(11),
    CHANGE COLUMN delivery_status so_delivery_status INT(11),
    CHANGE COLUMN payment_mode so_order_mode INT(11),
    CHANGE COLUMN amount_paid so_amount_paid INT(11),
    CHANGE COLUMN estimated_delivery_date so_estimated_delivery_date DATE,
    CHANGE COLUMN linked_item so_linked_item longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_bin,
    CHANGE COLUMN sales_note so_sales_note LONGTEXT,
    CHANGE COLUMN created_by_store so_created_by_store INT(11),
    CHANGE COLUMN created_by_store_type so_created_by_store_type INT(11),
    CHANGE COLUMN created_by so_created_by INT(11),
    CHANGE COLUMN created_on so_created_on DATETIME,
    CHANGE COLUMN updated_by so_updated_by INT(11),
    CHANGE COLUMN updated_on so_updated_on DATETIME;""",

    """ALTER TABLE store_expense
    CHANGE COLUMN store_expense_id se_store_expense_id INT(11) NOT NULL AUTO_INCREMENT,
    CHANGE COLUMN store_id se_store_id INT(11),
    CHANGE COLUMN store_type se_store_type INT(11),
    CHANGE COLUMN expense_amount se_expense_amount INT(11),
    CHANGE COLUMN expense_reason se_expense_reason VARCHAR(255),
    CHANGE COLUMN expense_date se_expense_date DATETIME,
    CHANGE COLUMN created_on se_created_on DATETIME,
    CHANGE COLUMN created_by se_created_by INT(11);""",

    """ALTER TABLE store_inventory
    CHANGE COLUMN store_inventory_id si_store_inventory_id INT(11) NOT NULL AUTO_INCREMENT,
    CHANGE COLUMN store_id si_store_id INT(11),
    CHANGE COLUMN store_type si_store_type INT(11),
    CHANGE COLUMN product_id si_product_id INT(11),
    CHANGE COLUMN product_quantity si_product_quantity INT(11),
    CHANGE COLUMN created_on si_created_on DATETIME,
    CHANGE COLUMN created_by si_created_by INT(11),
    CHANGE COLUMN last_updated_on si_last_updated_on DATETIME,
    CHANGE COLUMN last_updated_by si_last_updated_by INT(11);""",


    """ALTER TABLE units
    CHANGE COLUMN unit_id unit_unit_id INT(11) NOT NULL AUTO_INCREMENT,
    CHANGE COLUMN unit_name unit_name VARCHAR(255),
    CHANGE COLUMN status unit_status INT(11),
    CHANGE COLUMN created_on unit_created_on DATETIME,
    CHANGE COLUMN created_by unit_created_by INT(11),
    CHANGE COLUMN last_updated_on unit_last_updated_on DATETIME,
    CHANGE COLUMN last_updated_by unit_last_updated_by INT(11);""",

    """ALTER TABLE accountant
    CHANGE COLUMN accountant_id ac_accountant_id INT(11) NOT NULL AUTO_INCREMENT,
    CHANGE COLUMN name ac_name VARCHAR(255),
    CHANGE COLUMN email ac_email VARCHAR(255),
    CHANGE COLUMN phone ac_phone VARCHAR(255),
    CHANGE COLUMN password ac_password VARCHAR(255),
    CHANGE COLUMN profile_pic ac_profile_pic VARCHAR(255),
    CHANGE COLUMN address ac_address VARCHAR(255),
    CHANGE COLUMN document_1_type ac_document_1_type VARCHAR(255),
    CHANGE COLUMN document_1_url ac_document_1_url longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_bin,
    CHANGE COLUMN document_2_type ac_document_2_type VARCHAR(255),
    CHANGE COLUMN document_2_url ac_document_2_url longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_bin,
    CHANGE COLUMN status ac_status INT(11),
    CHANGE COLUMN created_by ac_created_by INT(11),
    CHANGE COLUMN created_on ac_created_on DATETIME,
    CHANGE COLUMN last_updated_by ac_last_updated_by INT(11),
    CHANGE COLUMN last_updated_on ac_last_updated_on DATETIME;"""
]

try:
    with getConnection().cursor() as cursor:
        for sql_query in sql_queries:
            cursor.execute(sql_query)

    print("Tables created successfully!")

except Exception as e:
    print(f"Error: {str(e)}")
