class Memory:
    def __init__(self):
        self.memory_store = []

    def store(self, data):
        self.memory_store.append(data)

    def retrieve(self, query: str):
        for entry in self.memory_store:
            if query.lower() in str(entry).lower():
                return entry
        return None
