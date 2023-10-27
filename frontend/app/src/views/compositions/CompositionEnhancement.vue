<template>
    <div class="composition-enhancement-page">

        <!-- <section id="composition-intro-section">
        <div class="composition-intro-text">
            <p class="story-text">
                You wrote an essay that requires some improvements in regards to creativity
            </p>
        </div>
    </section> -->
    <CompositionHelperModal :helper="selectedHelper" v-if="showHelper" @close="showHelper=false"/>

        <section id="composition-preview-section">
            <div class="composition-writing-container">
                <div class="composition-writing">
                    <HighlightWords class="composition-text" highlightClassName="highlight" :searchWords="highlightWords" :autoEscape="true"
                        :textToHighlight="composition.text"></HighlightWords>
                    <!-- <p class="composition-text">
                        {{ composition.text }}
                    </p> -->
                </div>
            </div>
            <div class="composition-helpers-container">
                <div class="composition-helpers-list">
                    <CompositionHelperCard v-for="helper in helpers" :key="helper.id" :helper="helper" @click="helperClicked(helper)" />

                </div>
            </div>
        </section>
    </div>
</template>
<script>
import CompositionHelperCard from '@/components/compositions/CompositionHelperCard.vue'
import { getDocs, query,getDoc } from 'firebase/firestore'
import { getCompositionHelpers,getCompositionDoc } from '@/firebase'
import HighlightWords from 'vue-highlight-words'
import CompositionHelperModal from '@/components/story/modals/CompositionHelperModal.vue'
export default {
    components: {
        CompositionHelperCard, HighlightWords,CompositionHelperModal
    },
    computed: {
        highlightWords() {

            if (this.to_highlight) {

                return this.to_highlight.split(',')
            }
            return []
        }
    },
    data() {
        return {
            composition: {                
            },
            to_highlight: null,
            helpers: [
            ],
            showHelper: false,
            selectedHelper:null
        }
    },
    methods: {
        _getCompositionHelpers() {
            var composition_id = this.$route.params['composition_id']
            getDocs(query(getCompositionHelpers(composition_id))).then(e => {
                this.helpers = e.docs.map(doc => {
                    return {
                        ...doc.data(),
                        id: doc.id
                    }
                })
            })
        },
        _getComposition(){
            var composition_id = this.$route.params['composition_id']
            getDoc(
            getCompositionDoc(composition_id)).then((doc)=>{
                console.log(doc.data())
                this.composition = {
                    ...doc.data(),
                    // id: doc.id
                }
            })

        },
        helperClicked(helper){
            this.selectedHelper=helper
            this.to_highlight = helper.original_narrative
            this.showHelper=true

            
        }
    },
    mounted() {
        this._getComposition()
        this._getCompositionHelpers()
    }
}
</script>
<style lang="scss">
@import "@/styles/composition-enhancement.scss";
</style>