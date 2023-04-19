<template>
  <header-component />
  <train-program-card v-bind="programCard" />
  <router-view />
  <footer-component />
</template>

<script>
import HeaderComponent from "./components/HeaderComponent.vue";
import FooterComponent from "./components/FooterComponent.vue";
import TrainProgramCard from "./views/trainProgramsView/components/trainProgramCard/TrainProgramCard.vue";
import BgImage from "@/views/trainProgramsView/assets/bg-image.jpg";

export default {
  name: "App",
  components: {
    HeaderComponent,
    FooterComponent,
    TrainProgramCard,
  },
  data: () => ({
    programCard: {
      bgImage: BgImage,
      title: "Программа тренировок в домашних условиях для мужчин",
      goal: "Набор массы",
      bodyType: "Любой",
      difficulty: "Новичок",
      isNew: true,
    },
  }),
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
