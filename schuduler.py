import asyncio
import random

class Server:
    def __init__(self, cpu_capacity, memory_capacity):
        self.cpu_capacity = cpu_capacity
        self.memory_capacity = memory_capacity
        self.tasks = []

    async def execute_task(self, task, speedup_factor=10):
        """
        模拟任务执行，包括资源占用和执行时间
        """
        if task.cpu_usage <= self.cpu_capacity and task.memory_usage <= self.memory_capacity:
            # 模拟任务执行时间
            await asyncio.sleep(task.execution_time/speedup_factor)
            # 释放资源
            self.cpu_capacity += task.cpu_usage
            self.memory_capacity += task.memory_usage
            print(f"Task {task.id} executed on server")
        else:
            print(f"Task {task.id} cannot be executed on server due to resource limitation")

    def add_task(self, task):
        """
        将任务加入到服务器的任务列表中
        """
        self.tasks.append(task)

    async def simulate_tasks(self):
        """
        模拟服务器执行任务的过程
        """
        while True:
            if self.tasks:
                task = self.tasks.pop(0)
                asyncio.create_task(self.execute_task(task))
            else:
                await asyncio.sleep(0.0001)

class Task:
    id_counter = 0

    def __init__(self, cpu_usage, memory_usage, execution_time):
        self.id = Task.id_counter
        Task.id_counter += 1
        self.cpu_usage = cpu_usage
        self.memory_usage = memory_usage
        self.execution_time = execution_time

async def main():
    server = Server(cpu_capacity=100, memory_capacity=1024)
    asyncio.create_task(server.simulate_tasks())

    for _ in range(10):
        # 模拟任务到达
        task = Task(cpu_usage=random.randint(10, 50),
                    memory_usage=random.randint(100, 200),
                    execution_time=random.randint(1, 5))
        server.add_task(task)
        await asyncio.sleep(random.uniform(0.5, 1.5)/10)
    await asyncio.sleep(10)

asyncio.run(main())
