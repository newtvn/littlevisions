<template>
    <div class="center-container" id="path-selector-header">
        <div class="image-header row default-gap">
            <img src="@/assets/images/choice.png" alt="">
            <h1 class="slideout-title">Choose Your Next Path</h1>
        </div>
    </div>
    <StoryProceedChoice :probabilities="probabilities" v-show="selectedOption === 'choice'" @writeOptionClick="selectedOption='write'"/>
    <StoryProceedWrite v-show="selectedOption === 'write'" @choiceOptionClick="selectedOption='choice'" :narrative="narrative"/>
</template>

<script>
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
        narrative:{
            type: String,
            required: true
        }
    },
    data() {
        return {
            selectedOption: 'write'
        }
    }
}

</script>