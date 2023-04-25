<template>
  <header-component />
  <router-view />
  <profile-view />
  <footer-component />
</template>

<script>
import HeaderComponent from "./components/headerComponent/HeaderComponent.vue";
import FooterComponent from "./components/footerComponent/FooterComponent.vue";
import ProfileView from "./views/profileView/ProfileView.vue";

export default {
  name: "App",
  components: {
    HeaderComponent, 
    FooterComponent, 
    ProfileView
  }
};
</script>

<style lang="scss">
@import url("@/styles/reset.scss");

#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}
</style>
