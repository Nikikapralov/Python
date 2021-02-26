class Section:
    def __init__(self, name):
        self.name = name
        self.tasks = []

    def add_task(self, task):
        if task not in self.tasks:
            self.tasks.append(task)
            return f'Task {task.details()} is added to the section'
        else:
            return f'Task is already in the section {self.name}'

    def complete_task(self, task_name):
        for task_object in self.tasks:
            if task_object.name == task_name:
                task_object.completed = True
                return f'Completed task {task_name}'
        return f'Could not find task with name {task_name}'

    def clean_section(self):
        removed_tasks = []
        for task_object in self.tasks:
            if task_object.completed:
                self.tasks.remove(task_object)
                removed_tasks.append(task_object)
        return f'Cleared {len(removed_tasks)} tasks.'

    def view_section(self):
        data_1 = f'Section {self.name}:\n'
        data_2 = ''
        for section_object in self.tasks:
            data_2 += f'{section_object.details()}\n'
        result = data_1 + data_2
        return result
