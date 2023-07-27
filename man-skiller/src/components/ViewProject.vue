<template>
    <H1>Project Details</H1>
    <div class="project-details">
        <h2 class="project-name">{{ project.name }}</h2>
        <div class="project-info">
            <div class="detail">
                <strong>Status:</strong> {{ project.status }}
            </div>
            <div class="detail">
                <strong>Manager:</strong> {{ project.manager_name }}
            </div>
            <div class="detail">
                <strong>Start Date:</strong> {{ project.s_date }}
            </div>
            <div class="detail">
                <strong>End Date:</strong> {{ project.e_date }}
            </div>
            <!-- Add other project details here -->
        </div>
        <div class="project-description">
            <h3>Description</h3>
            <p>{{ project.description }}</p>
        </div>

        <!-- Tasks Section -->
        <div class="tasks-section">
            <h3>Tasks</h3>
            <ul class="task-list">
                <li v-for="task in tasks" :key="task.id" class="task-item">
                    {{ task.name }} - {{ task.status }}
                </li>
            </ul>
        </div>

        <!-- Resources Section -->
        <div class="resources-section">
            <h3>Resources</h3>
            <ul class="resource-list">
                <li v-for="resource in resources" :key="resource.id" class="resource-item">
                    {{ resource.name }} - {{ resource.type }}
                </li>
            </ul>
        </div>


    </div>
</template>
  
<script>
import axios from 'axios';

export default {
    name: 'ViewProject',
    data() {
        return {
            project: {},
            tasks: [],
            resources: [],
        };
    },
    methods: {
        viewTasks() {
            // Add your view tasks logic here...
            console.log('View Tasks');
        },
        editProject() {
            // Add your edit project logic here...
            console.log('Edit Project');
        },
        deleteProject() {
            // Add your delete project logic here...
            console.log('Delete Project');
        }
    },
    async mounted() {
        try {
            const projectId = this.$route.params.id; // Get the project_id from the route parameter
            // console.log(projectId);
            // Fetch project details
            const projectResponse = await axios.get(`http://localhost:5000/projects/${projectId}`); // Replace with your project details API endpoint
            // console.log("Project Response:", projectResponse.data); 
            this.project = projectResponse.data;

            // Fetch tasks
              const tasksResponse = await axios.get(`http://localhost:5000/projects/${projectId}/tasks`); // Replace with your tasks API endpoint
              this.tasks = tasksResponse.data;
                // console.log(this.tasks);
            //   // Fetch resources
            const resourcePromises = this.tasks.map(async (task) => {
                console.log('Fetching resources for task:', task._id);
            const resourcesResponse = await axios.get(`http://localhost:5000/tasks/${task._id}/resources`);
            console.log(resourcesResponse.data);
            return resourcesResponse.data;
            });

        const resourcesArrays = await Promise.all(resourcePromises);

        // Flatten the array of resource arrays and assign it to this.resources
        this.resources = resourcesArrays.flat();
        
        const managerResponse = await axios.get(`http://localhost:5000/portfolio-managers/${this.project.manager_id}`);
        this.project.manager_name = managerResponse.data.name; // Add manager_name to the project object



        } catch (error) {
            console.error('Error fetching project data:', error);
        }


    },
};
</script>
  
<style>
/* Base styles for the project page */
.project-page {
    font-family: "Arial", sans-serif;
    max-width: 800px;
    margin: 0 auto;
    padding: 20px;
}

.project-name {
    font-size: 2em;
    color: #e14912;
    text-align: center;
    margin-bottom: 20px;
}

.project-info {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
    gap: 20px;
}

.detail {
    display: flex;
    align-items: center;
    padding: 15px 20px;
    background-color: #b3d4ff;
    border-radius: 8px;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    transition: transform 0.3s, box-shadow 0.3s;
    cursor: pointer;
    min-width: 200px;
}

.detail strong {
    color: #000000;
    margin-right: 10px;
}

/* Hover effect */
.detail:hover {
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
    transform: translateY(-4px);
}

