<template>
    <div class="center-container" id="path-selector-header">
        <div class="image-header row default-gap">
            <img src="@/assets/images/choice.png" alt="">
            <h1 class="slideout-title">Choose Your Next Path</h1>
        </div>
    </div>
    <StoryProceedChoice :probabilities="probabilities" v-show="selectedOption === 'choice'"
        @writeOptionClick="selectedOption = 'write'" @continueStory="continueStory" />
    <StoryProceedWrite v-show="selectedOption === 'write'" @choiceOptionClick="selectedOption = 'choice'"
        :narrative="narrative" @continueStory="continueStoryCustom" />
</template>

<script>
import api from '@/plugins/axios_utils';
import StoryProceedChoice from './StoryProceedChoice.vue';
import StoryProceedWrite from './StoryProceedWrite.vue';
export default {
    components: {
        StoryProceedChoice, StoryProceedWrite
    },
    props: {
        probabilities: {
            type: Array,
            default: () => []
        },
        narrative: {
            type: String,
            required: true
        }
    },
    data() {
        return {
            selectedOption: 'write'
        }
    },
    methods: {
        continueStory(selectedChoice) {
            var story_id = this.$route.params['story_id']
            api.post(`story/${story_id}/build/continue`, { prompt: selectedChoice.narrative }).then(
                (res) => {
                    var board_id = res.data.board_id
                    this.$emit("continueStory", board_id)
                }
            )
        },
        continueStoryCustom(enteredText) {
            var story_id = this.$route.params['story_id']
            api.post(`story/${story_id}/build/continue`, { prompt: enteredText }).then(
                (res) => {
                    var board_id = res.data.board_id
                    this.$emit("continueStory", board_id)
                }
            )
        }
    }
}

</script>