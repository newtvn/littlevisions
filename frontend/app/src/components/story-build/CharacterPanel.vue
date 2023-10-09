<template>
    <div class="characters-panel story-build-panel row">
        <p class="panel-subtitle">Your Characters</p>
        <div class="character-list row default-gap">

            <div class="character-item scale-hover" v-for="character in characters" :key="character.id">
                <div class="character-image">
                    <img src="https://i.pinimg.com/564x/92/52/7b/92527b5b5e7320a9ad3e75023215ba5b.jpg" alt="">
                </div>
            </div>

        </div>

        <button class="circle-btn scale-hover" id="character-panel-add-btn">
            <i class="fa fa-plus"></i>
        </button>
    </div>
</template>

<script>
import { firestore } from '@/firebase';
import { getDocs, query, collection } from 'firebase/firestore';
export default {
    data() {
        return {
            characters: []
        }
    },
    methods: {
        async getCharacters() {
            var story_id = this.$route.params['story_id']
            var charactersCollection = collection(firestore, `stories/${story_id}/characters`)
            getDocs(query(charactersCollection)).then(e => {
                // console.log(e.docs)
                this.characters = e.docs.map(doc => ({
                    ...doc.data(),
                    id: doc.id,
                }))
            })

        }
    },
    mounted() {
        this.getCharacters()
    }
}
</script>
