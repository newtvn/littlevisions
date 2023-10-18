<template>
    <router-link :to="{ name: 'build-story', params: { story_id: story.id } }">

        <div class="stories-book-card">
            <div class="book-image-container">

                <img :src="highlightImage" alt="">
                <div class="number-of-pages-container row default-gap">
                    <i class="fa fa-book"></i>
                    {{ pageCount }}
                </div>
            </div>
            <p class="stories-book-name">
                {{ story.title }}
            </p>
            <p class="stories-book-category">
                Romance
            </p>

        </div>
    </router-link>
</template>
<script>
import { getStoryboard } from '@/firebase';
import { getDocs, query,orderBy } from 'firebase/firestore';

export default {
    props: {
        story: {
            type: Object,
            required: true
        }
    },
    computed:{
        pageCount(){
            return this.pages.length
        },
        highlightImage(){
            if(this.pageCount >0){

                return this.pages[0].image_url
            }
            return ""
        }
    },
    data() {
        return {
            pages: []
        }
    },
    methods: {
        goToStory() {
            this.$router.push({
                name: "build-story", params: {
                    story_id: this.$props.story.id
                }
            })

        }
    },
    mounted() {
        getDocs(query(getStoryboard(this.$props.story.id), orderBy('datetime'))).then(e => {
            // console.log(e.docs)
            this.pages = e.docs.map(doc => ({
                ...doc.data(),
                id: doc.id,
            }))
        })
    }
}
</script>