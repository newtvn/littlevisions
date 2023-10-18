<template>
    <main id="my-stories">
        <div class="row space-btn">

            <!-- <h1 class="page-title">My Stories</h1> -->
            <!-- A search thing will be here -->
        </div>
        <section class="finished-stories-container">
            <h2 class="section-title">Unfinished Stories</h2>
            <div class="stories-book-list">
                <StoriesBookCard v-for="unfinished in unfinished" :key="unfinished.id" :story="unfinished" />

            </div>

        </section>
        <div class="unfinished-stories">
            <h2 class="section-title">Finished Stories</h2>
            <div class="exclusive-book-container">
                <div class="exclusive-book-card">
                    <img src="https://storage.googleapis.com/pai-images/5a58eba3fa3a4bc39710509d6c95fa80.jpeg" alt=""
                        class="exclusive-book-card-image">
                    <div class="exclusive-book-details">
                        <p class="exclusive-book-name">
                            Damsel in Distress
                        </p>
                        <div class="row">
                            <div class="number-of-pages-container row default-gap">
                                <i class="fa fa-book"></i>
                                54
                            </div>

                            <p class="caption">43 Reads</p>
                        </div>
                        <div class="book-categories row default-gap">
                            <p class="exclusive-book-category">
                                Romance
                            </p>
                            <p class="exclusive-book-category">
                                Romance
                            </p>

                        </div>


                    </div>
                </div>
            </div>
        </div>
    </main>
</template>
<script>
import StoriesBookCard from '@/components/StoriesBookCard.vue';
import { getDocs, orderBy, query, where } from 'firebase/firestore';
import { getStories } from '@/firebase'
export default {
    components: {
        StoriesBookCard
    },
    data() {
        return {
            unfinished: []
        }
    },
    mounted() {
        getDocs(query(getStories(), where("finished", "==", false), orderBy('datetime'))).then(e => {
            console.log(e.docs)
            this.unfinished = e.docs.map(doc => ({
                ...doc.data(),
                id: doc.id,
            }))
        })
    }
}
</script>
<style lang="scss">
@import "@/styles/story-mine.scss";
</style>