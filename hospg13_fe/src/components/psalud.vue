<template>
    <div class="signUp_psalud">
        <div class="container_signUp_psalud">
            <h2> Registrar Personal de Salud</h2>
            <form v-on:submit.prevent="proccesspsalud">
                <label id="psalud_username"> Username:
                    <input type="text" v-model="psalud.username" placeholder="Username">
                </label>
                <br/>
                <label id="psalud_rol"> Rol:
                    <input type="text" v-model="psalud.rol" placeholder="Rol">
                </label>
                <br/>
                <label id="psalud_especialidad"> Perfil:
                    <input type="text" v-model="psalud.especialidad" placeholder="Especialidad">
                </label>
                <br/>                
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
            psalud:{
                username: "",
                rol: "",
                especialidad:"",                                
            }
        }
    },

methods: {
        proccesspsalud:function(){
            axios.post("https://hospitalcasa-g12.herokuapp.com/Psalud/",
            this.psalud,{headers:{}}).then((result)=>{
                alert("Registro Exitoso");
                let dataSignUp={
                    username: this.psalud.username,
                    token_access: result.data.access,
                    token_refresh: result.data.refresh,
                }
                this.$emit('completedPsalud',dataSignUp)

            }).catch((error)=>{
                console.log(error)
                alert("Error: fallo el registro");
            });
        }
    }    
}
</script>

<style>
.signUp_psalud{
    margin: 0;
    padding: 0%;
    height: 100%;
    width: 100%;
    display: flex;
    justify-content: center;
    align-items: center;
}
.container_signUp_psalud {

    border: 3px solid #283747;
    border-radius: 10px;
    width: 25%;
    height: 95%;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
}
.signUp_psalud h2
{
    color: #283747;
}
.signUp_psalud form
{
    width: 70%;
}
.signUp_psalud input
{
height: 25px;
width: 100%;
box-sizing: border-box;
padding: 10px 20px;
margin: 5px0;
border: 1px solid #283747;
}
.signUp_psalud button
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
.signUp_psalud button:hover
{
color: #E5E7E9;
background: crimson;
border: 1px solid #283747;
}
</style>