<template>
	<div class="train-card">
		<img v-if="isNew" :src="iconSrc" alt="new" class="train-card__icon" />
		<div class="train-card__image-block" :style="{ backgroundImage: 'url(' + bgImage + ')' }">
			<p class="train-card__title">{{ title }}</p>
		</div>
		<ul class="train-card__list">
			<li class="train-card__item">
				<p class="train-card__text">Цель:</p>
				<p class="train-card__text train-card__text_bg_blue">{{ goal }}</p>
			</li>
			<li class="train-card__item">
				<p class="train-card__text">Телосложение:</p>
				<p class="train-card__text train-card__text_bg_blue">{{ bodyType }}</p>
			</li>
			<li class="train-card__item">
				<p class="train-card__text">Сложность:</p>
				<p class="train-card__text train-card__text_bg_blue">
					{{ difficulty }}
				</p>
			</li>
		</ul>
	</div>
</template>

<script>
import NewIconSrc from './assets/new-icon.svg';

export default {
	name: 'TrainProgramCard',
	components: {},
	props: {
		bgImage: String,
		title: String,
		goal: String,
		bodyType: String,
		difficulty: String,
		isNew: Boolean,
	},
	data: () => ({
		iconSrc: NewIconSrc,
	}),
};
</script>

<style lang="scss" scoped>
.train-card {
	position: relative;
	border: none;
	border-radius: 2px;
	overflow: hidden;
	box-sizing: border-box;
	&__icon {
		position: absolute;
		right: 0;
		right: 0;
		z-index: 5;
	}
	&__image-block {
		position: relative;
		width: 100%;
		height: 230px;
		background-position: center;
		background-repeat: no-repeat;
		background-size: cover;
	}
	&__title {
		position: absolute;
		left: 5px;
		bottom: 10px;
		font-weight: 400;
		font-size: 15px;
		text-transform: uppercase;
		display: inline-block;
		background: black;
		border-radius: 2px;
		padding: 0px 10px;
		line-height: 24px;
		color: white;
	}
	&__list {
		display: flex;
		justify-content: space-around;
		padding: 14px 0 23px;
		border: 1px solid #00bcd4;
		border-top: none;
		border-radius: 2px;
	}
	&__item {
	}
	&__text {
		font-weight: 400;
		font-size: 13px;
		line-height: 22px;
		text-align: center;
		color: #b2b2b2;
		margin-bottom: 3px;
		&_bg_blue {
			background: #00bcd4;
			border-radius: 2px;
			color: white;
			padding: 4px 18px;
			margin-bottom: 0;

			@media (max-width: 670px) {
				padding: 4px 10px;
			}
		}
	}
}
</style>
