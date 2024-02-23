# import Constraint

# class WhoKilledAgatha:
#     def __init__(self):
#         pass

#     def hate_constraint(self):
#         pass

#     def richer_constraint(self):
#         pass

from constraint import Problem, AllDifferentConstraint

# Create a problem instance
problem = Problem()

# Define the variables and their possible values
people = ['Agatha', 'Butler', 'Charles']
hates_values = [0, 1]
richer_values = [0, 1]

# Add variables to the problem
problem.addVariables(people, hates_values)
# problem.addVariables(people, richer_values)

# Add constraints based on the given information
problem.addConstraint(lambda a, b: a == 1 and b == 0, ('Agatha', 'Butler'))  # Agatha hates only the butler
problem.addConstraint(lambda b, a: a == 1 and b == 0, ('Butler', 'Agatha'))  # The butler hates everyone not richer than Agatha
problem.addConstraint(lambda a, c: a == 1 and c == 0, ('Agatha', 'Charles'))  # Agatha hates Charles
problem.addConstraint(lambda c, a: a == 1 and c == 0, ('Charles', 'Agatha'))  # Charles hates everyone Agatha hates
problem.addConstraint(lambda c, b: c == 0 and b == 1, ('Charles', 'Butler'))  # Charles doesn't hate the butler
problem.addConstraint(lambda b: b == 1, ('Butler',))  # The butler hates everyone not richer than Agatha
problem.addConstraint(lambda a, b: a == 1 and b == 1, ('Agatha', 'Agatha'))  # Agatha hates everyone

# Add an additional constraint to ensure that no one hates everyone
problem.addConstraint(AllDifferentConstraint(), people)

# Solve the problem
solutions = problem.getSolutions()

# Print the solution
if solutions:
    print("Solution found:")
    print(solutions[0])
else:
    print("No solution found.")
