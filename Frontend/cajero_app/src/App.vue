<template>
  <div id="app">
    <div>
      <b-nav pills class="fixed-top navbar-dark1">
        <b-nav-item v-on:click="init" v-if="is_auth" active>Inicio</b-nav-item>
        <b-nav-item v-on:click="Ingreso">Registro</b-nav-item>
        <b-nav-item v-on:click="Reservar">Reserva</b-nav-item>

        <!-- <button v-on:click="getBalance" v-if="is_auth">Saldo</button> -->
        <!-- <button v-if="is_auth">Transacción</button> -->
      </b-nav>
    </div>
    
    <div class="main-component">
      <router-view></router-view>
    </div>
    
    <!-- FOOTER -->
  <footer class="footer">
        <div class="container">
           <div class="row justify-content-center">             
                <div class="col-auto">
                    <p>© Copyright 2020 Reservas.com</p>
                </div>
           </div>
        </div>
    </footer>
  </div>
</template>

<script>
export default {
  name: 'App',
  components:{},
  
  data:function() {
    return {
      is_auth:localStorage.getItem('isAuth') || false
    }
  },
  
  methods: {

    init: function(){
      if(this.$route.name != "user"){
        let username = localStorage.getItem("current_username")
        this.$router.push({name: "user", params:{ username: username }})
      }
    },

    getBalance: function(){
      if(this.$route.name != "user_balance"){
        let username = localStorage.getItem("current_username")
        this.$router.push({name: "user_balance", params:{ username: username }})
      }
    },

    Ingreso: function(){
      if(this.$route.name != "Formulario"){
        this.$router.push({name: "Formulario"})
      }
    },
    Reservar: function(){
      if(this.$route.name != "Reserva"){
        this.$router.push({name: "Reserva"})
      }
    },
  },
  beforeCreate:function() {
    localStorage.setItem('current_username','camilo24')
    localStorage.setItem('isAuth',true)
    this.$router.push({name: "user", params:{ username: 'camilo24' }})  
  }
}
</script>

<style>
.footer{
  background-color:#E1E5E8;
  margin: 0px auto;
  padding: 20px 0px 20px 0px;
}
.navbar-dark1{
  background-color: #E1E5E8;
}

</style>
  