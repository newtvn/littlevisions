<template>
    <section id="library-section">
        <div class="center-container">
            <h3 class="section-title">Read from Our Library</h3>
        </div>
        <div class="row space-btn center-top" id="library-section-books">
            <button class="circle-btn secondary-background">
                <i class="fas fa-chevron-left"></i>
            </button>
            <div id="library-section-books-list">
                <BookCard v-for="book in bookList" :key="book.name" :book="book" />
                

            </div>
            <button class="circle-btn secondary-background">
                <i class="fas fa-chevron-right"></i>
            </button>

        </div>
    </section>
</template>

<script>
import BookCard from "./BookCard.vue"
import {storiesCollection } from "@/firebase"
import { useCollection } from 'vuefire'
// import { collection, } from 'firebase/firestore'

export default {
    name: "LibrarySection",
    components: {
        BookCard
},
    data(){
        return {
            bookList:[
                
            ]
        }
    },
    mounted(){
        
        this.bookList = useCollection(storiesCollection)
        
    }

}

</script>