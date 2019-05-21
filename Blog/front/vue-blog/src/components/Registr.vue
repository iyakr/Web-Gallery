<template>
  <div>
    <main class="container">
      <div class="row">
        <div class="col-md-8">
            <div class="form-section">
              <h2>Регистрация на сайте</h2>
              <form method="post">
                <div class="form-group">
                  <label class="col-form-label  requiredField">
                        Логин<span class="asteriskField">*</span>
                        </label>
                        <div class="">
                            <input v-model="username" type="text" maxlength="150" class="textinput textInput form-control">
                            <p id="">{{mess1}}</p>
                             <small class="form-text text-muted">Обязательное поле. Не более 150 символов. Только буквы, цифры и символы @/./+/-/_.</small>
                           </div>
                         </div>
                         <div class="form-group">
                           <label class="col-form-label  requiredField">
                          Пароль<span class="asteriskField">*</span>
                        </label> <div class="">
                          <input v-model="password1" class="textinput textInput form-control">
                          <p id="p">{{mess2}}</p>
                          <small  class="form-text text-muted"><ul>
                              <ul>
                            <a>Пароль должен содержать как минимум 8 символов.</a>
                            <a>Пароль не может состоять только из цифр.</a></ul></ul></small>
                          </div>
                        </div>
                        <div class="form-group">
                           <label class="col-form-label ">
                            Адрес электронной почты
                        </label>
                        <div class="">
                          <input v-model="email" type="email" maxlength="254" class="emailinput form-control"> </div>
                      </div>
                  <div class="form-row text-center">
                <button @click="createProfile" type="button" class="button">Зарегистрироваться</button>
                  </div>
              </form>
              <hr>
              <a @click="goPage('login')">У меня уже есть аккаунт</a>
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
                password1: '',
                mess1: '',
                mess2: '',
            }
        },
        methods: {
            goPage(item) {
                this.$router.push({name: item})
            },
            createProfile() {
                      $.ajax({
                          url: this.$store.getters.get_url_server + "api/User/reg2/",
                          type: "POST",
                          data: {
                              username: this.username,
                              email: this.email,
                              password: this.password1,
                          },
                          success: (response) => {
                              this.$router.push({name: 'login'})
                          },
                          error: (response) => {
                            if (response.status === 400) {
                                this.mess1 = response.responseJSON.username[0]
                                this.mess2 = response.responseJSON.password[0]
                            }

                          }
                      })
                  },
          }
}
</script>



<style lang="scss">
$color: #FF56FF;

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
</style>
