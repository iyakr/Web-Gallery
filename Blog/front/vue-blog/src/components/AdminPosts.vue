<template>
  <div class="home">
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
          url: this.$store.getters.get_url_server + 'api/Post/?page=1',
          count:2,
          type:"GET",
          success: (response) => {
            this.posts=response
          }
        })
      },
  }
  }
</script>
