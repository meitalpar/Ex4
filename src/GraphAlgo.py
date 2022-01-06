import copy
import json
import math
import random
import sys
from typing import List

import numpy

from GraphInterface import GraphInterface
from DiGraph import DiGraph, Node
import matplotlib.pyplot as plt

from GraphAlgoInterface import GraphAlgoInterface
from PokemonsAndAgents import Agents, Pokemons


class GraphAlgo(GraphAlgoInterface):

    def __init__(self, graph=DiGraph()):
        self.graph = graph

    def get_graph(self) -> GraphInterface:
        return self.graph

    def load_from_json(self, file_name: str) -> bool:
        # with open(file_name, "r") as f:
        f = json.loads(file_name)
        dict = f
        for n in dict["Nodes"]:
            if "pos" in n:
                s = n["pos"]
                l = s.split(",")
                self.graph.add_node(int(n["id"]), (float(l[0]), float(l[1]), float(l[2])))
            else:
                s = None
                self.graph.add_node(int(n["id"]), s)
        for v in dict["Edges"]:
            self.graph.add_edge(v["src"], v["dest"], v["w"])
        return True

    def save_to_json(self, file_name: str) -> bool:
        toJson = {"Edges": [], "Nodes": []}
        for v in self.graph.nodes.keys():  # make random pos
            if not self.graph.nodes[v].pos:
                self.graph.nodes[v].pos = random.uniform(0, 100), random.uniform(0, 100), random.uniform(0, 100)
        for v in self.graph.nodes.keys():
            p = self.graph.nodes[v].pos
            pos = f'{p[0]},{p[1]},{p[2]}'
            toJson["Nodes"].append({"pos": pos, "id": self.graph.nodes[v].id})
            for u in self.graph.edges[self.graph.nodes[v].id]:
                toJson["Edges"].append(
                    {"src": self.graph.nodes[v].id, "w": self.graph.nodes[u].id, "dest": self.graph.edges[v][u]})

        with open(file_name + ".json", "w") as f:
            json.dump(toJson, fp=f, indent=2)
        return True

    def dijkstra(self, src):
        ng = self.graph
        self.maxValue(ng)
        ng.nodes[src].w = 0
        q = []
        for t in ng.nodes:
            q.append(ng.nodes[t])
        while len(q) != 0:
            x = self.listMin(q)
            q.remove(x)
            x = x.id
            for e in ng.all_out_edges_of_node(x):
                if ng.nodes[e].w > ng.nodes[x].w + ng.edges[x][e]:  # if des_weight > src_weight + edges_weight
                    ng.nodes[e].w = (ng.nodes[x].w + ng.edges[x][e])  # des_weight = src_weight + edges_weight
                    ng.nodes[e].tag = x  # des_tag = src

    def maxValue(self, ng: DiGraph):
        for t in ng.nodes:
            ng.nodes[t].tag = -1
            ng.nodes[t].w = sys.float_info.max

    def listMin(self, l: []) -> int:  # take the minimum from the list(and remove)
        templist = []
        n = l.pop()
        templist.append(n)
        min = n.w
        key = n
        while len(l) != 0:
            n = l.pop()
            templist.append(n)
            if n.w < min:
                min = n.w
                key = n
        while len(templist) != 0:
            l.append(templist.pop())
        return key

    def shortest_path(self, id1: int, id2: int) -> (float, list):
        path = []
        self.dijkstra(id1)
        path.append(id2)  # start from the last and add the 'father'
        x = id2
        distance = 0.0
        while x != id1:
            y = x
            x = self.graph.nodes[x].tag
            if x == -1:
                return float('inf'), []
            path.append(x)
            distance += self.graph.edges[x][y]
        path.reverse()  # reverse all (cus we started from the des)
        return distance, path

    def copygraph(self, node_list: list, ng: DiGraph) -> DiGraph:
        for i in node_list:
            ng.add_node(i)
        for i in node_list:
            for e in self.graph.all_out_edges_of_node(i):
                ng.add_edge(i, e, self.graph.edges[i][e])
        return ng

    # def shortest_path_for_tsp(self, id1: int, id2: int, ng: DiGraph) -> (float, list):
    #     path = []
    #     self.dijkstra(id1, ng)
    #     path.append(id2)
    #     x = id2
    #     distance = 0.0
    #     while x != id1:
    #         y = x
    #         x = ng.nodes[x].tag
    #         if x == -1:
    #             return float('inf'), []
    #         path.append(x)
    #         distance += ng.edges[x][y]
    #     path.reverse()
    #     return distance, path

    def TSP(self, node_lst: List[int]) -> (List[int], float):
        path = []
        finalpath = []
        finaldis = float('inf')
        for s in node_lst:
            dis = 0.0
            newlst = copy.deepcopy(node_lst)
            newlst.remove(s)
            path.clear()
            while newlst:
                maxdis = float('inf')
                firstdis = 0
                temppath = []
                for node in newlst:
                    short = self.shortest_path(s, node)
                    firstdis = short[0]
                    if firstdis < maxdis:
                        temppath.clear()
                        maxdis = firstdis
                        temppath.extend(short[1])
                if maxdis == float('inf'):
                    break
                dis += maxdis
                path.extend(temppath)
                s = temppath.pop()
                newlst.remove(s)
                if all(item in path for item in node_lst) and dis < finaldis:
                    finalpath.clear()
                    finalpath.extend(path)
                    finaldis = dis
                    break
        self.deleteDupes(finalpath)
        return finalpath, finaldis

    # def tsp_rec(self, i: int, node_lst: List[int], ans_lst: List[int], w: float, finaldes, finalpath):
    #     if all(item in ans_lst for item in node_lst):
    #         finaldes = w
    #         finalpath.extend(ans_lst)
    #         ans_lst.clear()
    #         w = 0.0
    #         return finalpath, finaldes
    #     for n in self.graph.all_out_edges_of_node(i):
    #
    #         if n in ans_lst:
    #             continue
    #         w += self.graph.edges[i][n]
    #         ans_lst.append(n)
    #         self.tsp_rec(n, node_lst, ans_lst, w, finaldes, finalpath)
    #
    #     return finalpath, finaldes

    def deleteDupes(self, l: list):
        size = len(l)
        for i in range(len(l)):
            if i == len(l) - 1:
                break
            if l[i] == l[i + 1]:
                l.pop(i)
        return l

    def centerPoint(self) -> (int, float):
        valtoint = []
        ans = -1
        for node in self.graph.nodes.values():  # get the value index
            valtoint.append(node.id)
        mat = self.to_matrix(valtoint)
        N = self.graph.v_size()
        disans = sys.float_info.max
        for i in range(N):
            maxx = 0
            for j in range(N):
                dis = mat[i][j]
                if dis == sys.float_info.max:  # if not connected
                    return None, float('inf')
                if dis > maxx:
                    maxx = dis
            if maxx < disans:
                disans = maxx
                ans = self.graph.nodes[valtoint[i]].id
        if ans == -1:
            return None, float('inf')
        return disans, ans

    def to_matrix(self, valtoint):
        N = self.graph.v_size()
        inf = sys.float_info.max
        mat = [[inf for i in range(N)] for i in range(N)]  # make all inf

        #  make 0
        for i in range(N):
            mat[i][i] = 0
        #  set the init weights
        for v in self.graph.nodes.keys():
            for u in self.graph.edges[self.graph.nodes[v].id]:
                x = valtoint.index(self.graph.nodes[v].id)  # src
                y = valtoint.index(self.graph.nodes[u].id)  # des
                mat[x][y] = self.graph.edges[v][u]

        for k in range(N):
            for i in range(N):
                for j in range(N):
                    mat[i][j] = min(mat[i][j], mat[i][k] + mat[k][j])
        return mat

    def plot_graph(self) -> None:
        ng = copy.deepcopy(self.graph)
        g = self.graph
        for v in g.nodes.keys():
            if not g.nodes[v].pos:
                g = ng
                g.nodes[v].pos = random.uniform(0, 100), random.uniform(0, 100), random.uniform(0, 100)
        for v in g.nodes.keys():
            x, y, z = g.nodes[v].pos
            plt.plot(x, y, markersize=10, marker='.', color='pink')

            for u in g.edges[g.nodes[v].id]:
                his_x, his_y, his_z = g.nodes[u].pos
                plt.annotate("", xy=(x, y), xytext=(his_x, his_y), arrowprops=dict(arrowstyle="<-"))
            plt.text(x, y, str(g.nodes[v].id), color="blue", fontsize=10)

        plt.show()

    def choose_agent(self, agents: list[Agents], pokemon: Pokemons):
        a = None
        tmin = float('inf')
        p = []
        for agent in agents:
            if len(agent.path) < 1:
                agent.work = False
            if agent.work or agent.dest != -1:
                continue
            short = self.shortest_path(agent.src, pokemon.src)
            dist = short[0]
            agedis = math.sqrt(pow(agent.pos.x - self.graph.nodes[agent.src].pos.x, 2) +
                               pow(self.graph.nodes[agent.src].pos.y - agent.pos.y, 2))
            dist += pokemon.dis - agedis
            t = dist / agent.speed
            if t < tmin:
                tmin = t
                a = agent
                p = short[1]
        if a is not None:
            a.path = p
            a.path.append(pokemon.dest)
            a.work = True
            print(a.id, ":", a.path)
        return a, p

