class FileData:
    def __init__(self, data):
        self.profile_pic = data.get('profilePic', {}).get('doc', None)
        self.document1 = self.parse_documents(data.get('document1', {}))
        self.document2 = self.parse_documents(data.get('document2', {}))
        self.certificates = self.parse_certificates(data.get('certificates', {}))
        self.product_img = self.parse_product_images(data.get('productImages', {}))

    def parse_documents(self, doc_data):
        documents = []
        if doc_data:
            if isinstance(doc_data, list):
                for doc_item in doc_data:
                    doc = doc_item.get('doc', None)
                    if doc:
                        documents.append(doc)
            else:
                doc = doc_data.get('doc', None)
                if doc:
                    documents.append(doc)
        return documents

    def parse_certificates(self, cert_data):
        certificates = []
        if cert_data:
            if isinstance(cert_data, list):
                for cert_item in cert_data:
                    cert = cert_item.get('cert', None)
                    if cert:
                        certificates.append(cert)
            else:
                cert = cert_data.get('cert', None)
                if cert:
                    certificates.append(cert)
        return certificates

    def parse_product_images(self, image_data):
        product_images = []

        if image_data:
            if isinstance(image_data, list):
                for image_item in image_data:
                    image_url = image_item.get('prod_img', None)
                    if image_url:
                        product_images.append(image_url)
            else:
                image_url = image_data.get('prod_img', None)
                if image_url:
                    product_images.append(image_url)

        return product_images
