class FileSystem:
    # we have directories/paths
    # we then have files inside certain directories
    # these files have content in them

    # /a
    # /a/b
    # /a/b/c
    #/a/b/c -> d -> "hello"
    # need to know /b is in /a for ls

    # its like a tree where value = something if its a file

    # we have:
    # directory/file names AND content to store
    # absolute directory path -> children/whats in the directory
    # absolute file path -> content
    def __init__(self):
        self.directory = {} # given a directory (string), these are the folders/files in it (list[str])
        self.files = {} # given a file path (string), this is the content in it (string)
        self.directory["/"] = []

    def ls(self, path: str) -> List[str]:
        # return values in directory associated with path
        if path in self.files:
            return [path.rsplit("/", 1)[1]]
        else:
            # lexicographic order
            names = self.directory[path]
            names.sort()
            return names

    def mkdir(self, path: str) -> None:
        # check starting from root of directory exists
        # add key for each non existing directory
        subpathes = [p for p in path.split("/") if p]

        curr_path = ""
        for subpath in subpathes:
            prev_path = curr_path if curr_path else "/"
            curr_path += "/" + subpath
            if curr_path not in self.directory:
                self.directory[curr_path] = []
                if subpath not in self.directory[prev_path]:
                    self.directory[prev_path].append(subpath)


    def addContentToFile(self, filePath: str, content: str) -> None:
        # find filepath in files and modify value associated
        if filePath in self.files:
            self.files[filePath] += content
        else:
            parent_path, filename = filePath.rsplit("/", 1)
            parent_path = parent_path if parent_path else "/"
            self.mkdir(parent_path)
            if filename not in self.directory[parent_path]:
                self.directory[parent_path].append(filename)
            self.files[filePath] = content


    def readContentFromFile(self, filePath: str) -> str:
        # find filepath in files and return value associated
        return self.files[filePath]


# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.ls(path)
# obj.mkdir(path)
# obj.addContentToFile(filePath,content)
# param_4 = obj.readContentFromFile(filePath)
