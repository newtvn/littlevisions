<template>
    <NavBar />
    <RouterView />
</template>
<script>
import NavBar from '@/components/navigation/NavBar.vue';

export default {
    components: {
         NavBar
    },
    data() {
        return {
            compositions: [
                {
                    id: "shshs",
                    text: "a very long text",
                    title: "Mid-term composition refining",
                    comment: null,
                    progress: 20
                }
            ]
        }
    }
}
</script>
<style lang="scss">
@import '@/styles/compositions.scss'
</style>