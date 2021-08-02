<template>
    <div id="wrapper">
        <nav class="navbar is-dark">
            <div class="navbar-brand">
                <router-link to="/" class="navbar-item">
                    <strong>Final project</strong>

                </router-link>
                <a class="navbar-burger" aria-label="menu" aria-expanded="false" data-target="navbar-menu" @click="showMobileMenu = !showMobileMenu">
                    <span aria-hidden="true"></span>
                    <span aria-hidden="true"></span>
                    <span aria-hidden="true"></span>
                </a>
            </div>
            <div class="navbar-menu" id="navbar-menu" v-bind:class="{'is-active': showMobileMenu}" >
                <div class="navbar-end">
                    <router-link to="/category1" class="navbar-item">category1</router-link>
                    <router-link to="/category2" class="navbar-item">category2</router-link>

                    <div class="navbar-item">
                        <div class="buttons">
                            <router-link to="/log-in" class="button is-light">Log in</router-link>

                            <router-link to="/cart" class="button is-success">
                                <span class="icon"><i class="fas fa-shopping-cart"></i></span>
                                <span>Cart</span>
                            </router-link>
                        </div>

                    </div>

                </div>

            </div>
        </nav>

        <section class="section">
            <router-view/>
        </section>
        <footer>
            <p class="has-text-centered">Copyright (c) 2021</p>
        </footer>
    </div>
</template>

<script>
    export default {
        data(){
            return {
                showMobileMenu: false,
            }
        }
    }
</script>

<style lang="scss">
    @import '../node_modules/bulma';
</style>
