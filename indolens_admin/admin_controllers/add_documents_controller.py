import datetime
import json
import os

import pymysql
import pytz
from indolens.db_connection import getConnection

ist = pytz.timezone('Asia/Kolkata')


def getIndianTime():
    today = datetime.datetime.now(ist)
    return today


def add_document(documenturl, document_type, table, condition, user_id, updated_by):
    try:
        parts = documenturl.split('/')
        folder_name = parts[0]
        file_name = parts[-1]
        file_path = os.path.join("media", folder_name, file_name)

        if os.path.exists(file_path):
            os.remove(file_path)
            with getConnection().cursor() as cursor:
                get_documents_query = f"""
                SELECT {document_type} FROM {table} Where {condition} = {user_id}
                """
                cursor.execute(get_documents_query)
                documents = json.loads(cursor.fetchone()[0])
                documents.remove(documenturl)
                cursor.execute(f""" UPDATE {table} SET {document_type} = {json.dumps(documents)},
                 last_updated_on = '{getIndianTime()}', last_updated_by = {updated_by} WHERE {condition} = {user_id}""")
            return {
                "status": True,
                "message": "Document Deleted Successfully"
            }
        else:
            return {
                "status": False,
                "message": f"{file_name} Document Doesn't Exist"
            }

    except pymysql.Error as e:
        return {"status": False, "message": str(e)}, 301
    except Exception as e:
        return {"status": False, "message": str(e)}, 301


def add_products_image(new_images, productId, updated_by):
    try:
        with getConnection().cursor() as cursor:
            get_documents_query = f"""
            SELECT ci_product_images FROM central_inventory Where ci_product_id = {productId}
            """
            cursor.execute(get_documents_query)
            old_images = cursor.fetchone()
            print(old_images)
            print(json.loads(old_images['ci_product_images']))
            product_image = json.loads(old_images['ci_product_images']) + new_images.product_img
            print(product_image)
            cursor.execute(
                f""" UPDATE central_inventory SET ci_product_images = '{json.dumps(product_image)}', 
                ci_last_updated_on = '{getIndianTime()}', ci_last_updated_by = {updated_by} WHERE ci_product_id = {productId}""")
        return {
            "status": True,
            "message": "Document Deleted Successfully"
        }

    except pymysql.Error as e:
        return {"status": False, "message": str(e)}, 301
    except Exception as e:
        return {"status": False, "message": str(e)}, 301


def add_own_store_employee_image(file_data, employeeId, emp_obj, updated_by):
    try:
        with getConnection().cursor() as cursor:
            get_role = f""" SELECT ose_role from own_store_employees Where ose_employee_id = {employeeId}"""
            cursor.execute(get_role)
            role = cursor.fetchone()

            get_document1_query = f"""
                        SELECT ose_document_1_url FROM own_store_employees Where ose_employee_id = {employeeId}
                        """
            cursor.execute(get_document1_query)
            old_images = json.loads(cursor.fetchone()['ose_document_1_url'])
            document1 = old_images + file_data.document1

            cursor.execute(
                f""" UPDATE own_store_employees SET ose_document_1_url = '{json.dumps(document1)}', 
                ose_document_1_type = '{emp_obj.document_1_type}', ose_last_updated_on = '{getIndianTime()}', 
                ose_last_updated_by = {updated_by} WHERE ose_employee_id = {employeeId}""")

            get_document2_query = f"""
                        SELECT ose_document_2_url FROM own_store_employees Where ose_employee_id = {employeeId}
                        """
            cursor.execute(get_document2_query)
            old_images = json.loads(cursor.fetchone()['ose_document_2_url'])
            document2 = old_images + file_data.document2
            cursor.execute(
                f""" UPDATE own_store_employees SET ose_document_2_url = '{json.dumps(document2)}', 
                ose_document_2_type = '{emp_obj.document_2_type}', ose_last_updated_on = '{getIndianTime()}', 
                ose_last_updated_by = {updated_by} WHERE ose_employee_id = {employeeId}""")

            get_certificates_query = f"""
                        SELECT ose_certificates FROM own_store_employees Where ose_employee_id = {employeeId}
                        """
            cursor.execute(get_certificates_query)
            certificates = cursor.fetchone()['ose_certificates']

            if certificates is not None:
                old_images = json.loads(certificates)
                certificates = old_images + file_data.certificates
                cursor.execute(
                    f""" UPDATE own_store_employees SET ose_certificates = '{json.dumps(certificates)}', 
                    ose_last_updated_on = '{getIndianTime()}', ose_last_updated_by = {updated_by}
                    WHERE ose_employee_id = {employeeId}""")

        return {
            "status": True,
            "role": role['ose_role'],
            "message": "Document Inserted Successfully"
        }, 200

    except pymysql.Error as e:
        return {"status": False, "role": role[0], "message": str(e)}, 301
    except Exception as e:
        return {"status": False, "role": role[0], "message": str(e)}, 301


