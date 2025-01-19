from utils.constants import TASK_WEIGHTS

def calculate_rtp(user_data):
    """Calculate Real-Time Productivity (RTP) scores."""
    results = []
    for user in user_data["users"]:
        user_score = 0
        total_score = 0
        for task in user["tasks"]:
            weight = TASK_WEIGHTS[task["type"]]
            if "subTasks" in task:
                completed_subtasks = sum(1 for sub in task["subTasks"] if sub["completed"])
                total_subtasks = len(task["subTasks"])
                task_completion = completed_subtasks / total_subtasks if total_subtasks > 0 else 0
            else:
                task_completion = 1 if task["completed"] else 0

            user_score += weight * task_completion
            total_score += weight
        results.append({
            "name": user["name"],
            "total_tasks":len( user["tasks"]),
            "weight":TASK_WEIGHTS[task["type"]],
            "rtp": user_score,
            "rtp_percent": (user_score / total_score) * 100 if total_score > 0 else 0
        })
    return results
