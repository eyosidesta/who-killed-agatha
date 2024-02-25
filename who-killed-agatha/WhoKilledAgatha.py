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
        