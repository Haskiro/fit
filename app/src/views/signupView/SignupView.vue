<template>
	<div class="form-page">
		<h1 class="form-page__heading heading heading--h3">Регистрация</h1>

		<form class="form" @submit.prevent="register">
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
				/>
			</div>

			<p>
				Регистрируясь, вы соглашаетесь с
				<NuxtLink to="#" class="form-page__agreement-link"> правилами пользовательского соглашения </NuxtLink>
			</p>

			<input type="submit" :value="buttonText" class="form-page__btn btn btn--filled btn--huge" />
		</form>

		<NuxtLink v-if="additional.hasOwnProperty('href')" :to="additional.href" class="form-page__link">
			{{ additional.text }}
		</NuxtLink>
	</div>
</template>

<script>
// import store from '@/store';
import axios from 'axios';
export default {
	name: 'SignupPage',
	data() {
		return {
			form: {
				username: '',
				password: '',
				email: '',
			},
			buttonText: 'Регистрация',
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
	methods: {
		register() {
			debugger;
			// new Promise((resolve, reject) => {
			// 	axios({
			// 		url: 'http://127.0.0.1:8000/api/auth/register/',
			// 		method: 'POST',
			// 		data: this.form,
			// 	})
			// 		.then((response) => {
			// 			resolve(response);
			// 		})
			// 		.catch((error) => {
			// 			reject(error);
			// 		});
			// });
			// this.$store
			// 	.dispatch('register', this.form)
			// 	.then((response) => {
			// 		// Регистрация пользователя прошла успешно
			// 		console(response);
			// 		this.$router.push('/login');
			// 	})
			// 	.catch((error) => {
			// 		console(error);
			// 		this.error = error.response.data;
			// 	});
			// await store.dispatch('auth/register', this.form);
			// переход на следующую страницу
			//work
			axios
				.post('http://localhost:8000/api/auth/register/', this.form)
				.then(() => {
					this.$router.push('/login');
				})
				.catch((err) => {
					console.error(err);
				});
			// },
			// async register() {
			// 	try {
			// 		const data = await this.$axios.post('/api/auth/register/', this.form);
			// 		console.log(data);
			// 		this.$router.push('/login');
			// 	} catch {
			// 		console.error('Ошибка регистрации');
			// 	}
			// },
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
