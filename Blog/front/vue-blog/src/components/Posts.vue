
<template>
  <div>
  <main class="container-fluid">
    <div class="row">
      <div class="col-md-8">
        <div class="alert" v-for="post in posts">
            <h1>{{post.title }}</h1>
            <p>{{post.text| truncate(320, '...')}}</p>
            <p> <img class="mr-2 rounded" style="width: auto; height: auto;" :src="$store.getters.get_url_media + post.image"></p>
            <div class="row">
              <div class="mt-2">
                {{post.date| filterDateTime}}
                <p class="left">
                  <a href="">{{post.avtor.username}}</a></p>
              </div>
            </div>
            <a href="" @click="loadPost(post.id)" class="button" style="right: auto">Читать далее</a>
          </div>
           </div>
     </div>
   </main>
  </div>
</template>

<script>
export default {
        name:"Posts",
        props: {
          posts: ""

        },
        create(){
          console.log(this.$store.getters.get_user_info.img)
        },
        data() {
          return {
            postid: ""
          }
        },
        computed: {
          auth() {
              if (this.$store.getters.get_auth) return true
              else return false
          }
      },
        methods: {
          like(id) {
              $.ajax({
                  url: this.$store.getters.get_url_server + "api/Post/like/",
                  type: "POST",
                  data: {
                      pk: id,
                  },
                  success: (response) => {
                      this.$emit("reload")
                  },
                  error: (response) => {
                      console.log("False")
                  }
              })
          },
          loadPost(id) {

            this.$router.push({ name: 'post_detail', params: { postId: id }})
          },
        },
        filters: {
            // Фильтр полной даты числами
            filterDateTime(item) {
                let old_date = new Date(item)
                return `
                 ${old_date.getDate()}.${old_date.getMonth()}.${old_date.getFullYear()} в ${old_date.getHours()}:${old_date.getMinutes()}`
            },

      }
}
</script>



<style lang="scss">
    a {
    font-family: cursive;
    font-size: 18px;
  text-shadow: 1px 1px 1px silver,
               -1px 1px 1px silver;
     color:  #9E4997;

  transition: all .5s;
  }
    .alert {
    width: 900px;
    min-height: 300px;
    height: auto;
    border-radius: 5px;
    margin: 2% auto;
    box-shadow: 0 9px 50px hsla(20, 67%, 75%, 0.31);
    padding: 2%;
    background-image: linear-gradient(-225deg, #E3FDF5 50%, #FFE6FA 50%);
}
/* form Container */
form .con {
    display: -webkit-flex;
    display: flex;

    -webkit-justify-content: space-around;
    justify-content: space-around;

    -webkit-flex-wrap: wrap;
    flex-wrap: wrap;

      margin: 0 auto;
}




  $color: #F575FF;

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
.button {
  padding: 0.5em 1em;
  text-align: center;
  text-decoration: none;
  color: $color;
  border: 2px solid $color;
  font-size: 16px;
  font-family: cursive;
  display: inline-block ;
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


#loginModal{
      color: mediumpurple;

      position: inherit;
      padding: 3px;
      top: 5px;
      /* left: 620px; */
      cursor: not-allowed;
}


</style>
