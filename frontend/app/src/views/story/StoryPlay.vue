<template>
    <main id="story-play">
        <div class="story-section">
            <div class="story-text-section">
                <div class="center-container">

                    <StoryText :text="activeStory.text" v-if="activeStory" :key="activeStory.text" @complete="textComplete" :delay="70"/>
                    <audio :src="activeStory.audio_url" controls autoplay v-if="activeStory"></audio>
                </div>
            </div>
            <div class="story-image-section">
                <img :src="activeStory.image" alt="" v-if="activeStory">
            </div>
        </div>
        <div class="story-timeline">
            <div class="timeline-list">
                <TimelineCard v-for="(story, index) in stories" :key="index" :story="story"
                    :active="activeIndex == index" />

            </div>
        </div>
    </main>
</template>

<script>
import TimelineCard from '@/components/story/TimelineCard.vue';
import StoryText from '@/components/story/StoryText.vue';
import { getStoryboard } from '@/firebase'
import { getDocs, orderBy, query } from 'firebase/firestore';

export default {
    components: {
        TimelineCard, StoryText
    },
    data() {
        return {
            stories: [

            ],
            activeIndex: 0
        }
    },
    computed: {
        activeStory() {
            if (this.stories.length > 0) {

                return this.stories[this.activeIndex];
            }
            return null
        }

    },
    methods: {
        goToNext() {
            if (this.activeIndex < this.stories.length) {
                this.activeIndex++
            }
        },
        textComplete() {
            this.goToNext()

        }
    },
    mounted() {
        var storyId = this.$route.params['story_id']
        getDocs(query(getStoryboard(storyId), orderBy('datetime'))).then(e => {
            this.stories = e.docs.map(doc => ({
                ...doc.data(),
                id: doc.id,
            }))
        })


    }
}

</script>