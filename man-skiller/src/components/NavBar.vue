<template>
    <nav class="navbar">
      <div class="container">
        <router-link class="navbar-brand dashboard-link" to="/">Dashboard</router-link>
        <div class="nav-items">
          <router-link class="nav-link" to="/project-tasks">Project Tasks</router-link>
          <router-link class="nav-link" to="/resources">Resources</router-link>
          <router-link class="nav-link" to="/profile">Profile</router-link>
          <router-link class="nav-link" to="/add-project">Add Project</router-link>
          <div class="search-bar">
            <input type="text" placeholder="Search" class="search-input" />
            <button class="search-button">
              <i class="fas fa-search"></i>
            </button>
          </div>
          <a class="nav-link" href="#">
            Notifications <span class="badge">4</span>
          </a>
          <a class="nav-link" href="#">Settings</a>
          <a class="nav-link" href="#">Help/Support</a>
          <a class="nav-link" href="#">Logout</a>
        </div>
      </div>
    </nav>
  </template>

  <script>
  export default {
    name: "NavBar",
    
  }
</script>

  
  <style scoped>
  /* Add custom styles for the navigation bar here */
  .navbar {
    background-color: #333;
    padding: 10px;
  }
  
  .container {
    display: flex;
    align-items: center;
    justify-content: space-between;
  }
  
  .dashboard-link {
    color: #ffffff; /* Orange color */
    font-size: 20px;
    text-decoration: none;
  }
  
  .nav-items {
    display: flex;
    align-items: center;
  }
  
  .nav-link {
    color: #fff;
    text-decoration: none;
    font-size: 16px;
    padding: 8px 15px;
  }
  
  .nav-link:hover {
    background-color: #555;
    border-radius: 5px;
  }
  
  .badge {
    background-color: #ff6347; /* Tomato Red */
    color: #fff;
    padding: 3px 6px;
    border-radius: 50%;
    font-size: 12px;
    margin-left: 5px;
  }
  
  /* Search Bar Styles */
  .search-bar {
    display: flex;
    align-items: center;
    margin-left: 15px;
  }
  
  .search-input {
    border: none;
    border-radius: 20px;
    padding: 5px 30px 5px 10px;
    background-color: #fff;
    color: #333;
    outline: none;
  }
  
  .search-button {
    background: transparent;
    border: none;
    padding: 5px;
    cursor: pointer;
  }
  </style>
  