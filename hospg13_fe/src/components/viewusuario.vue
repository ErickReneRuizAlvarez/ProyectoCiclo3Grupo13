<template>
    <div class="view_Verpaciente">
        <div class="container_view_Verpaciente">
            <h2> Consultar Paciente </h2>
            <form v-on:submit.prevent="proccessviewusuario">
                <label id="viewusuario_Verpaciente"> IDPaciente:
                    <input type="number" v-model="viewusuario.Verpaciente" placeholder="IDPaciente">
                </label>
                <br/>                               
                <button type="submit">Consultar</button>  
            </form> 
        </div>
    </div>
</template>
<script>
import axios from 'axios';
export default {
    data:function(){
        return{
            viewusuario:{
                paciente:{
                username: "",
                persalud: "",
                direccion:"",
                ciudad: "",
                fechaNacimiento: "",                                
                }
            }
        }
    },
    methods: {
        proccessviewusuario:function(){
            axios.get("https://hospitalcasa-g12.herokuapp.com/.paciente/",
            {headers:{}}).then((result)=>{
                alert("consulta Exitoso");
                let dataSignUp={
                    username: this.viewusuario.username,
                    token_access: result.data.access,
                    token_refresh: result.data.refresh,
                }
                this.$emit('completedpaciente',dataSignUp)

            }).catch((error)=>{
                console.log(error)
                alert("Error: fallo la consulta");
            });
        }
    }

}
</script>

<style>
.view_Verpaciente{
    margin: 0;
    padding: 0%;
    height: 100%;
    width: 100%;
    display: flex;
    justify-content: center;
    align-items: center;
}
.container_view_Verpaciente {

    border: 3px solid #283747;
    border-radius: 10px;
    width: 25%;
    height: 95%;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
}
.view_Verpaciente h2
{
    color: #283747;
}
.view_Verpaciente form
{
    width: 70%;
}
.view_Verpaciente input
{
height: 25px;
width: 100%;
box-sizing: border-box;
padding: 10px 20px;
margin: 5px0;
border: 1px solid #283747;
}
.view_Verpaciente button
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
.view_Verpaciente button:hover
{
color: #E5E7E9;
background: crimson;
border: 1px solid #283747;
}
</style>