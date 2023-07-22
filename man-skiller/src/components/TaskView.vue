<template>
  <h1>Task View Page</h1>
  <div class="task-container">
    <div v-for="task in tasks" :key="task.id" class="task">
      <h2>{{ task.name }}</h2>
      <div class="task-details">
        <div>
          <p class="task-label">Description:</p>
          <p class="task-info">{{ task.description }}</p>
        </div>
        <div>
          <p class="task-label">Status:</p>
          <p class="task-info">{{ task.status }}</p>
        </div>
        <div>
          <p class="task-label">Assigned To:</p>
          <p class="task-info">{{ task.assignedTo }}</p>
        </div>
        <div>
          <p class="task-label">Due Date:</p>
          <p class="task-info">{{ task.dueDate }}</p>
        </div>
      </div>
    </div>
  </div>
  <div class="resources">
    <h3>Resources:</h3>
    <ul>
      <li v-for="resource in resources" :key="resource.id">
        {{ resource.name }} - {{ resource.type }}
      </li>
    </ul>
  </div>
</template>

<script>
export default {
  name: "TaskView",
  data() {
    return {
      tasks: [
        {
          id: 1,
          name: "Task 1",
          description: "This is task 1",
          status: "In Progress",
          assignedTo: "John Doe",
          dueDate: "2023-08-15",
          resources: [
            { id: 1, name: "Resource 1", type: "Type A" },
            { id: 2, name: "Resource 2", type: "Type B" },
            // Add more resources for task 1 as needed
          ],
        },
        {
          id: 2,
          name: "Task 2",
          description: "This is task 2",
          status: "Completed",
          assignedTo: "Jane Smith",
          dueDate: "2023-07-30",

        },
        // Add more tasks as needed
      ],
      resources: [
        { id: 3, name: "Resource 3", type: "Type C" },
        { id: 4, name: "Resource 4", type: "Type D" },
        // Add more resources for task 2 as needed
      ],
    };
  },
};
</script>


<style>
  /* Task Card Styles */
  .task-container {
    display: flex;
    flex-wrap: wrap;
    justify-content: space-between;
  }

  .task {
    width: 320px;
    background-color: #fff;
    border-radius: 10px;
    padding: 20px;
    margin-bottom: 20px;
    box-shadow: 0 5px 15px rgba(0, 0, 0, 0.1);
    transition: transform 0.2s;
  }

  .task:hover {
    transform: translateY(-5px);
  }

  .task-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 15px;
  }

  .task-status {
    padding: 5px 10px;
    font-size: 14px;
    font-weight: bold;
    color: #fff;
    border-radius: 5px;
    background-color: #29AAE1;
  }

  .task h2 {
    font-size: 20px;
    color: #555;
    margin: 0;
  }

  .task-body {
    line-height: 1.5;
  }

  .task-label {
    font-size: 14px;
    font-weight: bold;
    color: #666;
    margin-top: 10px;
  }

  .task-info {
    font-size: 16px;
    color: #444;
    margin: 0;
  }
  .task-footer {
    display: flex;
    justify-content: flex-end;
    margin-top: 15px;
  }

  .task-button {
    padding: 8px 16px;
    border-radius: 5px;
    font-size: 14px;
    text-decoration: none;
    background-color: #29AAE1;
    color: #fff;
    transition: background-color 0.3s;
  }

  .task-button:hover {
    background-color: #2188A6;
  }
</style>


