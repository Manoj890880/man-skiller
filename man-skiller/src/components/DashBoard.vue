<template>
    <div>
        <NavBar></NavBar>
        <main class="dashboard">
            <!-- User Info Section -->
            <section id="user-info">
                <div class="user-info-container">
                    <h2>Welcome to our platform, John Doe</h2>
                </div>
            </section>

            <!-- Portfolio Overview Section -->
            <section id="portfolio-overview" style="background-color: rgb(63, 171, 218);">
                <h2>Portfolio Overview</h2>
                <div class="metrics">
                    <div class="metric">
                        <span class="metric-label">Total Projects:</span>
                        <span class="metric-value">10</span>
                    </div>
                    <div class="metric">
                        <span class="metric-label">Completed Projects:</span>
                        <span class="metric-value">5</span>
                    </div>
                    <div class="metric">
                        <span class="metric-label">In Progress Projects:</span>
                        <span class="metric-value">5</span>
                    </div>
                </div>
            </section>
            <br>
            <!-- Associated Projects Section -->
            <div class="filters">
                <label for="status">Status:</label>
                <select id="status">
                    <option value="">All</option>
                    <option value="In Progress">In Progress</option>
                    <option value="Completed">Completed</option>
                    <option value="Pending">Pending</option>
                </select>
                <label for="portfolioManager">Portfolio Manager:</label>
                <select id="portfolioManager">
                    <option value="">All</option>
                    <option value="John Doe">John Doe</option>
                    <option value="Jane Smith">Jane Smith</option>
                    <option value="Mike Johnson">Mike Johnson</option>
                </select>
                <label for="sortBy">Sort By:</label>
                <select id="sortBy">
                    <option value="">None</option>
                    <option value="status">Status</option>
                    <option value="startDate">Start Date</option>
                </select>
                <label for="sortOrder">Sort Order:</label>
                <select id="sortOrder">
                    <option value="asc">Ascending</option>
                    <option value="desc">Descending</option>
                </select>
                <button id="applyFilters">Apply Filters</button>
            </div>
            <main>
                <table class="project-table">
                    <thead>
                        <tr>
                            <th>ID</th>
                            <th>Name</th>
                            <th>Status</th>
                            <th>Portfolio Manager</th>
                            <th>Start Date</th>
                            <th>End Date</th>
                            <th>Action</th> <!-- Added the Action column -->
                        </tr>
                    </thead>
                    <tbody>
                        <tr v-for="project in projects" :key="project._id">
                            <td>{{ project._id }}</td>
                            <td>{{ project.name }}</td>
                            <td>{{ project.status }}</td>
                            <td>{{ project.managerName }}</td>
                            <td>{{ project.s_date }}</td>
                            <td>{{ project.e_date }}</td>
                            <td>
                                <button class="action-btn view-btn">View</button>
                                <button class="action-btn edit-btn">Edit</button>
                                <button class="action-btn delete-btn">Delete</button>
                                <button class="action-btn view-task-list-btn">View Tasks</button>
                            </td>
                        </tr>
                        <tr>
                            <td>2</td>
                            <td>Project 2</td>
                            <td>Completed</td>
                            <td>Jane Smith</td>
                            <td>2023-07-15</td>
                            <td>2023-09-15</td>
                            <td>
                                <button class="action-btn view-btn">View</button>
                                <button class="action-btn edit-btn">Edit</button>
                                <button class="action-btn delete-btn">Delete</button>
                                <button class="action-btn view-task-list-btn">View Tasks</button>
                            </td>
                        </tr>
                        <!-- Add more project rows here -->
                    </tbody>
                </table>
                <div class="pagination">
                    <span>Page 1 of 3</span>
                    <button>Prev</button>
                    <button>1</button>
                    <button>2</button>
                    <button>3</button>
                    <button>Next</button>
                </div>
            </main>
        </main>
    </div>
</template>
  
<script>
import NavBar from './NavBar.vue';
import axios from "axios"

export default {
    name: "DashBoard",
    components: {
        NavBar
    },
    data() {
        return {
            name: '',
            projects: []
        }
    },

    methods: {
        async fetchManagerName(managerId) {
            const response = await axios.get(`http://localhost:5000/portfolio-managers/${managerId}`);
            return response.data.name;
        },

        async loadData() {
            let user = await axios.get("http://127.0.0.1:5000/portfolio-managers/64b955af822102f471219e24")
            this.name = user.name
            if (!user) {
                this.$router.push({ name: 'SignUp' })
            }
            let result = await axios.get("http://localhost:5000/projects/manager/64b955af822102f471219e24");
            const projectsWithManagerName = await Promise.all(result.data.map(async (project) => {
                const managerName = await this.fetchManagerName(project.manager_id);
                return { ...project, managerName };
            }));

            this.projects = projectsWithManagerName;
        }
    },

    async mounted() {
        this.loadData();
    }
}
</script>
  
