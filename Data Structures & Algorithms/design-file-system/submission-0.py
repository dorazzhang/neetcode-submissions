class FileSystem:

    def __init__(self):
        self.files = {}

    def createPath(self, path: str, value: int) -> bool:
        if path in self.files:
            return False
        parent = path.rsplit("/", 1)[0] # splits string from the right, only once on first occurrence of "/"

        if parent and parent not in self.files:
            return False
        
        self.files[path] = value
        return True

    def get(self, path: str) -> int:
        if path in self.files:
            return self.files[path]
        else:
            return -1


# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.createPath(path,value)
# param_2 = obj.get(path)
