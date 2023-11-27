def get_power_attribute(data):
    if data['categoryId'] == '1':
        if data['visionType'] == 'rx':
            power_attributes = {
                'vision_type': data.get('visionType', ''),
                'index': data.get('index', ''),
                'sph': data.get('sph', ''),
                'cyl': data.get('cyl', ''),
                'axis': data.get('axis', ''),
                'add': data.get('add', '')
            }
        else:
            power_attributes = {
                'vision_type': data.get('visionType', ''),
                'index': data.get('Index', ''),
                'sph': data.get('Spherical', ''),
                'cyl': data.get('Cylindrical', ''),
                'axis': data.get('Axis', ''),
                'add': data.get('Add', '')
            }
        print(power_attributes)
        return power_attributes

    elif data['categoryId'] == '2':
        print('this is contact lesn')
        power_attributes = {
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