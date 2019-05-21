<template>
  <div class="home">
    <main class="container">
      <div class="media text-muted pt-3">
              <div class="mr-2 img-rounded" width="50%" height="50%" >
                <img class="rounded-circle" style="width:50%; height: 50%;" :src="$store.getters.get_url_media + $store.getters.get_user_info.img"> </img>
              <p class="media-body pb-3 mb-0 small lh-125 border-bottom border-gray">
                <strong class="d-block text-gray-dark">@{{$store.getters.get_user_info.user.username}} </strong>
                  <b v-if="$store.getters.get_user_info.user.email">Email: </b>{{$store.getters.get_user_info.user.email}}
              </p>
              </div>
           <a @click="goPage('profile')" href="#" class="button floated ">Изменить профиль</a>
           <a @click="goPage('addPost')" href="#" class="button floated ">Добавить новый пост</a>

     </div>
    </main>
    <Posts :posts="posts" @reload="loadPosts"></Posts>

  </div>
</template>

<script>
  import Posts from '@/components/Posts.vue'
  export default {
    name: 'home',
    components: {
      Posts
    },
    data() {
      return {
        posts: ""
      }
    },
    created() {
      this.loadPosts()

    },
    methods: {
      loadPosts() {
        $.ajax({
          url: this.$store.getters.get_url_server + 'api/Post/MyPosts',
          type:"GET",
          success: (response) => {
            this.posts=response
          }
        })
      },
       goPage(item) {
              this.$router.push({name: item})
          },
  }
  }
</script>

<style lang="scss">
    .floated {
  float:right;
  margin-right:5px;
}
  .text {
    text-align:  center;
   }
</style>