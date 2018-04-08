from fuzzywuzzy import fuzz
import random
import string

class Agent:

    def __init__(self, length):
        self.string = ''.join(random.choice(string.ascii_letters) for _ in random(length))
        self.fitness = -1

    def __str__(self):
        return 'String: '+self.string


in_str = None
in_str_len = None
population = 20
generations = 1000


def initialize_agents(population, in_str_len):
    return [Agent(in_str_len) for _ in range(population)]


def evalution(agents):
    for agent in agents:
        agent.fitness = fuzz.ratio(agent.string, in_str)
    return agents


def selection(agents):
    agents = sorted(agents, key=lambda agent:agent.fitness, reverse=True)
    print('\n'.join(map(str, agents)))
    return agents[0:int(0.2*len(agents))]


def crossover(agents):
    offspring = []
    for _ in range((population-len(agents))/2):
        parent1 = random.choice(agents)
        parent2 = random.choice(agents)
        child1 = Agent(in_str_len)
        child2 = Agent(in_str_len)
        split = random.randint(0, in_str_len)
        child1.string = parent1.string[0:split]+parent2.string[split:in_str_len]
        child2.string = parent2.string[0:split]+parent1.string[split:in_str_len]
        offspring.append(child1)
        offspring.append(child2)

    return agents.extend(offspring)


def mutation(agents):
    for agent in agents:
        for indx, val in enumerate(agent.string):
            if random.uniform(0.0, 1.0) <= 0.1:
                agent.string = agent.string[0:indx]+random.choice(string.ascii_letters)+agent.string[indx+1, in_str_len]
    return agents


def genetic_algo():
    # initialize all agents
    agents = initialize_agents(population, in_str_len)
    for generation in range(generations):

        agents = evalution(agents)
        agents = selection(agents)
        agents = crossover(agents)
        agents = mutation(agents)

        if any( agent.fitness >=90 for agent in agents):
            print('TreshHold met')
            exit(0)

if __name__ == '__name__':
    print("hello")
    in_str = 'yergali'
    in_str_len = len(in_str)
    genetic_algo()