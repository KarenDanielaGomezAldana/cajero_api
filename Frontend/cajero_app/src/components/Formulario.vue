<template>
    <div class="distancia2">
        <form id="formulario" v-on:submit.prevent="submitForm">
            <div class="form-group row">
                <label for="name" class="col-md-3 col-form-label">Nombre</label>
                <div class="col-md-9">
                    <input type="text" class="form-control" id="username" placeholder="" v-model="form.username">
                </div>
            </div>
            <div class="form-group row">
                <label for="pass" class="col-md-3 col-form-label">Contraseña</label>
                <div class="col-md-9">
                    <input type="password" class="form-control" id="password" placeholder="" v-model="form.password">
                </div>
            </div>
            <div class="form-group row">
                <label for="email" class="col-md-3 col-form-label">Email</label>
                <div class="col-md-9">
                    <input type="text" class="form-control" id="email" placeholder="" v-model="form.email">
                </div>
            </div>            
            <div class="form-group row">
                <label class="col-md-3 col-form-label"></label>
                <div class="col-md-9">
                    <button class="btn btn-primary col-md-12">Registrar</button>
                </div>
            </div>
        </form>
    </div>
</template>

<script>
import axios from 'axios';
export default {
    name: 'PostFormAxios',
    data(){
        return{
            form: {
                username: '',
                password: '',
                email: ''
            }
        }
    },
    methods:{
        submitForm(){
            console.log(this.form)
            axios.post('http://127.0.0.1:8000/contact/', this.form)
                 .then((res) => {
                     console.log(res.data)//Perform Success Action
                 })
                 .catch((error) => {
                     // error.response.status Check status code
                 }).finally(() => {
                     //Perform action in always
                 });
        }
    }
}
</script>

<style>
#formulario{
    margin: 0 auto;
    text-align: center;
    border-radius: 10px;
    border: 1px solid #ffffff;
    width: 500px;
}
.espacio {
    width: 40%;
    text-align: center;
  }

.espacio1 {
    width: 60%;
    text-align: center;
  }
.distancia2{
  margin: 50px auto;
}
</style>
