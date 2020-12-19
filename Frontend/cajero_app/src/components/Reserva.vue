
<template>
    <div class="col-12 distancia6">
        <form id="formulario" v-on:submit.prevent="submitForm">

            <div class="form-group row">
                <label for="Nombre" class="col-md-3 col-form-label">Nombre</label>
                <div class="col-md-9">
                    <input type="text" class="form-control" id="Nombre" placeholder="" v-model="form.Nombre">
                </div>
            </div>

            <div class="form-group row">
                <label for="Destino" class="col-md-3 col-form-label">Destino</label>
                <div class="col-md-9">
                    <select class="col-md-9" type="list" id="Destino" name="menu">
                        <option value="0"></option>
                        <option value="1">Cartagena</option>
                        <option value="2">Medellin</option>
                        <option value="3">Bogotá</option>
                        <option value="3">Boyaca</option>
                        <option value="3">Nariño</option>
                    </select>  
                </div>
            </div>
                
                
            <div class="form-group row">
                <label for="Hotel" class="col-md-3 col-form-label">Hotel</label>
                <div class="col-md-9">
                    <input type="text" class="form-control" id="Hotel" placeholder="" v-model="form.Hotel">
                </div>
            </div>     

            <div class="form-group row">
                <label for="Habitaciones" class="col-md-3 col-form-label">Habitaciones</label>
                <div class="col-md-9">
                    <input type="number" class="form-control" id="Habitaciones" placeholder="" v-model="form.Habitaciones">
                </div>
            </div>  

            <div class="form-group row">
                <label for="Valor" class="col-md-3 col-form-label">Valor</label>
                <div class="col-md-9">
                    <input type="number" class="form-control" id="Valor" placeholder="" v-model="form.Valor">
                </div>
            </div>

            <div class="form-group row">
                <label for="Fecha_entrada" class="col-md-3 col-form-label">Fecha de llegada</label>
                <div class="col-md-9">
                    <input type="date" class="form-control" id="Fecha_entrada" placeholder="" v-model="form.Fecha_entrada">
                </div>  
            </div>

            <div class="form-group row">
                <label for="Fecha_salida" class="col-md-3 col-form-label">Fecha de salida</label>
                <div class="col-md-9">
                    <input type="date" class="form-control" id="Fecha_salida" placeholder="" v-model="form.Fecha_salida">
                </div>  
            </div>

            <div class="form-group row">
                <label class="col-md-3 col-form-label"></label>
                <div class="col-md-9">
                    <button class="btn btn-primary col-md-12">RESERVAR</button>
                </div>
            </div>

        </form>
    </div>
</template>

<script>
import axios from 'axios';
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'

export default {
    name: 'PostFormAxios',
    data(){
        return{
            form: {
                Nombre: '',
                Destino: '',
                Hotel: '',
                Habitaciones: '',
                valor: '',
                Fecha_entrada: '',
                Fecha_salida: ''
            }
        }
    },
    methods:{
        submitForm(){
            console.log(this.form)
            axios.post('http://127.0.0.1:8000/reserva/', this.form)
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

.distancia6{
  margin: 50px auto;
}
</style>
