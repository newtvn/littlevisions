<template>
    <div class="story-build-screen">
        <slideout @closing="onClosing" v-model="panelVisible" dock="bottom" size="600px">
            <StoryProceed :probabilities="probabilities" narrative="The narrative will go here"/>
        </slideout>
        <StoryPanel @continueStory="continueStory" />

        <div class="storyboard-panel story-build-panel">

            <p class="panel-subtitle" style="text-align: center;">Your Storyboard</p>

            <div class="storyboard-panel-list">
                <div class="storyboard-item scale-hover">
                    <img src="https://static.wikia.nocookie.net/spongebob/images/7/72/No_Weenies_Allowed_019.png/" alt="">
                </div>
                <div class="storyboard-item scale-hover">
                    <img src="https://rhetoricandpopularculture.files.wordpress.com/2013/02/spongebob_mr_krabs_and_plankton.jpg"
                        alt="">
                </div>
            </div>
        </div>

        <CharacterPanel />

        <div class="extra-controls row">
            <div class="row default-gap">
                <i class="fa fa-heart"></i>
                <p class="caption">Like</p>

            </div>
            <div class="row default-gap">
                <i class="fa fa-flag"></i>
                <p class="caption">Report</p>
            </div>
        </div>





    </div>
</template>
<style lang="scss">
@import '@/styles/story-build.scss';
</style>
<script>
import CharacterPanel from '@/components/story-build/CharacterPanel.vue'
import StoryPanel from '@/components/story-build/StoryPanel.vue'

import StoryProceed from '@/components/story-build/StoryProceed.vue'
export default {
    components: {
        CharacterPanel, StoryPanel,
        StoryProceed
    },
    data() {
        return {
            panelVisible: false,
            selectedChoice: null,
            probabilities: [
                {
                    id: 1,
                    text: "The hair met a very handsome prince and fell in love",
                    title: "The Meetup"
                },
                {
                    id: 2,
                    text: "The hare fell in a very deep dark hole, with no one to call",
                    title: "The Fall"
                },
                {
                    id: 3,
                    text: "The hare heard a scream and got very curious to what's happening",
                    title: "The Scream"
                },
            ]

        }
    },
    methods: {
        continueStory() {
            this.panelVisible = true;
        },
        choosePath() {
            if (this.selectedChoice != null) {

                this.panelVisible = false;
            }
        }
    }
}
</script>