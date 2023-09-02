<template>
    <div class="story-build-sidebar">
        <div class="storyboard-header">
            <div class="center-container">

                <h4>Your Storyboard</h4>
            </div>
        </div>
        <div class="storyboard-body">
            <div class="storyboard-list">
                <StoryBoardItem v-for="item in items" :key="item.id" :story="item" />
            </div>
        </div>
    </div>
</template>
<script>
import StoryBoardItem from './StoryBoardItem.vue';
import { useCollection } from 'vuefire'
import {getStoryboard} from '@/firebase'

export default {
    components: {
        StoryBoardItem
    },
    data(){
        return {
            items: []
        }
    },
    mounted(){
        var story_id = this.$route.params['story_id']
        this.items = useCollection(getStoryboard(story_id))
        
    }
}

</script>