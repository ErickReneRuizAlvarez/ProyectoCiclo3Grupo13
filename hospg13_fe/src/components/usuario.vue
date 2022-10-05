<template>
    <div class="signUp_user">
        <div class="container_signUp_user">
            <h2> Registrar Usuario</h2>
            <form v-on:submit.prevent="proccessSignUp">
                <label id="user_username"> Username:
                    <input type="text" v-model="user.username" placeholder="Username">
                </label>
                <br/>
                <label id="user_password"> Password:
                    <input type="password" v-model="user.password" placeholder="Password">
                </label>
                <br/>
                <label id="user_perfil"> Perfil:
                    <input type="text" v-model="user.perfil" placeholder="Perfil">
                </label>
                <br/>
                <label id="user_name"> Nombre:
                    <input type="text" v-model="user.nombre" placeholder="Nombre">
                </label>
                <br/>
                <label id="user_apellidos"> Apellidos:
                    <input type="text" v-model="user.apellidos" placeholder="Apellidos">
                </label>
                <br/>
                <label id="user_telefono"> Telefono:
                    <input type="text" v-model="user.telefono" placeholder="Telefono">
                </label>
                <br/>
                <label id="user_genero"> Genero:
                    <input type="text" v-model="user.genero" placeholder="Genero">
                </label>
                <button type="submit">Registrarse</button>
  
            </form> 
        </div>
    </div>
</template>

<script>
import axios from 'axios';
export default {
    data:function(){
        return{
            user:{
                username: "",
                password: "",
                perfil:"",
                nombre: "",
                apellidos: "",
                tefefono:"",
                genero:"",                
            }

        }
    },

methods: {
        proccessSignUp:function(){
            axios.post("https://hospitalcasa-g12.herokuapp.com/usuario/",
            this.user,{headers:{}}).then((result)=>{
                alert("Registro Exitoso");
                let dataSignUp={
                    username: this.user.username,
                    token_access: result.data.access,
                    token_refresh: result.data.refresh,
                }
                this.$emit('completedSignUp',dataSignUp)

            }).catch((error)=>{
                console.log(error)
                alert("Error: fallo el registro");
            });
        }
    }    
}
</script>

<style>
.signUp_user{
    margin: 0;
    padding: 0%;
    height: 100%;
    width: 100%;
    display: flex;
    justify-content: center;
    align-items: center;
}
.container_signUp_user {

    border: 3px solid #283747;
    border-radius: 10px;
    width: 25%;
    height: 95%;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
}
.signUp_user h2
{
    color: #283747;
}
.signUp_user form
{
    width: 70%;
}
.signUp_user input
{
height: 25px;
width: 100%;
box-sizing: border-box;
padding: 10px 20px;
margin: 5px0;
border: 1px solid #283747;
}
.signUp_user button
{
width: 100%;
height: 40px;
color: #E5E7E9;
background: #283747;
border: 1px solid #E5E7E9;
border-radius: 5px;
padding: 10px 25px;
margin: 5px0 25px0;

}
.signUp_user button:hover
{
color: #E5E7E9;
background: crimson;
border: 1px solid #283747;
}
</style>