class BaseTask:
    def __init__(self, name):
        self.name = name
        self.prerequisites = []

class AdvancedTask(BaseTask):
    def __init__(self, name, difficulty):
        super().__init__(name)
        self.difficulty = difficulty


class TaskManager:
    def __init__(self, tasks):
        """
        tasks: List of BaseTask or AdvancedTask objects
        """
        self.tasks = tasks
        self.adjacency = {}
        self.build_adjacency()

    def build_adjacency(self):
        # Build an adjacency list from the tasks
        for task in self.tasks:
            self.adjacency[task.name] = []
        for task in self.tasks:
            for prereq in task.prerequisites:
                self.adjacency[prereq.name].append(task.name)

    def find_task_order(self):
        visited = set()
        order = []

        def dfs(task_name):
            if task_name in visited:
                return  # Already processed, skip
            visited.add(task_name)
            for neighbor in self.adjacency[task_name]:
                dfs(neighbor)
            order.append(task_name)

        for t in self.tasks:
            dfs(t.name)

        # Reverse the order to get tasks in a "prereq first" sequence
        return order[::-1]