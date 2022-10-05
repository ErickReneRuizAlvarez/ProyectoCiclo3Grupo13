<template>
    <div class="signUp_familiar">
        <div class="container_signUp_familiar">
            <h2> Registrar Familiar</h2>
            <form v-on:submit.prevent="proccessfamiliar">
                <label id="familiar_username"> Username:
                    <input type="text" v-model="familiar.username" placeholder="Username">
                </label>
                <br/>
                <label id="familiar_idpaciente"> ID Paciente:
                    <input type="number" v-model="familiar.idpaciente" placeholder="Id_Paciente">
                </label>
                <br/>
                <label id="familiar_parentesco"> Parentesco:
                    <input type="text" v-model="familiar.parentesco" placeholder="Parentesco">
                </label>
                <br/>
                <label id="familiar_correo"> Correo electrónico:
                    <input type="text" v-model="familiar.correo" placeholder="e-mail">
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
            familiar:{
                username: "",
                idpaciente: "",
                parentesco:"",
                correo: "",                                
            }
        }
    },

methods: {
        proccessfamiliar:function(){
            axios.post("https://hospitalcasa-g12.herokuapp.com/familiar/",
            this.familiar,{headers:{}}).then((result)=>{
                alert("Registro Exitoso");
                let dataSignUp={
                    username: this.familiar.username,
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
.signUp_familiar{
    margin: 0;
    padding: 0%;
    height: 100%;
    width: 100%;
    display: flex;
    justify-content: center;
    align-items: center;
}
.container_signUp_familiar {

    border: 3px solid #283747;
    border-radius: 10px;
    width: 25%;
    height: 95%;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
}
.signUp_familiar h2
{
    color: #283747;
}
.signUp_familiar form
{
    width: 70%;
}
.signUp_familiar input
{
height: 25px;
width: 100%;
box-sizing: border-box;
padding: 10px 20px;
margin: 5px0;
border: 1px solid #283747;
}
.signUp_familiar button
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
.signUp_familiar button:hover
{
color: #E5E7E9;
background: crimson;
border: 1px solid #283747;
}
</style>