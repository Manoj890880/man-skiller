<template>
    <NavBar></NavBar>
    <div style="background-color: rgb(50, 115, 189); height: 100vh;">
    <div class="container">
        <h1>Add New Project</h1>
        <form action="#" method="post">
            <div class="form-group">
                <label for="projectName">Project Name:</label>
                <input type="text" id="projectName" name="projectName" required>
            </div>
            <div class="form-group">
                <label for="status">Status:</label>
                <select id="status" name="status" required>
                    <option value="" disabled selected>Select Status</option>
                    <option value="Planned">Planned</option>
                    <option value="In Progress">In Progress</option>
                    <option value="Completed">Completed</option>
                </select>
            </div>
            <div class="form-group">
                <label for="startDate">Start Date:</label>
                <input type="date" id="startDate" name="startDate" required>
            </div>
            <div class="form-group">
                <label for="endDate">End Date:</label>
                <input type="date" id="endDate" name="endDate" required>
            </div>
            <button type="submit">Add Project</button>
        </form>
    </div>
</div>
</template>


<script>
import NavBar from './NavBar.vue';
export default {
    name: "AddProject",
    components: {
        NavBar
    }
}

</script>


<style scoped>
body {
    font-family: Arial, sans-serif;
    margin: 0;
    padding: 0;
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100vh;
    background-color: #3ea0dd;
}

.container {
    background-color: #fff;
    padding: 30px;
    border-radius: 5px;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    width: 30%;
    margin: auto;
    
}

h1 {
    font-size: 24px;
    margin-bottom: 20px;
    text-align: center;
}

.form-group {
    margin-bottom: 20px;
}

label {
    display: block;
    font-size: 16px;
    font-weight: bold;
    margin-bottom: 5px;
}

input[type="text"],
select,
input[type="date"] {
    width: 100%;
    padding: 10px;
    border: 1px solid #ccc;
    border-radius: 5px;
}

button {
    background-color: #007bff;
    color: #fff;
    border: none;
    padding: 12px 20px;
    border-radius: 5px;
    cursor: pointer;
    width: 100%;
    font-size: 16px;
    font-weight: bold;
    transition: background-color 0.2s ease;
}

button:hover {
    background-color: #0056b3;
}
</style>