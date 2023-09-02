<template>
    <main id="story-build">
        <ProceedModal v-if="showProceedModal" @close="showProceedModal = false" @proceed="proceedStory" />
        <div class="story-content">
            <StoryText :text="storyboard.text" @complete="textComplete = true" v-if="storyboard"/>

        </div>
        <StoryBoard />

        <div class="story-footer">
            <div class="fitted-container">

                <div class="row default-gap">
                    <p class="button-prefix">Continue Story</p>
                    <button class="primary-btn circle-btn" @click="showProceedModal = true">
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
import { getStoryboardDoc } from '@/firebase'
import { useDocument } from 'vuefire'
export default {
    name: "StoryBuild",
    components: {
        StoryBoard, StoryText, ProceedModal
    },
    data() {
        return {
            showProceedModal: false,
            textComplete: false,
            storyboard: null
        }
    },
    computed: {

        
    },
    methods: {
        proceedStory() {
            this.showProceedModal = false,
                console.log("Do some proceed thing")
        }
    },
    mounted() {
        var storyId = this.$route.params['story_id']
        var boardId = this.$route.params['board_id']

        if (boardId) {
            this.storyboard = useDocument(getStoryboardDoc(storyId, boardId))
        }
    }
}
</script>