def add_franchise_store_employee_image(file_data, employeeId, emp_obj, updated_by):
    try:
        with getConnection().cursor() as cursor:
            get_role = f""" SELECT fse_role from franchise_store_employees Where fse_employee_id = {employeeId}"""
            cursor.execute(get_role)
            role = cursor.fetchone()

            get_document1_query = f"""
                        SELECT fse_document_1_url FROM franchise_store_employees Where fse_employee_id = {employeeId}
                        """
            cursor.execute(get_document1_query)
            old_images = json.loads(cursor.fetchone()['fse_document_1_url'])
            document1 = old_images + file_data.document1

            cursor.execute(
                f""" UPDATE franchise_store_employees SET fse_document_1_url = '{json.dumps(document1)}', 
                fse_document_1_type = '{emp_obj.document_1_type}', fse_last_updated_on = '{getIndianTime()}', 
                fse_last_updated_by = {updated_by} WHERE fse_employee_id = {employeeId}""")

            get_document2_query = f"""
                        SELECT fse_document_2_url FROM franchise_store_employees Where fse_employee_id = {employeeId}
                        """
            cursor.execute(get_document2_query)
            old_images = json.loads(cursor.fetchone()['fse_document_2_url'])
            document2 = old_images + file_data.document2
            cursor.execute(
                f""" UPDATE franchise_store_employees SET fse_document_2_url = '{json.dumps(document2)}', 
                fse_document_2_type = '{emp_obj.document_2_type}', fse_last_updated_on = '{getIndianTime()}', 
                fse_last_updated_by = {updated_by} WHERE fse_employee_id = {employeeId}""")

            get_certificates_query = f"""
                        SELECT fse_certificates FROM franchise_store_employees Where fse_employee_id = {employeeId}
                        """
            cursor.execute(get_certificates_query)
            certificate = cursor.fetchone()['fse_certificates']
            if certificate is not None:
                old_images = json.loads(certificate)
                certificates = old_images + file_data.certificates
                cursor.execute(
                    f""" UPDATE franchise_store_employees SET fse_certificates = '{json.dumps(certificates)}',
                    fse_last_updated_on = '{getIndianTime()}', fse_last_updated_by = {updated_by}
                    WHERE fse_employee_id = {employeeId}""")

        return {
            "status": True,
            "role": role['fse_role'],
            "message": "Document Inserted Successfully"
        }, 200

    except pymysql.Error as e:
        return {"status": False, "role": role[0], "message": str(e)}, 301
    except Exception as e:
        return {"status": False, "role": role[0], "message": str(e)}, 301


