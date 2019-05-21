<template>
  <div>
  <main class="container">
    <div class="row">
      <div class="col-md-8">
          <div class="alert alert-light">
            <h1>{{postid.title }}</h1>
            <p v-html="postid.text"></p>

            <div>
                <!-- <img v-bind:src='postid.avtor.img'  class="user_image"> -->
              </div>
              <div class="mt-2">
                <span class="text-muted" ><b class="user_image">Дата: </b>{{postid.date| filterDateTime}}</span>
                  <p><b class="user_image">Автор: </b><a href="">{{postid.avtor.username}}</a></p>
                         <a href="#" v-if="avtoriz" @click="updatePost(postid.id)" class="button1 floated1">Изменить</a>
                          <a href="#" v-if="avtoriz" @click="DeletePost(postid.id)" class="button2 floated1">Удалить</a>
              </div>
          </div>
          </div>
    </div>
   </main>
  </div>
</template>

<script>
export default {
        name:"PostDetail",

        // props: {
        //   post: ""
        // },
        data() {
          return {
            postid: ""

          }
        },
        created() {
          this.loadPost()
        },
        // beforeCreate(){
        //   $.ajax({
        //     url: this.$store.getters.get_url_server + 'api/v1/posts/'+this.$route.params.postId+'/',
        //     type:"GET",
        //     success: (response) => {
        //     this.postid=response
        //     }
        //   })
        // },
        computed: {
            auth() {
                if (this.$store.getters.get_auth) return true
                else return false
            },
            avtoriz() {
                if ((this.$store.getters.get_auth) && (this.$store.getters.get_user_info.user.username == this.postid.avtor.username || this.$store.getters.get_user_info.user.username == "Administrator")) return true
                else return false
            }
        },
        methods: {
          goPage(item) {
              this.$router.push({name: item})
          },
          like(id) {
              $.ajax({
                  url: this.$store.getters.get_url_server + "api/Post/like/",
                  type: "POST",
                  data: {
                      pk: id,
                  },
                  success: (response) => {
                      this.loadPost()
                  },
                  error: (response) => {
                      console.log("False")
                  }
              })
          },
          loadPost() {
            $.ajax({
              url: this.$store.getters.get_url_server + 'api/Post/Posts/'+this.$route.params.postId+'/',
              type:"GET",
              success: (response) => {
              this.postid=response
              }
            })
          },
          DeletePost(id) {
            this.$router.push({ name: 'delete_post', params: {Id: id }})
          },
          updatePost(id) {
            this.$router.push({ name: 'edit_post', params: {Id: id }})
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
  .floated {
      display: inline-block;
      float:right;
      margin-left:5px;
}
    .floated1 {
  float:left;
  margin-right:5px;
}
  .button2 {
    padding: 0.5em 1em;
    text-align: center;
    text-decoration: none;
    color: #FF0865;
    border: 2px solid #FF0865;
    font-size: 14px;
    display: inline-block;
    border-radius: 0.3em;
    transition: all 0.2s ease-in-out;
    position: relative;
    overflow: hidden;

    &:before {
      content: "";
      background-color: rgba(255, 255, 255, 0.5);
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
      background-color: #FF0865;
      color: #fff;
      border-bottom: 4px solid darken(#FF0865, 10%);

      &:before {
        transform: skewX(-45deg) translateX(13.5em);
        transition: all 0.5s ease-in-out;
      }
    }
  }
</style>
