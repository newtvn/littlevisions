<template>
    <NavBar />
    <div class="container">

        <router-view v-slot="{ Component,route }">
            <transition name="fade" mode="out-in">
                <component :is="Component" :key="route.path" />
            </transition>
        </router-view>
    </div>
    </template>
<script>
import NavBar from "@/components/navigation/NavBar.vue";

export default {
    name: "StoryView",
    components: {
        NavBar
    },

}
</script>
<style lang="scss">
@import '@/styles/story.scss';


.fade-enter-active,
.fade-leave-active {
    transition: opacity 0.3s;
}

.fade-enter,
.fade-leave-to {
    opacity: 0;
}
</style>
