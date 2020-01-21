class TasksHandlerBase(object):
    @classmethod
    def add_task_to_queue(cls, task, task_args, task_kwargs, queue, *args, **kwargs):
        raise NotImplementedError
