class MemoryManager:
    def __init__(self):
        self.short_term = {}
        self.long_term = {}

    def store(self, key, value, long_term=False):
        if long_term:
            self.long_term[key] = value
        else:
            self.short_term[key] = value

    def retrieve(self, key, long_term=False):
        if long_term:
            return self.long_term.get(key)
        return self.short_term.get(key)
