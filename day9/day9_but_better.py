heights = [[int(c) for c in line.strip()] for line in open("inputs.txt", "r").readlines()]
N = len(heights)
M = len(heights[0])


def neighbours(y, x):
    surrounding_heights = [(y + 1, x), (y - 1, x), (y, x + 1), (y, x - 1)]
    return [(a, b) for a, b in surrounding_heights if 0 <= a < N and 0 <= b < M]


# Part 1
lowpoints = []
for y in range(N):
    for x in range(M):
        if all(heights[y][x] < heights[a][b] for a, b in neighbours(y, x)):
            lowpoints.append((y, x))
l=[heights[y][x] + 1 for y, x in lowpoints]
print("Part 1:", sum(l),l)

# Part 2
def get_basin(y, x):
    basin = {(y, x)}
    for a, b in neighbours(y, x):
        if heights[a][b] > heights[y][x] and heights[a][b] < 9:
            basin |= get_basin(a, b)
    return basin

basin_sizes = sorted([len(get_basin(y, x)) for y, x in lowpoints])
print("Part 2:", basin_sizes[-1] * basin_sizes[-2] * basin_sizes[-3])