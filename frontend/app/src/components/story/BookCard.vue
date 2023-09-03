<template>
    <div class="card feature-card">
        <div class="row default-gap">
            <div class="book-image-background">

                <img class="book-image"
                    :src="book.image" />
            </div>

            <div class="column">

                <p class="book-title">{{ book.name }}</p>
                <div class="row book-author">
                    <img :src="author.image"
                        alt="" class="tiny-image profile-image">
                    <p class=" caption">{{ author.name }}</p>
                </div>
            </div>
        </div>

        <div class="feature-storyboard">
            <img v-for="story in storyboard" :key="story.id" :src="story.image"
                alt="" class="circle-image small">
        </div>

        <button class="primary-btn circle-btn" @click="readClick">
            <i class="fas fa-book"></i>
        </button>
    </div>
</template>
<script>
import {getStoryboard} from '@/firebase'
import { useCollection } from 'vuefire'
export default {
    name: "BookCard",
    props: {
        book: {
            type: Object,
            default: () => {
                return {
                    name: "The Ugly Duckling",
                    image: "https://images.unsplash.com/photo-1560306165-4100411e6ed4?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=2036&q=80"
                }
            }
        },
        author: {
            type: Object,
            default: () => {
                return {
                    name: "Brian Newton",
                    image: "https://images.unsplash.com/photo-1515041219749-89347f83291a?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Mnx8Y2FydG9vbnxlbnwwfHwwfHx8MA%3D%3D&auto=format&fit=crop&w=500&q=60"

                }
            }
        },
        
    },
    data(){
        return {
            storyboard: []
        }
    },
    methods:{
        readClick(){
            this.$router.push({name:'flipbook',params:{story_id: this.book.id}})
        }
    },
    mounted(){
        var board = useCollection(getStoryboard(this.$props.book.id))
        this.storyboard=board
        
    }
}
</script>