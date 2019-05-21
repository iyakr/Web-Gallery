import Vue from 'vue'
import Router from 'vue-router'
import Home from './views/Home.vue'
import Login from './components/Login.vue'
import Exit from './components/Exit.vue'
// import MyPosts from './components/MyPosts.vue'
import MyPosts from './views/My_posts.vue'
import Profile from './views/Profile.vue'
import PostDetail from './components/PostDetail.vue'
import DeletePost from './components/DeletePost.vue'
import AddPost from './components/AddPost.vue'
import EditPost from './components/EditPost.vue'
import Registr from './components/Registr.vue'
import AdminPosts from './components/AdminPosts'

import store from './store'

Vue.use(Router)

export default new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/',
      name: 'home',
      component: Home
    },
    {
      path: '/login',
      name: 'login',
      component: Login
    },
    {
      path: '/exit',
      name: 'exit',
      component: Exit
    },
    {
      path: '/add',
      name: 'addPost',
      component: AddPost
    },
    {
      path: '/my',
      name: 'my_posts',
      component: MyPosts,
      beforeEnter: (to,from, next) => {
        if (store.getters.get_auth){
          next()
        }
        else {
          next({name: 'home'})
      }
    }
    },
    {
      path: '/profile',
      name: 'profile',
      component: Profile,

    },
    {
      path: '/post/:postId',
      name: 'post_detail',
      component: PostDetail
    },
    {
      path: '/delete/:Id',
      name: 'delete_post',
      component: DeletePost,
    },
    {
      path: '/edit/:Id',
      name: 'edit_post',
      component: EditPost,
    },
    {
      path: '/reg/',
      name: 'reg',
      component: Registr,
    },
      {
      path: '/adminposts',
      name: 'adminposts',
      component: AdminPosts
    },
  ]
})
