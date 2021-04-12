import pickle

from exceptions import ContactAlreadyExistsError, ContactNotExistsError


class DictCache:

    def __init__(self):
        self.dict_cache = {}

    def key_exits(self, key):
        return key in self.dict_cache.keys()

    def ensure_key_exists(self, key):
        if not self.key_exits(key):
            raise ContactNotExistsError

    def get(self, key):
        self.ensure_key_exists(key)
        return pickle.loads(self.dict_cache.get(key))

    def get_keys(self):
        return self.dict_cache.keys()

    def add(self, key, value):
        if self.key_exits(key):
            raise ContactAlreadyExistsError
        else:
            self.dict_cache[key] = pickle.dumps(value)

    def delete(self, key):
        self.ensure_key_exists(key)
        del self.dict_cache[key]

    def update(self, key, value):
        self.delete(key)
        self.add(key, value)
