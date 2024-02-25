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

    