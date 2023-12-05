def get_power_attribute(data):
    if data['categoryId'] == '2':
        power_attributes = {
            'vision_type': data.get('visionType', ''),
            'stock_type': data.get('stockType', '')
        }
        print(power_attributes)
        return power_attributes

    elif data['categoryId'] == '3':
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