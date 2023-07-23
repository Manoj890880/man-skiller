
    
<template>
    <NavBar></NavBar>
    <h1>Add Project</h1>
    <div class="register">
        <input type="text" placeholder="Enter Project Name" v-model="name">

        <input type="text" placeholder="Enter status" v-model="status">



        <input type="date" placeholder="Enter Start Date" v-model="s_date">
        <input type="date" placeholder="Enter End Date" v-model="e_date">


        <button v-on:click="signup()">Add Project</button>

    </div>
</template>



<script>
import NavBar from './NavBar.vue';
import axios from "axios"

export default {
    name: "AddResource",
    components: {
        NavBar
    },
    data() {
        return {
            name: "",
            status: "",

            s_date: "",
            e_date: "",
            manager_id: ""

        }

    },
    methods: {
        async signup() {
            let result = await axios.post("http://127.0.0.1:5000/projects", {
                name: this.name,
                status: this.status,

                s_date: this.s_date,
                e_date: this.e_date,
                manager_id: "64b955af822102f471219e24"
            })


            if (result.status) {

                // localStorage.setItem("user-info", JSON.stringify(result.data))
                this.$router.push({ name: 'DashBoard' })
            }

        }
    },
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