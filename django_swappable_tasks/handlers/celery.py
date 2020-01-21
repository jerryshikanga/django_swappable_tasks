from django_swappable_tasks.handlers import TasksHandlerBase


class CeleryHandler(TasksHandlerBase):
    @classmethod
    def add_task_to_queue(cls, task, task_args, task_kwargs, queue, *args, **kwargs):
        return task.delay(*task_args, **task_kwargs)
