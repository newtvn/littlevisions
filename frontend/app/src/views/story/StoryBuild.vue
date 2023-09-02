<template>
    <main id="story-build">
        <ProceedModal v-if="showProceedModal" @close="showProceedModal=false" @proceed="proceedStory"/>
        <div class="story-content">
            <StoryText :text="text" @complete="textComplete = true" />

        </div>
        <StoryBoard />

        <div class="story-footer">
            <div class="fitted-container">

                <div class="row default-gap">
                    <p class="button-prefix">Continue Story</p>
                    <button class="primary-btn circle-btn" @click="showProceedModal=true">
                        <i class="fas fa-chevron-right"></i>
                    </button>
                </div>
            </div>
        </div>
    </main>
</template>
<script>
import StoryBoard from "@/components/story/StoryBoard.vue"
import StoryText from "@/components/story/StoryText.vue"
import ProceedModal from "@/components/story/modals/ProceedModal.vue"
export default {
    name: "StoryBuild",
    components: {
        StoryBoard, StoryText, ProceedModal
    },
    data() {
        return {
            showProceedModal: false,
            textComplete: false,
            text: "Once upon a time, in a land far, far away, there was an enchanted forest unlike any other. The trees whispered secrets to the wind, and the leaves danced with the morning dew.Deep within this magical woodland lived a peculiar creature named Lumina.Lumina was a firefly with wings that shimmered like a thousand tiny stars.She was the guardian of the forest, responsible for keeping its secrets safe ......"
        }
    },
    methods:{
        proceedStory(){
            this.showProceedModal = false,
            console.log("Do some proceed thing")
        }
    }
}
</script>