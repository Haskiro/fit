<template>
    <div class="profile-page">
        <aside class="profile-page__aside-info aside-info">
            <div class="aside-info__info-block">
                <img src="./assets/avatar.jpg" alt="" class="aside-info__avatar">
                <p class="aside-info__name">Name Surname</p>
            </div>
            <div class="aside-info__btn-list">
                <div class="aside-info__btn aside-info__btn--bg-color-blue">
                    <img src="./assets/trains-icon.svg" alt="" class="aside-info__btn-icon">
                    <p class="aside-info__btn-text">Мои тренировки</p>
                </div>
                <div class="aside-info__btn">
                    <img src="./assets/stat-icon.svg" alt="" class="aside-info__btn-icon">
                    <p class="aside-info__btn-text">Статистика</p>
                </div>
                <div class="aside-info__btn">
                    <img src="./assets/plan-icon.svg" alt="" class="aside-info__btn-icon">
                    <p class="aside-info__btn-text">План тренировок</p>
                </div>
            </div>
        </aside>
        <div class="profile-page__trains-block trains-block">
            <h2 class="trains-block__title">Мои тренировки</h2>
            <ul class="trains-block__list">
                <li 
                    class="trains-block__item"
                    v-for="program in trainProgramList"
                    :key="program.id"
                >
                    <train-program-card v-bind="program" />
                </li>
            </ul>
        </div>
    </div>
</template>

<script>
import TrainProgramCard from './components/trainProgramCard/TrainProgramCard.vue';
import bgImage from "./assets/bg-image.jpg";

export default {
    name: "ProfileView",
    components: { TrainProgramCard },
    data: () => ({
        trainProgramList: [
            {
                id: 1,
                bgImage: bgImage,
                title: "Программа тренировок в домашних условиях для мужчин",
                goal: "Набор массы",
                bodyType: "Любой",
                difficulty: "Новичок",
                isNew: true,
            },
            {
                id: 1,
                bgImage: bgImage,
                title: "Программа тренировок в домашних условиях для мужчин",
                goal: "Набор массы",
                bodyType: "Любой",
                difficulty: "Новичок",
                isNew: true,
            },
        ]
    })
}
</script>

<style lang="scss">
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700&family=Roboto:wght@400;700&display=swap');

.profile-page {
    width: 100%;
    display: flex;
    justify-content: flex-start;
    align-content: center;
    flex-direction: row;
    background-color: #EEEEEE;
}

.aside-info {
    width: 316px;
    height: auto;
    display: flex;
    justify-content: flex-start;
    align-items: flex-start;
    flex-direction: column;
    background-color: #FFFFFF;
    margin-left: 5%;
    margin-top: 40px;
    margin-bottom: 20px;

    &__info-block {
        width: 90%;
        height: 130px;
        display: flex;
        justify-content: flex-start;
        align-items: center;
        padding-top: 20px;
        padding-bottom: 20px;
    }

    &__avatar {
        width: 90px;
        height: 90px;
        border-radius: 50%;
        margin-left: 12px;
        margin-right: 12px;
    }

    &__name {
        font-family: 'Roboto', sans-serif;
        font-size: 22px;
        font-weight: 700;
    }

    &__btn-list {
        width: 100%;
        display: flex;
        justify-content: flex-start;
        align-items: center;
        flex-direction: column;
        padding: 20px 0px 20px 0px;
        border-top: 1px solid #E5E5E5;
    }

    &__btn {
        width: 90%;
        height: 40px;
        display: flex;
        align-items: center;
        justify-content: flex-start;
        margin-bottom: 8px;
        border-radius: 4px;

        &--bg-color-blue {
            background-color: #E3F2FD;
        }
    }
    
    &__btn-icon {
        margin-left: 10px;
    }

    &__btn-text {
        margin-left: 10px;
    }
}

.trains-block {
    display: flex;
    justify-content: center;
    align-items: flex-start;
    flex-direction: column;
    margin-left: 10%;
    margin-top: 40px;

    &__title {
        font-family: 'Roboto', sans-serif;
        font-size: 32px;
        font-weight: 400;
        line-height: 24px;
        color: #000000;
        margin-bottom: 40px;
    }

    &__item {
        margin-bottom: 20px;
    }
}
</style>