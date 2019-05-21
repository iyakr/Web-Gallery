<template>
  <div>
  <main class="container">
    <div class="row">
      <div class="col-md-8">
        <div class="form-section">
          <p>Вы уверены,что хотите удалить пост "{{postid.title}}" ?</p>

            <form  method="POST">
            <a href="#"  @click="deletePost()" class="button2 floated1">Удалить</a>
              <a href="#" @click="goPage('my_posts')" class="button1 floated">Отмена</a>
            </form>

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
        beforeCreate(){
          $.ajax({
            url: this.$store.getters.get_url_server + '/api/Post/Posts/'+this.$route.params.postId+'/',
            type:"GET",
            success: (response) => {
            this.postid=response
            }
          })
        },
        computed: {
            auth() {
                if (this.$store.getters.get_auth) return true
                else return false
            }
        },
        methods: {
          goPage(item) {
              this.$router.push({name: item})
          },

          loadPost() {
            $.ajax({
              url: this.$store.getters.get_url_server + 'api/Post/Posts/'+this.$route.params.Id+'/',
              type:"GET",
              success: (response) => {
              this.postid=response
              }
            })
          },
          deletePost(id) {
              // if (this.$store.getters.get_user_info.user.username == this.postid.avtor.username || this.$store.getters.get_user_info.user.username == ""){
                $.ajax({
                  url: this.$store.getters.get_url_server + 'api/Post/Posts/'+this.$route.params.Id+'/',
                  type:"DELETE",
                  data: {
                      pk: id,
                  },
                  success: (response) => {
                    window.location = '/my'
                  }
                })
              // }
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
.button-group {
  list-style: none;
  display: inline-block;
}
</style>
