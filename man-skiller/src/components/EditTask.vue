<template>
    <h1>Edit Task</h1>
    <div class="register">
        <input type="text" placeholder="Enter Name" v-model="name">

        <input type="text" placeholder="Enter status" v-model="status">
        <input type="text" placeholder="Enter role" v-model="role">

        <input type="text" placeholder="Enter Bio" v-model="bio">
        <input type="date" placeholder="Enter Date" v-model="date">
        <input type="text" placeholder="Enter Email" v-model="email">
        <input type="password" placeholder="Enter Password" v-model="password">
        <button v-on:click="signup()">Sign Up</button>
        <p>
            <router-link to="/log-in">Log in</router-link>
        </p>
    </div>
</template>



<script>
import axios from "axios"

export default {
    name: "EditTask",
    data() {
        return {
            name: "",
            status: "",
            role: "",
            bio: "",
            date: "",

            email: "",
            password: ""
        }

    },
    methods: {
        async signup() {
            let result = await axios.post("http://127.0.0.1:5000/portfolio-managers", {
                name: this.name,
                status: this.status,
                role: this.role,
                bio: this.bio,
                date: this.date,
                email: this.email,
                password: this.password
            })

            console.log(result.email);
            if (result.status) {

                // localStorage.setItem("user-info", JSON.stringify(result.data))
                this.$router.push({ name: 'DashBoard' })
            }

        }
    },
    // mounted() {
    //     let user = localStorage.getItem("user-info")
    //     if (user) {
    //         this.$router.push({ name: 'HomePage' })
    //     }
    // }
}
</script>

<style>
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