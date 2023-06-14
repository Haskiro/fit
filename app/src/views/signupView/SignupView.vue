<template>
	<div class="form-page">
		<h1 class="form-page__heading heading heading--h3">Регистрация</h1>

		<div v-if="showError" class="form-page__error">
			<p>ошибка при регистрации</p>
		</div>
		<form class="form" @submit.prevent="register">
			<div v-if="isLoading" class="form-page__is-loading">Загрузка...</div>
			<div v-for="(input, i) in inputs" :key="i" class="form__input-container">
				<label :for="i" class="visually-hidden">
					{{ input.placeholder }}
				</label>
				<input
					:id="i"
					v-model="form[input.name]"
					:type="input.type"
					:name="input.name"
					class="input"
					:placeholder="input.placeholder"
					required
				/>
			</div>

			<p class="form-page__link-text">
				Регистрируясь, вы соглашаетесь с
				<NuxtLink to="#" class="form-page__link-link"> правилами пользовательского соглашения </NuxtLink>
			</p>

			<input
				type="submit"
				:value="buttonText"
				:disabled="isLoading"
				class="form-page__btn btn btn--filled btn--huge"
			/>
		</form>

		<RouterLink v-if="additional.hasOwnProperty('href')" :to="additional.href" class="form-page__link">
			{{ additional.text }}
		</RouterLink>
	</div>
</template>

<script>
import axios from 'axios';
export default {
	name: 'SignupPage',
	data() {
		return {
			form: {
				username: '',
				password: '',
				email: '',
				first_name: '',
				last_name: '',
			},
			buttonText: 'Регистрация',
			inputs: [
				{ type: 'text', placeholder: 'Введите никнейм', name: 'username' },
				{ type: 'email', placeholder: 'Введите email', name: 'email' },
				{ type: 'text', placeholder: 'Имя', name: 'first_name' },
				{ type: 'text', placeholder: 'Фамилия', name: 'last_name' },
				{ type: 'password', placeholder: 'Введите пароль', name: 'password' },
			],
			additional: {
				href: '/login',
				text: 'Уже есть аккаунт? Войти',
			},
			isLoading: false,
			showError: false,
		};
	},
	methods: {
		register() {
			this.isLoading = true;
			axios
				.post(`${process.env.VUE_APP_API_URL}auth/register/`, this.form)
				.then(() => {
					this.isLoading = false;
					this.$router.push('/login');
				})
				.catch((err) => {
					this.showError = true;
					console.error(err);
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

	&__heading {
		margin-bottom: 3.5rem;
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
		color: #ffffff;
		text-decoration: none;
		margin-top: 1.25rem;
		font-size: 14px;
		font-family: 'Roboto', sans-serif;
		font-weight: 200;
	}

	&__link-text {
		display: block;
		width: 100%;
		text-align: center;
		font-weight: lighter;
		color: #ffffff;
		text-decoration: none;
		margin-top: 0.5rem;
		font-size: 14px;
		font-family: 'Roboto', sans-serif;
		font-weight: 200;
	}

	&__link-link {
		color: #0fb9bc;
	}

	&__btn {
		margin-top: 1.25rem;
		display: inline-block;
		cursor: pointer;
		border: none;
		font: inherit;
		font-family: 'Roboto', sans-serif;
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
