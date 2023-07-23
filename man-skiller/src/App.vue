<template>
  <router-view></router-view>
</template>

<script>


export default {
  name: 'App',

}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;

}

body {
  padding: 0;
  margin: 0;
}

.nav a {
  float: left;
  color: aliceblue;
  padding: 14px;
  text-align: center;
  font-size: 17px;
  text-decoration: none;
  margin-left: 5px;
}

.nav a:hover {
  background-color: aqua;
  color: black;
}

.logo {
  width: 100px;
}

.register input,
.login input,
.add input {
  width: 300px;
  height: 40px;
  padding-left: 20px;
  display: block;
  margin-bottom: 30px;
  margin-left: auto;
  margin-right: auto;
  border: 1px solid skyblue;
}

.register button,
.login button,
.add button {
  width: 320px;
  height: 40px;
  border: 1px solid skyblue;
  background-color: skyblue;
  color: aliceblue;
  cursor: pointer;
}
</style>