def add_sub_admin_doc(file_data, subAdminId, emp_obj, updated_by):
    try:
        with getConnection().cursor() as cursor:
            get_document1_query = f"""
                        SELECT admin_document_1_url FROM admin Where admin_admin_id = {subAdminId}
                        """
            cursor.execute(get_document1_query)
            old_images = json.loads(cursor.fetchone()['admin_document_1_url'])
            document1 = old_images + file_data.document1

            cursor.execute(
                f""" UPDATE admin SET admin_document_1_url = '{json.dumps(document1)}', 
                admin_document_1_type = '{emp_obj.document_1_type}', admin_last_updated_on = '{getIndianTime()}', 
                admin_last_updated_by = {updated_by} WHERE admin_admin_id = {subAdminId}""")

            get_document2_query = f"""
                        SELECT admin_document_2_url FROM admin Where admin_admin_id = {subAdminId}
                        """
            cursor.execute(get_document2_query)
            old_images = json.loads(cursor.fetchone()['admin_document_2_url'])
            document2 = old_images + file_data.document2
            cursor.execute(
                f""" UPDATE admin SET admin_document_2_url = '{json.dumps(document2)}', 
                admin_document_2_type = '{emp_obj.document_2_type}', admin_last_updated_on = '{getIndianTime()}', 
                admin_last_updated_by = {updated_by} WHERE admin_admin_id = {subAdminId}""")

        return {
            "status": True,
            "message": "Document Inserted Successfully"
        }, 200

    except pymysql.Error as e:
        return {"status": False, "message": str(e)}, 301
    except Exception as e:
        return {"status": False, "message": str(e)}, 301


def add_area_head_doc(file_data, areaHeadId, area_head, updated_by):
    try:
        with getConnection().cursor() as cursor:
            get_document1_query = f"""
                        SELECT ah_document_1_url FROM area_head Where ah_area_head_id = {areaHeadId}
                        """
            cursor.execute(get_document1_query)
            old_images = json.loads(cursor.fetchone()['ah_document_1_url'])
            document1 = old_images + file_data.document1

            cursor.execute(
                f""" UPDATE area_head SET ah_document_1_url = '{json.dumps(document1)}', 
                ah_document_1_type = '{area_head.document1_type}', ah_last_updated_on = '{getIndianTime()}', 
                ah_last_updated_by = {updated_by} WHERE ah_area_head_id = {areaHeadId}""")

            get_document2_query = f"""
                        SELECT ah_document_2_url FROM area_head Where ah_area_head_id = {areaHeadId}
                        """
            cursor.execute(get_document2_query)
            old_images = json.loads(cursor.fetchone()['ah_document_2_url'])
            document2 = old_images + file_data.document2
            cursor.execute(
                f""" UPDATE area_head SET ah_document_2_url = '{json.dumps(document2)}', 
                ah_document_2_type = '{area_head.document2_type}', ah_last_updated_on = '{getIndianTime()}', 
                ah_last_updated_by = {updated_by} WHERE ah_area_head_id = {areaHeadId}""")

        return {
            "status": True,
            "message": "Document Inserted Successfully"
        }, 200

    except pymysql.Error as e:
        return {"status": False, "message": str(e)}, 301
    except Exception as e:
        return {"status": False, "message": str(e)}, 301


def add_marketing_heads_doc(file_data, marketingHeadId, marketing_head, updated_by):
    try:
        with getConnection().cursor() as cursor:
            get_document1_query = f"""
                        SELECT document_1_url FROM marketing_head Where marketing_head_id = {marketingHeadId}
                        """
            cursor.execute(get_document1_query)
            old_images = json.loads(cursor.fetchone()[0])
            document1 = old_images + file_data.document1

            cursor.execute(
                f""" UPDATE marketing_head SET document_1_url = '{json.dumps(document1)}', 
                document_1_type = '{marketing_head.document_1_type}', last_updated_on = '{getIndianTime()}', 
                last_updated_by = {updated_by} WHERE marketing_head_id = {marketingHeadId}""")

            get_document2_query = f"""
                        SELECT document_2_url FROM marketing_head Where marketing_head_id = {marketingHeadId}
                        """
            cursor.execute(get_document2_query)
            old_images = json.loads(cursor.fetchone()[0])
            document2 = old_images + file_data.document2
            cursor.execute(
                f""" UPDATE marketing_head SET document_2_url = '{json.dumps(document2)}', 
                document_2_type = '{marketing_head.document_2_type}', last_updated_on = '{getIndianTime()}', 
                last_updated_by = {updated_by} WHERE marketing_head_id = {marketingHeadId}""")

        return {
            "status": True,
            "message": "Document Inserted Successfully"
        }, 200

    except pymysql.Error as e:
        return {"status": False, "message": str(e)}, 301
    except Exception as e:
        return {"status": False, "message": str(e)}, 301


