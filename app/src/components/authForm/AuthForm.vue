<template>
	<section ref="page" class="form-page">
		<h1 class="form-page__heading heading heading--h3">
			{{ heading }}
		</h1>

		<form class="form" @submit.prevent>
			<div v-for="(input, i) in inputs" :key="i" class="form__input-container">
				<label :for="i" class="visually-hidden">
					{{ input.placeholder }}
				</label>
				<input
					:id="i"
					ref=""
					:type="input.type"
					:name="input.name"
					class="input"
					:placeholder="input.placeholder"
				/>
			</div>

			<p v-if="$slots.agreement" class="form-page__agreement">
				<slot name="agreement"> </slot>
			</p>

			<input type="submit" :value="buttonText" class="form-page__btn btn" />
		</form>

		<router-link :to="additional.href" class="form-page__link">
			{{ additional.text }}
		</router-link>
	</section>
</template>

<script>
export default {
	name: 'AuthForm',
	props: {
		heading: {
			type: String,
			required: true,
		},
		inputs: {
			type: Array,
			required: true,
		},
		additional: {
			type: Object,
			required: false,
			default: () => ({}),
		},
		buttonText: {
			type: String,
			required: true,
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
