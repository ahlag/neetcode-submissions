class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        # A tree with n nodes cannot have more than n - 1 edges.
        # If it has more, there must be a cycle.
        if len(edges) > (n - 1):
            return False

        # Build an adjacency list for the undirected graph.
        # For each edge u-v, add v to u's neighbors and u to v's neighbors.
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        # Track all nodes visited during DFS.
        visit = set()

        def dfs(node, par):
            # If we visit the same node again, we found a cycle.
            if node in visit:
                return False

            # Mark current node as visited.
            visit.add(node)

            # Visit all neighbors of the current node.
            for nei in adj[node]:
                # Skip the parent node because this is an undirected graph.
                # Example: if we came from 0 to 1, then 1 will also see 0 as a neighbor.
                if nei == par:
                    continue

                # If DFS from a neighbor finds a cycle, return False.
                if not dfs(nei, node):
                    return False

            # No cycle found from this path.
            return True

        # A valid tree must satisfy both:
        # 1. No cycle from DFS
        # 2. All n nodes are connected and visited
        return dfs(0, -1) and len(visit) == n