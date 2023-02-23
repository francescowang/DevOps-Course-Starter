from todo_app.view_model import TaskViewModel
from todo_app.data.item_status import TaskStatus


def test_not_started_tasks():
    # Arrange
    items = [
        TaskStatus("Task 1", "Code", "NOT STARTED"),
        TaskStatus("Task 2", "Sleep", "DOING"),
        TaskStatus("Task 3", "Gym", "COMPLETED")            
    ]
    
    # Act
    view_model = TaskViewModel(items)
    not_started_tasks = view_model.not_started_items
    
    # Assert
    assert len(not_started_tasks) == 1
    item = not_started_tasks[0]
    assert item.status == "NOT STARTED"


def test_doing_tasks():
    # Arrange
    items = [
        TaskStatus("Task 1", "Code", "NOT STARTED"),
        TaskStatus("Task 2", "Sleep", "DOING"),
        TaskStatus("Task 3", "Gym", "COMPLETED")  
    ]
    
    # Act
    view_model = TaskViewModel(items)
    doing_tasks = view_model.doing_items
    
    # Assert
    assert len(doing_tasks) == 1
    item = doing_tasks[0]
    assert item.status == "DOING"


def test_completed_tasks():
    # Arrange
    items = [
        TaskStatus("Task 1", "Code", "NOT STARTED"),
        TaskStatus("Task 2", "Sleep", "DOING"),
        TaskStatus("Task 3", "Gym", "COMPLETED")  
    ]
    
    # Act
    view_model = TaskViewModel(items)
    completed_tasks = view_model.completed_items
    
    # Assert
    assert len(completed_tasks) == 1
    item = completed_tasks[0]
    assert item.status == "COMPLETED"
