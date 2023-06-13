<template>
	<div class="train-programs">
		<div class="train-programs__teaser">
			<div class="container train-programs__teaser-body">
				<p class="train-programs__text">Программы тренировок в тренажерном зале</p>
				<div class="train-programs__control control">
					<form class="control__search" @submit.prevent="handleSearch">
						<input type="text" class="control__input" placeholder="Поиск по названию..." name="value" />
						<button type="submit" class="control__search-button">поиск</button>
					</form>
					<div class="control__filters">
						<p class="control__text">Сортировать:</p>
						<button
							type="button"
							class="control__button"
							:class="{
								active: filters.difFilter.isActive,
								up: filters.difFilter.direction === 'up',
								down: filters.difFilter.direction === 'down',
							}"
							@click="() => handleFilter('dif')"
						>
							по сложности
							<svg
								v-if="filters.difFilter.isActive"
								width="9"
								height="7"
								viewBox="0 0 9 7"
								xmlns="http://www.w3.org/2000/svg"
								fill="#D9D9D9"
							>
								<path d="M4.5 0L8.39711 6.75H0.602886L4.5 0Z" />
							</svg>
						</button>
						<button
							type="button"
							class="control__button"
							:class="{
								active: filters.newFilter.isActive,
							}"
							@click="() => handleFilter('new')"
						>
							сначала новые
						</button>
					</div>
				</div>
			</div>
		</div>
		<ul class="train-programs__list container">
			<li v-for="program in programs" :key="program.id" class="train-programs__item">
				<router-link :to="`/train-programs/${program.id}`">
					<TrainProgramCard v-bind="program" />
				</router-link>
			</li>
		</ul>
	</div>
</template>

<script>
import TrainProgramCard from '@/components/trainProgramCard/TrainProgramCard.vue';
// import { mapState } from 'vuex';
import store from '@/store';

export default {
	name: 'TrainProgramView',
	components: { TrainProgramCard },
	data: () => ({
		filters: {
			difFilter: {
				isActive: false,
				direction: 'none    ',
			},
			newFilter: {
				isActive: false,
			},
		},
		programs: [],
	}),
	// computed: {
	// 	...mapState({
	// 		programs: (state) => state.programs.programs,
	// 	}),
	// },

	async mounted() {
		await store.dispatch('programs/fetchAllPrograms');
		this.programs = store.state.programs.programs;
	},
	methods: {
		handleSearch: function (ev) {
			const str = ev.target[0].value;
			console.log(store.getters['programs/searchProgramsByTitle'](str));
			this.programs = store.getters['programs/searchProgramsByTitle'](str);
		},
		handleFilter: function (type) {
			switch (type) {
				case 'dif':
					if (!this.filters.difFilter.isActive) {
						this.filters.difFilter = {
							isActive: true,
							direction: 'up',
						};
						this.programs = store.getters['programs/sortProgramsByComplexity']('up');
					} else if (this.filters.difFilter.direction === 'up') {
						this.filters.difFilter.direction = 'down';
						this.programs = store.getters['programs/sortProgramsByComplexity']('down');
					} else {
						this.filters.difFilter = {
							isActive: false,
							direction: 'none',
						};
					}
					break;
				case 'new':
					this.filters.newFilter.isActive = !this.filters.newFilter.isActive;
					this.programs = store.getters['programs/sortProgramsByNewness'];
			}
		},
	},
};
</script>

<style lang="scss" scoped>
.train-programs {
	&__teaser {
		// height: calc(100vh - 127px);
		height: 510px;
		max-height: 900px;
		width: 100%;
		box-sizing: border-box;
		background: url(./assets/bg-image.jpg);
		background-position: center;
		background-repeat: no-repeat;
		background-size: cover;
		padding: 35px 0px;

		// @media (max-width: 1024px) {
		// 	height: calc(70vh - 127px);
		// }
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
	&__text {
		font-style: normal;
		font-weight: 400;
		font-size: 34px;
		line-height: 58px;
		text-align: center;
		color: #ffffff;

		@media (max-width: 768px) {
			font-size: 24px;
		}
	}
	&__control {
		position: absolute;
		bottom: 0;
		left: 20px;
	}
	&__list {
		display: grid;
		grid-template-columns: repeat(2, 1fr);
		gap: 10px;
		margin-bottom: 240px;
		margin-top: 20px;

		@media (max-width: 640px) {
			grid-template-columns: 1fr;
		}
	}
	&__item {
		& a {
			text-decoration: none;
		}
	}
}
.control {
	width: calc(100% - 20px);
	&__search {
		width: 50%;
		position: relative;

		@media (max-width: 1024px) {
			width: 70%;
		}

		@media (max-width: 768px) {
			width: calc(100% - 20px);
		}
	}
	&__input {
		height: 33px;
		width: 100%;
		padding: 0 114px 0 24px;
		background: #ffffff;
		border-radius: 2px;
		border: none;
		font-weight: 400;
		font-size: 13px;
		line-height: 18px;
		color: black;
		&::placeholder {
			color: #4d4d4d;
		}
	}
	&__filters {
		margin-top: 20px;
		display: grid;
		grid-template-columns: 90px repeat(2, 130px);
		gap: 13px;
		align-items: center;

		@media (max-width: 420px) {
			grid-template-columns: repeat(2, 130px);
		}
	}
	&__text {
		font-weight: 400;
		font-size: 12px;
		line-height: 20px;
		color: white;

		@media (max-width: 420px) {
			grid-column: span 2;
			grid-row: span 1;
		}
	}
	&__search-button {
		position: absolute;
		top: 0;
		right: 0;
		width: 89px;
		height: 33px;
		background: #0fb9bc;
		border-radius: 0px 2px 2px 0px;
		border: none;
		color: white;
		font-weight: 400;
		font-size: 13px;
		line-height: 18px;
		cursor: pointer;
	}
	&__button {
		width: 100%;
		height: 28px;
		border: 1px solid #b8c3cd;
		border-radius: 14px;
		background: rgba(0, 0, 0, 0.5);
		font-weight: 400;
		font-size: 12px;
		line-height: 20px;
		color: #b8c3cd;
		cursor: pointer;

		&.active {
			background: #b8c3cd;
			color: black;
			& svg {
				fill: black;
			}

			&.down svg {
				rotate: 180deg;
			}
		}
	}
}
</style>
