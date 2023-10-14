<template>
    <div class="story-text-panel story-build-panel">
        <div class="audio-controls">
            <div class="audio-indicator row default-gap" @click="playAudio">
                <i class="fa-solid fa-microphone"></i>
                David
            </div>
        </div>
        <StoryText :text="storyboard.narrative" v-if="storyboard" />
        <div class="story-controls">
            <div class="row space-btn">
                <div class="row default-gap label-indicator">


                    <button class="circle-btn center-container">
                        <i class="fa fa-flag-checkered"> </i>
                    </button>
                    <i class="fa fa-arrow-left indicator"></i>
                    <p class="fancy-label">Finish Your Story</p>
                </div>
                <div class="row default-gap label-indicator">

                    <p class="fancy-label">Continue Your Story</p>
                    <i class="fa fa-arrow-right indicator"></i>
                    <button class="circle-btn center-container bg-primary" @click="$emit('continueStory')">
                        <i class="fa fa-step-forward"> </i>
                    </button>
                </div>
            </div>
        </div>
    </div>
</template>
<script>
import StoryText from '@/components/story/StoryText.vue';
// import api from '@/plugins/axios_utils';
export default {
    components: {
        StoryText
    },
    props: {
        storyboard: {
            type: Object,
            required: true
        }
    },
    data() {
        return {
            narration_url: null
        }
    },
    methods: {
        playAudio() {
            var audio = new Audio(this.narration_url)
            audio.play().catch(e=>{
                console.log(e)
            })
        },
        getAudio() {
            // var story_id = this.$route.params['story_id']
            // var board_id = this.$route.params['board_id']
            if ("narration_url" in this.$props.storyboard) {
                this.narration_url = this.$props.storyboard.narration_url

            }
            else {
                // api.get(`story/${story_id}/narration/generate/${board_id}`).then(res => {
                //     this.narration_url = res.data.narration_url

                // })
            }
        }
    },
    mounted() {
        this.getAudio()
    }
}
</script>