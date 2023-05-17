<template>
	<AuthForm heading="Регистрация" :inputs="inputs" :additional="additional" button-text="Зарегистрироваться">
		<template #agreement>
			Регистрируясь, вы соглашаетесь с
			<RouterLink to="#" class="form-page__agreement-link"> правилами пользовательского соглашения </RouterLink>
		</template>
	</AuthForm>
</template>

<script>
import AuthForm from '@/components/authForm/AuthForm.vue';
export default {
	name: 'SignupPage',
	components: {
		AuthForm,
	},
	layout: 'auth',
	data() {
		return {
			inputs: [
				{ type: 'text', placeholder: 'Введите никнейм', name: 'username' },
				{ type: 'email', placeholder: 'Введите email', name: 'email' },
				{ type: 'password', placeholder: 'Введите пароль', name: 'password' },
			],
			additional: {
				href: '/login',
				text: 'Уже есть аккаунт? Войти',
			},
		};
	},
};
</script>

<style lang="scss" scoped>
.form-page {
	&__agreement-link {
		text-decoration: none;
		color: #19cbfc;
		font-weight: 100;
	}
}
</style>
