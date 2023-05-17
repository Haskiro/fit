<template>
	<div class="train-program">
		<div class="train-program__teaser">
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
		<ul class="train-program__exercise-list exercise-list">
			<li v-for="(item, i) in trainProgram.exerciseList" :key="i" class="exercise-list__item">
				<p class="exercise-list__item-name">
					{{ item.name }}
				</p>
				<p class="exercise-list__item-quantity">
					{{ item.quantity }}
				</p>
				<img :src="'./assets/' + item.img" alt="exercise photo" />
			</li>
		</ul>
	</div>
</template>

<script>
import bgImage from './assets/bg-image.jpg';
// import bgImage2 from "./assets/bg-image2.jpg";
export default {
	name: 'ProgramDetailView',
	components: {},
	data: () => ({
		breadcrumbs: [
			{ name: 'Главная', to: '/#' },
			{ name: 'Программы', to: '/#' },
			{ name: 'Упругая попа', to: '/#' },
		],
		trainProgram: {
			id: 1,
			bgImage: bgImage,
			title: 'Фулбоди для мужчин',
			description:
				'Комплекс упражнений на всё тело для мужчин. Подходит для начинающих и опытных спортсменов после длительного перерыва. Программа универсальная. Подходит как для набора мышечной массы на начальном этапе, так и для похудения при соответствующем плане питания.',
			info: [
				{ title: 'Цель', description: 'Набор массы' },
				{ title: 'Длительность цикла:', description: '8 недель' },
				{ title: 'Время тренировки:', description: '75-90 минут' },
				{ title: 'Место тренировок:', description: 'Спортзал' },
				{ title: 'Тренировок в неделю:', description: '4 дня' },
				{ title: 'Уровень подготовки:', description: 'Любитель' },
			],
			exerciseList: [
				{
					name: 'Приседания со штангой на плечах',
					quantity: '4х12,10,8,6',
					img: 'exercises1.jpg',
				},
				{
					name: 'Приседания со штангой на плечах',
					quantity: '4х12,10,8,6',
					img: 'exercises1.jpg',
				},
				{
					name: 'Приседания со штангой на плечах',
					quantity: '4х12,10,8,6',
					img: 'exercises1.jpg',
				},
				{
					name: 'Приседания со штангой на плечах',
					quantity: '4х12,10,8,6',
					img: 'exercises1.jpg',
				},
				{
					name: 'Приседания со штангой на плечах',
					quantity: '4х12,10,8,6',
					img: 'exercises1.jpg',
				},
				{
					name: 'Приседания со штангой на плечах',
					quantity: '4х12,10,8,6',
					img: 'exercises1.jpg',
				},
			],
		},
		filters: {
			difFilter: {
				isActive: false,
				direction: 'none    ',
			},
			newFilter: {
				isActive: false,
			},
		},
	}),
};
</script>

<style lang="scss" scoped>
.train-program {
	&__teaser {
		height: calc(90vh - 127px);
		max-height: 900px;
		width: 100%;
		box-sizing: border-box;
		background: url(./assets/bg-image.jpg);
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
