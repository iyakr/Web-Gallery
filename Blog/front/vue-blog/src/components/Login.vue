<template>
  <div>
      <main class="container">
        <div class="row">
          <div class="col-md-8">
            <div class="form-section">
              <h2>Вход в аккаунт</h2>
              <form >
                <p><b>{{mess}}</b></p>
                  <div class="form-group">
                    <label for="disabledTextInput">Логин</label>
                    <input v-model="user.username" type="text" class="form-control" placeholder="Введите логин">
                  </div>
                  <div class="form-group t">
                    <label for="inputPassword5" >Пароль</label>
                    <input v-model="user.password1" placeholder="Введите пароль" type="password" id="inputPassword5" class="form-control" aria-describedby="passwordHelpBlock">

                  </div>
                <div class="form-row text-center">
                <button type="button " class="button" @click="setLogin()" >Войти</button>
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
      name: "Login",
      data() {
          return {
              user: {
                  username: "",
                  password1: ""
              },
              mess: '',
          }
      },
      methods: {
          setLogin() {
              $.ajax({
                  url: this.$store.getters.get_url_server + 'auth/token/login/',
                  type: "POST",
                  data: {
                      username: this.user.username,
                      password: this.user.password1
                  },
                  success: (response) => {
                      sessionStorage.setItem("token", response.auth_token)
                      this.$store.commit("set_auth", true)

                      $.ajaxSetup({
                          headers: {'Authorization': "Token " + sessionStorage.getItem('token')},
                      });
                      this.$router.push({name:"home"})
                  },
                  error: (response) => {
                      if (response.status === 400) {
                          this.mess = response.responseJSON.username[0]
                      }
                  }
              })
          },
      }
  }
</script>

<style lang="scss">
@import url('https://fonts.googleapis.com/css?family=Abel|Abril+Fatface|Alegreya|Arima+Madurai|Dancing+Script|Dosis|Merriweather|Oleo+Script|Overlock|PT+Serif|Pacifico|Playball|Playfair+Display|Share|Unica+One|Vibur');
/* End Fonts */
/* Start Global rules */
* {
    padding: 0;
    margin: 0;
    box-sizing: border-box;
}
/* End Global rules */

/* Start body rules */
body {
    background-image: linear-gradient(-225deg, #E3FDF5 0%, #FFE6FA 100%);
background-image: linear-gradient(to top, #a8edea 0%, #fed6e3 100%);
background-attachment: fixed;
  background-repeat: no-repeat;

    font-family: cursive;
/*   the main font */
    font-family: 'Abel', sans-serif;
opacity: .95;
/* background-image: linear-gradient(to top, #d9afd9 0%, #97d9e1 100%); */
}




/* Start form  attributes */
form {
    width: 450px;
    min-height: 500px;
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

/* the header form form */
header {
    margin: 2% auto 10% auto;
    text-align: center;
}
/* Login title form form */
header h2 {
    font-size: 250%;
    font-family: 'Playfair Display', serif;
    color: #3e403f;
}
/*  A welcome message or an explanation of the login form */
header p {letter-spacing: 0.05em;}



/* //////////////////////////////////////////// */
/* //////////////////////////////////////////// */


.input-item {
    background: #fff;
    color: #333;
    padding: 14.5px 0px 15px 9px;
    border-radius: 5px 0px 0px 5px;
}



/* Show/hide password Font Icon */
#eye {
    background: #fff;
    color: #333;

    margin: 5.9px 0 0 0;
    margin-left: -20px;
    padding: 15px 9px 19px 0px;
    border-radius: 0px 5px 5px 0px;

    float: right;
    position: relative;
    right: 1%;
    top: -.2%;
    z-index: 5;

    cursor: pointer;
}
/* inputs form  */
input[class="form-input"]{
    width: 240px;
    height: 50px;

    margin-top: 2%;
    padding: 15px;

    font-size: 16px;
    font-family: 'Abel', sans-serif;
    color: #5E6472;

    outline: none;
    border: none;

    border-radius: 0px 5px 5px 0px;
    transition: 0.2s linear;

}
input[id="txt-input"] {width: 250px;}
/* focus  */
input:focus {
    transform: translateX(-2px);
    border-radius: 5px;
}

/* //////////////////////////////////////////// */
/* //////////////////////////////////////////// */

/* input[type="text"] {min-width: 250px;} */
/* buttons  */
button {
    display: inline-block;
    color: #252537;

    width: 280px;
    height: 50px;

    padding: 0 20px;
    background: #fff;
    border-radius: 5px;

    outline: none;
    border: none;

    cursor: pointer;
    text-align: center;
    transition: all 0.2s linear;

    margin: 7% auto;
    letter-spacing: 0.05em;
}
/* Submits */
.submits {
    width: 48%;
    display: inline-block;
    float: left;
    margin-left: 2%;
}
/* buttons hover */
button:hover {
    transform: translatey(3px);
    box-shadow: none;
}

/* buttons hover Animation */
button:hover {
    animation: ani9 0.4s ease-in-out infinite alternate;
}
@keyframes ani9 {
    0% {
        transform: translateY(3px);
    }
    100% {
        transform: translateY(5px);
    }
}
$color: #7AE5CF;

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
  padding: 0.5em 3em;
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