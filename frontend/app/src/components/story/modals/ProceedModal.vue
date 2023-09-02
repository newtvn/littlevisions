<template>
    <BaseModal>
        <template v-slot:header>
            <p class="subtitle">How Should Your Story Proceed?</p>
        </template>

        <template v-slot:body>
            <div class="possibility-list">
                <PossibilityListCard v-for="possibility in possibilities" :key="possibility.id" :possibility="possibility" :final="possibility.final" :active="selectedPossibility==possibility" @click="selectedPossibility=possibility"/>
                
            </div>
            <p class="possibility-text" v-if="selectedPossibility">{{ selectedPossibility.text }}</p>
        </template>

        <template v-slot:footer>

            <div class="fitted-container row left-auto default-gap">
                <p class="button-prefix">
                    Continue My Story
                </p>
                <button class="primary-btn circle-btn" @click="buttonClick">
                    <i class="fas fa-chevron-right"></i>
                </button>
            </div>
        </template>
    </BaseModal>
</template>
<script>
import BaseModal from '@/components/BaseModal.vue';
import PossibilityListCard from '../PossibilityListCard.vue';
export default {
    components: {
        BaseModal,
        PossibilityListCard
    },
    data() {
        return {
            selectedPossibility: null,
            possibilities: [
                {
                    id: 1,
                    text: "Possibility 1",
                    image: "",
                    final: false
                },
                {
                    id: 2,
                    text: "Possibility 2",
                    image: "",
                    final: false
                },
                {
                    id: 3,
                    text: "Possibility 3",
                    image: "",
                    final: false
                },
                {
                    id: 4,
                    text: "Possibility 4",
                    image: "",
                    final: true
                }

            ]
        }
    },
    methods:{
        buttonClick(){
            console.log("Build next part here")
            this.$emit("proceed",this.selectedPossibility.id)
            //            this.$emit('close');
        }
    }
}

</script>