/* Different box styles for each detail */
.detail:nth-child(2n) {
    background-color: #e6f0ff;
}

.detail:nth-child(3n) {
    background-color: #ffe6f0;
}

.detail:nth-child(4n) {
    background-color: #e6ffe6;
}

.detail:nth-child(5n) {
    background-color: #f0e6ff;
}

/* Responsive layout */
@media (max-width: 600px) {
    .project-info {
        flex-direction: column;
        align-items: center;
    }
}

/* Container styles */
.project-description {

    background-color: #b3d4ff;
    width: 90%;
    padding: 10px;
    border-radius: 10px;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    margin: auto;
    margin-top: 20px;
}

/* Heading styles */
.project-description h3 {
    color: #007bff;
    /* Blue color */
    font-size: 24px;
    margin-bottom: 10px;
    border-bottom: 2px solid #007bff;
    /* Blue color */
    padding-bottom: 8px;
}

/* Paragraph styles */
.project-description p {
    color: #444;
    font-size: 16px;
    line-height: 1.6;
}

/* Add a hover effect */
.project-description:hover {
    transform: translateY(-2px);
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
}

/* CSS */

/* Container styles */
.tasks-section {
    background-color: #96d6d7;
    border-radius: 10px;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    max-width: 90%;
    margin: 0 auto;
    padding: 10px;
    margin-top: 20px;
}

/* Section title styles */
.section-title {
    color: #b29898;
    font-size: 50px;
    font-weight: bold;
    margin-bottom: 15px;
    text-align: center;
}

/* Task item styles */
.task-item {
    background-color: rgb(196, 186, 196);
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 12px;
    border-bottom: 1px solid #9d6969;
    transition: transform 0.2s ease;
}

.task-item:last-child {
    border-bottom: none;
    /* Remove bottom border for the last task item */
}

/* Task info styles */
.task-info {
    flex: 1;
    display: flex;
    align-items: center;
}

/* Task name styles */
.task-name {
    color: #a38888;
    font-size: 25px;
    font-weight: bold;
    margin-right: 25px;
}

/* Task status styles */
.task-status {
    padding: 6px 10px;
    font-size: 14px;
    border-radius: 15px;
    text-transform: uppercase;
    font-weight: bold;
}

/* Task status badges */
.inprogress {
    background-color: #ffc107;
    color: #fff;
}

.completed {
    background-color: #28a745;
    color: #fff;
}

.pending {
    background-color: #dc3545;
    color: #fff;
}

/* View button styles */
.view-button {
    padding: 8px 16px;
    background-color: #007bff;
    color: #fff;
    border: none;
    border-radius: 5px;
    cursor: pointer;
    transition: background-color Red;
}

.view-button:hover {
    background-color: #0056b3;
    transform: scale(1.05);
}

/* Hover effect */
.task-item:hover {
    background-color: #f2f2f2;
    transform: translateY(-2px);
    /* Add a subtle lift effect on hover */
    box-shadow: 0 6px 12px rgba(0, 0, 0, 0.1);
    /* Add shadow on hover */
}

:root {
    --primary-color: #007bff;
    --secondary-color: #17a2b8;
}



.resources-section {
    width: 90%;
    background-color: #7ba37e;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    padding: 10px;
    border-radius: 5px;
    display: flex;
    flex-direction: column;
    align-items: center;
    margin: auto;
    margin-top: 20px;
}

.resources-section h3 {
    font-size: 24px;
    margin: 0;
    padding: 10px 0;
    border-bottom: 1px solid var(--primary-color);
}

.resource-list {
    list-style: none;
    padding: 0;
    margin: 0;
    width: 95%;
}

.resource-item {
    padding: 15px;
    border-radius: 5px;
    display: flex;
    justify-content: space-between;
    align-items: center;
    background-color: #90c2c9;
    transition: background-color 0.3s ease;
}

.resource-item:nth-child(even) {
    background-color: #91b6bc;
}

.resource-item:hover {
    background-color: #ffffff;
    color: #000000;
}

.resource-item span {
    color: #666;
}
</style>


