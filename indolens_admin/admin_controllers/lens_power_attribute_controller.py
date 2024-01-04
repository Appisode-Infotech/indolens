def get_power_attribute(data):
    if data['categoryId'] == '2':
        power_attributes = {
            'vision_type': data.get('visionType', ''),
            'stock_type': data.get('stockType', ''),
            'index': data.get('index', '')
        }
        return power_attributes

    elif data['categoryId'] == '3':
        power_attributes = {
            'stock_type': data.get('ContactLensStockType', ''),
            'contact_lens_type': data.get('contact_lens_type', ''),
            'contact_lens_disposability': data.get('contact_lens_disposability', '')
        }
        return power_attributes
    else:
        power_attributes = {}
        return power_attributes
