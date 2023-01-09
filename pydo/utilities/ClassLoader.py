def get_task_class(task_name: str):
    if task_name:
        task = __import__(f"pydo.tasks.{task_name}", fromlist=[task_name])
        return getattr(task, task_name)


def get_task_config_class(task_name: str):
    if task_name:
        config_name = task_name + "Config"
        task = __import__(f"pydo.config.{config_name}", fromlist=[config_name])
        return getattr(task, config_name)
