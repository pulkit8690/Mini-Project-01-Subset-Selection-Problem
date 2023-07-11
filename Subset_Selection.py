import random as r

# Parameter Setting
Set = [-12, -3, -6, 7, 2, -2, 6, 3, 9, -7, -5, -8, 1, 11, -9, -4]
SetLB = 3
SetUB = 6
ResultList = set()    # Store Result List i.e. list of sets whose sum is zero
Iterations = 1000   # Number of Iterations

# Start Program
for i in range(Iterations):
    # Select set size randomly
    SetSize = r.randint(SetLB, SetUB)

    # Select number of elements from Set
    Chromosome = r.sample(list(Set), SetSize)
    Chromosome.sort()

    # Sum the number of elements in the Chromosome
    if sum(Chromosome) == 0:
        ResultList.add(tuple(Chromosome))

# Print all the sets whose sum is zero
for r in ResultList:
    print(r)

# Print total sets
print("\nTotal Sets: ", len(ResultList))
