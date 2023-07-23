<template>
    <h1>LogIn Page</h1>
    <div class="login">
        <input type="text" placeholder="Enter Email" v-model="email">
        <input type="password" placeholder="Enter Password" v-model="password">
        <button v-on:click="login()">Login</button>
        <p v-if="loginError">Email or Password is incorrect.</p> <!-- Show error message -->
        <p>
            <router-link to="/sign-up">Sign Up</router-link>
        </p>
    </div>
</template>

<script>
import axios from 'axios';

export default {
    name: 'LogIn',
    data() {
        return {
            email: '',
            password: '',
            loginError: false, // Flag to show login error
        };
    },
    methods: {
        async login() {
            try {
                let result = await axios.get(
                    `http://localhost:5000/portfolio-managers?email=${this.email}&password=${this.password}`
                );

                console.log(result);
                this.$globalData.someValue = result.data["_id"]
                console.log(this.$globalData.someValue);
                this.$router.push({ name: 'DashBoard' });
                
                
            } catch (error) {
                // Handle any network or server errors
                console.error(error);
                // Show login error message
                this.loginError = true;
            }
        },
    },
    mounted() {
        if (this.$globalData.someValue) {
            this.$router.push({ name: 'DashBoard' });
        }
    },
}




</script>


