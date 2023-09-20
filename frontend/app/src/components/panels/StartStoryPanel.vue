
<template>
    <div class="header-container">
        <AvatarSpeak :text="avatar_text" type="tertiary" />

        <div class="try-again-container">
            <div class="row default-gap label-indicator">

                <p class="fancy-label">Click This To Try Again</p>
                <i class="fa fa-arrow-right indicator"></i>
                <button class="circle-btn center-container">
                    <i class="fa fa-refresh"> </i>
                </button>
            </div>
        </div>
    </div>
    <div class="slideout-body story-content">
        <p class="story-title">The Curious Squirrel</p>
        <StoryText :text="narrative" />

    </div>
    <div class="slideout-footer footer-container ">


        <button class="primary-btn full-width bg-tertiary">
            Start Writing
        </button>
    </div>
</template>
<script>
import AvatarSpeak from '../AvatarSpeak.vue';
import StoryText from '../story/StoryText.vue';
export default {
    components: {
        AvatarSpeak, StoryText
    },
    data() {
        return {
            avatar_text: "Hey, we've got a story to start with! If you want a different one, you can click the 'Try Again' button. If not, click 'Start Writing'!",
            narrative: "Once upon a time in a magical forest, a curious squirrel named Sammy discovered a mysterious key beneath an ancient oak tree."
        }
    }
}
</script>