from ortools.algorithms import pywrapknapsack_solver
from process_data import get_data


def main():
    # Create the solver.
    solver = pywrapknapsack_solver.KnapsackSolver(
        pywrapknapsack_solver.KnapsackSolver.
        KNAPSACK_MULTIDIMENSION_BRANCH_AND_BOUND_SOLVER, 'KnapsackExample')

    str_n = ['00050', '00100', '00200', '00500', '01000']
    problem_types = [
        '00Uncorrelated',
        '01WeaklyCorrelated',
        '02StronglyCorrelated',
        '03InverseStronglyCorrelated',
        '04AlmostStronglyCorrelated',
        '05SubsetSum',
        '06UncorrelatedWithSimilarWeights',
        '07SpannerUncorrelated',
        '08SpannerWeaklyCorrelated',
        '09SpannerStronglyCorrelated',
        '10MultipleStronglyCorrelated',
        '11ProfitCeiling',
        '12Circle'
    ]

    problems = []
    for t in problem_types:
        tmp = []
        for k in str_n:
            tmp.append(f"data/{t}/n{k}/R01000/s001.kp")
        problems.append(tmp)

    for problem in problems:
        for file in problem:
            values, weights, capacities = get_data(file)
            solver.Init(values, weights, capacities)
            solver.set_time_limit(300)
            computed_value = solver.Solve()
            packed_items = []
            packed_weights = []
            total_weight = 0
            individuals = []
            with open('result.txt', 'a') as writer:
                writer.write(f'Solution for {file}\n')
                writer.write(f'Total value = {computed_value}\n')
                for i in range(len(values)):
                    if solver.BestSolutionContains(i):
                        individuals.append(1)
                        packed_items.append(i)
                        packed_weights.append(weights[0][i])
                        total_weight += weights[0][i]
                    else:
                        individuals.append(0)
                writer.write(f'Total weight: {total_weight}\n')
                writer.write(f'Packed items: {packed_items}\n')
                writer.write(f'Packed_weights: {packed_weights}\n')
                writer.write(f'Best Ever Individual: {individuals}\n')


if __name__ == '__main__':
    main()
