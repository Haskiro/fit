<template>
	<AuthForm heading="Вход" :inputs="inputs" :additional="additional" button-text="Войти">
		<template #agreement>
			<RouterLink to="#" class="form-page__agreement-link"> Забыли пароль? </RouterLink>
		</template>
	</AuthForm>
</template>

<script>
import AuthForm from '@/components/authForm/AuthForm.vue';
export default {
	name: 'LoginPage',
	components: {
		AuthForm,
	},
	layout: 'auth',
	data() {
		return {
			inputs: [
				{ type: 'email', placeholder: 'Почта или никнейм', name: 'email' },
				{ type: 'password', placeholder: 'Пароль', name: 'password' },
			],
			additional: {
				href: '/signup',
				text: 'Нет аккаунта? Зарегистрироваться',
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
