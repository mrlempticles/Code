import heapq

class DSU:
    def __init__(self, n):
        self.parent = list(range(n+1))
        self.rank = [0] * (n+1)

    def find(self, x):
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, a, b):
        ra, rb = self.find(a), self.find(b)
        if ra != rb:
            if self.rank[ra] < self.rank[rb]:
                ra, rb = rb, ra
            self.parent[rb] = ra
            if self.rank[ra] == self.rank[rb]:
                self.rank[ra] += 1


class Solution:
    def processQueries(self, c, connections, queries):
        dsu = DSU(c)

        # Build connected components
        for u, v in connections:
            dsu.union(u, v)

        # Group nodes by component
        comp_nodes = {}
        for node in range(1, c + 1):
            root = dsu.find(node)
            if root not in comp_nodes:
                comp_nodes[root] = []
            comp_nodes[root].append(node)

        # Prepare heaps
        heaps = {}
        for root, nodes in comp_nodes.items():
            heapq.heapify(nodes)
            heaps[root] = nodes

        online = [True] * (c + 1)
        result = []

        # Process queries
        for t, x in queries:
            if t == 1:  
                if online[x]:
                    result.append(x)
                    continue

                root = dsu.find(x)
                heap = heaps[root]

                # Remove offline nodes (lazy deletion)
                while heap and not online[heap[0]]:
                    heapq.heappop(heap)

                result.append(heap[0] if heap else -1)

            else:  
                online[x] = False

        return result
