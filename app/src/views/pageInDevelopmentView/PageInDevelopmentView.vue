<template>
	<div class="block">
		<p class="block__text">Страница в разработке</p>
	</div>
</template>

<script>
export default {
	name: 'PageInDevelopment',
};
</script>

<style lang="scss">
.block {
	width: 100%;
	height: 100vh;
	display: flex;
	justify-content: center;
	align-items: center;

	&__text {
		font-family: 'Roboto', sans-serif;
		font-size: 32px;
		font-weight: 600;
	}
}
</style>
