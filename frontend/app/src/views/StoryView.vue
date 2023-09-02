<template>
    <NavBar />
   <RouterView/>
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
</style>