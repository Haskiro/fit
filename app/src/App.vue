<template>
<<<<<<< HEAD
  <header-component />
  <router-view />
  <footer-component />
=======
	<!-- <header-component /> -->
	<router-view />
	<!-- <footer-component /> -->
>>>>>>> 117bfc11d69686dbe8c898c6c7a707bac50c2d9b
</template>

<script>
import HeaderComponent from "@/components/headerComponent/HeaderComponent.vue";
import FooterComponent from "@/components/footerComponent/FooterComponent.vue";

export default {
<<<<<<< HEAD
  name: "App",
  components: {
    HeaderComponent,
    FooterComponent,
  },
  data: () => ({}),
=======
	name: 'App',
	components: {
		// HeaderComponent,
		// FooterComponent,
	},
	data: () => ({}),
>>>>>>> 117bfc11d69686dbe8c898c6c7a707bac50c2d9b
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
