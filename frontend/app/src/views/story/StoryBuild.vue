<template>
    <main id="story-build">
        <Loading v-model:active="isLoading" :can-cancel="false" :is-full-page="true" />

        <ProceedModal v-if="showProceedModal" @close="showProceedModal = false" @proceed="proceedStory"
            @proceedCustom="proceedStoryCustom" :possibilities="possibilities" />
        <div class="story-content">
            <StoryText :text="storyboard.text" @complete="textComplete = true" v-if="storyboard" :delay="80" />
            <div class="center-container">
                <audio :src="audio_url" controls autoplay v-if="audio_url"></audio>
            </div>

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
import { getStoryboardDoc, createStoryBoard, getStoryNarrative, pushSoundToFirebase } from '@/firebase'
import { mapState } from "vuex"
import { callOpenAIGpt } from "@/open_ai_api"
import { Timestamp ,getDoc} from "firebase/firestore"
import tts from "@/eleven_labs"
import Loading from 'vue-loading-overlay';
import 'vue-loading-overlay/dist/css/index.css';
export default {
    name: "StoryBuild",
    components: {
        StoryBoard, StoryText, ProceedModal, Loading
    },
    data() {
        return {
            showProceedModal: false,
            textComplete: false,
            storyboard: null,
            possibilities: [],
            audio_url: null,
            isLoading: false
        }
    },
    computed: {
        ...mapState(['currentStoryText'])

    },
    methods: {
        pushSpeechToFirebase(blob) {
            var storyId = this.$route.params['story_id']
            var boardId = this.$route.params['board_id']
            pushSoundToFirebase(storyId, boardId, blob)

        },
        readText(text) {
            if (this.storyboard) {
                if (this.storyboard.audio_url) {
                    this.audio_url = this.storyboard.audio_url
                    return
                }
                else {
                    console.log("Not Found", text)
                    tts(text,).then(data => {
                        console.log(data)
                        const blob = new Blob([data], { type: 'audio/mpeg' });
                        this.pushSpeechToFirebase(blob)
                        const url = URL.createObjectURL(blob);
                        this.audio_url = url
                        return ;
                    })
                }
            }
            // Speak the utterance
            // window.speechSynthesis.speak(utterance);
        },
        proceedStory(possibility) {
            this.isLoading = true
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
            }).finally(() => {
                this.isLoading = false
            })




        },

        buildPrompt() {
            var story_id = this.$route.params['story_id']

            return getStoryNarrative(story_id).then(narrative => {

                return `Give me 4 possible paths in 30 words that extend the following narrative. Your response should be a valid extension on the narrative. Number the paths only using the 1. system: ${narrative}`
            })
        },
        async getPossibilities() {
            this.buildPrompt().then(prompt => {
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
    watch: {
        // storyboard(oldValue, newvalue) {
        //     this.$nextTick(() => {
        //         if (newvalue != undefined) {

        //             this.readText(newvalue.text)
        //         }
        //     })

        // }
    },
    mounted() {
        this.getPossibilities()

        var storyId = this.$route.params['story_id']
        var boardId = this.$route.params['board_id']

        if (boardId) {
            getDoc(getStoryboardDoc(storyId,boardId)).then(doc=>{
                var data = {
                    ...doc.data(),
                    id: doc.id
                }
                this.storyboard = data
                this.readText(data['text'])
            })

            // this.storyboard = useDocument(getStoryboardDoc(storyId, boardId), { once: true })

            // this.readText(this.storyboard.text)
        }



    }
}
</script>