<template>
    <header class="header">
        <div class="header__container">
            <a href="#" class="header__logo-block logo-block">
                <div href="#" class="logo-block__logo">
                    <img src="../assets/logo.svg" alt="" class="logo-block__logo-img">
                    <p class="logo-block__logo-name">Fit</p>
                </div>
                <p class="logo-block__slogan">Надо подкачаться!</p>
            </a>
            <nav class="header__nav-block nav-block">
                <a href="" class="nav-block__link">Главная</a>
                <a href="" class="nav-block__link">О нас</a>
                <a href="" class="nav-block__link">Тренеры</a>
                <a href="" class="nav-block__link">Программы</a>
                <a href="" class="nav-block__link">Отзывы</a>
                <a href="" class="nav-block__link">Контакты</a>
                <a href="" class="nav-block__link nav-block__link--btn">Профиль</a>
            </nav>
        </div>
    </header>
</template>

<script>
export default {

}
</script>

<style lang="scss">
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700&family=Roboto:wght@400&display=swap');

.header {
    width: 100%;
    height: 130px;
    display: flex;
    justify-content: center;
    align-items: center;
    background-color: #022637;

    &__container {
        width: 1400px;
        height: 100%;
        display: flex;
        justify-content: space-between;
        align-items: center;
    }
}

.logo-block {
    width: 190px;
    height: 116px;
    display: flex;
    justify-content: center;
    align-items: center;
    flex-direction: column;
    text-decoration: none;

    &__logo {
        width: 100%;
        height: 100px;
        display: flex;
        justify-content: space-between;
        align-items: center;
        flex-direction: row;
    }

    &__logo-img {
        width: 100px;
        height: 90px;
    }

    &__logo-name {
        font-family: 'Inter', sans-serif;
        font-size: 64px;
        font-weight: 700;
        color: #FFFFFF;
    }

    &__slogan {
        width: 100%;
        height: 26px;
        font-family: 'Inter', sans-serif;
        font-size: 20px;
        font-weight: 400;
        color: #FFFFFF;
        margin: 0;
        padding: 0;
    }
}

.nav-block {
    width: 70%;
    height: 100%;
    display: flex;
    justify-content: space-between;
    align-items: center;

    &__link {
        font-family: 'Roboto', sans-serif;
        font-size: 18px;
        font-weight: 400;
        color: #FCFCFC;
        text-transform: uppercase;
        text-decoration: none;

        &--btn {
            padding: 16px 42px;
            color: #000000;
            background-color: #0FB9BC;
        }
    }
}
</style>
