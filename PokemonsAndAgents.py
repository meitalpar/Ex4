import math

import DiGraph

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
        self.edgeval = 0

    def __repr__(self):
        return f'Pokemon: value: {self.value}, type: {self.type}, pos: x-{self.pos[0]}, y-{self.pos[1]}, src: {self.src}'

    def cal_edges(self, g: DiGraph):
        po = self
        for src in g.nodes.keys():
            for dest in g.edges[g.nodes[src].id]:
                edgedis = math.sqrt(pow(g.nodes[src].pos.x - g.nodes[dest].pos.x, 2)  # Edge Distance
                                    + pow(g.nodes[src].pos.y - g.nodes[dest].pos.y, 2))
                pokdis1 = math.sqrt(  # Pokemon Distance to src
                    pow(g.nodes[src].pos.x - float(po.pos[0]), 2) + pow(g.nodes[src].pos.y - float(po.pos[1]), 2))
                pokdis2 = math.sqrt(  # Pokemon Distance to dest
                    pow(g.nodes[dest].pos.x - float(po.pos[0]), 2) + pow(g.nodes[dest].pos.y - float(po.pos[1]), 2))
                pokdis = pokdis1 + pokdis2  # Pokemon Distance
                if abs(edgedis - pokdis) <= epsilon:  # if equal
                    if po.type < 0:  # if down
                        po.src = max(src, dest)
                        po.dest = min(src, dest)
                    elif po.type > 0:  # if up
                        po.dest = max(src, dest)
                        po.src = min(src, dest)
                    po.dis = math.sqrt(
                        pow(g.nodes[po.src].pos.x - float(po.pos[0]), 2) + pow(g.nodes[po.src].pos.y - float(po.pos[1]),
                                                                               2))


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


class AgePok:
    def __init__(self):
        self.age = {}
        self.edgeval = tuple()  # Edge Value - all pokemons on the same edge
