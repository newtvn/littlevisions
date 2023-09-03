<template>
    <main id="story-home">
        <Loading v-model:active="isLoading" :can-cancel="false" :is-full-page="true" />
        <PickModal v-if="showPickModal" @close="showPickModal = false" @complete="completePick" />
        <WriteModal v-if="showWriteModal" @close="showWriteModal = false" @complete="completeWrite" />
        <section id="hero-section">
            <div class="center-container" id="hero-text-container">
                <h1>Write your own story</h1>
                <p>Start writing your own story and share it with the world</p>
            </div>
            <div class="row default-gap" id="start-story">
                <!-- <p class="button-prefix">Start a New Story</p> -->
                <button class="primary-btn padded-btn" @click="showPickModal = true">
                    <div class="row">
                        Start a New Story
                        <i class="fas fa-plus"></i>
                    </div>

                </button>
            </div>
        </section>
        <LibrarySection />
    </main>
</template>
<script>
import LibrarySection from "@/components/story/LibrarySection.vue"
import PickModal from "@/components/story/modals/PickModal.vue";
import WriteModal from "@/components/story/modals/WriteModal.vue"
import { callOpenAiImage, callOpenAIGpt } from "@/open_ai_api";
import { createStory, createStoryBoard } from "@/firebase"
import { Timestamp } from "firebase/firestore"
import Loading from 'vue-loading-overlay';
import 'vue-loading-overlay/dist/css/index.css';
export default {
    name: "StoryHome",
    components: {
        LibrarySection, PickModal, WriteModal, Loading
    },
    data() {
        return {
            showPickModal: false,
            showWriteModal: false,
            isLoading: false
        }
    },
    methods: {
        createStoryClick(prompt) {
            this.isLoading = true
            callOpenAiImage(prompt, 1).then(e => {

                var image_url = e[0].url;
                var data = {
                    image: image_url,
                    name: prompt
                }
                //create the story in firebase
                createStory(data).then(story_ref => {
                    //build initial storyboard
                    callOpenAIGpt(`Generate a beginning of a story with the following guide ${prompt}.30 words maximum`).then(e => {
                        var text = e.choices[0].message.content
                        var storyboard = {
                            text: text,
                            image: image_url,
                            datetime: Timestamp.now()
                        }
                        createStoryBoard(story_ref.id, storyboard).then(board_ref => {

                            this.$store.dispatch("clearNarrative")
                            this.$store.dispatch('setNarrative', text)
                            this.$router.push({ name: 'build-story', params: { story_id: story_ref.id, board_id: board_ref.id } })
                        })
                    })
                })


            }).finally(() => {
                this.loading = false
            })
        },
        completePick(e) {
            this.showPickModal = false
            if (e.write) {
                this.showWriteModal = true
            }
            else {
                this.createStoryClick(e.choice)
            }

        },

        completeWrite(e) {
            this.showWriteModal = false
            this.createStoryClick(e)
        }
    }
}
</script>