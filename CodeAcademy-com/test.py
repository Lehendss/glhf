# ITERATIVE
#def walk_interative(steps):
#    for step in range(steps):
#        print(step)

#walk_interative(10)


# RECURSIVE
def walk_recursive(steps):
    if steps == 0:
        return
    walk_recursive(steps - 1)
    print(steps)

walk_recursive(8)