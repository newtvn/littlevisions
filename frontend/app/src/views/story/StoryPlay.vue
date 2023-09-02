<template>
    <main id="story-play">
        <div class="story-section">
            <div class="story-text-section">
                <div class="center-container">

                    <StoryText :text="activeStory.text " v-if="activeStory"/>
                </div>
            </div>
            <div class="story-image-section">
                <img :src="activeStory.image" alt="" v-if="activeStory">
            </div>
        </div>
        <div class="story-timeline">
            <div class="timeline-list">
                <TimelineCard v-for="story,index in stories" :key="story.id" :story="story" :active="activeIndex==index"/>
                
            </div>
        </div>
    </main>
</template>

<script>
import TimelineCard from '@/components/story/TimelineCard.vue';
import StoryText from '@/components/story/StoryText.vue';
export default {
    components: {
        TimelineCard,StoryText
    },
    data(){
        return {
            stories: [

            ],
            activeIndex: 0
        }
    },
    computed:{
        activeStory(){
            if(this.stories.length>0){
                
                return this.stories[this.activeIndex];
            }
            return null
        }
    
    }
}

</script>