graph = {
    'Malioboro': ['Tugu', 'Kraton'],
    'Tugu': ['Malioboro', 'Prambanan'],
    'Kraton': ['Malioboro', 'Alun-Alun', 'Tamansari'],
    'Alun-Alun': ['Kraton', 'Tamansari'],
    'Tamansari': ['Alun-Alun', 'Tebing Breksi'],
    'Prambanan': ['Tugu', 'Tebing Breksi'],
    'Tebing Breksi': []
}

heuristics = {
    'Malioboro': 15,
    'Tugu': 13,
    'Kraton': 10,
    'Alun-Alun': 9,
    'Tamansari': 6,
    'Prambanan': 7,
    'Tebing Breksi': 0
}

def greedy_bfs(start, goal):
    from queue import PriorityQueue
    visited = set()
    pq = PriorityQueue()
    pq.put((heuristics[start], start, [start]))
    
    while not pq.empty():
        (h, current, path) = pq.get()
        if current == goal:
            return path
        visited.add(current)
        for neighbor in graph[current]:
            if neighbor not in visited:
                pq.put((heuristics[neighbor], neighbor, path + [neighbor]))
    return None

# Tes program
route = greedy_bfs('Malioboro', 'Tebing Breksi')
print("Rute terbaik:", route)
