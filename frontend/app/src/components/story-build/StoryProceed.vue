<template>
    <StoryProceedChoice :probabilities="probabilities" v-if="selectedOption === 'choice'"
        @writeOptionClick="selectedOption = 'write'" @continueStory="continueStory" />
    <StoryProceedWrite v-if="selectedOption === 'write'" @choiceOptionClick="selectedOption = 'choice'"
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
            let loader = this.$loading.show()

            api.post(`story/${story_id}/build/continue`, { prompt: selectedChoice.narrative }).then(
                (res) => {
                    var board_id = res.data.board_id
                    this.$emit("continueStory", board_id)
                }
            ).finally(() => {
                loader.hide()
            })
        },
        continueStoryCustom(enteredText) {
            var story_id = this.$route.params['story_id']
            let loader = this.$loading.show()
            api.post(`story/${story_id}/build/continue`, { prompt: enteredText }).then(
                (res) => {
                    var board_id = res.data.board_id
                    this.$emit("continueStory", board_id)
                }
            ).finally(() => {
                loader.hide()
            })
        }
    }
}

</script>