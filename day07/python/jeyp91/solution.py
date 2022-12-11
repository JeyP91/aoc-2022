class Node:

    def __init__(self, name, filesystem_type, parent, size):
        self.name = name
        self.parent = parent
        self.size = size
        self.children = []
        self.filesystem_type = filesystem_type

    def name(self):
        return self.name

    def parent(self):
        return self.parent

    def add_child(self, child):
        self.children.append(child)

    def get_size(self):
        size = self.size
        for child in self.children:
            size += child.get_size()
        return size

    def get_children(self):
        return self.children

    def get_child(self, name):
        for child in self.children:
            if child.name == name:
                return child
        return None

    def collect_small_folders(self, threshold, small_folder_collector):
        if self.filesystem_type == "dir" and self.get_size() <= threshold:
            small_folder_collector.append(self.get_size())
        for child in self.children:
            child.collect_small_folders(threshold, small_folder_collector)

    def find_delete_folder(self, threshold, delete_collector):
        if self.filesystem_type == "dir" and self.get_size() >= threshold and (delete_collector == 0 or delete_collector > self.get_size()):
            delete_collector = self.get_size()
        for child in self.children:
            delete_collector = child.find_delete_folder(threshold, delete_collector)
        return delete_collector


def create_filesystem(input_string):
    commands = input_string.split("\n")
    root = Node(name="/", filesystem_type="dir", parent=None, size=0)
    current_node = root
    position = 1
    while position < len(commands):
        if commands[position][0] == "$":
            current_command = commands[position][2:]
            if current_command[:2] == "cd":
                if commands[position][5:] == "..":
                    current_node = current_node.parent
                else:
                    current_node = current_node.get_child(commands[position][5:])
                position += 1
            if current_command[:2] == "ls":
                position += 1
                while position < len(commands) and commands[position][0] != "$":
                    command = commands[position].split(" ")
                    if command[0] == "dir":
                        new_child = Node(name=command[1], filesystem_type="dir", parent=current_node, size=0)
                        current_node.add_child(new_child)
                    else:
                        new_child = Node(name=command[1], filesystem_type="file", parent=current_node, size=int(command[0]))
                        current_node.add_child(new_child)
                    position += 1
    return root


def part_1(root):
    small_folder_collector = []
    root.collect_small_folders(100000, small_folder_collector)
    return sum(small_folder_collector)


def part_2(root):
    filesystem_size = root.get_size()
    free_space = 70000000 - filesystem_size
    min_delete_folder = 30000000 - free_space
    delete_collector = 0
    delete_collector = root.find_delete_folder(min_delete_folder, delete_collector)
    return delete_collector


def main():
    # Read the input file and parse the initial configuration and the movements
    with open('input.txt') as input_file:
        # Parse the initial configuration of the stacks
        input_string = input_file.read()
    filesystem = create_filesystem(input_string)

    print("Solution day 7, part 1: ", part_1(filesystem))
    print("Solution day 7, part 2: ", part_2(filesystem))


main()
