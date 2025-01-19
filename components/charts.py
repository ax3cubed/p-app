import streamlit as st
import plotly.express as px
import pandas as pd

def render_charts(data, scores):
    """Render nested donut charts and task-type-specific charts for productivity visualization."""
    st.subheader("Visualization")
    
    # Bar chart for overall RTP
    df_scores = pd.DataFrame(scores)
    fig = px.bar(
        df_scores, 
        x="name", 
        y="rtp", 
        title="Real-Time Productivity Scores", 
        labels={"rtp": "RTP (%)", "name": "User"}
    )
    st.plotly_chart(fig)

    # Generate charts for each user
    for user_index, user in enumerate(data["users"]):
        st.subheader(f"{user['name']}'s Task Analysis")

        # Nested Donut Chart
        task_data = []
        for task in user["tasks"]:
            task_data.append({
                "Task Name": task["name"],
                "Task Type": task["type"],
                "Status": "Completed" if task["completed"] else "Incomplete"
            })
            if "subTasks" in task:
                for sub in task["subTasks"]:
                    task_data.append({
                        "Task Name": sub["name"],
                        "Task Type": task["type"],
                        "Status": "Completed" if sub["completed"] else "Incomplete"
                    })
        
        df_donut = pd.DataFrame(task_data)
        fig_donut = px.sunburst(
            df_donut,
            path=["Task Type", "Status", "Task Name"],
            title=f"{user['name']}'s Task Completion Breakdown (Nested Donut)",
            color="Status",
            color_discrete_map={"Completed": "green", "Incomplete": "red"}
        )
        st.plotly_chart(fig_donut)

        # Separate Charts for LOW, MID, and HIGH Tasks
        for task_type in ["LOW", "MID", "HIGH"]:
            filtered_tasks = [
                {"Task Name": task["name"], "Status": "Completed" if task["completed"] else "Incomplete"}
                for task in user["tasks"] if task["type"] == task_type
            ]
            # Include subtasks
            for task_index, task in enumerate(user["tasks"]):
                if task["type"] == task_type and "subTasks" in task:
                    filtered_tasks.extend([
                        {"Task Name": sub["name"], "Status": "Completed" if sub["completed"] else "Incomplete"}
                        for sub in task["subTasks"]
                    ])

            if filtered_tasks:
                df_filtered = pd.DataFrame(filtered_tasks)
                task_completion = {
                    "Task Type": task_type,
                    "Total Tasks": len(filtered_tasks),
                    "Completed": sum(1 for task in filtered_tasks if task["Status"] == "Completed"),
                }
                rtp = (task_completion["Completed"] / task_completion["Total Tasks"]) * 100

                # Show RTP score
                st.write(f"**{task_type} Tasks RTP:** {rtp:.2f}%")

                # Pie chart for task completion
                fig_task = px.pie(
                    df_filtered,
                    names="Status",
                    title=f"{task_type} Tasks Completion Breakdown",
                    color="Status",
                    color_discrete_map={"Completed": "green", "Incomplete": "red"}
                )
                st.plotly_chart(fig_task, key=f"fig_task_chart_{task_type}_{user_index}_{task_index}")
