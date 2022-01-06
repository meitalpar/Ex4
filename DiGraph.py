import ast

from GraphInterface import GraphInterface


class Node:
    def __init__(self, id, pos, tag=0, w=0.0):
        self.id = id
        self.pos = pos
        self.tag = tag
        self.w = w
        self.edgeout = 0  # for get_all_v
        self.edgein = 0  # for get_all_v

    def getid(self):
        return self.id

    def __repr__(self) -> str:
        return f"{self.id}: |edges_out| {self.edgeout} |edges in| {self.edgein}"


class DiGraph(GraphInterface):
    def __init__(self, mc=0):
        self.nodes = {}
        self.edges = {}
        self.edgesIn = {}
        self.mc = mc

    def v_size(self) -> int:
        return len(self.nodes)

    def e_size(self) -> int:
        sum = 0
        for i in self.edges:
            sum += len(self.edges[i])
        return sum

    def get_all_v(self) -> dict:
        # dic = {}
        # for v in self.nodes.keys():
        # p = self.nodes[v].pos
        # dic[self.nodes[v].id] = f"{self.nodes[v].id}, |edges_out| {len(self.all_out_edges_of_node(v))}, |edges in|: {len(self.all_in_edges_of_node(v))}"
        return self.nodes

    def all_in_edges_of_node(self, id1: int) -> dict:
        return self.edgesIn[id1]

    def all_out_edges_of_node(self, id1: int) -> dict:
        return self.edges[id1]

    def get_mc(self) -> int:
        return self.mc

    def add_edge(self, id1: int, id2: int, weight: float) -> bool:
        if not self.edges.get(id1) and not self.edgesIn.get(id2):
            pass
        if id1 in self.nodes and id2 in self.nodes:
            self.edges[id1][id2] = weight
            self.edgesIn[id2][id1] = weight
            self.mc += 1
            self.nodes[id1].edgeout += 1
            self.nodes[id2].edgein += 1
            return True
        return False

    def add_node(self, node_id: int, pos: tuple = None) -> bool:
        if node_id in self.nodes:
            pass
        else:
            self.nodes[node_id] = Node(node_id, pos)
            self.edges[node_id] = {}
            self.edgesIn[node_id] = {}
            self.mc += 1
            return True
        return False

    def remove_node(self, node_id: int) -> bool:
        if node_id not in self.nodes:
            pass
        else:
            self.nodes.pop(node_id)
            self.mc += 1
            return True
        return False

    def remove_edge(self, node_id1: int, node_id2: int) -> bool:
        if not self.edges.get(node_id1) and not self.edgesIn.get(node_id2):
            pass
        else:
            self.nodes[node_id1].edgeout -= 1
            self.nodes[node_id2].edgein -= 1
            self.edges[node_id1].pop(node_id2)
            self.edgesIn[node_id2].pop(node_id1)
            self.mc += 1
            return True
        return False

    def __repr__(self) -> str:
        return f"|V|={self.v_size()}, |E|={self.e_size()}"
