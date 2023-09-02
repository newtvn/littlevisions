<template>
    <BaseModal id="pick-modal">
        <template v-slot:header>

            <p class="modal-title">How do you want your story to start</p>
        </template>
        <template v-slot:body>
            
            <input type="text" class="text-field" placeholder="Example: I am a superhero" v-model="prompt">
            
        </template>

        <template v-slot:footer>
            <div class="row default-gap button-row">

                <p class="button-prefix">Start my Story</p>
                <button class="primary-btn circle-btn" @click="buttonClick">
                    <i class="fas fa-arrow-right"></i>
                </button>
            </div>
        </template>

    </BaseModal>
</template>
<script>
import BaseModal from "@/components/BaseModal.vue"
export default {
    name: "PickModal",
    components: {
        BaseModal
    },
    data() {
        return {
            prompt: null
           
        }
    },
    methods: {
        buttonClick(){
            this.$emit("complete",this.prompt)
        }
    
    }
}
</script>