def get_power_attribute(data):
    if data['product_category_id'] == '2':
        if data['stock_type'] == 'stock':
            power_attributes = {
                'lens_type': data.get('lens_type', 'NA'),
                'stock_type': data.get('stock_type', 'NA'),
                'leftLensSphStock': data.get('leftLensSphStock', 'NA'),
                'leftLensCylStock': data.get('leftLensCylStock', 'NA'),
                'leftLensAxisStock': data.get('leftLensAxisStock', 'NA'),
                'leftLensAddStock': data.get('leftLensAddStock', 'NA'),
                'leftLensPdStock': data.get('leftLensPdStock', 'NA'),
                'rightLensSphStock': data.get('rightLensSphStock', 'NA'),
                'rightLensCylStock': data.get('rightLensCylStock', 'NA'),
                'rightLensAxisStock': data.get('rightLensAxisStock', 'NA'),
                'rightLensAddStock': data.get('rightLensAddStock', 'NA'),
                'rightLensPdStock': data.get('rightLensPdStock', 'NA'),
            }
            return power_attributes
        else:
            power_attributes = {
                'lens_type': data.get('lens_type', 'NA'),
                'stock_type': data.get('stock_type', 'NA'),
                'leftLensSphRx': data.get('leftLensSphRx', 'NA'),
                'leftLensCylRx': data.get('leftLensCylRx', 'NA'),
                'leftLensAxisRx': data.get('leftLensAxisRx', 'NA'),
                'leftLensAddRx': data.get('leftLensAddRx', 'NA'),
                'leftLensPdRx': data.get('leftLensPdRx', 'NA'),
                'rightLensSphRx': data.get('rightLensSphRx', 'NA'),
                'rightLensCylRx': data.get('rightLensCylRx', 'NA'),
                'rightLensAxisRx': data.get('rightLensAxisRx', 'NA'),
                'rightLensAddRx': data.get('rightLensAddRx', 'NA'),
                'rightLensPdRx': data.get('rightLensPdRx', 'NA'),
            }
            return power_attributes

    elif data['product_category_id'] == '3':
        power_attributes = {
            'stock_type': data.get('ContactLensStockType', 'NA'),
            'contact_lens_type': data.get('lens_physicality', 'NA'),
            'contact_lens_disposability': data.get('lens_disposablility', 'NA'),
            'power': data.get('cl_power', 'NA'),
            'bc': data.get('cl_bc', 'NA'),
            'dia': data.get('cl_dia', 'NA'),
            'cyl': data.get('cl_cylinder', 'NA'),
            'axis': data.get('cl_axis', 'NA'),
            'eye': data.get('cl_eye', 'NA')
        }
        return power_attributes

    else:
        print('this is other product with no power attributes')
        power_attributes = {}
        return power_attributes


def get_eye_test_power_attribute(data):
    power_attributes = {
        'test_type': data.get('test_type', 'NA'),
        'RightDvSph': data.get('RightDvSph', 'NA'),
        'RightDvCyl': data.get('RightDvCyl', 'NA'),
        'RightDvAxis': data.get('RightDvAxis', 'NA'),
        'RightDvVision': data.get('RightDvVision', 'NA'),
        'RightNvSph': data.get('RightNvSph', 'NA'),
        'RightNvCyl': data.get('RightNvCyl', 'NA'),
        'RightNvAxis': data.get('RightNvAxis', 'NA'),
        'RightNvVision': data.get('RightNvVision', 'NA'),
        'LeftDvSph': data.get('LeftDvSph', 'NA'),
        'LeftDvCyl': data.get('LeftDvCyl', 'NA'),
        'LeftDvAxis': data.get('LeftDvAxis', 'NA'),
        'LeftDvVision': data.get('LeftDvVision', 'NA'),
        'LeftNvSph': data.get('LeftNvSph', 'NA'),
        'LeftNvCyl': data.get('LeftNvCyl', 'NA'),
        'LeftNvAxis': data.get('LeftNvAxis', 'NA'),
        'LeftNvVision': data.get('LeftNvVision', 'NA'),
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