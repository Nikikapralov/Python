class MyDictionary:
    
    __LOAD_FACTOR_LIMIT = 0.75
    __DEFAULT_CAPACITY = 4
    
    def __init__(self):
        self.__capacity = self.__DEFAULT_CAPACITY
        self.__keys = [[] for i in range(self.__capacity)]
        self.__values = [[] for i in range(self.__capacity)]

    @property
    def keys(self):
        return [item for current_list in self.__keys for item in current_list]

    @property
    def values(self):
        return [value for value_list in self.__values for value in value_list]

    def __setitem__(self, key, value):
        while self.__compute_load_factor() >= self.__LOAD_FACTOR_LIMIT:
            self.__extend_dict()

        index_hash = self.__hash_function(key)

        if self.__is_key_in_dict(index_hash, key):
            self.__set_value_to_an_existing_key(index_hash, key, value)
            return

        self.__set_value_to_a_new_key(index_hash, key, value)

    def __getitem__(self, key):
        index_hash = self.__hash_function(key)
        if self.__is_key_in_dict(index_hash, key):
            index_bucket = self.__get_index_bucket(index_hash, key)
            return self.__values[index_hash][index_bucket]
        raise KeyError('Key is not in dictionary!')

    def __len__(self):
        return len(self.keys)

    def __str__(self):
        key_values = zip(self.keys, self.values)
        result = '{' + ", ".join([f"{key}: {value}"
                                  if isinstance(key, int) else f"'{key}': {value}"
                                  for key, value in key_values]) + '}'
        return result

    def add(self, key, value):
        self.__setitem__(key, value)

    def pop(self, key, default=False):
        index_hash = self.__hash_function(key)
        if self.__is_key_in_dict(index_hash, key):
            index_bucket = self.__get_index_bucket(index_hash, key)
            result = self.__values[index_hash][index_bucket]
            self.__keys[index_hash].remove(self.__keys[index_hash][index_bucket])
            self.__values[index_hash].remove(self.__values[index_hash][index_bucket])
            return result
        if default is False:
            raise KeyError('Key not in dictionary!')
        return default

    def clear(self):
        self.__capacity = self.__DEFAULT_CAPACITY
        self.__keys = [[] for i in range(self.__capacity)]
        self.__values = [[] for i in range(self.__capacity)]

    def items(self):
        zipped_key_value = zip(self.keys, self.values)
        return [item for item in zipped_key_value]

    def __hash_function(self, key):
        index_hash = hash(key) % self.__capacity
        return index_hash

    def __is_key_in_dict(self, index_hash, key):
        if key in self.__keys[index_hash]:
            return True
        return False

    def __get_index_bucket(self, index_hash, key):
        index_bucket = self.__keys[index_hash].index(key)
        return index_bucket

    def __extend_dict(self):
        self.__capacity *= 2
        new_keys = [[] for i in range(self.__capacity)]
        new_values = [[] for i in range(self.__capacity)]
        zipped_keys_values = zip(self.keys, self.values)
        self.__keys = new_keys
        self.__values = new_values
        for key, value in zipped_keys_values:
            index_hash = self.__hash_function(key)
            self.__set_value_to_a_new_key(index_hash, key, value)

    def __set_value_to_an_existing_key(self, index_hash, key, value):
        index_bucket = self.__get_index_bucket(index_hash, key)
        self.__values[index_hash][index_bucket] = value

    def __set_value_to_a_new_key(self, index_hash, key, value):
        self.__keys[index_hash].append(key)
        self.__values[index_hash].append(value)

    def __compute_load_factor(self):
        k = len(self.__keys)
        n = len([bucket for bucket in self.__keys if bucket])
        return n / k

    def get(self, key, return_value=None):
        try:
            index_hash = self.__hash_function(key)
            index_bucket = self.__get_index_bucket(index_hash, key)
            if self.__is_key_in_dict(index_hash, key):
                return self.__values[index_hash][index_bucket]
        except ValueError:
            return return_value

''''Dictionary using a hash table. This dictionary table is not a perfect hash table implementation but is 
more memory efficient as a result. The implementation is using separate chaining as an approach to 
collision handling. The load has been chosen as per the JAVA implementation.'''
