<template>
  <div >

    <main class="container ">
      <div class="row ">
        <div class="col-md-8">
          <div class="form-section ">
            <p>Настройка профиля</p>
            <div class="media text-muted pt-3">
              <div class="mr-2 rounded" width="100%" height="100%" >
                <img class="mr-2 rounded" style="width: auto; height: auto;" :src="$store.getters.get_url_media + $store.getters.get_user_info.img"> </img>
              </div>
              <p class="media-body pb-3 mb-0 small lh-125 border-bottom border-gray">
                <strong class="d-block text-gray-dark">@{{$store.getters.get_user_info.user.username}} </strong>
                  <b v-if="$store.getters.get_user_info.user.email">Email: </b>{{$store.getters.get_user_info.user.email}}
              </p>

            </div>
            <p class="mt-4 text-center" >Редактировать данные пользователя</p>
            <form method="POST" class="form1">

          <div class="form-group">
            <label  class="p1 col-form-label  requiredField">
                Имя пользователя<span class="asteriskField">*</span>
              </label>
              <div class="">
                <input v-model="username" type="text" maxlength="150" class="p1 textinput textInput form-control" >
                <small class="form-text text-muted">Обязательное поле. Не более 150 символов. Только буквы, цифры и символы @/./+/-/_.</small>
              </div>
            </div>
            <div class="form-group">
              <label for="id_email" class="p1 col-form-label ">
                Адрес электронной почты
              </label>
            <div class="">
              <input v-model="email" type="email" maxlength="254" class="p1 emailinput form-control" >
            </div>
          </div>
          <div class="form-group">
              <div class="p1">
              Изменить изображение профиля:
                <!-- <input type="file" id="file"> -->
              <input id="file" type="file" class="p1 mt-3 form-control-file">

            </div>
          </div>
 <div class="form-row text-center">
              <button type="button"  @click="updateProfile($store.getters.get_user_info.user.id)" class="button1" name="button">Сохранить изменения</button>
 </div>
            </form>
          </div>
         </div>
        </div>
       </main>



  </div>
</template>


<script>

export default {
  data() {
    return {
      username: '',
      email: '',
    }
  },

  methods: {
    goPage(item) {
      this.$router.push({name: item})
    },
    updateIMG(id) {
      var file = $('#file');
      // элемент, в который выведим ответ сервера
      var result = $('#result');
      // если файл выбран, то
      if (file.prop('files').length) {
        // создаём объект FormData

        var formData = new FormData();
        // добавляем в объект FormData файл
        formData.append('img', file.prop('files')[0]);
        formData.append('pk', id);
        $.ajax({
          url: this.$store.getters.get_url_server + "api/User/update-ava/" + this.$store.getters.get_user_info.id + "/",
          data: formData,
          processData: false,
          contentType: false,
          type: 'PUT',
          success: (response) => {
            window.location.reload()
          },
          error: (response) => {
            console.log("False")
          }

        })
      }
    },
    updateProfile(id) {

      this.updateIMG(this.$store.getters.get_user_info.id)

      $.ajax({
        url: this.$store.getters.get_url_server + "api/User/red/" + this.$store.getters.get_user_info.user.id + "/",
        type: "PUT",
        data: {
          pk: id,
          username: this.username,
          email: this.email,
        },
        success: (response) => {
          // this.$store.actions.user_info(this.$store.getters)
          window.location.reload()
          // this.$router.push({name: 'profile'})
        },
        error: (response) => {
          console.log("False")
        }
      })
    },
    onFileChange(e) {
      var files = e.target.files || e.dataTransfer.files;
      if (!files.length)
        return;
      this.createImage(files[0]);
      this.formData.append('file', files[0]);
      this.file = files[0];
    },
    createImage(file) {
      var image = new Image();
      var reader = new FileReader();
      var vm = this;
      reader.onload = function (e) {
        vm.image = e.target.result;
      };
      reader.readAsDataURL(file);


    }
  }
}
</script>


<style lang="scss">
  p {
    font-family: cursive;
    font-size: 24px;
  text-shadow: 1px 1px 1px silver,
               -1px 1px 1px silver;
     color:  #9E4997;

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
