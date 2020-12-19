<template>
    <div id="Inicio">

      <div>
        <b-carousel
        id="carousel-1"
        v-model="slide"
        :interval="4000"
        img-width="1024"
        img-height="480"
        controls
        indicators
        background="btn-primary"

        style="text-shadow: 1px 1px 2px #333;"
        @sliding-start="onSlideStart"
        @sliding-end="onSlideEnd"
        >
      <!-- Text slides with image -->

      <b-carousel-slide
        caption="First slide"
        text="Nulla vitae elit libero, a pharetra augue mollis interdum."
        img-src="https://mdbootstrap.com/img/Photos/Slides/img%20(46).jpg"
      ></b-carousel-slide>

      <b-carousel-slide
        caption="First slide"
        text="Nulla vitae elit libero, a pharetra augue mollis interdum."
        img-src="https://mdbootstrap.com/img/Photos/Horizontal/Nature/6-col/img(117).jpg"
      ></b-carousel-slide>
    </b-carousel>
  </div>


        <div class="row distancia">
            <div class="col-lg-2">
                <b-img src="https://i.ibb.co/RSYwTQf/Cartagena.jpg" height="200" width="205"></b-img>
                <h6>Cartagena</h6>
                <p><a class="btn navbar-dark btn-primary" href="#" role="button">Reserva Ya &raquo;</a></p>
            </div><!-- /.col-lg-4 -->
            <div class="col-lg-2">
                <b-img src="https://i.ibb.co/hgSm2PY/Santa-Marta.jpg"  height="200" width="205"></b-img>
                <h6>Santa Marta</h6>
                <p><a class="btn navbar-dark btn-primary" href="#" role="button">Reserva Ya &raquo;</a></p>
            </div><!-- /.col-lg-4 -->
            <div class="col-lg-2">
                <b-img src="https://i.ibb.co/D579z64/Medellin.jpg" height="200" width="205"></b-img>
                <h6>Medellin</h6>
                <p><a class="btn navbar-dark btn-primary" href="#" role="button">Reserva Ya &raquo;</a></p>
            </div><!-- /.col-lg-4 -->
            <div class="col-lg-2">
                <b-img src="https://i.ibb.co/r2rfMj3/Bogota.jpg" height="200" width="205"></b-img>
                <h6>Bogotá</h6>
                <p><a class="btn navbar-dark btn-primary" href="#" role="button">Reserva Ya &raquo;</a></p>
            </div><!-- /.col-lg-4 -->
            <div class="col-lg-2">
                <b-img src="https://i.ibb.co/1vRckBh/San-Andres-Colombia.jpg" height="200" width="205"></b-img>
                <h6>San Andrés</h6>
                <p><a class="btn navbar-dark btn-primary" href="#" role="button">Reserva Ya &raquo;</a></p>
            </div><!-- /.col-lg-4 -->
            <div class="col-lg-2">
                <b-img src="https://i.ibb.co/rp7fMdt/Guajira.jpg" height="200" width="205"></b-img>
                <h6>La Guajira</h6>
                <p><a class="btn navbar-dark btn-primary" href="#" role="button">Reserva Ya &raquo;</a></p>
            </div><!-- /.col-lg-4 -->
        </div><!-- /.row -->
    </div>
</template>

<script>
    export default {
      
        name: "Inicio",
        data:function(){
            return {
                username: "none"
            }
        },
        created: function(){
            this.username = this.$route.params.username
        }
    }

</script>







<style>
/* Carousel base class */
.carousel {
  margin-bottom: 0rem;
  height: 300px;
}
/* Since positioning the image, we need to help out the caption */
.carousel-caption {
  bottom: 3rem;
  z-index: 10;
  
}
/* Declare heights because of positioning of img element */
.carousel-item {
  height: 32rem;
  height: 300px;
}
.carousel-item > img {
  position: absolute;
  top: 0;
  left: 0;
  min-width: 100%;
  height: 32rem;
}
.row-header{
    margin: 0px auto;
    padding: 0px auto;
}
.row-content{
    margin: 10px auto;
    padding: 50px 0px 50px 0px;
    border-bottom: 1px ridge;
    min-height: 400px;
}
.distancia0{
  margin: 0px auto;
}
.distancia{
  margin: 20px auto;
}
</style>