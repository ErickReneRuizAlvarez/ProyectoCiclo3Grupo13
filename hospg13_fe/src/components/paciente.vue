<template>
    <div class="signUp_paciente">
        <div class="container_signUp_paciente">
            <h2> Registrar Paciente</h2>
            <form v-on:submit.prevent="proccesspaciente">
                <label id="paciente_username"> Username:
                    <input type="text" v-model="paciente.username" placeholder="Username">
                </label>
                <br/>
                <label id="paciente_psalud"> psalud:
                    <input type="number" v-model="paciente.persalud" placeholder="Psalud">
                </label>
                <br/>
                <label id="paciente_direccion"> Direccion:
                    <input type="text" v-model="paciente.direccion" placeholder="Direccion">
                </label>
                <br/>
                <label id="paciente_ciudad"> Ciudad:
                    <input type="text" v-model="paciente.ciudad" placeholder="Ciudad">
                </label>
                <br/>
                <label id="paciente_fechanac"> Fecha de Nacimiento:
                    <input type="text" v-model="paciente.fechaNacimiento" placeholder="Fecha Nacimiento">
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
            paciente:{
                username: "",
                persalud: "",
                direccion:"",
                ciudad: "",
                fechaNacimiento: "",                                
            }
        }
    },

methods: {
        proccesspaciente:function(){
            axios.post("https://hospitalcasa-g12.herokuapp.com/paciente/",
            this.paciente,{headers:{}}).then((result)=>{
                alert("Registro Exitoso");
                let dataSignUp={
                    username: this.paciente.username,
                    token_access: result.data.access,
                    token_refresh: result.data.refresh,
                }
                this.$emit('completedpaciente',dataSignUp)

            }).catch((error)=>{
                console.log(error)
                alert("Error: fallo el registro");
            });
        }
    }    
}
</script>

<style>
.signUp_paciente{
    margin: 0;
    padding: 0%;
    height: 100%;
    width: 100%;
    display: flex;
    justify-content: center;
    align-items: center;
}
.container_signUp_paciente {

    border: 3px solid #283747;
    border-radius: 10px;
    width: 25%;
    height: 95%;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
}
.signUp_paciente h2
{
    color: #283747;
}
.signUp_paciente form
{
    width: 70%;
}
.signUp_paciente input
{
height: 25px;
width: 100%;
box-sizing: border-box;
padding: 10px 20px;
margin: 5px0;
border: 1px solid #283747;
}
.signUp_paciente button
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
.signUp_paciente button:hover
{
color: #E5E7E9;
background: crimson;
border: 1px solid #283747;
}
</style>