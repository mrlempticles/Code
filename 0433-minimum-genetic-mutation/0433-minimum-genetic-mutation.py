
class Solution(object):
    def minMutation(self, startGene, endGene, bank):
        if startGene == endGene:
            return 0

        bank = set(bank)

        if endGene not in bank:
            return -1

        queue = [(startGene, 0)]
        visited = set()
        visited.add(startGene)

        genes = ['A', 'C', 'G', 'T']

        while queue:
            gene, steps = queue.pop(0)

            for i in range(8):
                for char in genes:

                    newGene = gene[:i] + char + gene[i+1:]

                    if newGene == endGene:
                        return steps + 1

                    if newGene in bank and newGene not in visited:
                        visited.add(newGene)
                        queue.append((newGene, steps + 1))

        return -1
