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
            x, y, z = po.pos[0], po.pos[1], po.pos[2]
            po.cal_edges(g)
            pokemons.append(po)

    def test_agents(self):
        self.fail()

    def test_age_pok(self):
        self.fail()
