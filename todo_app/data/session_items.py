from flask import session

_DEFAULT_ITEMS = [
    { 'id': 1, 'status': 'Not Started', 'title': 'List saved todo items' },
    { 'id': 2, 'status': 'Not Started', 'title': 'Allow new items to be added' }
]


def get_items():
    """
    Fetches all saved items from the session.

    Returns:
        list: The list of saved items.
    """
    return session.get('items', _DEFAULT_ITEMS.copy())


def get_item(id): # remove code and add an API
    """
    Fetches the saved item with the specified ID.

    Args:
        id: The ID of the item.

    Returns:
        item: The saved item, or None if no items match the specified ID.
    """
    items = get_items()
    return next((item for item in items if item['id'] == int(id)), None)


def add_item(title):  # remove code and add an API
    """
    Adds a new item with the specified title to the session.

    Args:
        title: The title of the item.

    Returns:
        item: The saved item.
    """
    items = get_items()

    # Determine the ID for the item based on that of the previously added item
    id = items[-1]['id'] + 1 if items else 0

    item = { 'id': id, 'title': title, 'status': 'Unfinished' }

    # Add the item to the list
    items.append(item)
    session['list_of_tasks'] = items

    return item


def save_item(task):  # remove code and add an API
    """
    Updates an existing item in the session. If no existing item matches the ID of the specified item, nothing is saved.

    Args:
        item: The item to save.
    """
    existing_tasks = get_items()
    updated_tasks = [task if task['id'] == existing_task['id'] else existing_task for existing_task in existing_tasks]

    session['list_of_tasks'] = updated_tasks # 'list_of_tasks' can be any name as long as it makes sense

    return task

def delete_item(task): # parameter  # remove code and add an API
    items = get_items()
    items.remove(task) # argument
    session['list_of_tasks'] = items
    return items