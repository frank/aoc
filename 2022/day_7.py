from collections import deque


class Directory:
    def __init__(self, name: str, parent=None):
        self.name = name
        self.parent = parent if parent is not None else self
        self.children = {}  # children directories
        self.files = {}  # file names with sizes

    def __str__(self):
        names = []
        nav = self
        while nav.parent is not nav:
            names.append(nav.name)
            nav = nav.parent
        full_path = "/" + "/".join(names[::-1])
        return full_path + "/" if names else "/"

    def root(self):
        nav = self
        while nav.parent is not nav:
            nav = nav.parent
        return nav

    def cd(self, destination: str):
        if destination == "..":
            return self.parent
        elif destination == "/":
            return self.root()
        else:
            return self.children[destination]

    def ls(self, items: list[list[str]]):
        for md, name in items:
            if md == "dir":
                self.children[name] = Directory(name=name, parent=self)
            else:
                self.files[name] = int(md)
        return self

    @property
    def size(self):
        files_size = sum([file_size for file_size in self.files.values()])
        children_size = sum([child.size for child in self.children.values()])
        return files_size + children_size

    def all_dirs(self):
        stack = deque([self])
        while stack:
            node = stack.pop()
            yield node
            for child in node.children.values():
                stack.append(child)


def get_data() -> list[tuple[str]]:
    with open("inputs/day_7.txt", "r") as file:
        instructions = []
        lines = [line.rstrip("\n").split() for line in file.readlines()]
        parsing_ls = False
        ls_outputs = []
        for i in range(len(lines)):
            if lines[i][0] == "$":

                if parsing_ls:
                    instructions.append(("ls", ls_outputs))
                    parsing_ls = False
                    ls_outputs = []

                if lines[i][1] == "cd":
                    instructions.append(tuple(lines[i][1:]))

                if lines[i][1] == "ls":
                    parsing_ls = True

            elif lines[i][0] != "$" and parsing_ls:
                ls_outputs.append(tuple(lines[i]))

        if parsing_ls:
            instructions.append(("ls", ls_outputs))

        return instructions


def build_dirtree(instructions: list[tuple[str]]):
    assert instructions[0] == ("cd", "/")  # start from the root directory
    wd = Directory(name="/")
    for cmd, args in instructions:
        f = getattr(wd, cmd)
        wd = f(args)
    wd = wd.root()
    return wd


def part_one(wd: Directory):
    total_size = 0
    for d in wd.all_dirs():
        if d.size <= 100000:
            total_size += d.size
    print(total_size)


def part_two(wd: Directory):
    total_space = 70000000
    needed_space = 30000000
    used_space = wd.size
    to_delete = used_space + needed_space - total_space

    best = wd.size
    excess = total_space - needed_space
    for d in wd.all_dirs():
        if d.size >= to_delete:
            _excess = total_space - (used_space - d.size + needed_space)
            if _excess < excess:
                best = d.size
                excess = _excess

    print(best)


if __name__ == "__main__":
    data = get_data()
    dirtree = build_dirtree(instructions=data)
    part_one(dirtree)
    part_two(dirtree)
