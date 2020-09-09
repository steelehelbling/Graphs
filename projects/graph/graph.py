"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        self.vertices[v1].add(v2)

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        to_visit = Queue()
        visited = set()
        to_visit.enqueue(starting_vertex)

        while to_visit.size() > 0:
            v = to_visit.dequeue()
            if v not in visited:
                print(v)
                visited.add(v)
                for neighbor in self.get_neighbors(v):
                    to_visit.enqueue(neighbor)

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        to_visit = Stack()
        visited = set()
        to_visit.push(starting_vertex)
        while to_visit.size() > 0:
            v = to_visit.pop()
            if v not in visited:
                print(v)
                visited.add(v)
                for neighbor in self.get_neighbors(v):
                    to_visit.push(neighbor)

    def dft_recursive(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        visited = set()

        def inner_recursive(starting_vertex):
            if starting_vertex not in visited:
                print(starting_vertex)
                visited.add(starting_vertex)
                for neighbor in self.get_neighbors(starting_vertex):
                    inner_recursive(neighbor)

        inner_recursive(starting_vertex)

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        to_visit = Queue()
        visited = set()
        path = [starting_vertex]
        to_visit.enqueue(path)
        while to_visit.size() > 0:
            remove = to_visit.dequeue()
            last = remove[-1]
            if last == destination_vertex:
                return remove
            if last not in visited:
                visited.add(last)
                for neighbor in self.get_neighbors(last):
                    to_visit.enqueue(remove+[neighbor])

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        to_visit = Stack()
        visited = set()
        to_visit.push([starting_vertex])
        while to_visit.size() > 0:
            remove = to_visit.pop()
            last = remove[-1]
            if last == destination_vertex:
                return remove
            if last not in visited:
                visited.add(last)
                for neighbor in self.get_neighbors(last):
                    to_visit.push(remove+[neighbor])

    def dfs_recursive(self, vertex, destination_vertex, path=[], visited=set()):
        if len(path) == 0:
            path.append(vertex)
        visited.add(vertex)
        if vertex == destination_vertex:
            return path
        for neighbor in self.get_neighbors(vertex):
            if neighbor not in visited:
                res = self.dfs_recursive(
                    neighbor, destination_vertex, path+[neighbor], visited)
                if res is not None:
                    return res


if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
