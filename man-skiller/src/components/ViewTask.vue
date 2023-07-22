<template>
  <NavBar></NavBar>
  <div class="task-container">
    <h2>Tasks <button class="add-task-btn">Add Task</button></h2>
    
    <table class="task-table">
      <thead>
        <tr>
          <th>ID</th>
          <th>Name</th>
          <th>Status</th>
          <th>Assigned To</th>
          <th>Start Date</th>
          <th>End Date</th>
          <th>Action</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="task in tasks" :key="task._id">
          <td>{{ task._id }}</td>
          <td>{{ task.name }}</td>
          <td>{{ task.status }}</td>
          <td>{{ task.assigned_to }}</td>
          <td>{{ task.start_date }}</td>
          <td>{{ task.end_date }}</td>
          <td>
            <button class="action-btn view-btn" @click="viewTask(task._id)">View</button>
            <button class="action-btn edit-btn" @click="editTask(task._id)">Edit</button>
            <button class="action-btn delete-btn" @click="deleteTask(task._id)">Delete</button>
            <button class="action-btn view-resources-btn" @click="viewResources(task._id)">View Resources</button>
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
import NavBar from './NavBar.vue';

export default {
  name: 'TaskPage',
  components: {
    NavBar
  },
  data() {
    return {
      tasks: [
        { _id: '1', name: 'Task 1', status: 'In Progress', assigned_to: 'John Doe', start_date: '2023-07-20', end_date: '2023-07-25' },
        { _id: '2', name: 'Task 2', status: 'Completed', assigned_to: 'Jane Smith', start_date: '2023-07-15', end_date: '2023-07-30' },
        // Add more tasks here...
      ]
    };
  },
  methods: {
    viewTask(taskId) {
      // Add your view task logic here...
      console.log('View Task:', taskId);
    },
    editTask(taskId) {
      // Add your edit task logic here...
      console.log('Edit Task:', taskId);
    },
    deleteTask(taskId) {
      // Add your delete task logic here...
      console.log('Delete Task:', taskId);
    },
    viewResources(taskId) {
      // Add your view resources logic here...
      console.log('View Resources:', taskId);
    }
  }
};
</script>

<style>
h2{ 
    color: #2196F3;
}
/* General styles for the task container */
.task-container {
  margin: 20px;
  padding: 20px;
  border: 1px solid #ccc;
  border-radius: 5px;
  background-color: #1F2739;
}

/* Table styles */
.task-table {
  width: 100%;
  border-collapse: collapse;
  background-color: #fff;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
}

.task-table th,
.task-table td {
  padding: 12px;
  text-align: left;
  border-bottom: 1px solid #ccc;
}

/* Header row styles */
.task-table th {
  background-color: #f2f2f2;
  font-weight: bold;
}

/* Alternate row styles */
.task-table tbody tr:nth-child(odd) {
  background-color: #f8f8f8;
}

/* Hover effect for rows */
.task-table tbody tr:hover {
  background-color: #8e6363;
  cursor: pointer;
}

/* Status styles */
.task-table td:nth-child(3) {
  font-weight: bold;
}

/* Button styles */
.action-btn {
    text-align: center;
  padding: 8px 16px;
  color: #fff;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  transition: background-color 0.2s;
  text-transform: uppercase;
  font-weight: bold;
  margin-right: 20px;
}

/* Apply styles to specific buttons in the table */
.action-btn.view-btn {
  background-color: #4CAF50;
}

.action-btn.edit-btn {
  background-color: #2196F3;
}

.action-btn.delete-btn {
  background-color: #F44336;
}

.action-btn.view-resources-btn {
  background-color: #FFC107;
}

.action-btn:hover {
  background-color: #103936;
}

/* Flexbox styles for centering the content */
.add-task-btn {
  padding: 10px 20px;
  background-color: #007bff;
  color: #fff;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  font-size: 16px;
  transition: background-color 0.3s ease;
  gap: 100px;
  margin-left: 85%;
}

.add-task-btn:hover {
  background-color: #0056b3;
}

.add-task-btn:focus {
  outline: none;
}

</style>

