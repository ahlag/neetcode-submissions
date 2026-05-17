class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:
        # Build adjacency list:
        # adj[u] = list of [neighbor, weight]
        adj = {}
        for i in range(n):
            adj[i] = []
            
        # s = source node, d = destination node, w = edge weight
        for s, d, w in edges:
            adj[s].append([d, w])

        # shortest will store the final shortest distance to each node
        shortest = {}

        # Min heap stores [current_distance, node]
        # Start from src with distance 0
        minHeap = [[0, src]]

        while minHeap:
            # Get the node with the smallest current distance
            w1, n1 = heapq.heappop(minHeap)

            # If we already finalized this node, skip it
            if n1 in shortest:
                continue

            # Record the shortest distance to this node
            shortest[n1] = w1

            # Try all outgoing edges from n1
            for n2, w2 in adj[n1]:
                # If neighbor not finalized yet,
                # push new possible distance into heap
                if n2 not in shortest:
                    heapq.heappush(minHeap, [w1 + w2, n2])

        # Any node not reached from src gets distance -1
        for i in range(n):
            if i not in shortest:
                shortest[i] = -1

        return shortest