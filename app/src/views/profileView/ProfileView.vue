<template>
	<div class="profile-page">
		<div class="profile-page__body container">
			<aside class="profile-page__aside-info aside-info">
				<div class="aside-info__info-block">
					<img :src="user.photo" alt="" class="aside-info__avatar" />
					<p class="aside-info__name">{{ user.first_name + ' ' + user.last_name }}</p>
				</div>
				<div class="aside-info__btn-list">
					<div class="aside-info__btn aside-info__btn--bg-color-blue">
						<img src="./assets/trains-icon.svg" alt="" class="aside-info__btn-icon" />
						<p class="aside-info__btn-text">Мои тренировки</p>
					</div>
					<div class="aside-info__btn">
						<img src="./assets/stat-icon.svg" alt="" class="aside-info__btn-icon" />
						<p class="aside-info__btn-text">Статистика</p>
					</div>
					<div class="aside-info__btn">
						<img src="./assets/plan-icon.svg" alt="" class="aside-info__btn-icon" />
						<p class="aside-info__btn-text">План тренировок</p>
					</div>
				</div>
			</aside>
			<div class="profile-page__trains-block trains-block">
				<h2 class="trains-block__title">Мои тренировки</h2>
				<ul v-if="user.programs_data?.length > 0" class="trains-block__list">
					<li v-for="program in user.programs_data" :key="program.id" class="trains-block__item">
						<router-link :to="`/train-programs/${program.id}`">
							<TrainProgramCard v-bind="program" />
						</router-link>
					</li>
				</ul>
				<p v-else class="trains-block__plug">Еще ни одной тренировки не добавлено</p>
			</div>
		</div>
	</div>
</template>

<script>
import TrainProgramCard from '@/components/trainProgramCard/TrainProgramCard.vue';
import store from '@/store';

export default {
	name: 'ProfileView',
	components: { TrainProgramCard },
	data: () => ({
		user: {},
	}),
	async mounted() {
		await store.dispatch('getUserData');
		this.user = store.getters['currentUser'];
		console.log(this.user);
	},
};
</script>

<style lang="scss">
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700&family=Roboto:wght@400;700&display=swap');

.profile-page {
	background-color: #eeeeee;

	&__body {
		width: 100%;
		display: flex;
		justify-content: flex-start;
		align-content: center;
		height: 100%;
		@media (max-width: 750px) {
			flex-direction: column;
		}
	}
}

.aside-info {
	width: 316px;
	height: auto;
	display: flex;
	justify-content: flex-start;
	align-items: flex-start;
	flex-direction: column;
	background-color: #ffffff;
	margin-top: 40px;
	margin-bottom: 20px;
	@media (max-width: 750px) {
		width: 100%;
	}

	&__info-block {
		width: 90%;
		height: 130px;
		display: flex;
		justify-content: flex-start;
		align-items: center;
		padding-top: 20px;
		padding-bottom: 20px;
		@media (max-width: 1024px) {
			justify-content: center;
		}
	}

	&__avatar {
		width: 90px;
		height: 90px;
		border-radius: 50%;
		margin-left: 12px;
		margin-right: 12px;
		object-fit: cover;

		@media (max-width: 750px) {
			margin: 0;
		}

		@media (max-width: 560px) {
			width: 60px;
			height: 60px;
		}
	}

	&__name {
		font-family: 'Roboto', sans-serif;
		font-size: 22px;
		font-weight: 700;

		@media (max-width: 750px) {
			margin-left: 20px;
		}
		@media (max-width: 560px) {
			margin-left: 12px;
		}
	}

	&__btn-list {
		width: 100%;
		display: flex;
		justify-content: flex-start;
		align-items: center;
		flex-direction: column;
		padding: 20px 0px 20px 0px;
		border-top: 1px solid #e5e5e5;
	}

	&__btn {
		width: 90%;
		height: 40px;
		display: flex;
		align-items: center;
		justify-content: flex-start;
		margin-bottom: 8px;
		border-radius: 4px;

		&--bg-color-blue {
			background-color: #e3f2fd;
		}
	}

	&__btn-icon {
		margin-left: 10px;
	}

	&__btn-text {
		margin-left: 10px;
	}
}

.trains-block {
	// display: flex;
	// justify-content: center;
	// align-items: flex-start;
	// flex-direction: column;

	margin-left: 10%;
	margin-top: 40px;
	flex-grow: 2;

	&__plug {
		font-family: 'Roboto', sans-serif;
		font-size: 20px;
		font-weight: 400;
		line-height: 24px;
		color: #000000;
		text-align: center;
	}

	@media (max-width: 1024px) {
		width: 100%;
		justify-content: center;
		align-items: center;
		margin-left: 20px;
	}

	@media (max-width: 750px) {
		margin-left: 0px;
	}
	&__title {
		font-family: 'Roboto', sans-serif;
		font-size: 32px;
		font-weight: 400;
		line-height: 24px;
		color: #000000;
		margin-bottom: 40px;
		text-align: center;
	}

	&__list {
		width: 100%;
		display: grid;
		grid-template-columns: repeat(2, 1fr);
		gap: 20px;
		@media (max-width: 1100px) {
			grid-template-columns: 1fr;
		}

		@media (max-width: 750px) {
			grid-template-columns: repeat(2, 1fr);
		}

		@media (max-width: 700px) {
			grid-template-columns: 1fr;
		}
	}

	&__item {
		margin-bottom: 20px;
		& a {
			text-decoration: none;
		}
	}
}
</style>
