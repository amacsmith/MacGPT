from .base_agent import BaseAgent
import asyncio

class TaskAgent(BaseAgent):
    def __init__(self):
        self.tasks = {}

    async def process(self, content):
        task_name, action = content.split(':')
        if action == 'start':
            return await self.start_task(task_name)
        elif action == 'stop':
            return await self.stop_task(task_name)

    async def start_task(self, task_name):
        if task_name in self.tasks:
            return f"Task {task_name} is already running"
        self.tasks[task_name] = asyncio.create_task(self.run_task(task_name))
        return f"Started task {task_name}"

    async def stop_task(self, task_name):
        if task_name not in self.tasks:
            return f"Task {task_name} is not running"
        self.tasks[task_name].cancel()
        del self.tasks[task_name]
        return f"Stopped task {task_name}"

    async def run_task(self, task_name):
        while True:
            print(f"Running task {task_name}")
            await asyncio.sleep(60)  # Simulate a periodic task