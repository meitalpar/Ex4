import math

from src import DiGraph

epsilon = 0.00001


class Pokemons:
    def __init__(self, dict: dict):
        self.value = dict["value"]
        self.type = dict["type"]
        s = dict["pos"]
        self.pos = s.split(",")
        self.dis = None
        self.src = None
        self.dest = None

    def __repr__(self):
        return f'Pokemon: value: {self.value}, type: {self.type}, pos: x-{self.pos[0]}, y-{self.pos[1]}, src: {self.src}'

    def cal_edges(self, g: DiGraph):
        po = self
        for src in g.nodes.keys():
            # print(g.nodes[src].pos[0])
            for dest in g.edges[g.nodes[src].id]:
                # m = (g.nodes[src].pos[1] - g.nodes[dest].pos[1]) / (g.nodes[src].pos[0] - g.nodes[dest].pos[0])
                edgedis = math.sqrt(pow(g.nodes[src].pos.x - g.nodes[dest].pos.x, 2)
                                    + pow(g.nodes[src].pos.y - g.nodes[dest].pos.y, 2))
                pokdis1 = math.sqrt(pow(g.nodes[src].pos.x - float(po.pos[0]), 2) + pow(g.nodes[src].pos.y - float(po.pos[1]), 2))
                pokdis2 = math.sqrt(pow(g.nodes[dest].pos.x - float(po.pos[0]), 2) + pow(g.nodes[dest].pos.y - float(po.pos[1]), 2))
                pokdis = pokdis1 + pokdis2
                # po.pos[1] - g.nodes[src].pos[1]) == (m * (po.pos[0] - g.nodes[src].pos[1])) and
                if abs(edgedis - pokdis) <= epsilon:
                    if po.type < 0:
                        po.src = max(src, dest)
                        po.dest = min(src, dest)
                    elif po.type > 0:
                        po.dest = max(src, dest)
                        po.src = min(src, dest)
                    po.dis = math.sqrt(
                        pow(g.nodes[po.src].pos.x - float(po.pos[0]), 2) + pow(g.nodes[po.src].pos.y - float(po.pos[1]), 2))


class Agents:
    def __init__(self, dict: dict):
        self.id = dict["id"]
        self.value = dict["value"]
        self.src = dict["src"]
        self.dest = dict["dest"]
        self.speed = dict["speed"]
        s = dict["pos"]
        self.pos = s.split(",")

    def __repr__(self):
        return f'Agents: id: {self.id}, value: {self.value}, src: {self.src}, dest: {self.dest},' \
               f' speed: {self.speed}, pos: x-{self.pos.x}, y-{self.pos.y}'
