<template>
    <div id="story-path-container">
        <div class="center-container">

            <div class="paths-selector">
                <div class="paths-carousel row">

                    <button class="circle-btn" @click="previousPath">
                        <i class="fa fa-chevron-left"></i>

                    </button>

                    <div class="path-text-container center-container">
                        <Transition name="fade" appear>

                            <p class="story-text" v-if="selectedChoice" v-auto-animate>{{ selectedChoice.narrative }} </p>
                        </Transition>
                    </div>
                    <button class="circle-btn" @click="nextPath">
                        <i class="fa fa-chevron-right"></i>

                    </button>
                </div>
                <div class="center-container">

                    <div class="path-indicators row default-gap">
                        <div class="path-indicator" v-for="probability in probabilities" :key="probability" :class="{active:probability==selectedChoice}">
                        </div>
                    </div>
                </div>

            </div>
        </div>


        <div class="story-controls">
            <div class="row space-btn">
                <div class="row default-gap label-indicator">


                    <button class="circle-btn center-container bg-secondary" @click="$emit('writeOptionClick')">
                        <i class="fa fa-pencil" > </i>
                    </button>
                    <i class="fa fa-arrow-left indicator"></i>
                    <p class="fancy-label">Write My Own Path</p>
                </div>
                <div class="row default-gap label-indicator" v-if="selectedChoice !== null">

                    <p class="fancy-label">Choose This Path</p>
                    <i class="fa fa-arrow-right indicator"></i>
                    <button class="circle-btn center-container bg-primary" @click="$emit('continueStory', selectedChoice)">
                        <i class="fa fa-step-forward"> </i>
                    </button>
                </div>
            </div>
        </div>

    </div>
</template>

<script>
export default {

    components: {

    },
    props: {
        probabilities: {
            type: Array,
            default: () => []
        }
    },
    data() {
        return {
            selectedChoice: null
        }
    },
    methods: {
        continueStory() {
            this.$emit("continueStory", this.selectedChoice)
        },
        nextPath(){
            let index = this.probabilities.indexOf(this.selectedChoice)
            if(index < this.probabilities.length - 1){
                this.selectedChoice = this.probabilities.at(index + 1)
            }
        
        },
        previousPath(){
            let index = this.probabilities.indexOf(this.selectedChoice)
            if(index > 0){
                this.selectedChoice = this.probabilities.at(index - 1)
            }
        }
    },
    mounted(){
        this.selectedChoice = this.$props.probabilities.at(0)
    }
}
</script>