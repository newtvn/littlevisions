<template>
    <div class="storyboard-panel story-build-panel">

        <p class="panel-subtitle" style="text-align: center;">Your Storyboard</p>

        <div class="storyboard-panel-list">
            <StoryBoardItem v-for="item in items" :key="item" :item="item"/>
            

        </div>
    </div>
</template>

<script>
import { getDocs, query, orderBy } from 'firebase/firestore'
import { getStoryboard } from '@/firebase'
import StoryBoardItem from '../story/StoryBoardItem.vue'
export default {
    components:{
        StoryBoardItem
    },
    data() {
        return {
            items: []
        }
    },
    methods: {
        async getBoards() {
            var story_id = this.$route.params['story_id']
            getDocs(query(getStoryboard(story_id), orderBy('datetime'))).then(e => {
                // console.log(e.docs)
                this.items = e.docs.map(doc => ({
                    ...doc.data(),
                    id: doc.id,
                }))
            })
        },
    
    },
    mounted() {
        this.getBoards()
    }
}
</script>