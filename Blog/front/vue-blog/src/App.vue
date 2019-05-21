<template>
  <div id="app">
    <Menu>
    </Menu>
    <router-view/>
  </div>
</template>

<script>
  import Menu from '@/components/Menu.vue'
  export default {
    name: 'app',
    components: {
      Menu
    },
    created(){
      if (sessionStorage.getItem("token")){
        this.$store.commit("set_auth", true)
        $.ajaxSetup({
            headers: {'Authorization': "Token " + sessionStorage.getItem('token')},
        });
        this.$store.dispatch("user_info")
      }
      else {
        this.$store.commit("set_auth", false)
      }
    },
  }
</script>


<style lang="scss">

  .alert-light {
    border-color: #ffc9f6
  }
  .user_image {
    width: 64px;
    height: 64px;
    border-radius: 50%;
    margin-right: 5px;
    margin-left: 14px
  }
  .material-icons{
        color: lightpink;
        /* line-height: 20px; */
        /* padding: 6px 16px; */
        position: inherit;
        padding: 3px;
        top: 5px;
        cursor: pointer;
  }
  .form-section {
      background: #ffc9f6;
      padding: 20px;
      border: 1px solid #ffc9f6;
      box-sizing: border-box;
      width: 100%;
      -webkit-box-shadow: 0 2px 3px 0 rgba(240, 79, 255, 0.21);
      -moz-box-shadow: 0 2px 3px 0 rgb(240, 79, 255, 0.21);
      box-shadow: 0 2px 3px 0 rgb(240, 79, 255, 0.21);
  }

  .form-section > h2 {
    color: #ffc9f6;
    margin-bottom: 10px;
  }
</style>
