import json
import math
from types import SimpleNamespace
import time

from PokemonsAndAgents import Pokemons, Agents, AgePok


class GameAlgo():
    def pokemons(self, client, g):
        pokemons = []
        getPokemons = client.get_pokemons()
        jsonPokemon = json.loads(getPokemons)
        d = {}
        for p in jsonPokemon["Pokemons"]:
            po = Pokemons(p["Pokemon"])
            x, y, z = po.pos[0], po.pos[1], po.pos[2]
            po.cal_edges(g)
            pokemons.append(po)
            if po.src is not None:
                if (po.src, po.dest) in d:
                    d[po.src, po.dest] += po.value
                else:
                    d[po.src, po.dest] = po.value
        pokemons.sort(key=lambda a: a.value, reverse=True)  # sort by value
        so = sorted(d.items(), key=lambda kv: kv[1], reverse=True)

        return so, pokemons

    def agents(self, client, my_scale):
        agents = []
        getAgent = client.get_agents()
        jsonAgent = json.loads(getAgent)
        for a in jsonAgent["Agents"]:
            agen = Agents(a["Agent"])
            x, y, z = agen.pos[0], agen.pos[1], agen.pos[2]
            agen.pos = SimpleNamespace(x=my_scale(float(x), x=True),
                                       y=my_scale(float(y), y=True, z=my_scale(float(z), z=True)))
            agents.append(agen)
        agents.sort(key=lambda a: a.speed, reverse=True)  # sort by speed
        return agents

    def choose_agent(self, agent: agents, pokemon: int, graph):
        dist, short = graph.shortest_path(agent.src, pokemon)
        t = dist / agent.speed
        return t, short


    def run(self, client, agents, agentPath, graph, so):

        for agent in agents:
            agent.work = True
            if agent.id in agentPath.age and len(
                            agentPath.age[agent.id]) > 0 and agent.src == agentPath.age[agent.id][0]:
                agentPath.age[agent.id].remove(agent.src)
            for p in so:
                tmin = float('inf')
                a = None
                path = []
                bo = False
                for agent2 in agents:
                    if bo:
                        break
                    if agent2.id in agentPath.age and agentPath.age[agent2.id] != {} and len(
                            agentPath.age[agent2.id]) > 0:
                        if p[0][1] in agentPath.age[agent2.id] and p[0][0] in agentPath.age[agent2.id]:
                            bo = True
                            break
                    else:
                        dist, short = self.choose_agent(agent2, p[0][0], graph)
                        if dist < tmin:
                            tmin = dist
                            a = agent2
                            path = short
                if bo:
                    bo = False
                    continue
                if a is not None:
                    agentPath.age[a.id] = path
                    agentPath.age[a.id].append(p[0][1])
            if agent.id in agentPath.age and agentPath.age[agent.id] != {} and len(
                    agentPath.age[agent.id]) > 0:
                next_node = agentPath.age[agent.id][0]
                client.choose_next_edge(
                    '{"agent_id":' + str(agent.id) + ', "next_node_id":' + str(next_node) + '}')
            # if agent.dest != -1:
    #             if agent.src != agentPath.age[agent.id][0]:
    #                 self.sleep(agent, agentPath)
    #
    # def sleep(self, agent, agentPath):
    #     time.sleep(0.015)
    #     if agent.src != agentPath.age[agent.id][0]:
    #         return self.sleep(agent, agentPath)