<style scoped>
/* Add custom styles for the Dashboard page here */
body {
    background-color: #28a745;
}

/* Existing CSS styles remain the same */

/* New styles for advanced and interactive effects in user info section */
#user-info {
    background-color: #329dea;
    color: #ffffff;
    padding: 40px 0;
    text-align: center;
}

.user-info-container {
    max-width: 800px;
    margin: 0 auto;
}

h2 {
    font-size: 24px;
    margin-bottom: 20px;
}

/* Add a subtle animation effect to the user info section */
#user-info {
    animation: fadeInDown 0.8s ease;
}

@keyframes fadeInDown {
    from {
        opacity: 0;
        transform: translateY(-20px);
    }

    to {
        opacity: 1;
        transform: translateY(0);
    }
}

/* Add a hover effect to the h2 text */
h2:hover {
    color: #f9f9f9;
}

/* Add a button-like appearance to the user info container */
.user-info-container {
    width: 90%;
    background-color: #9e8f8f;
    display: inline-block;
    padding: 20px;
    border-radius: 10px;
    box-shadow: 0 4px 8px rgba(32, 23, 23, 0.1);
    transition: transform 0.2s ease, box-shadow 0.2s ease;
}

.user-info-container:hover {
    transform: translateY(-5px);
    box-shadow: 0 6px 12px rgba(0, 0, 0, 0.1);
    cursor: pointer;
}


/* Existing CSS styles remain the same */

/* New styles for advanced and interactive effects in portfolio overview section */


/* Updated background colors for portfolio overview section */
#portfolio-overview {

    text-align: center;
    margin-top: 10px;
    background-color: #f5f7fa;
    /* Light gray background */
    padding: 40px 0;
}

h2 {
    font-size: 24px;
    color: #333;
    margin-bottom: 20px;
}

.metrics {
    display: flex;
    justify-content: center;
}

.metric {
    padding: 15px 20px;
    margin: 0 10px;
    background-color: #fff;
    /* White background */
    border-radius: 8px;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    transition: transform 0.2s ease, box-shadow 0.2s ease;
    cursor: pointer;
}

.metric:hover {
    transform: translateY(-5px);
    box-shadow: 0 6px 12px rgba(0, 0, 0, 0.1);
}

.metric-label {
    font-size: 16px;
    color: #666;
}

.metric-value {
    font-size: 24px;
    color: #007bff;
    font-weight: bold;
    margin-top: 5px;
}

/* Add a subtle animation effect to metric values */
.metric-value {
    animation: fadeIn 0.8s ease;
}

@keyframes fadeIn {
    from {
        opacity: 0;
    }

    to {
        opacity: 1;
    }
}

