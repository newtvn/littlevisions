<template>
    <div class="characters-panel story-build-panel row">
        <p class="panel-subtitle">Your Characters</p>
        <div class="character-list row default-gap">

            <CharacterItem v-for="character in characters" :key="character.id" :character="character" />

        </div>

        <button class="circle-btn scale-hover" id="character-panel-add-btn" @click="$emit('createCharacter')">
            <i class="fa fa-plus"></i>
        </button>
    </div>
</template>

<script>
import CharacterItem from './CharacterItem.vue';
import api from '@/plugins/axios_utils';
import { getDocs } from 'firebase/firestore';
import { getCharacters } from '@/firebase'
export default {
    components: {
        CharacterItem
    },
    data() {
        return {
            characters: []
        }
    },
    methods: {

        async getFromFirebase() {
            var story_id = this.$route.params['story_id']

            getDocs(getCharacters(story_id)).then(e => {
                // console.log(e.docs)
                this.characters = e.docs.map(doc => ({
                    ...doc.data(),
                    id: doc.id,
                }))

            })

        },
        async getCharacters() {
            var story_id = this.$route.params['story_id']

            api.get(`story/${story_id}/characters`)


        }
    },
    mounted() {
        this.getFromFirebase().then(() => {
            if (this.characters.length == 0) {
                this.getCharacters()
            }

        })
    }
}
</script>
