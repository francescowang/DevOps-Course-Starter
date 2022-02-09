from flask import session

_DEFAULT_ITEMS = [
    { 'id': 1, 'status': 'Unfinished', 'title': 'Rest' },
    { 'id': 2, 'status': 'Unfinished', 'title': 'Eat' },
    { 'id': 3, 'status': 'Unfinished', 'title': 'Code' },
    { 'id': 4, 'status': 'Unfinished', 'title': 'Gym' },
]

def get_items():
    """
    Fetches all saved items from the session.

    Returns:
        list: The list of saved items.
    """
    return session.get('tasks', _DEFAULT_ITEMS.copy())


def get_item(id):
    """
    Fetches the saved item with the specified ID.

    Args:
        id: The ID of the item.

    Returns:
        item: The saved item, or None if no items match the specified ID.
    """
    tasks = get_items()
    return next((task for task in tasks if task['id'] == int(id)), None)


def add_item(title):
    """
    Adds a new item with the specified title to the session.

    Args:
        title: The title of the item.

    Returns:
        item: The saved item.
    """
    tasks = get_items()
    # Determine the ID for the item based on that of the previously added item
    id = tasks[-1]['id'] + 1 if tasks else 0
    task = { 'id': id, 'title': title, 'status': 'Unfinished' }
    # Add the item to the list
    tasks.append(task)
    session['tasks'] = tasks
    return task


def save_item(task):
    """
    Updates an existing item in the session. If no existing item matches the ID of the specified item, nothing is saved.

    Args:
        item: The item to save.
    """
    existing_tasks = get_items()
    updated_tasks = [task if task['id'] == existing_task['id'] else existing_task for existing_task in existing_tasks]
    session['tasks'] = updated_tasks # 'tasks' can be any name as long as it makes sense
    return task

def delete_item(task): # parameter # remove code and add an API
    tasks = get_items()
    tasks.remove(task) # argument
    session['tasks'] = tasks
    return tasks