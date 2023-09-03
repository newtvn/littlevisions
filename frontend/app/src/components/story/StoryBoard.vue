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
// import { useCollection } from 'vuefire'
import { getStoryboard } from '@/firebase'
import { getDocs, orderBy, query } from 'firebase/firestore';

export default {
    components: {
        StoryBoardItem
    },
    data() {
        return {
            items: []
        }
    },
    mounted() {
        var story_id = this.$route.params['story_id']
        getDocs(query(getStoryboard(story_id), orderBy('datetime'))).then(e => {
            // console.log(e.docs)
            this.items = e.docs.map(doc => ({
                ...doc.data(),
                id: doc.id,
            }))
        })

    }
}

</script>