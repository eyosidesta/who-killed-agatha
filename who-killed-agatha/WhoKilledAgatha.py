from constraint import Problem, AllDifferentConstraint

class AgathaSolver:
    def __init__(self):
        self.problem = Problem()

    def add_variables(self):
        people = ['Agatha', 'Butler', 'Charles']
        hates_values = [0, 1]
        richer_values = [0, 1, 'not_defined']

        # Adding variables to the problem
        self.problem.addVariables(people, hates_values)
        self.problem.addVariables([f"{person}_richer" for person in people], richer_values)

    def add_basic_constraints(self):
        # Adding basic constraints based on the given information
        self.problem.addConstraint(lambda a, c: a == 1 and c == 0, ('Agatha', 'Charles'))  # Agatha hates Charles
        self.problem.addConstraint(lambda c, a: a == 1 and c == 0, ('Charles', 'Agatha'))  # Charles hates everyone Agatha hates
        self.problem.addConstraint(lambda c, b: c == 0 and b == 1, ('Charles', 'Butler'))  # Charles doesn't hate the butler
        self.problem.addConstraint(lambda b: b == 1, ('Butler',))  # The butler hates everyone not richer than Agatha
        self.problem.addConstraint(lambda a_richer, b_richer: a_richer == 1 and b_richer == 0, ('Agatha_richer', 'Butler_richer'))  # Agatha is not richer than the butler
        self.problem.addConstraint(lambda a, b, c: a == 1 and c == 0 and b == 0, ('Agatha', 'Butler', 'Charles'))  # Agatha hates Charles and herself
        self.problem.addConstraint(AllDifferentConstraint(), ['Agatha', 'Butler', 'Charles'])  # No one hates everyone

    def add_solution_constraints(self):
        # Additional constraints for the solution
        self.problem.addConstraint(lambda a_richer, a: a_richer == 'not_defined' and a == 0, ('Agatha_richer', 'Agatha'))

    def solve(self):
        # Solve the problem
        solutions = self.problem.getSolutions()

        # Print the solution
        if solutions:
            print("Solution found:")
            print(solutions[0])
        else:
            print("No solution found.")

agatha_solver = AgathaSolver()
agatha_solver.add_variables()
agatha_solver.add_basic_constraints()
agatha_solver.add_solution_constraints()
agatha_solver.solve()
    