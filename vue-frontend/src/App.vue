<template>
  <div id="app">
    <nav class="navbar navbar-expand-lg navbar-light bg-light">
      <router-link to='/' class="navbar-brand">Vue.js Front end</router-link>
      <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarNav">
        <ul class="navbar-nav mr-auto">
          <li class="nav-item active">
            <router-link to='/' class="nav-link">Home <span class="sr-only">(current)</span></router-link>
          </li>
          <li class="nav-item">
            <router-link to='/items' class="nav-link">Items</router-link>
          </li>
          <li class="nav-item">
            <router-link to='/reviews' class="nav-link">Reviews</router-link>
          </li>
        </ul>
        <ul class="navbar-nav">
          <li class="nav-item">
            <router-link to='/register' class="nav-link">Register</router-link>
          </li>
          <li class="nav-item">
            <router-link to='/login' class="nav-link">Login</router-link>
          </li>
        </ul>
      </div>
    </nav>
    <img alt="Vue logo" src="./assets/logo.png">
    <router-view class="container"/>
  </div>
</template>

<script>
export default {
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
</style>
