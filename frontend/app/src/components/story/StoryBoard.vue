<template>
    <div class="story-build-sidebar">
        <div class="storyboard-header">
            <div class="center-container">
                <div class="row default-gap">
                    <h4>Storyboard</h4>
                    <button class="circle-btn primary-btn" @click="playButton">
                        <i class="fas fa-play"></i>
                    </button>
                </div>
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
    methods:{
        playButton(){
        var story_id = this.$route.params['story_id']

            this.$router.push({name: 'play-story',params:{story_id:story_id}})
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