def get_power_attribute(data):
    if data['product_category_id'] == '2':
        if data['stock_type'] == 'stock':
            power_attributes = {
                'lens_type': data.get('lens_type', ''),
                'stock_type': data.get('stock_type', ''),
                'leftLensPowerStock': data.get('leftLensPowerStock', ''),
                'leftLensBCStock': data.get('leftLensBCStock', ''),
                'leftLensDiaStock': data.get('leftLensDiaStock', ''),
                'leftLensCylinderStock': data.get('leftLensCylinderStock', ''),
                'leftLensAxisStock': data.get('leftLensAxisStock', ''),
                'rightLensPowerStock': data.get('rightLensPowerStock', ''),
                'rightLensBCStock': data.get('rightLensBCStock', ''),
                'rightLensDiaStock': data.get('rightLensDiaStock', ''),
                'rightLensCylinderStock': data.get('rightLensCylinderStock', ''),
                'rightLensAxisStock': data.get('rightLensAxisStock', ''),
            }
            print(power_attributes)
            return power_attributes
        else:
            power_attributes = {
                'lens_type': data.get('lens_type', ''),
                'stock_type': data.get('stock_type', ''),
                'leftLensPowerRx': data.get('leftLensPowerRx', ''),
                'leftLensBCRx': data.get('leftLensBCRx', ''),
                'leftLensDiaRx': data.get('leftLensDiaRx', ''),
                'leftLensCylinderRx': data.get('leftLensCylinderRx', ''),
                'leftLensAxisRx': data.get('leftLensAxisRx', ''),
                'rightLensPowerRx': data.get('rightLensPowerRx', ''),
                'rightLensBCRx': data.get('rightLensBCRx', ''),
                'rightLensDiaRx': data.get('rightLensDiaRx', ''),
                'rightLensCylinderRx': data.get('rightLensCylinderRx', ''),
                'rightLensAxisRx': data.get('rightLensAxisRx', ''),
            }
            print(power_attributes)
            return power_attributes

    elif data['product_category_id'] == '3':
        if data['lens_type'] == 'rx':
            power_attributes = {
                'lens_type': data.get('lens_type', ''),
                'lens_physicality': data.get('lens_physicality', ''),
                'lens_disposablility': data.get('lens_disposablility', ''),
                'cl_power': data.get('cl_power', ''),
                'cl_bc': data.get('cl_bc', ''),
                'cl_dia': data.get('cl_dia', ''),
                'cl_cylinder': data.get('cl_cylinder', ''),
                'cl_axis': data.get('cl_axis', '')
            }
            return power_attributes
        else:
            power_attributes = {
                'stock_type': data.get('ContactLensStockType', ''),
                'contact_lens_type': data.get('contact_lens_type', ''),
                'contact_lens_disposability': data.get('contact_lens_disposability', ''),
                'power': data.get('contactLensPower', ''),
                'bc': data.get('contactLensBC', ''),
                'dia': data.get('contactLensDia', ''),
                'cyl': data.get('contactLensCylinder', ''),
                'axis': data.get('contactLensAxis', '')
            }
            return power_attributes

    else:
        print('this is other product with no power attributes')
        power_attributes = {}
        return power_attributes

