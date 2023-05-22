<template>
	<HeaderComponent />
	<router-view />
	<FooterComponent />
</template>

<script>
import HeaderComponent from '@/components/headerComponent/HeaderComponent.vue';
import FooterComponent from '@/components/footerComponent/FooterComponent.vue';

export default {
	name: 'App',
	components: {
		FooterComponent,
		HeaderComponent,
	},
	data: () => ({}),
};
</script>

<style lang="scss">
@import url('@/styles/global.scss');

#app {
	font-family: Avenir, Helvetica, Arial, sans-serif;
	-webkit-font-smoothing: antialiased;
	-moz-osx-font-smoothing: grayscale;
}
</style>
