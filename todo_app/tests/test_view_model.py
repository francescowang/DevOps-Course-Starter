from todo_app.view_model import TaskViewModel
from todo_app.data.trello_items import TaskStatus


def test_not_started_tasks():
    # Arrange
    items = [
        TaskStatus("Task 1", "Code", "NOT STARTED"),
        TaskStatus("Task 2", "Sleep", "DOING"),
        TaskStatus("Task 3", "Gym", "COMPLETED")            
    ]

    view_model = TaskViewModel(items)
    
    # Act
    not_started_tasks = view_model.not_started_items

    # Assert
    assert len(view_model.not_started_items) == 1


def test_doing_tasks():
    items = [
        TaskStatus("Task 1", "Code", "NOT STARTED"),
        TaskStatus("Task 2", "Sleep", "DOING"),
        TaskStatus("Task 3", "Gym", "COMPLETED")  
    ]
    
    view_model = TaskViewModel(items)

    assert len(view_model.doing_items) == 1


def test_completed_tasks():
    items = [
        TaskStatus("Task 1", "Code", "NOT STARTED"),
        TaskStatus("Task 2", "Sleep", "DOING"),
        TaskStatus("Task 3", "Gym", "COMPLETED")  
    ]
    
    view_model = TaskViewModel(items)

    assert len(view_model.completed_items) == 1