<template>
    <div class="header-container">
        <AvatarSpeak :text="avatar_text" type="secondary" />
    </div>
    <div class="slideout-body story-content">
        <div class="flex-wrap explore-choice-card-list">
            <ExploreChoiceCard v-for="choice,index in choices" :key="index" :choice="choice" :selected="choice==selectedChoice" @click="selectedChoice=choice"/>
        </div>

    </div>
    <div class="slideout-footer footer-container ">


        <button class="primary-btn full-width bg-secondary" @click="writeStory">
            Start Writing
        </button>
    </div>
</template>

<script>
import AvatarSpeak from '../AvatarSpeak.vue';
import ExploreChoiceCard from '../ExploreChoiceCard.vue';
export default {
    components: {
        AvatarSpeak,ExploreChoiceCard
    },
    data() {
        return {
            avatar_text: "Hello! Choose what your story will be about. Click on your favorite option below to start your adventure!",
            choices: [
                { "title": "The Big African Boy", "mood": "sad" },
                { "title": "The Beautiful Princess", "mood": "happy" },
                { "title": "The Forgetful Dragon", "mood": "funny" },
                { "title": "The Haunted House", "mood": "scary" },
                { "title": "The Selfish Rat", "mood": "funny" },
                { "title": "The Mysterious Cat", "mood": "" },
            ],
            selectedChoice: null
        }
    },
    methods:{
        writeStory(){
            if(this.selectedChoice!=null){

                this.$emit('startWrite',this.selectedChoice.title)
            }
        }
    }
}
</script>