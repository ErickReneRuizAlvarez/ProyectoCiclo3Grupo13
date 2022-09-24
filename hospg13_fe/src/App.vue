<template>
  <nav>
    <router-link to="/">Home</router-link> |
    <router-link to="/about">About</router-link>
  </nav>
  <router-view/>
</template>

<script>

  export default{

  data: function(){
  },

  methods:{
  },

  created: function(){
  }
}
</script>


<style>
  body{
    margin: 0 0 0 0;
  }

  .header{
    margin:0;
    padding:0;
    width: 100%;
    height: 10vh;
    min-height: 100px;
    background-color: #283747;
    color:#E5E7E9;
    display: flex;
    justify-content: space-between;
    align-items: center;
  }

  .header h1{
    width: 20%;
    text-align: center;
  }
</style>
