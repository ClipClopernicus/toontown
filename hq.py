from Toon import Task
import random
from functools import partial
from print_speed import print_medium as pm 
import time

class HQ:
    def __init__(self, player):
        self.player = player
        self.unique_tasks = [
            #Task(description="Defeat a Pencil Pusher",
                #task_name= "unique_task1",
                #reward_callback= partial(player.add_new_gag, "Plant Pot", "drop", increment_level=False),
                #reward_description= "New gag: Drop Plant pot!",
                #reward_type = "New Gag",
                #target_progress= 1,
                #task_type="type_name",
                #task_detail="Pencil Pusher"
                #),  
                  #for future new gags reference
            Task(description="Defeat a Micromanager",
                task_name= "unique_task2",
                reward_callback= partial(player.increase_max_task_capacity, 1),
                reward_description= "increase maximum task capacity by 1!",
                reward_type = "max_task_capacity",
                target_progress= 1,
                task_type="type_name",
                task_detail="Micromanager"
                ),
            
            Task(description="Earn 20 Jellybeans",
                task_name= "unique_task3",
                reward_callback= partial(player.increase_health, 1),
                reward_description= "increase max laffpoints by 1!",
                reward_type = "laffpoints",
                target_progress= 20,
                task_type="earn_jellybeans",
                task_detail="20" 
                ),
            
            Task(description="Defeat 4 Level 4+ cogs",
                task_name= "unique_task4",
                reward_callback= partial(player.increase_max_inventory_capacity, 10),
                reward_description= "increase max inventory capacity by 10!",
                reward_type = "max_inventory_capacity",
                target_progress= 1,
                task_type="level",
                task_detail="4"
            ),
        ]
        self.repeatable_tasks_tasks = [
            Task(description="Defeat an enemy",
                task_name= "Task1",
                reward_callback= partial(player.earn_jellybeans, 20),
                reward_description= "20 jellybeans!",
                reward_type = "jellybeans",
                target_progress= 1,
                task_type="level",
                task_detail="1" 
                ),
            Task(description="Defeat 4 Bossbots",
                task_name= "Task2",
                reward_callback= partial(player.increase_health, 4),
                reward_description= "increase max laffpoints by 4!",
                reward_type = "laffpoints",
                target_progress= 2,
                task_type="cog_class",
                task_detail="Bossbot"
                ),
            Task(description="Defeat a Lawbot",
                task_name= "Task1",
                reward_callback= partial(player.increase_health, 1),
                reward_description= "increase max laffpoints by 1!",
                reward_type = "laffpoints",
                target_progress= 1,
                task_type="cog_class",
                task_detail="Lawbot" 
                ),
            Task(description="Defeat 2 level 3 cogs",
                task_name= "Task1",
                reward_callback= partial(player.increase_health, 2),
                reward_description= "increase max laffpoints by 2!",
                reward_type = "laffpoints",
                target_progress= 2,
                task_type="level",
                task_detail="3" 
                ),
            Task(description="Defeat a Cashbot",
                task_name= "Task1",
                reward_callback= partial(player.increase_health, 1),
                reward_description= "increase max laffpoints by 1!",
                reward_type = "laffpoints",
                target_progress= 1,
                task_type="cog_class",
                task_detail="Cashbot" 
                ),
            
        ]    
            
    def get_random_tasks(self, number=6):
        available_unique_tasks = [task for task in self.unique_tasks 
                                  if task.task_name not in [t.task_name for t in self.player.current_tasks]
                                  and task.task_name not in self.player.completed_tasks]
        tasks_to_assign = []
        
        while available_unique_tasks and len(tasks_to_assign) < number:
            task = available_unique_tasks.pop()
            tasks_to_assign.append(task)
        
        repeatable_tasks_left = self.repeatable_tasks_tasks.copy()    
        while len(tasks_to_assign) < number and repeatable_tasks_left:
            task = random.choice(repeatable_tasks_left)
            tasks_to_assign.append(task)
            repeatable_tasks_left.remove(task)
            
        while len(tasks_to_assign) < number:    
            tasks_to_assign.append(random.choice(self.repeatable_tasks_tasks))
            
        return tasks_to_assign
    
    def assign_task_to_toon(self, player, task):
        self.player.add_task(task)
        
    def turn_in_tasks(self):
        tasks_to_remove = []
        for task in self.player.current_tasks:
            if task.status == "ready for turn-in":
                task.complete(self.player)
                self.player.tasks_completed += 1
                tasks_to_remove.append(task)
            if task.reward_type == "laffpoints": 
                pm(f"Your maximum laffpoints is now {self.player.max_health}!!")
            if task.reward_type =="max_task_capacity":
                pm(f" Your maximum task capacity is now {self.player.max_task_capacity}!!")
            if task.reward_type =="max_inventory_capacity":
                pm(f" Your maximum inventory capacity is now {self.player.max_inventory_capacity}!!")
            if task.reward_type =="jellybeans":
                pm(f" You earbed {task.description} and now have {self.player.jellybeans}")
            
            if task.task_name in [unique_task.task_name for unique_task in self.unique_tasks]:
                self.player.completed_tasks.add(task.task_name)
                print("Completed tasks:", self.player.completed_tasks)
            if self.player.completed_tasks == 5:
                self.player.add_new_gag("Plant Pot", "drop", increment_level=False)
                
        for task in tasks_to_remove:
            self.player.current_tasks.remove(task)
            self.player.task_counts -= 1
            



    