<template>
	<div ref="page" class="form-page">
		<h1 class="form-page__heading heading heading--h3">Вход</h1>

		<form class="form" @submit.prevent="submit">
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
			iform: {
				login: '',
				password: '',
			},
			buttonText: 'Войти',
			inputs: [
				{ type: 'string', placeholder: 'Введите email', name: 'login' },
				{ type: 'password', placeholder: 'Введите пароль', name: 'password' },
			],
			additional: {
				href: '/signup',
				text: 'Нет аккаунта? Зарегистрироваться',
			},
		};
	},
	methods: {},
};
</script>

<style lang="scss" scoped>
.form-page {
	display: flex;
	flex-direction: column;
	justify-content: center;
	align-items: center;
	height: 100%;
	padding-bottom: 2rem;
	margin: 10%;

	&__heading {
		margin-bottom: 3.5rem;
	}

	&__link {
		display: block;
		width: 100%;
		text-align: center;
		color: #f8f3e6;
		text-decoration: none;
		margin-top: 1.25rem;
	}

	&__agreement {
		font-weight: 300;
		font-size: 0.875rem;
		line-height: 130%;
		margin-top: 0.625rem;
	}

	&__agreement-link {
		text-decoration: none;
		color: #ffffff;
		font-family: 'Gilroy';
		font-style: normal;
		font-weight: 300;
		font-size: 14px;
		line-height: 16px;
		margin-top: 20px;
		margin-bottom: 20px;
		text-align: right;
	}

	&__btn {
		margin-top: 1.25rem;
	}
}
</style>
