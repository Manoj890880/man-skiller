<template>
  <div class="container">
    <div v-for="(task, index) in tasks" :key="index" class="task-card">
      <h2>{{ task.title }}</h2>
      <p><strong>Description:</strong> {{ task.description }}</p>
      <p><strong>Assigned To:</strong> {{ task.assignee }}</p>
      <p><strong>Due Date:</strong> {{ task.dueDate }}</p>
      <div class="status-badge" :class="getStatusClass(task.status)">
        {{ task.status }}
      </div>

      <!-- Resource Section for each Task -->
      <div class="resource-card">
        <h3>Resources</h3>
        <ul>
          <li v-for="(resource, index) in task.resources" :key="index" class="resource-item">
            {{ resource }}
          </li>
        </ul>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "TaskView",
  data() {
    return {
      tasks: [
        {
          title: "Task 1",
          description:
            "This is a sample task description for Task 1. Replace this text with the actual description of the task.",
          assignee: "John Doe",
          dueDate: "2023-07-31",
          status: "In Progress",
          resources: ["Resource 1", "Resource 2", "Resource 3"],
        },
        {
          title: "Task 2",
          description:
            "This is a sample task description for Task 2. Replace this text with the actual description of the task.",
          assignee: "Jane Smith",
          dueDate: "2023-08-15",
          status: "Completed",
          resources: ["Resource A", "Resource B"],
        },
        // Add more tasks as needed
      ],
    };
  },
  methods: {
    getStatusClass(status) {
      return status === "In Progress" ? "status-in-progress" : "status-completed";
    },
  },
};
</script>


<style scoped>
body {
  font-family: 'Roboto', sans-serif;
  background-color: #f5f5f5;
  margin: 0;
  display: flex;
  justify-content: center;
  align-items: center;
  min-height: 100vh;
}

.container {
  max-width: 100%;
  width: 100%;
  padding: 20px;
}

.task-card {
  background-color: #d2e9ff;
  /* Light Blue */
  box-shadow: 0px 0px 20px rgba(0, 0, 0, 0.1);
  border-radius: 10px;
  padding: 20px;
  margin: 10px 0;
  width: 90%;
  margin: auto;
  margin-top: 10px;
  text-align: left;
}

.task-card h2 {
  font-size: 24px;
  color: #e74c3c;
  margin-bottom: 12px;
  font-weight: 700;
  text-align: center;
}

.task-card p {
  font-size: 16px;
  line-height: 1.6;
  color: #333;
  margin-bottom: 8px;
  text-align: justify;
}

.status-badge {
  
  display: inline-block;
  background-color: #f39c12;
  color: #fff;
  font-size: 12px;
  padding: 6px 12px;
  border-radius: 30px;
  text-transform: uppercase;
  letter-spacing: 1px;
  margin-top: 10px;
  
}

.resource-card {
  margin-top: 30px;
  background-color: #d7f5d5;
  box-shadow: 0px 0px 20px rgba(0, 0, 0, 0.1);
  border-radius: 10px;
  padding: 20px;
  margin-top: 10px;
}

.resource-card h3 {
  font-size: 18px;
  color: #1abc9c;
  margin-bottom: 10px;
  font-weight: 700;
  text-align: center;
}

.resource-card ul {
  list-style-type: none;
  padding: 0;
  margin: 0;
}

.resource-card li {
  font-size: 14px;
  color: #333;
  line-height: 1.6;
  margin-bottom: 5px;
  padding-left: 20px;
  position: relative;
  content: left;
}

.resource-card li::before {
  content: "▸";
  color: #e74c3c;
  position: absolute;
  left: 0;
}

.resource-item {
  text-align: left;
}</style>