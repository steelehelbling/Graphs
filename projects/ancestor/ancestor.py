class Stack():
    def __init__(self):
        self.stack = []
    def push(self, value):
        self.stack.append(value)
    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None
    def size(self):
        return len(self.stack)


class Graph:
    def __init__(self):
        self.vertices = {}
    def add_vertex(self, vertex_id):
        if vertex_id not in self.vertices:
            self.vertices[vertex_id] = set()
    def add_edge(self, v1, v2):
        self.vertices[v1].add(v2)
    def get_neighbors(self, vertex_id):
        return self.vertices[vertex_id]


def create_graph(ancestors):
    new = Graph()
    for parent, child in ancestors:
        new.add_vertex(parent)
        new.add_vertex(child)
        new.add_edge(child, parent)
    return new

def earliest_ancestor(ancestors, starting_node):
    graph = create_graph(ancestors)

    to_visit = Stack()
    visited = set()
    to_visit.push([starting_node])
    array = []

    while to_visit.size() > 0:
        delete = to_visit.pop()
        last = delete[-1]

        if len(delete) > len(array):
            array = delete

        if last not in visited:
            visited.add(last)
            parents = graph.get_neighbors(last)

            for parent in parents:
                new_graph = delete+[parent]
                to_visit.push(new_graph)

    if starting_node == array[-1]:
        return -1
    else:
        return array[-1]