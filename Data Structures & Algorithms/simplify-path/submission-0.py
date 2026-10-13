class Solution:
    def simplifyPath(self, path: str) -> str:
        # single period : curr directory
        # double period : previous directory
        # multiple slashes = one slash
        # sequence of periods are just a valid direcotry or file name

        # if you reach a .. you pop off of the stack
        # slashes are just delimeters you can split the abs path with

        path = path.split("/")
        print(path)

        stack = []

        for directory in path:
            if directory == '..' and stack:
                stack.pop()
            elif directory != '.' and directory != '..' and directory != '':
                stack.append(directory)
        
        return "/" + "/".join(stack)