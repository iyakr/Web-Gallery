 <template>
    <div>
      <nav class="top-menu">
  <ul class="menu-main">
    <li class="left-item"><a  href="#" @click="goPage('home')"> Главная</a></li>
   <li class="left-item"><a  v-if="auth"  @click="goPage('my_posts')" href="#" >Моя галерея</a></li>
       <li class="left-item"><a v-if= "auth" @click="goPage('addPost')" href="#" >Создать пост</a></li>
     <!-- {% if user.is_authenticated %} -->
         <li class="right-item "> <a v-if="auth" @click="logout" href="#">Выйти</a></li>
      <li class="right-item"><a v-if="auth" @click="goPage('profile')" href="#">Личный кабинет</a></li>
       <li class="right-item"><a @click="goPage('adminposts')" href="#">Супер</a></li>




    <!-- {% else %} -->
    <li class="right-item"><a v-if="!auth" href="#" @click="goPage('reg')">Регистрация</a></li>
    <li class="right-item"><a v-if="!auth" href="#" @click="goPage('login')">Войти</a></li>
                <!-- {% endif %} -->
</ul>
  <a @click="goPage('home')" class="navbar-logo" href=""><img src="../components/logo.png" style="width:120px" ></a>
      </nav>
    </div>
</template>

<script>

export default {
      name: "Menu",
      computed: {
        auth() {
            if (this.$store.getters.get_auth) return true
            else return false
        },
          superuser() {
            if (this.$store.getters.get_superuser) return true
              else return false
          }
    },
      // mixins: [
      //     auth
      // ],
      methods: {
          goPage(item) {
              this.$router.push({name: item})
          },

          logout() {
              this.$store.commit("set_auth", false)
              sessionStorage.removeItem("token")
              $.ajaxSetup({
                  headers: {'Authorization': ""},
              });
              window.location = '/exit'
          }
      }
}
</script>

<style lang="scss">

    footer{
      padding: 15px;
      background: #f8c6ff;
      color: #f8c6ff;
      float: left;
      width: 100%;
      margin-top: 50px;
    }
    footer a {color: #08c9f8}
    footer a:hover {color: #f8c6ff}

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


  @import url('https://fonts.googleapis.com/css?family=Arimo');
.top-menu {
  position: relative;
  background: rgba(34,34,34,.2);
}
.menu-main {
  list-style: none;
  margin: 0;
  padding: 0;
}
.menu-main:after {
  content: "";
  display: table;
  clear: both;
}
.left-item {float: left;}
.right-item {float: right;}
.navbar-logo {
  position: absolute;
  left: 50%;
  top: 50%;
  transform: translate(-50%,-50%);
}
.menu-main a {
  text-decoration: none;
  display: block;
  line-height: 80px;
  padding: 0 20px;
  font-size: 18px;
  letter-spacing: 2px;
  font-family: 'Menlo',cursive;

  color: white;
  transition: .3s linear;
}
.menu-main a:hover {background: rgba(0,0,0,.3);}
@media (max-width: 830px) {
.menu-main {
  padding-top: 90px;
  text-align:left;
}
.navbar-logo {
  position: absolute;
  left: 50%;
  top: 5px;
  transform: translateX(-50%);
}
.menu-main li {
  float: none;
  display: inline-block;
}
.menu-main a {
  line-height: normal;
  padding: 20px 15px;
  font-size: 16px;
}
}
@media (max-width: 630px) {
.menu-main li {display: block;}
}
</style>
