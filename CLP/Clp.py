import random

class Individual:
    def __init__(self, gene_length, target_sum):
        self.geneLength = gene_length
        self.genes = [random.randint(0, 9) for _ in range(self.geneLength)]
        self.fitness = 0
        self.target_sum = target_sum

    def calc_fitness(self):
        gene_sum = sum(self.genes)
        self.fitness = -abs(self.target_sum - gene_sum)  


class Population:
    def __init__(self, size, gene_length, target_sum):
        self.popSize = size
        self.individuals = [Individual(gene_length, target_sum) for _ in range(self.popSize)]
        self.fittest = None
        self.gene_length = gene_length
        self.target_sum = target_sum

    def initialize_population(self):
        self.individuals = [Individual(self.gene_length, self.target_sum) for _ in range(self.popSize)]

    def calculate_fitness(self):
        for individual in self.individuals:
            individual.calc_fitness()
        self.get_fittest()

    def get_fittest(self):
        self.fittest = max(self.individuals, key=lambda ind: ind.fitness)
        return self.fittest

    def get_second_fittest(self):
        sorted_inds = sorted(self.individuals, key=lambda ind: ind.fitness, reverse=True)
        return sorted_inds[1]

    def get_least_fittest_index(self):
        min_index = min(range(len(self.individuals)), key=lambda i: self.individuals[i].fitness)
        return min_index


class SimpleDemoGA:
    def __init__(self, target_sum, gene_length):
        self.target_sum = target_sum
        self.gene_length = gene_length
        self.population = Population(size=10, gene_length=gene_length, target_sum=target_sum)
        self.fittest = None
        self.second_fittest = None
        self.generationCount = 0

    def selection(self):
        self.fittest = self.population.get_fittest()
        self.second_fittest = self.population.get_second_fittest()

    def crossover(self):
        cross_over_point = random.randint(0, self.gene_length - 1)
        for i in range(cross_over_point):
            self.fittest.genes[i], self.second_fittest.genes[i] = self.second_fittest.genes[i], self.fittest.genes[i]

    def mutation(self):
        mutation_point = random.randint(0, self.gene_length - 1)
        self.fittest.genes[mutation_point] = random.randint(0, 9)

        mutation_point = random.randint(0, self.gene_length - 1)
        self.second_fittest.genes[mutation_point] = random.randint(0, 9)

    def get_fittest_offspring(self):
        return self.fittest if self.fittest.fitness > self.second_fittest.fitness else self.second_fittest

    def add_fittest_offspring(self):
        self.fittest.calc_fitness()
        self.second_fittest.calc_fitness()
        least_fittest_index = self.population.get_least_fittest_index()
        self.population.individuals[least_fittest_index] = self.get_fittest_offspring()

    def run(self):
        self.population.initialize_population()
        self.population.calculate_fitness()

        print(f"Generation: {self.generationCount}, Best fitness: {self.population.fittest.fitness}")

        while self.population.fittest.fitness != 0:
            self.generationCount += 1

            self.selection()
            self.crossover()

            if random.random() < 0.7:
                self.mutation()

            self.add_fittest_offspring()
            self.population.calculate_fitness()

            print(f"Generation: {self.generationCount}, Best fitness: {self.population.fittest.fitness}")

        print(f"\nSolution found in generation {self.generationCount}")
        fittest_individual = self.population.get_fittest()
        print("Genes (numbers):", *fittest_individual.genes)
        print("Sum:", sum(fittest_individual.genes))


if __name__ == "__main__":
    # Get user input
    T = int(input("Enter target sum (T): "))
    k = int(input("Enter number of elements (k): "))

    demo = SimpleDemoGA(target_sum=T, gene_length=k)
    demo.run()
