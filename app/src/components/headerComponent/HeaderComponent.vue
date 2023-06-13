<template>
	<header class="header">
		<div class="header__container">
			<router-link :to="{ name: 'PageInDevelopment' }" class="header__logo-block logo-block">
				<div href="#" class="logo-block__logo">
					<img src="@/assets/logo.svg" alt="" class="logo-block__logo-img" />
					<p class="logo-block__logo-name">Fit</p>
				</div>
				<p class="logo-block__slogan">Надо подкачаться!</p>
			</router-link>
			<input id="menu-toggle" class="header__menu-toggle" type="checkbox" />
			<label class="header__menu-btn" for="menu-toggle">
				<span class="header__burger"></span>
			</label>
			<nav class="header__nav-block nav-block">
				<router-link :to="{ name: 'PageInDevelopment' }" class="nav-block__link">Главная</router-link>
				<router-link :to="{ name: 'PageInDevelopment' }" class="nav-block__link">О нас</router-link>
				<router-link :to="{ name: 'PageInDevelopment' }" class="nav-block__link">Тренеры</router-link>
				<router-link :to="{ name: 'TrainProgramsPage' }" class="nav-block__link">Программы</router-link>
				<router-link :to="{ name: 'PageInDevelopment' }" class="nav-block__link">Отзывы</router-link>
				<router-link :to="{ name: 'PageInDevelopment' }" class="nav-block__link">Контакты</router-link>
				<router-link
					v-if="isLoggedIn"
					:to="{ name: 'ProfilePage' }"
					class="nav-block__link nav-block__link--btn"
					>Профиль</router-link
				>
				<router-link v-else :to="{ name: 'LoginPage' }" class="nav-block__link nav-block__link--btn"
					>Войти</router-link
				>
			</nav>
		</div>
	</header>
</template>

<script>
export default {
	computed: {
		isLoggedIn() {
			return this.$store.getters.isLoggedIn;
		},
		user() {
			return this.$store.state.auth.user;
		},
	},
};
</script>
<style lang="scss">
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700&family=Roboto:wght@400&display=swap');

.header {
	width: 100%;
	height: 130px;
	display: flex;
	justify-content: center;
	align-items: center;
	background-color: #022637;

	&__container {
		width: 90%;
		height: 100%;
		display: flex;
		justify-content: space-between;
		align-items: center;
	}

	&__menu-toggle {
		display: none;

		&:checked ~ .header__menu-btn > span {
			transform: rotate(0);
			background: rgba(0, 0, 0, 0);
		}

		&:checked ~ .header__menu-btn > span::before {
			transform: rotate(45deg);
			margin-top: 8px;
		}

		&:checked ~ .header__menu-btn > span::after {
			transform: rotate(135deg);
		}

		&:checked ~ .nav-block {
			visibility: visible;
		}
	}

	&__menu-btn {
		display: none;
		align-items: center;
		justify-content: center;
		cursor: pointer;
		z-index: 10;

		@media (max-width: 1180px) {
			display: flex;
		}
	}

	&__burger,
	&__burger::before,
	&__burger::after {
		display: block;
		position: absolute;
		width: 30px;
		height: 2px;
		background-color: #ffffff;
	}

	&__burger::before {
		content: '';
		margin-top: -8px;
	}

	&__burger::after {
		content: '';
		margin-top: 8px;
	}
}

.logo-block {
	width: 190px;
	height: 116px;
	display: flex;
	justify-content: center;
	align-items: center;
	flex-direction: column;
	text-decoration: none;

	&__logo {
		width: 100%;
		height: 100px;
		display: flex;
		justify-content: space-between;
		align-items: center;
		flex-direction: row;
	}

	&__logo-img {
		width: 100px;
		height: 90px;
	}

	&__logo-name {
		font-family: 'Inter', sans-serif;
		font-size: 64px;
		font-weight: 700;
		color: #ffffff;
	}

	&__slogan {
		width: 100%;
		height: 26px;
		font-family: 'Inter', sans-serif;
		font-size: 20px;
		font-weight: 400;
		color: #ffffff;
		margin: 0;
		padding: 0;
	}
}

.nav-block {
	width: 70%;
	height: 100%;
	display: flex;
	justify-content: space-between;
	align-items: center;

	@media (max-width: 1180px) {
		margin: 0;
		top: 0;
		left: 0;
		visibility: hidden;
		position: absolute;
		width: 100%;
		height: 100vh;
		background-color: #022637;
		justify-content: center;
		flex-direction: column;
		z-index: 9;
	}

	&__link {
		font-family: 'Roboto', sans-serif;
		font-size: 18px;
		font-weight: 400;
		color: #fcfcfc;
		text-transform: uppercase;
		text-decoration: none;

		@media (max-width: 1180px) {
			margin-bottom: 18px;
		}

		&--btn {
			padding: 16px 42px;
			color: #000000;
			background-color: #0fb9bc;
		}
	}
}
</style>
