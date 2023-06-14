<template>
	<div ref="page" class="form-page">
		<h1 class="form-page__heading heading heading--h3">Вход</h1>

		<div v-if="showError" class="form-page__error">
			<p>Ошибка при входе</p>
		</div>

		<form class="form" @submit.prevent="login">
			<div v-if="isLoading" class="form-page__is-loading">Загрузка...</div>
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
					required
				/>
			</div>

			<RouterLink to="#" class="form-page__link"> Забыли пароль? </RouterLink>

			<input
				type="submit"
				:value="buttonText"
				class="form-page__btn btn btn--filled btn--huge"
				:disabled="isLoading"
			/>
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
			isLoading: false,
			showError: false,
		};
	},
	methods: {
		login() {
			this.isLoading = true;
			this.$store
				.dispatch('login', this.form)
				.then((response) => {
					this.isLoading = false;
					console.log(response);
					this.$router.push('/');
				})
				.catch((error) => {
					this.errors = error.response.data;
					this.showError = true;
					debugger;
					this.isLoading = false;
				});
		},
	},
};
</script>

<style lang="scss" scoped>
@use '@/styles/form.scss';
.form-page {
	font-family: 'Roboto', sans-serif;
	display: flex;
	background-color: #1e1e1e;
	flex-direction: column;
	justify-content: center;
	align-items: center;
	height: 100vh;
	padding-bottom: 2rem;
	position: relative;

	&__heading {
		margin-bottom: 3.5rem;
	}

	&__error {
		margin-bottom: 10px;
		color: red;
	}

	&__is-loading {
		font-size: 25px;
		color: #d3d0d0;
		margin-top: 10px;
	}

	&__link {
		display: block;
		width: 100%;
		text-align: center;
		font-weight: lighter;
		color: #f8f3e6;
		text-decoration: none;
		margin-top: 1.25rem;
		font-size: 14px;
		font-family: 'Roboto', sans-serif;
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
		font-family: 'Roboto', sans-serif;
		font-weight: 500;
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
