from types import SimpleNamespace
from unittest import TestCase

from DiGraph import DiGraph
from PokemonsAndAgents import Pokemons, Agents, AgePok


class Test(TestCase):
    def test_pokemons(self):
        pokemons = []
        g = DiGraph()
        for n in range(4):
            g.add_node(n)
        g.add_edge(0, 1, 1)
        g.add_edge(1, 0, 1.1)
        g.add_edge(1, 2, 1.3)
        g.add_edge(2, 3, 1.1)
        g.add_edge(1, 3, 1.9)
        for n in g.nodes.keys():
            x, y, z = 0, 0, 0
            g.nodes[n].pos = SimpleNamespace(x=float(x), y=float(y), z=float(z))
        dic = {
            "Pokemons": [
                {
                    "Pokemon": {
                        "value": 5.0,
                        "type": -1,
                        "pos": "35.197656770719604,32.10191878639921,0.0"
                    }
                }
            ]
        }
        d = {}
        for p in dic["Pokemons"]:
            po = Pokemons(p["Pokemon"])
            po.cal_edges(g)
            pokemons.append(po)
        for p in pokemons:
            self.assertEqual(5.0, p.value)
            self.assertEqual(-1, p.type)
            self.assertEqual(35.197656770719604, float(p.pos[0]))
            self.assertEqual(32.10191878639921, float(p.pos[1]))
            self.assertEqual(None, p.src)

    def test_agents(self):
        agents = []
        g = DiGraph()
        for n in range(4):
            g.add_node(n)
        g.add_edge(0, 1, 1)
        g.add_edge(1, 0, 1.1)
        g.add_edge(1, 2, 1.3)
        g.add_edge(2, 3, 1.1)
        g.add_edge(1, 3, 1.9)
        for n in g.nodes.keys():
            x, y, z = 0, 0, 0
            g.nodes[n].pos = SimpleNamespace(x=float(x), y=float(y), z=float(z))
        dic = {
            "Agents": [
                {
                    "Agent":
                        {
                            "id": 0,
                            "value": 0.0,
                            "src": 0,
                            "dest": 1,
                            "speed": 1.0,
                            "pos": "35.18753053591606,32.10378225882353,0.0"
                        }
                }
            ]
        }
        for a in dic["Agents"]:
            agen = Agents(a["Agent"])
            x, y, z = agen.pos[0], agen.pos[1], agen.pos[2]
            agen.pos = SimpleNamespace(x=float(x), y=float(y), z=float(z))
            agents.append(agen)
            print(agents)
        for a in agents:
            self.assertEqual(0, a.id)
            self.assertEqual(0.0, a.value)
            self.assertEqual(0, a.src)
            self.assertEqual(1, a.dest)
            self.assertEqual(35.18753053591606, float(a.pos.x))
            self.assertEqual(32.10378225882353, float(a.pos.y))
            self.assertEqual(1.0, a.speed)

