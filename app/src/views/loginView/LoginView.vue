<template>
	<div ref="page" class="form-page">
		<h1 class="form-page__heading heading heading--h3">Вход</h1>

		<form class="form" @submit.prevent="login">
			<div v-for="(input, i) in inputs" :key="i" class="form__input-container">
				<label :for="input.name" class="visually-hidden">
					{{ input.placeholder }}
				</label>
				<input
					:id="input.name"
					v-model="form[input.name]"
					:type="input.type"
					:name="input.name"
					class="input"
					:placeholder="input.placeholder"
				/>
			</div>

			<RouterLink to="#" class="form-page__agreement-link"> Забыли пароль? </RouterLink>

			<input type="submit" :value="buttonText" class="form-page__btn btn btn--filled btn--huge" />
		</form>

		<RouterLink v-if="additional.hasOwnProperty('href')" :to="additional.href" class="form-page__link">
			{{ additional.text }}
		</RouterLink>
	</div>
</template>

<script>
export default {
	name: 'LoginPage',
	components: {},
	data() {
		return {
			form: {
				username: '',
				email: '',
				password: '',
			},
			buttonText: 'Войти',
			inputs: [
				{ type: 'text', placeholder: 'Введите никнейм', name: 'username' },
				{ type: 'email', placeholder: 'Введите email', name: 'email' },
				{ type: 'password', placeholder: 'Введите пароль', name: 'password' },
			],
			additional: {
				href: '/signup',
				text: 'Нет аккаунта? Зарегистрироваться',
			},
		};
	},
	methods: {
		login() {
			this.$store
				.dispatch('login', this.form)
				.then((response) => {
					// Авторизация пользователя прошла успешно
					console.log(response);
					this.$router.push('/');
				})
				.catch((error) => {
					this.error = error.response.data;
				});
		},
	},
};
</script>

<style lang="scss" scoped>
@use '@/styles/form.scss';
.form-page {
	font-family: 'Gilroy';
	display: flex;
	background-color: #1e1e1e;
	flex-direction: column;
	justify-content: center;
	align-items: center;
	height: 100vh;
	padding-bottom: 2rem;

	&__heading {
		margin-bottom: 3.5rem;
	}

	&__link {
		display: block;
		width: 100%;
		text-align: center;
		font-weight: lighter;
		color: #ffffff;
		text-decoration: none;
		margin-top: 1.25rem;
		font-size: 14px;
		font-family: 'Gilroy';
	}

	&__agreement {
		font-weight: 300;
		font-size: 0.875rem;
		line-height: 130%;
		margin-top: 0.625rem;
		color: #f8f3e6;
	}

	&__btn {
		margin-top: 1.25rem;
		display: inline-block;
		cursor: pointer;
		border: none;
		font: inherit;
		font-family: 'Gilroy', sans-serif;
		font-weight: 300;
		background: #0fb9bc;
		text-decoration: none;
		padding-top: 20px;
		padding-bottom: 20px;
		border-radius: 5px;
	}
}
.visually-hidden {
	display: none;
}
</style>