def add_accountant_doc(file_data, accountantId, accountant, updated_by):
    try:
        with getConnection().cursor() as cursor:
            get_document1_query = f"""
                        SELECT ac_document_1_url FROM accountant Where ac_accountant_id = {accountantId}
                        """
            cursor.execute(get_document1_query)
            old_images = json.loads(cursor.fetchone()['ac_document_1_url'])
            document1 = old_images + file_data.document1

            cursor.execute(
                f""" UPDATE accountant SET ac_document_1_url = '{json.dumps(document1)}', 
                ac_document_1_type = '{accountant.document_1_type}', ac_last_updated_on = '{getIndianTime()}', 
                ac_last_updated_by = {updated_by} WHERE ac_accountant_id = {accountantId}""")

            get_document2_query = f"""
                        SELECT ac_document_2_url FROM accountant Where ac_accountant_id = {accountantId}
                        """
            cursor.execute(get_document2_query)
            old_images = json.loads(cursor.fetchone()['ac_document_2_url'])
            document2 = old_images + file_data.document2
            cursor.execute(
                f""" UPDATE accountant SET ac_document_2_url = '{json.dumps(document2)}', 
                ac_document_2_type = '{accountant.document_2_type}', ac_last_updated_on = '{getIndianTime()}', 
                ac_last_updated_by = {updated_by} WHERE ac_accountant_id = {accountantId}""")

        return {
            "status": True,
            "message": "Document Inserted Successfully"
        }, 200

    except pymysql.Error as e:
        return {"status": False, "message": str(e)}, 301
    except Exception as e:
        return {"status": False, "message": str(e)}, 301


def add_lab_technician_doc(file_data, LabTechnicianId, lab_technician, updated_by):
    try:
        with getConnection().cursor() as cursor:
            get_document1_query = f"""
                        SELECT lt_document_1_url FROM lab_technician Where lt_lab_technician_id = {LabTechnicianId}
                        """
            cursor.execute(get_document1_query)
            old_images = json.loads(cursor.fetchone()['lt_document_1_url'])
            document1 = old_images + file_data.document1

            cursor.execute(
                f""" UPDATE lab_technician SET lt_document_1_url = '{json.dumps(document1)}', 
                lt_document_1_type = '{lab_technician.document_1_type}',
                 lt_last_updated_on = '{getIndianTime()}', lt_last_updated_by = {updated_by} 
                 WHERE lt_lab_technician_id = {LabTechnicianId}""")

            get_document2_query = f"""
                        SELECT lt_document_2_url FROM lab_technician Where lt_lab_technician_id = {LabTechnicianId}
                        """
            cursor.execute(get_document2_query)
            old_images = json.loads(cursor.fetchone()['lt_document_2_url'])
            document2 = old_images + file_data.document2
            cursor.execute(
                f""" UPDATE lab_technician SET lt_document_2_url = '{json.dumps(document2)}', 
                lt_document_2_type = '{lab_technician.document_2_type}', lt_last_updated_on = '{getIndianTime()}', 
                lt_last_updated_by = {updated_by} WHERE lt_lab_technician_id = {LabTechnicianId}""")

        return {
            "status": True,
            "message": "Document Inserted Successfully"
        }, 200

    except pymysql.Error as e:
        return {"status": False, "message": str(e)}, 301
    except Exception as e:
        return {"status": False, "message": str(e)}, 301
