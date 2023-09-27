<template>
    <div class="story-build-screen">

        <StoryPanel/>

        <div class="storyboard-panel story-build-panel">

            <p class="panel-subtitle" style="text-align: center;">Your Storyboard</p>

            <div class="storyboard-panel-list">
                <div class="storyboard-item scale-hover">
                    <img src="https://static.wikia.nocookie.net/spongebob/images/7/72/No_Weenies_Allowed_019.png/" alt="">
                </div>
                <div class="storyboard-item scale-hover">
                    <img src="https://rhetoricandpopularculture.files.wordpress.com/2013/02/spongebob_mr_krabs_and_plankton.jpg" alt="">
                </div>
            </div>
        </div>

        <CharacterPanel/>

        



    </div>
</template>
<style lang="scss">
@import '@/styles/story-build.scss';
</style>
<script>
import CharacterPanel from '@/components/story-build/CharacterPanel.vue'
import StoryPanel from '@/components/story-build/StoryPanel.vue'
export default {
    components: {
        CharacterPanel,StoryPanel
    }
}
</script>