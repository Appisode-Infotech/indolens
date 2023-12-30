def get_power_attribute(data):
    if data['product_category_id'] == '2':
        if data['stock_type'] == 'stock':
            power_attributes = {
                'lens_type': data.get('lens_type', ''),
                'stock_type': data.get('stock_type', ''),
                'leftLensSphStock': data.get('leftLensPowerStock', ''),
                'leftLensCylStock': data.get('leftLensBCStock', ''),
                'leftLensAxisStock': data.get('leftLensDiaStock', ''),
                'leftLensAddStock': data.get('leftLensCylinderStock', ''),
                'leftLensPdStock': data.get('leftLensAxisStock', ''),
                'rightLensSphStock': data.get('rightLensSphStock', ''),
                'rightLensCylStock': data.get('rightLensCylStock', ''),
                'rightLensAxisStock': data.get('rightLensAxisStock', ''),
                'rightLensAddStock': data.get('rightLensAddStock', ''),
                'rightLensPdStock': data.get('rightLensPdStock', ''),
            }
            return power_attributes
        else:
            power_attributes = {
                'lens_type': data.get('lens_type', ''),
                'stock_type': data.get('stock_type', ''),
                'leftLensSphRx': data.get('leftLensSphRx', ''),
                'leftLensCylRx': data.get('leftLensCylRx', ''),
                'leftLensAxisRx': data.get('leftLensAxisRx', ''),
                'leftLensAddRx': data.get('leftLensAddRx', ''),
                'leftLensPdRx': data.get('leftLensPdRx', ''),
                'rightLensSphRx': data.get('rightLensSphRx', ''),
                'rightLensCylRx': data.get('rightLensCylRx', ''),
                'rightLensAxisRx': data.get('rightLensAxisRx', ''),
                'rightLensAddRx': data.get('rightLensAddRx', ''),
                'rightLensPdRx': data.get('rightLensPdRx', ''),
            }
            return power_attributes

    elif data['product_category_id'] == '3':
        if data['lens_type'] == 'stock':
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

