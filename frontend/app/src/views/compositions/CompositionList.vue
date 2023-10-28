<template>
    <main id="composition-list">
        <div class="row default-gap">
            <img src="@/assets/images/stitch.png" class="title-image" />
            <h1 class="main-title">Creativity Assignments</h1>
        </div>
        <div class="composition-list row default-gap">

            <CompositionCard v-for="composition in compositions" :key="composition.id" :title="composition.title"
                :comment="composition.comment" :progress="composition.progress" @click="goToComposition(composition.id)" />

        </div>
    </main>
</template>
<script>
import CompositionCard from "@/components/compositions/CompositionCard.vue"
import { getDocs, query } from "firebase/firestore"
import { getCompositions } from "@/firebase"
export default {
    components: {
        CompositionCard
    },
    data() {
        return {
            compositions: [
                {
                    id: "P9NmuKH1zt9DUkqVBbaq",
                    text: "a very long text",
                    title: "Mid-term composition refining",
                    comment: null,
                    progress: 20
                }
            ]
        }
    },
    methods: {
        goToComposition(id) {
            this.$router.push({
                name: 'composition-enhancement', params: {
                    composition_id: id
                }
            })
        },
        fetchCompositions() {
            getDocs(query(getCompositions())).then(e => {
                this.compositions = e.docs.map(doc => {
                    return {
                        ...doc.data(),
                        id: doc.id
                    }
                })

            })
        }
    },
    mounted(){
        this.fetchCompositions()
    }
}
</script>