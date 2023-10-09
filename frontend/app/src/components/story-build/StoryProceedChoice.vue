<template>
    
    <div id="story-path-container">

        <div class="path-card-selector">
            <div class="path-card-list">
                <PathCard v-for="probability in probabilities" :key="probability.title" @click="selectedChoice = probability"
                    :selected="selectedChoice == probability">
                    <template v-slot:front>
                        <div class="center-container">
                            <p class="path-card-front-title">
                                {{ probability.mood }}
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

                <StoryText :text="selectedChoice.narrative" v-if="selectedChoice != null" :delay="40" />
                <div class="center-container" v-else>
                    <AvatarSpeak text="You need to make a choice to continue. Choose a card on your left" />
                </div>
            </div>
            <div class="story-controls">
                <div class="row space-btn">
                    <div class="row default-gap label-indicator">


                        <button class="circle-btn center-container" @click="$emit('writeOptionClick')">
                            <i class="fa fa-pencil"> </i>
                        </button>
                        <i class="fa fa-arrow-left indicator"></i>
                        <p class="fancy-label">Write My Own Path</p>
                    </div>
                    <div class="row default-gap label-indicator" v-if="selectedChoice !== null">

                        <p class="fancy-label">Choose This Path</p>
                        <i class="fa fa-arrow-right indicator"></i>
                        <button class="circle-btn center-container bg-primary" @click="$emit('continueStory',selectedChoice)">
                            <i class="fa fa-step-forward"> </i>
                        </button>
                    </div>
                </div>
            </div>

        </div>
    </div>
</template>

<script>
import PathCard from '@/components/PathCard.vue'
import StoryText from '@/components/story/StoryText.vue'
import AvatarSpeak from '@/components/AvatarSpeak.vue'
export default {

    components: {
        PathCard, StoryText, AvatarSpeak
    },
    props: {
        probabilities: {
            type: Array,
            default: () => []
        }
    },
    data() {
        return {
            selectedChoice: null
        }
    },
    methods: {
        continueStory() {
            this.$emit("continueStory", this.selectedChoice)
        }
    }
}
</script>