/* Add a gradient background to metric values on hover */
.metric:hover .metric-value {
    background: linear-gradient(90deg, #007bff, #0056b3);
    -webkit-background-clip: text;
    background-clip: text;
    -webkit-text-fill-color: transparent;
}



.filters {
    display: flex;
    align-items: center;
    justify-content: space-between;
    flex-wrap: wrap;
    padding: 10px;
    background-color: #0b83af;
    border: 1px solid #715c5c;
    border-radius: 5px;
    margin-bottom: 20px;
}

label {
    font-weight: bold;
}

select {
    padding: 8px;
    font-size: 14px;
    border: 1px solid #ccc;
    border-radius: 5px;
    background-color: #fff;
    transition: border-color 0.3s ease;
}

select:hover {
    border-color: #999;
}

button {
    padding: 10px 20px;
    font-size: 14px;
    border: none;
    border-radius: 5px;
    background-color: #0400ff;
    color: #fff;
    cursor: pointer;
    transition: background-color 0.3s ease;
}

button:hover {
    background-color: #3d44a4;
}

@media screen and (max-width: 600px) {
    .filters {
        flex-direction: column;
        align-items: flex-start;
    }

    select,
    button {
        margin-bottom: 10px;
        width: 100%;
    }
}

table {
    width: 100%;
    border-collapse: collapse;
}

th,
td {
    border: 1px solid #ccc;
    padding: 8px;
}

th {
    background-color: #f2f2f2;
}

tr:nth-child(even) {
    background-color: #f2f2f2;
}

.pagination {
    margin-top: 20px;
    display: flex;
    align-items: center;
    justify-content: center;
}

.pagination button {
    padding: 8px 12px;
    margin: 0 5px;
    border: 1px solid #ccc;
    background-color: #fff;
    cursor: pointer;
}

.pagination button:hover {
    background-color: #f2f2f2;
}

/* The previous CSS styles remain the same */

.filters {
    margin-bottom: 10px;
}

.filters label,
.filters select,
.filters button {
    margin-right: 10px;
}

/* Existing CSS styles remain the same */

.action-btn {
    padding: 8px 12px;
    margin-right: 5px;
    border: none;
    border-radius: 5px;
    cursor: pointer;
    transition: background-color 0.3s ease;
}

.view-btn {
    background-color: #007bff;
    color: #fff;
}

.view-btn:hover {
    background-color: #0056b3;
}

.edit-btn {
    background-color: #ffc107;
    color: #333;
}

.edit-btn:hover {
    background-color: #e0a800;
}

.delete-btn {
    background-color: #dc3545;
    color: #fff;
}

.delete-btn:hover {
    background-color: #c82333;
}

/* Existing CSS styles remain the same */

/* New styles for advanced and interactive effects */
body {
    background-color: #f9f9f9;
}

.project-table {
    /* Add box shadow to create a 3D effect */
    box-shadow: 0 2px 6px rgba(0, 0, 0, 0.1);
}

th {
    /* Add a gradient background color for the header */
    background: linear-gradient(90deg, #007bff, #0056b3);
    color: #fff;
}

th,
td {
    /* Add a subtle border radius to the table cells */
    border-radius: 5px;
}

td {
    /* Add a box shadow to the table cells on hover for depth effect */
    transition: box-shadow 0.3s ease;
}

td:hover {
    box-shadow: 0 2px 6px rgba(0, 0, 0, 0.2);
}

.action-btn {
    /* Add a gradient background for action buttons */
    background: linear-gradient(90deg, #007bff, #0056b3);
    color: #fff;
    border: none;
    border-radius: 5px;
    cursor: pointer;
    transition: transform 0.2s ease, background-color 0.2s ease;
}

.action-btn:hover {
    /* Add a scale-up effect on hover */
    transform: scale(1.1);
    background-color: #0056b3;
}

.action-btn:active {
    /* Add a scale-down effect on click */
    transform: scale(0.95);
}

.view-btn {
    /* Adjust the color of the view button for contrast */
    background: linear-gradient(90deg, #41c3e6, #1f9bc9);
}

.edit-btn {
    /* Adjust the color of the edit button for contrast */
    background: linear-gradient(90deg, #f9c107, #d99900);
    color: #333;
}

.delete-btn {
    /* Adjust the color of the delete button for contrast */
    background: linear-gradient(90deg, #f55d6e, #d53242);
}

/* Add some spacing between the pagination buttons */
.pagination button {
    margin: 0 5px;
}

/* New styles for pagination buttons on hover */
.pagination button:hover {
    background-color: #007bff;
    color: #fff;
    box-shadow: 0 2px 6px rgba(0, 0, 0, 0.2);
}

/* New styles for pagination buttons on active state */
.pagination button:active {
    transform: scale(0.95);
}


/* Existing CSS styles remain the same */

/* New styles for advanced and interactive effects in pagination */
.pagination {
    display: flex;
    align-items: center;
    justify-content: center;
    margin-top: 20px;
}

.pagination span {
    font-size: 14px;
    margin-right: 20px;
}

.pagination button {
    padding: 8px 12px;
    font-size: 14px;
    border: none;
    border-radius: 5px;
    cursor: pointer;
    transition: transform 0.2s ease, background-color 0.2s ease, box-shadow 0.2s ease;
}

.pagination button:first-child {
    margin-right: 10px;
}

/* Add a gradient background for pagination buttons */
.pagination button:not([disabled]) {
    background: linear-gradient(90deg, #007bff, #0056b3);
    color: #fff;
}

/* Adjust the color of the disabled (Prev and Next) buttons for contrast */
.pagination button[disabled] {
    background-color: #f2f2f2;
    color: #999;
    cursor: not-allowed;
}

/* Add a subtle box shadow to the pagination buttons on hover for depth effect */
.pagination button:not([disabled]):hover {
    box-shadow: 0 2px 6px rgba(0, 0, 0, 0.2);
}

/* Add a scale-up effect on hover for active page button */
.pagination button:not([disabled]):hover:not(.active-page) {
    transform: scale(1.1);
    background-color: #0056b3;
}

/* Add a scale-down effect on click for active page button */
.pagination button:not([disabled]).active-page:active {
    transform: scale(0.95);
}

/* Add a green background for the active page button */
.pagination button.active-page {
    background-color: #28a745;
}

/* Adjust the color of the Prev and Next buttons on hover for contrast */
.pagination button[disabled]:hover {
    background-color: #f2f2f2;
    color: #999;
}
</style>
  