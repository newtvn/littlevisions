<template>
    <div class="story-build-screen">
        <slideout @closing="onClosing" v-model="panelVisible" dock="bottom" size="600px">
            <div class="center-container" id="path-selector-header">
                <div class="image-header row default-gap">
                    <img src="@/assets/images/choice.png" alt="">
                    <h1 class="slideout-title">Choose Your Next Path</h1>
                </div>
            </div>
            <div id="story-path-container">

                <div class="path-card-selector">
                    <div class="path-card-list">
                        <PathCard v-for="probability in probabilities" :key="probability.id"
                            @click="selectedChoice = probability" :selected="selectedChoice == probability">
                            <template v-slot:front>
                                <div class="center-container">
                                    <p class="path-card-front-title">
                                        {{ probability.id }}
                                    </p>
                                </div>
                            </template>
                            <template v-slot:back>
                                <div class="center-container">
                                    <p class="path-card-back-title">
                                        {{ probability.title }}
                                    </p>
                                </div>
                            </template>
                        </PathCard>




                    </div>

                </div>
                <div class="path-text-container">

                    <div class="path-text-view">
                        <!-- <p class="story-text" v-if="selectedChoice != null">{{ selectedChoice.text }}</p> -->

                        <StoryText :text="selectedChoice.text" v-if="selectedChoice != null" :delay="40" />
                        <div class="center-container" v-else>
                            <AvatarSpeak text="You need to make a choice to continue. Choose a card on your left" />
                        </div>
                    </div>
                    <div class="story-controls">
                        <div class="row space-btn">
                            <div class="row default-gap label-indicator">


                                <button class="circle-btn center-container">
                                    <i class="fa fa-pencil"> </i>
                                </button>
                                <i class="fa fa-arrow-left indicator"></i>
                                <p class="fancy-label">Write My Own Path</p>
                            </div>
                            <div class="row default-gap label-indicator" v-if="selectedChoice!==null">

                                <p class="fancy-label">Choose This Path</p>
                                <i class="fa fa-arrow-right indicator"></i>
                                <button class="circle-btn center-container bg-primary" @click="$emit('continueStory')">
                                    <i class="fa fa-step-forward"> </i>
                                </button>
                            </div>
                        </div>
                    </div>

                </div>
            </div>
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

        <div class="extra-controls">
            <p class="caption">Report This Suggetsion</p>
        </div>





    </div>
</template>
<style lang="scss">
@import '@/styles/story-build.scss';
</style>
<script>
import CharacterPanel from '@/components/story-build/CharacterPanel.vue'
import StoryPanel from '@/components/story-build/StoryPanel.vue'
import PathCard from '@/components/PathCard.vue'
import StoryText from '@/components/story/StoryText.vue'
import AvatarSpeak from '@/components/AvatarSpeak.vue'
export default {
    components: {
        CharacterPanel, StoryPanel, PathCard,
        StoryText,
        AvatarSpeak
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