from project.category import Category
from project.document import Document
from project.topic import Topic


class Storage:
    def __init__(self):
        self.categories: list[Category] = []
        self.topics: list[Topic] = []
        self.documents: list[Document] = []

    def add_category(self, category: Category):
        self.add_object(category, self.categories)

    def add_topic(self, topic: Topic):
        self.add_object(topic, self.topics)

    def add_document(self, document: Document):
        self.add_object(document, self.documents)

    def edit_category(self, category_id: int, new_name: str):
        self.edit_object(category_id, self.categories, new_name)

    def edit_topic(self, topic_id: int, new_topic: str, new_storage_folder: str):
        self.edit_object(topic_id, self.topics, new_topic, new_storage_folder)

    def edit_document(self, document_id: int, new_name: str):
        self.edit_object(document_id, self.documents, new_name)

    def delete_category(self, category_id: int):
        self.delete_object(category_id, self.categories)

    def delete_topic(self, topic_id: int):
        self.delete_object(topic_id, self.topics)

    def delete_document(self, document_id: int):
        self.delete_object(document_id, self.documents)

    def get_document(self, doc_id: int):
        return next((d for d in self.documents if d.id == doc_id), None)

    def __repr__(self):
        return "\n".join(repr(d) for d in self.documents)

    @staticmethod
    def add_object(obj, collection: list):
        if obj not in collection:
            collection.append(obj)

    def edit_object(self, _id: int, collection: list, *args):
        curr_obj = self.find_object_by_id(_id, collection)
        if curr_obj:
            curr_obj.edit(args)

    def delete_object(self, _id: int, collection: list):
        obj_to_delete = self.find_object_by_id(_id, collection)
        if obj_to_delete:
            collection.remove(obj_to_delete)

    @staticmethod
    def find_object_by_id(_id: int, collection: list):
        return next((obj for obj in collection if obj.id == _id), None)