<template>
  <NavBar></NavBar>

  <h1>Update Page</h1>

  <form action="" class="add">
    <input type="text" name="name" placeholder="Enter Your Name" v-model="manager.name">

    <input type="text" placeholder="Enter status" v-model="manager.status">
    <input type="text" placeholder="Enter role" v-model="manager.role">
    <input type="text" placeholder="Enter Bio" v-model="manager.bio">

    <input type="text" placeholder="Enter Email" v-model="manager.email">
    <input type="password" placeholder="Enter Password" v-model="manager.password">
    <button type="button" v-on:click="updateProfile()">Update Profile</button>
  </form>
</template>
    
<script>
import NavBar from './NavBar.vue';
import axios from 'axios';
export default {
  name: "UpdatePage",
  components: {

    NavBar
  },
  data() {
    return {
      manager: {
        name: '',
        status: '',
        role: '',
        bio: "",
        email: '',
        password: ''
      }

    }
  },
  methods: {
    async updateProfile() {
      console.log(this.manager);
      const result = await axios.put('http://127.0.0.1:5000/portfolio-managers/9', {
        name: this.manager.name,
        status: this.manager.status,
        role: this.manager.role,
        bio: this.manager.bio,
        email: this.manager.email,
        password: this.manager.password,
      });
      if (result.status == 200) {
        this.$router.push({ name: 'DashBoard' });
      }
      console.log(result.data);
    }
  },
  async mounted() {

    const result = await axios.get("http://127.0.0.1:5000/portfolio-managers/64b955af822102f471219e24")
    // console.log(this.$route.params.id);
    console.log(result);
    this.manager = result.data
  }
}
</script>

  
<style>
.add {
  max-width: 400px;
  margin: 0 auto;
  padding: 20px;
  background-color: #f9f9f9;
  border: 1px solid #ccc;
  border-radius: 5px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

.add input[type="text"],
.add input[type="password"],
.add textarea,
.add select {
  width: 100%;
  height: 40px;
  padding: 8px;
  margin-bottom: 15px;
  border: 1px solid #ccc;
  border-radius: 5px;
  background-color: #fff;
  color: #333;
  font-size: 16px;
}

.add textarea {
  resize: vertical;
  /* Allow vertical resizing of the textarea */
}

.add select {
  appearance: none;
  /* Remove default arrow in select dropdown */
  background-image: url('data:image/svg+xml;charset=utf-8,%3Csvg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 16 16"%3E%3Cpath d="M8 10.5a.5.5 0 01-.387-.188L4.615 6H2.5a.5.5 0 010-1h3.272a.5.5 0 01.386.187l3.998 4.748L12.884 5H16a.5.5 0 110 1h-3.272a.5.5 0 01-.386-.187L8 6.624 5.658 9.812a.5.5 0 01-.386.188H2.5a.5.5 0 010-1h2.115L8 5.062l1.385 3.937H13.5a.5.5 0 110 1h-3.272a.5.5 0 01-.386-.187L8 10.5z"%3E%3C/path%3E%3C/svg%3E');
  /* Custom arrow icon for select dropdown */
  background-repeat: no-repeat;
  background-position: right 10px center;
  background-size: 10px;
  padding-right: 30px;
}

.add button {
  width: 100%;
  height: 40px;
  background-color: #007bff;
  color: #fff;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  font-size: 16px;
  transition: background-color 0.2s ease-in-out;
}

.add button:hover {
  background-color: #0056b3;
}

/* Style the label element */
.add label {
  display: block;
  margin-bottom: 5px;
  font-weight: bold;
  color: #333;
}

/* Style the form header */
.add h1 {
  text-align: center;
  margin-bottom: 20px;
  color: #333;
}

/* Center the form link */
.add p {
  text-align: center;
  margin-top: 10px;
}

/* Style the router-link */
.add .router-link {
  color: #007bff;
  text-decoration: none;
}

.add .router-link:hover {
  text-decoration: underline;
}
</style>
  