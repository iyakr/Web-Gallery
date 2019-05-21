<template>
  <div class="col-md-8">
    <div class="form-section">
        <p class="mt-4 text-center" >Новый пост</p>
      <form method="post" class="form1">
        <!-- <input type="hidden" name="csrfmiddlewaretoken" value="50V3YSO7g3ReBCsCENzbbw8btkKKFWyFOCYQxGt2O1zxi1z80MwLkKONfoZXSRFu"> -->
        <div id="div_id_title" class="form-group">
          <label for="id_title" class="p1 col-form-label  requiredField">
                  Заголовок<span class=" p1 asteriskField">*</span>
                </label> <div class="">
                  <input v-model="title" type="text" name="title" maxlength="50" class="p1 textinput textInput form-control">
                </div>
              </div>
              <div  class="form-group">
                <label for="id_text" class="p1">
                  Немного текста<span class="p1 asteriskField">*</span>
                 </label>
                 <div class="">
                   <textarea v-model="text" name="text" cols="40" rows="10" class=" p1 textarea form-control"></textarea>
                 </div>
                  <div class="form-group">
                       <label for="id_image" class="p1  requiredField">
                       Добавить изображение<span class="asteriskField">*</span>
                       </label>
                       <input id="file" type="file" class="p1 mt-3 form-control-file">

                  </div>
               </div>
           <div class="form-row text-center">
        <button @click="addPost" type="button" class="button1" >Опубликовать</button>
           </div>
      </form>
    </div>
  </div>
</template>


<script>
export default {
        data() {
            return {
                title: '',
                text: '',

            }
        },
        methods: {
            goPage(item) {
                this.$router.push({name: item})
            },
            addPost() {
                      $.ajax({
                          url: this.$store.getters.get_url_server + "api/Post/MyPosts/",
                          type: "POST",
                          data: {
                              image: this.image,
                              title: this.title,
                              text: this.text,

                          },
                          success: (response) => {
                              this.$router.push({name: 'my_posts'})
                          },
                          error: (response) => {
                              console.log("False")
                              // this.$router.push({name: 'my_posts'})
                          }
                      })
                  },
          }
}
</script>


<style lang="scss">
     .p1 {
    font-family: cursive;
    font-size: 18px;

     color:  plum;

  transition: all .5s;
  }
  p {
    font-family: cursive;
    font-size: 24px;
  text-shadow: 1px 1px 1px silver,
               -1px 1px 1px silver;
     color:  #ffff;

  transition: all .5s;
  }
  h1:hover {
    text-shadow: -1px -1px 1px silver,
                 1px -1px 1px silver;
     color: white;
    }

$color: #18F7E0;

@keyframes sheen {
  0% {
    transform: skewY(-45deg) translateX(0);
  }
  100% {
    transform: skewY(-45deg) translateX(12.5em);
  }
}

.wrapper {
  display: block;
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
}
.button1 {
  padding: 0.5em 1em;
  text-align: center;
  text-decoration: none;
  color: $color;
  border: 2px solid $color;
  font-size: 14px;
  display: inline-block;
  border-radius: 0.3em;
  transition: all 0.2s ease-in-out;
  position: relative;
  overflow: hidden;
  &:before {
    content: "";
    background-color: rgba(255,255,255,0.5);
    height: 100%;
    width: 3em;
    display: block;
    position: absolute;
    top: 0;
    left: -5.5em;
    transform: skewX(-45deg) translateX(0);
    transition: none;
  }
  &:hover {
    background-color: $color;
    color: #fff;
    border-bottom: 4px solid darken($color, 10%);
    &:before {
      transform: skewX(-45deg) translateX(13.5em);
     transition: all 0.5s ease-in-out;
    }
  }
}
  .form1 {
    width: 650px;
    min-height: 500px;
    height: auto;
    border-radius: 5px;
    margin: 2% auto;
    box-shadow: 0 9px 50px hsla(20, 67%, 75%, 0.31);
    padding: 2%;
    background-image: linear-gradient(-225deg, #E3FDF5 50%, #FFE6FA 50%);
}
</style>

