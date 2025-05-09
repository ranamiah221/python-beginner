def is_safe(vertex, color, graph, colors):
    for neighbor in graph[vertex]:
        if colors[neighbor] == color:
            return False
    return True

def solve(vertex, graph, K, colors, N):
    if vertex == N:
        return True
    for c in range(1, K + 1):
        if is_safe(vertex, c, graph, colors):
            colors[vertex] = c
            if solve(vertex + 1, graph, K, colors, N):
                return True
            colors[vertex] = 0
    return False

def graph_coloring(filename):
    try:
        with open(filename, 'r') as file:
            lines = [line.strip() for line in file if line.strip()]
        if len(lines) == 0:
            print("Input file is empty.")
            return

        N, M, K = map(int, lines[0].split())
        if len(lines) - 1 != M:
            print(f"Expected {M} edges but found {len(lines)-1}.")
            return

        graph = [[] for _ in range(N)]
        for line in lines[1:]:
            u, v = map(int, line.split())
            graph[u].append(v)
            graph[v].append(u)

        colors = [0] * N
        if solve(0, graph, K, colors, N):
            print(f"Coloring Possible with {K} Colors")
            print("Color Assignment:", colors)
        else:
            print(f"Coloring Not Possible with {K} Colors")
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    except ValueError as ve:
        print(f"Value Error in input file: {ve}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Run the program
if __name__ == "__main__":
    input_file = "input.txt"  # Make sure this file exists and has valid input
    graph_coloring(input_file)
