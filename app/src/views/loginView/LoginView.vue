<template>
  <AuthForm
    heading="Вход"
    :inputs="inputs"
    :additional="additional"
    button-text="Войти"
  >

    <template v-slot:agreement>
      <RouterLink to="#" class="form-page__agreement-link">
        Забыли пароль?
      </RouterLink>
    </template>

  </AuthForm>
</template>

<script>
import AuthForm from '@/components/authForm/AuthForm.vue'
  export default {
    components: {
      AuthForm,
    },
    name: 'LoginPage',
    layout: 'auth',
    data () {
      return {
      inputs: [
        { type: 'email', placeholder: 'Почта или никнейм', name: 'email' },
        { type: 'password', placeholder: 'Пароль', name: 'password' },
      ],
      additional: {
        href: '/signup',
        text: 'Нет аккаунта? Зарегистрироваться'
      }
    }
  }
}
</script>

<style lang="scss" scoped>

</style>