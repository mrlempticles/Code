
class Solution(object):
    def loudAndRich(self, richer, quiet):
        n = len(quiet)

        # Build adjacency list
        graph = [[] for _ in range(n)]

        for a, b in richer:
            graph[b].append(a)

        ans = [-1] * n

        def dfs(person):
            if ans[person] != -1:
                return ans[person]

            # Initially, person is the quietest
            ans[person] = person

            for richer_person in graph[person]:
                candidate = dfs(richer_person)

                if quiet[candidate] < quiet[ans[person]]:
                    ans[person] = candidate

            return ans[person]

        for i in range(n):
            dfs(i)

        return ans
