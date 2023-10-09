<template>
    <div class="characters-panel story-build-panel row">
        <p class="panel-subtitle">Your Characters</p>
        <div class="character-list row default-gap">

           <CharacterItem v-for="character in characters" :key="character.id" :character="character"/>

        </div>

        <button class="circle-btn scale-hover" id="character-panel-add-btn">
            <i class="fa fa-plus"></i>
        </button>
    </div>
</template>

<script>
import { firestore } from '@/firebase';
import CharacterItem from './CharacterItem.vue';
import { getDocs, query, collection } from 'firebase/firestore';
export default {
    components:{
        CharacterItem
    },
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
