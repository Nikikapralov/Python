class Storage:
    def __init__(self):
        self.categories = []
        self.topics = []
        self.documents = []

    def __repr__(self):
        output = self.get_output()
        return output

    def get_output(self):
        result = ''
        last_index = len(self.documents) - 1
        for index in range(len(self.documents)):
            if index == last_index:
                result += self.documents[index].__repr__()
                break
            result += self.documents[index].__repr__() + '\n'
        return result

    def add_category(self, category):
        if category not in self.categories:
            self.categories.append(category)

    def add_topic(self, topic):
        if topic not in self.topics:
            self.topics.append(topic)

    def add_document(self, document):
        if document not in self.documents:
            self.documents.append(document)

    def get_category(self, category_id):
        category = [category for category in self.categories if category_id == category.id]
        return category[0]

    def get_topic(self, topic_id):
        topic = [topic for topic in self.topics if topic_id == topic.id]
        return topic[0]

    def get_document(self, document_id):
        document = [document for document in self.documents if document_id == document.id]
        return document[0]

    def edit_category(self, category_id, new_name):
        category = self.get_category(category_id)
        category.name = new_name

    def edit_topic(self, topic_id, new_name, new_storage_folder):
        topic = self.get_topic(topic_id)
        topic.topic = new_name
        topic.storage_folder = new_storage_folder

    def edit_document(self, document_id, new_file_name):
        document = self.get_document(document_id)
        document.file_name = new_file_name

    def delete_category(self, category_id):
        category = self.get_category(category_id)
        self.categories.remove(category)

    def delete_document(self, document_id):
        document = self.get_document(document_id)
        self.documents.remove(document)

    def delete_topic(self, topic_id):
        topic = self.get_topic(topic_id)
        self.topics.remove(topic)
