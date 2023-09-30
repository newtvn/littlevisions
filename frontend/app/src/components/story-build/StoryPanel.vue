<template>
    <div class="story-text-panel story-build-panel">
        <div class="audio-controls">
            <div class="audio-indicator row default-gap">
                <i class="fa-solid fa-microphone"></i>
                David
            </div>
        </div>
        <StoryText
            text="Once upon a time in a magical forest, a curious squirrel named Sammy discovered a mysterious key beneath an ancient oak tree." />
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
export default {
    components: {
        StoryText
    }
}
</script>