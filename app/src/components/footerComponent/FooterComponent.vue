<template>
    <footer class="footer">
        <div class="footer__container">
            <div class="footer__column column">
                <div class="column__logo">
                    <router-link :to="{name: 'PageInDevelopment'}" class="column__logo-block logo-block">
                        <div href="#" class="logo-block__logo">
                            <img src="./assets/logo.svg" alt="" class="logo-block__logo-img">
                            <p class="logo-block__logo-name">Fit</p>
                        </div>
                        <p class="logo-block__slogan">Надо подкачаться!</p>
                    </router-link>
                </div>
            </div>
            <div class="footer__column column">
                <div class="column__contacts" id="contacts">
                    <p class="column__text">Контакты</p>
                    <br>
                    <p class="column__text">+7 977 365 84 33</p>
                    <p class="column__text">polyfit@gmail.com</p>
                    <br>
                    <p class="column__text">По всем вопросам обращайтесь по выше указанным контактам</p>
                    <br>
                    <p class="column__text">Консультация бесплатная</p>
                </div>
            </div>
            <div class="footer__column column">
                <div class="column__socials">
                    <p class="column__text">Наши соц сети</p>
                    <a href="" class="column__soc-link soc-link"><img src="./assets/instagram-logo.svg" alt="" class="soc-link__icon"><p class="soc-link__text">Instagram</p></a>
                    <a href="" class="column__soc-link soc-link"><img src="./assets/telegram-logo.svg" alt="" class="soc-link__icon"><p class="soc-link__text">Telegram</p></a>
                    <a href="" class="column__soc-link soc-link"><img src="./assets/vk-logo.svg" alt="" class="soc-link__icon"><p class="soc-link__text">VK</p></a>
                </div>
            </div>
            <div class="footer__column column">
                <div class="column__nav">
                    <router-link :to="{name: 'PageInDevelopment'}" class="column__link column__link--btn">Главная</router-link>
                    <router-link :to="{name: 'PageInDevelopment'}" class="column__link">О нас</router-link>
                    <router-link :to="{name: 'PageInDevelopment'}" class="column__link">Тренеры</router-link>
                    <router-link :to="{name: 'PageInDevelopment'}" class="column__link">Отзывы</router-link>
                </div>
            </div>
        </div>
    </footer>
</template>

<script>
export default {

}
</script>

<style lang="scss">
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700&family=Roboto:wght@400&display=swap');

.footer {
    width: 100%;
    height: 312px;
    display: flex;
    justify-content: center;
    align-items: center;
    background-color: #022637;

    &__container {
        width: 90%;
        height: 100%;
        display: flex;
        justify-content: space-between;
        align-items: center;
    }
}

.column {
    width: 25%;
    height: 100%;
    display: flex;
    justify-content: center;
    align-items: center;

    &__logo, &__contacts, &__socials, &__nav {
        height: 250px;
        display: flex;
        justify-content: flex-start;
        align-items: flex-start;
        flex-direction: column;
    }

    &__logo {
        width: 100%;
    }

    &__contacts, &__socials, &__nav {
        width: 70%;
    }

    &__text {
        font-family: 'Roboto', sans-serif;
        font-size: 18px;
        font-weight: 400;
        line-height: 24px;
        color: #FCFCFC;
        text-decoration: none;
        margin: 0;
        padding: 0;
    }

    &__link {
        font-family: 'Roboto', sans-serif;
        font-size: 18px;
        font-weight: 400;
        line-height: 24px;
        color: #FCFCFC;
        text-decoration: none;
        padding: 8px 42px;

        &--btn {
            padding: 16px 42px;
            background-color: #942B7F;
            margin-bottom: 8px;
        }
    }
}

.soc-link {
    height: 44px;
    display: flex;
    justify-content: flex-start;
    align-items: center;
    text-decoration: none;

    &__text {
        font-family: 'Roboto', sans-serif;
        font-size: 18px;
        font-weight: 400;
        line-height: 24px;
        color: #FCFCFC;
        margin-left: 8px;
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
</style>