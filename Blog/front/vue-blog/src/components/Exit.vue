<template>
  <div class="form-section">
    <p>Вы вышли из аккаунта!</p>
    <button class="button floated1" href="" @click="goPage('login')">Войти в аккаунт</button>
    <button class="button floated1" href="" @click="goPage('reg')">Зарегистрироваться</button>
  </div>
</template>


<script>
export default {
  methods: {
      goPage(item) {
          this.$router.push({name: item})
      },
    }
}
</script>


<style>

</style>
