<template>
    <main id="story-build">
        <ProceedModal v-if="showProceedModal" @close="showProceedModal = false" @proceed="proceedStory"
            @proceedCustom="proceedStoryCustom" :possibilities="possibilities" />
        <div class="story-content">
            <StoryText :text="storyboard.text" @complete="textComplete = true" v-if="storyboard" />

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
import { getStoryboardDoc, createStoryBoard, getStoryNarrative } from '@/firebase'
import { useDocument } from 'vuefire'
import { mapState } from "vuex"
import { callOpenAIGpt } from "@/open_ai_api"
import { Timestamp } from "firebase/firestore"

export default {
    name: "StoryBuild",
    components: {
        StoryBoard, StoryText, ProceedModal
    },
    data() {
        return {
            showProceedModal: false,
            textComplete: false,
            storyboard: null,
            possibilities: []
        }
    },
    computed: {
        ...mapState(['currentStoryText'])

    },
    methods: {
        proceedStory(possibility) {
            var storyId = this.$route.params['story_id']
            var data = {
                text: possibility.text,
                image: possibility.image,
                datetime: Timestamp.now()
            }

            createStoryBoard(storyId, data).then((e) => {

                this.showProceedModal = false;
                this.$store.dispatch('setNarrative', possibility.text)

                this.$router.replace({ name: 'build-story', params: { story_id: storyId, board_id: e.id } })
            })

        },

        buildPrompt() {
            var story_id = this.$route.params['story_id']

            return getStoryNarrative(story_id).then(narrative => {

                return `Give me 4 possible paths in 30 words that extend the following narrative. Your response should be a valid extension on the narrative. Number the paths only using the 1. system: ${narrative}`
            })
        },
        async getPossibilities() {
            this.buildPrompt().then(prompt=>{
                callOpenAIGpt(prompt).then(e => {
                var message = e.choices[0].message.content
                var split_message = message.split("\n")
                // console.log(split_message)
                split_message.forEach((element, index) => {
                    var text = element.replace(/^\d+\.\s/, '')
                    this.possibilities.push({
                        id: index,
                        text: text,
                    })
                });
            })
            })
            

        },


    },
    mounted() {
        this.getPossibilities()

        var storyId = this.$route.params['story_id']
        var boardId = this.$route.params['board_id']

        if (boardId) {
            this.storyboard = useDocument(getStoryboardDoc(storyId, boardId))
        }
        getStoryNarrative(storyId).then(e=>{
            console.log(e)
        })


    }
}
</script>