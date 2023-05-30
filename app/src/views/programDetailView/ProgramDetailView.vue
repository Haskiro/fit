<template>
	<div class="train-program">
		<div class="train-program__teaser" :style="{ backgroundImage: 'url(' + trainProgram.photo + ')' }">
			<div class="container train-programs__teaser-body">
				<div ccclass="train-program__bread-crumbs bread-crumbs">
					<RouterLink v-for="(crumb, i) in breadcrumbs" :key="i" :to="crumb.to" class="bread-crumbs__links">
						{{ crumb.name }}
					</RouterLink>
				</div>

				<h3 class="train-program__heading">
					{{ trainProgram.title }}
				</h3>
				<p class="train-program__description">
					{{ trainProgram.description }}
				</p>

				<div class="train-program__info-container">
					<div class="train-program__about-program">
						<button class="train-program__btn">Начать программу</button>
					</div>
					<div class="train-program__info">
						<div v-for="(item, i) in trainProgram.info" :key="i" class="train-program__info-item">
							<p class="train-program__info-title">
								{{ item.title }}
							</p>
							<p class="train-program__info-description">
								{{ item.description }}
							</p>
						</div>
					</div>
				</div>
			</div>
		</div>
		<div class="train-program__plan">
			<p class="train-program__plan-text">Тренировочный план</p>
		</div>
		<ul
			v-if="trainProgram.exercises_data && trainProgram.exercises_data.length > 0"
			class="train-program__exercise-list exercise-list"
		>
			<li v-for="(item, i) in trainProgram.exercises_data" :key="i" class="exercise-list__item">
				<p class="exercise-list__item-name">
					{{ item.title }}
				</p>
				<p class="exercise-list__item-quantity">
					{{ item.approaches }}
				</p>
				<img :src="`${host + item.photo}`" />
			</li>
		</ul>
		<p v-else class="train-program__not-found">Ни одного упражнения не найдено</p>
	</div>
</template>

<script>
import store from '@/store';
export default {
	name: 'ProgramDetailView',
	components: {},
	data: () => ({
		breadcrumbs: [
			{ name: 'Главная', to: '/#' },
			{ name: 'Программы', to: '/#' },
			{ name: 'Упругая попа', to: '/#' },
		],
		trainProgram: {},
		host: process.env.VUE_APP_HOST,
	}),
	computed: {
		isExerciseListVisible() {
			return this.trainProgram.exercises_data && this.trainProgram.exercises_data.length > 0;
		},
	},
	async mounted() {
		await store.dispatch('programs/fetchProgramById', this.$route.params.id);
		this.trainProgram = store.state.programs.checkedProgram;
	},
};
</script>

<style lang="scss" scoped>
.train-program {
	&__not-found {
		text-align: center;
		padding: 20px;
		padding-bottom: 30px;
		font-size: 30px;
	}
	&__teaser {
		height: calc(90vh - 127px);
		max-height: 900px;
		width: 100%;
		box-sizing: border-box;
		// background: url(./assets/bg-image.jpg);
		background-position: center;
		background-repeat: no-repeat;
		background-size: cover;
		padding: 20px 0px;

		@media (max-width: 1024px) {
			height: calc(70vh - 127px);
		}

		@media (max-width: 500px) {
			height: calc(85vh - 127px);
		}
	}
	&__teaser-body {
		position: relative;
		padding-top: 115px;
		height: 100%;

		@media (max-width: 1024px) {
			padding-top: 70px;
		}

		@media (max-width: 560px) {
			padding-top: 20px;
		}
	}
	&__heading {
		font-size: 44px;
		font-weight: 400;
		color: #ffffff;
		font-family: 'Rubik';
		margin-top: 24px;

		@media (max-width: 1024px) {
			font-size: 35px;
		}

		@media (max-width: 500px) {
			margin-top: 10px;
		}
	}
	&__description {
		font-family: 'Roboto';
		font-size: 15px;
		font-weight: 400;
		line-height: 24px;
		color: #ffffff;
		max-width: 520px;
		margin-top: 10px;

		@media (max-width: 1024px) {
			max-width: 450px;
		}
	}
	&__btn {
		font-family: 'Roboto', sans-serif;
		font-size: 14px;
		font-weight: 400;
		color: #fcfcfc;
		text-decoration: none;
		padding: 15px 60px;
		color: #000000;
		background-color: #0fb9bc;
		margin-top: 146px;
		border: none;

		@media (max-width: 768px) {
			padding: 15px 20px;
		}

		@media (max-width: 500px) {
			margin-top: 20px;
			margin-bottom: 10px;
		}
	}
	&__info-container {
		display: flex;
		justify-content: space-between;

		@media (max-width: 500px) {
			display: block;
		}
	}
	&__info {
		max-width: 450px;
		columns: 2;
		background: #ffffff;
		padding: 26px 80px 10px 34px;
		border-radius: 4px;
		column-gap: 80px;

		@media (max-width: 768px) {
			column-gap: 20px;
			padding: 26px 20px 10px 20px;
		}
	}
	&__info-item {
		margin-bottom: 20px;
	}
	&__info-title {
		font-family: 'Roboto';
		font-size: 12px;
		line-height: 16px;
		letter-spacing: 0.12px;
		color: #9a9a9a;
	}
	&__info-description {
		font-family: 'Roboto';
		font-weight: 400;
		font-size: 18px;
		line-height: 28px;
		letter-spacing: 0.4px;
		color: #323232;
	}

	&__plan {
		background: #f7f7f7;
		max-width: 1228px;
		margin: 20px auto;
		height: 158px;
		display: flex;
		justify-content: center;
		align-items: center;
	}
	&__plan-text {
		font-size: 32px;
		line-height: 48px;
		color: #323232;
	}

	.bread-crumbs {
		display: flex;

		&__links {
			font-size: 14px;
			line-height: 24px;
			font-weight: 400;
			color: #506690;
			margin-left: 23px;
			text-decoration: none;

			@media (max-width: 500px) {
				margin-left: 15px;
			}
		}
		&__links:first-child {
			@media (max-width: 500px) {
				margin-left: 0;
			}
		}
	}
}

.exercise-list {
	max-width: 918px;
	margin: 100px auto;
	&__item {
		display: flex;
		height: 300px;
	}
	&__item-quantity {
		padding: 134px 72px 134px 16px;
		background-color: #faedeb;
	}
	&__item-name {
		padding: 136px 15px;
		background-color: #faedeb;
	}
}
</style>
