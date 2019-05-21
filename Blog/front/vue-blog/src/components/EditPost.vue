<template>

  <div class="col-md-8">
    <div class="form-section">
      <p>Редактирование поста </p>
      <form method="post">
      <div id="div_id_title" class="form-group">
          <label for="id_title" class="p1 col-form-label  requiredField">
                  Заголовок<span class=" p1 asteriskField">*</span>
                </label> <div class="">

                  <input v-model="title" type="text"  name="title" maxlength="50" class="p1 textinput textInput form-control">
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
                       Добавить изображение<span class="asteriskField"></span>
                       </label>
                       <input id="file" type="file" class="p1 mt-3 form-control-file">
                  </div>
               </div>
           <div class="form-row text-center">
        <button @click="updatePost" type="button" class="button1" >Сохранить</button>
           </div>
      </form>
    </div>
  </div>
</template>


<script>
export default {
  name:"EditPost",
  created() {
    this.loadPost()
  },
     data() {
      return {
          title: '',
          text: '',
          image:'',
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
          this.title=response.title,
          this.text=response.text,
          this.image=response.image

          }
        })
      },
      updatePost() {
                $.ajax({
                    url: this.$store.getters.get_url_server + 'api/Post/Posts/'+this.$route.params.Id+'/',
                    type: "PUT",
                    data: {
                        pk: this.$route.params.Id,
                        title: this.title,
                        text: this.text,
                        image: this.image,
                        avtor: this.$store.getters.get_user_info.user,
                        // user_like: this.$store.getters.get_user_info.user,
                    },
                    success: (response) => {
                        this.$router.push({name: 'My_posts'})
                    },
                    error: (response) => {
                        console.log("False")
                        // this.$router.push({name: 'My_posts'})
                    }
                })
            },
    }
}
</script>


<style>

</style>