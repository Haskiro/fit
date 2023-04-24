<template>
  <header-component />
  <router-view />
  <footer-component />
</template>

<script>
import HeaderComponent from "@/components/headerComponent/HeaderComponent.vue";
import FooterComponent from "@/components/footerComponent/FooterComponent.vue";


export default {
  name: "App",
  components: {
    HeaderComponent,
    FooterComponent,
  },
  data: () => ({}),
};
</script>

<style lang="scss">
@import url("@/styles/global.scss");

#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}
</style>
