<template>
    <NavBar></NavBar>
    <h1>Edit Project</h1>
    <div class="register">
        <input type="text" placeholder="Enter Project Name" v-model="project.name">
        <input type="text" placeholder="Enter status" v-model="project.status">
        <input type="date" placeholder="Enter Start Date" v-model="project.s_date">
        <input type="date" placeholder="Enter End Date" v-model="project.e_date">
        <button v-on:click="updateProject()">Edit Project</button>
    </div>
</template>

<script>
import NavBar from './NavBar.vue';
import axios from "axios"

export default {
    name: "EditProject",
    components: {
        NavBar
    },
    data() {
        return {
            project: {
                name: "",
                status: "",
                s_date: "",
                e_date: "",
            }
        }
    },
    methods: {
        async updateProject() {
            try {
                const result = await axios.patch('http://localhost:5000/projects/' + this.$route.params.id, {
                    name: this.project.name,
                    status: this.project.status,
                    s_date: this.project.s_date,
                    e_date: this.project.e_date,
                });

                if (result.status === 200) {
                    // The update was successful, you can handle it as needed
                    // For example, redirecting to the dashboard
                    this.$router.push({ name: 'DashBoard' });
                } else {
                    // Handle any potential errors or unsuccessful responses here
                    // For example, display an error message to the user
                    console.error('Failed to update project:', result.data);
                }
            } catch (error) {
                // Handle any network errors here
                console.error('Error updating project:', error);
            }
        }
    },
    async mounted() {
        const result = await axios.get("http://localhost:5000/projects/" + this.$route.params.id)
        this.project = result.data
    }
}
</script>


<style scoped>
.logo {
    width: 100px;
}

.register input {
    width: 300px;
    height: 40px;
    padding-left: 20px;
    display: block;
    margin-bottom: 30px;
    margin-left: auto;
    margin-right: auto;
    border: 1px solid skyblue;
}

.register button {
    width: 320px;
    height: 40px;
    border: 1px solid skyblue;
    background-color: skyblue;
    color: aliceblue;
    cursor: pointer;
}
</style>