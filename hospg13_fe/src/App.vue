<template>
  <div id="app" class="app">
    <div class="header">
        <h1>Hospitalización en Casa</h1>
        <nav>
            <button v-if="!is_auth" v-on:click="loadLogIn"> Iniciar Sesión </button>
            <br><br/>
            <button v-if="is_auth" v-on:click="loadHome" > Inicio </button>
            <button v-if="is_auth" v-on:click="loadAccount"> Cuenta </button >
            <button v-if="is_auth" v-on:click="logOut"> Cerrar Sesión </button>
           
            <button v-if="!is_auth" v-on:click="loadSignUp"> Registrarse </button>
            <button v-if="!is_auth" v-on:click="loadPsalud"> Registrar Personal Salud </button>
            <button v-if="!is_auth" v-on:click="loadPaciente"> Registrar Paciente </button>
            <button v-if="!is_auth" v-on:click="loadFamiliar"> Registrar Familiar </button>
            <br/><br/>
            <button v-if="!is_auth" v-on:click="loadConsulta"> Consultar Paciente </button>            
            
        </nav>
    </div>
  <div class="main-component">
    <router-view 
      v-on:completedLogIn= "completedLogIn"
      v-on:completedSignUp= "completedSignUp"
      v-on:completedPsalud= "completedPsalud"
      v-on:completedPaciente= "completedPaciente"
      v-on:completedFamiliar= "completedFamiliar"
      v-on:completedConsulta= "completedConsulta"
      v-on:logOut="logOut"
    ></router-view>    
  </div>  
  <div class="footer">
      <h2> Derechos de autor reservados para el Grupo 60-12 </h2>
  </div>
</div>    
</template>

<script>
export default({
  name: 'App',
  data: function(){
      return{
        is_auth: false
      }
  },
  methods:{
    
    loadLogIn: function(){
        this.$router.push({name:"LogIn"})
    },
    loadSignUp: function(){
      this.$router.push({name:"regUsuario"})
    },
    loadPsalud: function(){
      this.$router.push({name:"regPsalud"})
    },
    loadPaciente: function(){
      this.$router.push({name:"regPaciente"})
    },
    loadFamiliar: function(){
      this.$router.push({name:"regFamiliar"})
    },
    loadConsulta: function(){
      this.$router.push({name:"viewpaciente"})
    },
    completedLogIn: function(data){
        
        localStorage.setItem("isAuth", true);
        localStorage.setItem("username", data.username);
        localStorage.setItem("token_access", data.token_access);
        localStorage.setItem("token_refresh", data.token_refresh);
        alert("Auntentificación Exitoda");
        this.veryAuth();
    },
  },
  created: function(){
  }

})
</script>

<style>

body{
  margin: 0 0 0 0; 
}
.header{
  margin: 0;
  padding: 0;
  width:100%;
  height: 10vh;
  min-height: 100px;
  background-color: #283747;
  color: #E5E7E9;
  display: flex;
  justify-content: space-between;
  align-items: center;
} 
.header h1{
  width: 50%;
  text-align: center;
}

.main-component
{
  height: 75vh;
  margin: 0%;
  padding: 0%;
  background: #FDFEFE;
}

.footer
{
  margin:0;
  padding:0;
  width: 100%;
  height: 10vh;
  min-height: 100px;
  background-color: #283747;
  color: #E5E7E9;
}
.footer h2{
  width: 100%;
  height: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
}
</style>