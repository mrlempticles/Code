import heapq

class TaskManager:
    def __init__(self, tasks):
        # taskId -> (userId, priority)
        self.taskInfo = {}
        # heap stores (-priority, -taskId, userId)
        self.heap = []

        for userId, taskId, priority in tasks:
            self.taskInfo[taskId] = (userId, priority)
            heapq.heappush(self.heap, (-priority, -taskId, userId))

    def add(self, userId, taskId, priority):
        # Ensure uniqueness (in case reusing same taskId)
        self.taskInfo[taskId] = (userId, priority)
        heapq.heappush(self.heap, (-priority, -taskId, userId))

    def edit(self, taskId, newPriority):
        userId, _ = self.taskInfo[taskId]
        # Update task info and push new entry
        self.taskInfo[taskId] = (userId, newPriority)
        heapq.heappush(self.heap, (-newPriority, -taskId, userId))

    def rmv(self, taskId):
        # Just remove from map; heap entry will be skipped lazily
        if taskId in self.taskInfo:
            del self.taskInfo[taskId]

    def execTop(self):
        # Skip invalid/outdated heap entries
        while self.heap:
            negPriority, negTaskId, userId = heapq.heappop(self.heap)
            taskId = -negTaskId
            priority = -negPriority
            if (
                taskId in self.taskInfo
                and self.taskInfo[taskId][0] == userId
                and self.taskInfo[taskId][1] == priority
            ):
                del self.taskInfo[taskId]
                return userId
        return -1

# Your TaskManager object will be instantiated and called as such:
# obj = TaskManager(tasks)
# obj.add(userId,taskId,priority)
# obj.edit(taskId,newPriority)
# obj.rmv(taskId)
# param_4 = obj.execTop()