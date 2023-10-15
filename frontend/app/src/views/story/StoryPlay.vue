<template>
    <div class="story-play-background">
        <img :src="activeStory.image_url" alt="" v-if="activeStory" class="background-image">

        <div class="story-play-content">

            <div class="navigation-title-container">

                <button class="circle-btn bg-primary">
                    <i class="fas fa-chevron-left"></i>
                </button>
                <p class="navigation-title" v-if="activeStory">
                    {{ activeStory.title }}
                </p>
            </div>
            <div class="story-text-container">
                <p class="story-text" v-if="activeStory">
                    {{ activeStory.narrative }}
                </p>
                <!-- <StoryText :text="activeStory.narrative" v-if="activeStory" :delay="70" @complete="textComplete"/> -->
            </div>
            <div class="story-image-container">
                <img :src="activeStory.image_url" alt="" v-if="activeStory">
            </div>
            <div class="story-timeline-container">
                <div class="board-timeline">
                    <div class="board-timeline-item" v-for="story,index in stories" :key="story.id"
                        :class="{ active: activeStory == story }" @click="activeIndex=index">
                        <img :src="story.image_url" alt="">
                    </div>
                </div>
                <div class="audio-timeline">

                </div>
            </div>

        </div>
    </div>
</template>

<script>

import { getStoryboard } from '@/firebase'
import { getDocs, orderBy, query } from 'firebase/firestore';
import { Howl } from 'howler';

export default {
    components: {
    },

    data() {
        return {
            stories: [

            ],
            activeIndex: 0,
            narration_sound: null,
            music_sound: null
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
            setTimeout(()=>{
                if(this.narration_sound){

                    this.narration_sound.stop()
                }
                if(this.music_sound){

                    this.music_sound.fade(0,1)
                }

                this.goToNext()
            },2000)

        },
        getSoundsArray() {
            var sounds = []

            if ("music_url" in this.activeStory) {
                sounds.push(this.activeStory.music_url)
            }
            if ("narration_url" in this.activeStory) {
                sounds.push(this.activeStory.narration_url)
            }
            console.log(sounds)
            return sounds
        },
        playSound() {
            if ("music_url" in this.activeStory) {
                this.music_sound = new Howl({
                    src: this.activeStory.music_url,
                    autoplay: true,
                    volume: 0.1
                })


            }
            if ("narration_url" in this.activeStory) {

                this.narration_sound= new Howl({
                    src: this.activeStory.narration_url,
                    autoplay: true,
                    onend: ()=>{
                        this.textComplete()
                    }
                })

            }
        }
    },
    watch: {
        activeStory() {
            this.playSound()
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
<style lang="scss">
@import "@/styles/story-play.scss";
</style>