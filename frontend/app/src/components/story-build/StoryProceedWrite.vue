<template>
      <div class="center-container" id="path-selector-header">
        <div class="image-header row default-gap">
            <img src="@/assets/images/choice.png" alt="">
            <h1 class="slideout-title">Choose Your Next Path</h1>
        </div>
    </div>
    <div class="container" id="story-choice-write-container">
        <div class="center-container">

            <!-- <p class="current-narrative">{{ narrative }}</p> -->
        </div>


        <div class="form-container" id="write-story-input">
            <div class="row default-gap label-indicator">

                <p class="fancy-label">Write what should happen next</p>
                <i class="fa fa-arrow-down indicator"></i>
            </div>
            <input type="text" class="textarea full-width" autofocus v-model="text">
            <p class="form-caption">The limit is your imagination</p>
        </div>
        <div class="story-controls">
            <div class="row space-btn">
                <div class="row default-gap label-indicator">


                    <button class="circle-btn center-container bg-secondary" @click="$emit('choiceOptionClick')">
                        <i class="fa fa-pencil"> </i>
                    </button>
                    <i class="fa fa-arrow-left indicator"></i>
                    <p class="fancy-label">Make A Choice</p>
                </div>
                <div class="row default-gap label-indicator" v-if="selectedChoice !== null">

                    <p class="fancy-label">Use This Path</p>
                    <i class="fa fa-arrow-right indicator"></i>
                    <button class="circle-btn center-container bg-primary" @click="$emit('continueStory',text)">
                        <i class="fa fa-step-forward"> </i>
                    </button>
                </div>
            </div>
        </div>
    </div>
</template>
<script>
export default {
    props:{
        narrative:{
            type: String,
            required: true
        }
    },
    data() {
        return {
            text: null
        }
    }
}

</script>