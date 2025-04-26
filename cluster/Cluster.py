import random
import csv

all_points = [(random.randint(0, 19), random.randint(0, 19)) for _ in range(100)]
init_centers = [(random.randint(0, 19), random.randint(0, 19)) for _ in range(10)]

# Save data into the file
with open('data.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['type', 'x', 'y'])
    for pt in all_points:
        writer.writerow(['point', pt[0], pt[1]])
    for center in init_centers:
        writer.writerow(['center', center[0], center[1]])


def manhattan_distance(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def cluster_points(pts, centroids):
    assignment = {i: [] for i in range(len(centroids))}
    for pt in pts:
        dists = [manhattan_distance(pt, c) for c in centroids]
        closest = dists.index(min(dists))
        assignment[closest].append(pt)
    return assignment


def move_centers(grouped_pts):
    updated_centers = []
    for pts in grouped_pts.values():
        if pts:
            avg_x = round(sum(p[0] for p in pts) / len(pts))
            avg_y = round(sum(p[1] for p in pts) / len(pts))
            updated_centers.append((avg_x, avg_y))
        else:
            updated_centers.append((random.randint(0, 19), random.randint(0, 19)))
    return updated_centers


old_assignment = None
centers = init_centers.copy()

for _ in range(100):  
    new_assignment = cluster_points(all_points, centers)
    if new_assignment == old_assignment:
        break
    old_assignment = new_assignment
    centers = move_centers(new_assignment)


canvas = [[' ' for _ in range(20)] for _ in range(20)]


for group in new_assignment.values():
    for p in group:
        x, y = p
        canvas[y][x] = '.'

for c in centers:
    x, y = c
    canvas[y][x] = 'X'

for row in canvas:
    print(''.join(row))
