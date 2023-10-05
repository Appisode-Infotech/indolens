class FileData:
    def __init__(self, data):
        self.profile_pic = data.get('profilePic', {}).get('doc', None)
        self.document1 = self.parse_documents(data.get('document1', {}))
        self.document2 = self.parse_documents(data.get('document2', {}))

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
