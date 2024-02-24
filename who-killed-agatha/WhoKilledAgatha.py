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
richer_values = [0, 1, 'not_defined']

# Add variables to the problem
problem.addVariables(people, hates_values)
problem.addVariables([f"{person}_richer" for person in people], richer_values)

# Add constraints based on the given information
problem.addConstraint(lambda a, c: a == 1 and c == 0, ('Agatha', 'Charles'))  # Agatha hates Charles

