def get_power_attribute(data):
    if data['product_category_id'] == '2':
        if data['stock_type'] == 'stock':
            power_attributes = {
                'lens_type': data.get('lens_type', ''),
                'stock_type': data.get('stock_type', ''),
                'leftLensSphStock': data.get('leftLensSphStock', ''),
                'leftLensCylStock': data.get('leftLensCylStock', ''),
                'leftLensAxisStock': data.get('leftLensAxisStock', ''),
                'leftLensAddStock': data.get('leftLensAddStock', ''),
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
        power_attributes = {
            'stock_type': data.get('ContactLensStockType', ''),
            'contact_lens_type': data.get('lens_physicality', ''),
            'contact_lens_disposability': data.get('lens_disposablility', ''),
            'power': data.get('cl_power', ''),
            'bc': data.get('cl_bc', ''),
            'dia': data.get('cl_dia', ''),
            'cyl': data.get('cl_cylinder', ''),
            'axis': data.get('cl_axis', ''),
            'eye': data.get('cl_eye', '')
        }
        return power_attributes

    else:
        print('this is other product with no power attributes')
        power_attributes = {}
        return power_attributes


def get_eye_test_power_attribute(data):
    power_attributes = {
        'test_type': data.get('test_type', ''),
        'RightDvSph': data.get('RightDvSph', ''),
        'RightDvCyl': data.get('RightDvCyl', ''),
        'RightDvAxis': data.get('RightDvAxis', ''),
        'RightDvVision': data.get('RightDvVision', ''),
        'RightNvSph': data.get('RightNvSph', ''),
        'RightNvCyl': data.get('RightNvCyl', ''),
        'RightNvAxis': data.get('RightNvAxis', ''),
        'RightNvVision': data.get('RightNvVision', ''),
        'LeftDvSph': data.get('LeftDvSph', ''),
        'LeftDvCyl': data.get('LeftDvCyl', ''),
        'LeftDvAxis': data.get('LeftDvAxis', ''),
        'LeftDvVision': data.get('LeftDvVision', ''),
        'LeftNvSph': data.get('LeftNvSph', ''),
        'LeftNvCyl': data.get('LeftNvCyl', ''),
        'LeftNvAxis': data.get('LeftNvAxis', ''),
        'LeftNvVision': data.get('LeftNvVision', ''),
        'unifocal': data.get('unifocal', ''),
        'bifocal': data.get('bifocal', ''),
        'progressive': data.get('progressive', ''),
        'cr39': data.get('cr39', ''),
        'arc': data.get('arc', ''),
        'pdr': data.get('pdr', ''),
        'pdl': data.get('pdl', ''),
        'glass': data.get('glass', ''),
        'highIndex': data.get('highIndex', ''),
        'pg': data.get('pg', ''),
        'constant': data.get('constant', ''),
        'distance': data.get('distance', ''),
        'near': data.get('near', ''),

    }
    return power_attributes