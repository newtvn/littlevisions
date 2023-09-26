<template>
    <div class="header-container">
        <AvatarSpeak :text="avatar_text" type="primary"/>
    </div>
    <div class="slideout-body">

        <div class="form-container" id="write-story-input">
            <div class="row default-gap label-indicator">

                <p class="fancy-label">Write Your Imagination here</p>
                <i class="fa fa-arrow-down indicator"></i>
            </div>
            <input type="text" class="textarea full-width" autofocus v-model="text">
            <p class="form-caption">Example: I am a forgetful dragon stuck in a very beautiful cave</p>
        </div>
    </div>
    <div class="slideout-footer footer-container ">


        <button class="bg-primary primary-btn full-width" @click="writeStory">
            Start Writing Your Story
        </button>
    </div>
</template>

<script>
import AvatarSpeak from "@/components/AvatarSpeak.vue"
export default {
    components: {
        AvatarSpeak
    },
    props: {
        isOpen: {
            type: Boolean, default: false
        }
    },
    data() {
        return {
            text: null,
            visible: false,
            avatar_text: "Hey there! Type whatever you like in the box below and then click 'Start Writing.' Let's have some fun!"
        }

    },
    methods:{
        writeStory(){
            this.$emit('startWrite',this.text)
        }
    },

    mounted() {
        this.visible = this.$props.isOpen
    }
}
</script>