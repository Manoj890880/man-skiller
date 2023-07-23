<template>
    <div class="container">
      <h2>Resource List</h2>
      <ul class="resource-list" id="resourceList">
        <!-- Resources will be added dynamically here -->
        <li class="resource-item">
          <h3>Resource Label</h3>
          <p>Description of the resource goes here.</p>
        </li>
      </ul>
      <button class="add-resource-btn" @click="addResource">Add Resource</button>
    </div>
  </template>
  
  <script>
  export default {
    name:"ViewResource",
    methods: {
      addResource() {
        // Your logic to add a new resource goes here
        console.log("Adding a new resource!");
      },
    },
  };
  </script>
  
  <style scoped>
    
    .container {
      max-width: 85%;
      margin: 0 auto;
      padding: 20px;
      background-color: #c3d185;
      margin-top: 50px;
    }
    h2 {
      font-size: 24px;
      color: #333;
    }
    .resource-list {
      list-style: none;
      padding: 0;
    }
    .resource-item {
      background-color: #ffd58e; /* Change the resource-item background color */
      border-radius: 8px;
      box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
      padding: 20px;
      margin-bottom: 20px;
    }
    .resource-item h3 {
      font-size: 18px;
      color: #333;
      margin: 0 0 10px;
    }
    .resource-item p {
      font-size: 14px;
      color: #666;
      margin: 0;
    }
    .add-resource-btn {
      background-color: #ff4e50;
      color: #fff;
      border: none;
      padding: 14px 28px;
      font-size: 16px;
      border-radius: 8px;
      cursor: pointer;
      
      bottom: -30px;
      right: 20px;
      transition: background-color 0.3s;
      box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
      z-index: 2;
    }
    .add-resource-btn:hover {
      background-color: #ff6b6e;
    }
  </style>
  