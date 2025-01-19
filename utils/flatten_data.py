def flatten_data(data):
    rows = []
    for user in data["users"]:
        user_name = user["name"]
        for task in user["tasks"]:
            task_name = task["name"]
            task_description = task["description"]
            task_start = task["startDateTime"]
            task_end = task["endDateTime"]
            task_completed = task["completed"]
            task_type = task["type"]
            
            # If the task has subtasks, add them as separate rows
            if "subTasks" in task:
                for subtask in task["subTasks"]:
                    rows.append({
                        "User": user_name,
                        "Task Name": task_name,
                        "Subtask Name": subtask["name"],
                        "Subtask Description": subtask["description"],
                        "Start DateTime": subtask["startDateTime"],
                        "End DateTime": subtask["endDateTime"],
                        "Completed": subtask["completed"],
                        "Type": subtask["type"]
                    })
            else:
                rows.append({
                    "User": user_name,
                    "Task Name": task_name,
                    "Subtask Name": None,
                    "Subtask Description": None,
                    "Start DateTime": task_start,
                    "End DateTime": task_end,
                    "Completed": task_completed,
                    "Type": task_type
                })
    return rows
