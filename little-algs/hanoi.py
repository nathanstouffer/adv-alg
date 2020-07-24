# a short program to solve towers of hanoi

# method to recursively solve towers of hanoi
def hanoi(puzzle, n, src, dst, tmp):
    if (n > 0):
        hanoi(puzzle, n-1, src, tmp, dst)
        puzzle[dst].append(puzzle[src].pop(-1))
        output_puzzle(puzzle)
        hanoi(puzzle, n-1, tmp, dst, src)


# method to output the state
def output_puzzle(puz):
    out = ""
    for p in range(0, 3):                   # iterate over each peg
        out += "\npeg " + str(p) + ":"      # begin output line
        for disk in puz[p]:                 # iterate over disks on this peg
            out += " " + str(disk)          # add disk to output
    print(out)

# method to initialize the puzzle
# as a list of lists
def init_puz(num_disks):
    puz = [[], [], []]                      # initialize puzzle as a list of 3 lists
    for d in range(0, num_disks):           # create disks (in reverse order)
        puz[0].append(d)                    # add disk to list
    puz[0].reverse()               # reverse the list
    return puz

num_disks = 5
puz = init_puz(num_disks)
hanoi(puz, num_disks, 0, 2, 1)
