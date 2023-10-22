<template>
    <BaseModal id="character-modal">
        <template v-slot:header>
            <div class="modal-header-image center-container">

                <div class="image-header">
                    <div class="padded-container">

                        <GooglyEyes/>
                    </div>
                </div>
                <p class="modal-title">Create A Character</p>
            </div>
        </template>
        <template v-slot:body>
            <div class="center-container">
                <div class="full-width-container" v-if="section == 1">


                    <p class="large-text f500">What is Your Character's Name?</p>
                    <div class="character-form-container center-container">
                        <input type="text" class="underline-input" v-model="name">
                    </div>
                </div>
                <div class="full-width-container" v-if="section == 2">


                    <p class="large-text f500">What's {{ name }} Like?</p>
                    <div class="character-form-container center-container">
                        <input type="text" class="underline-input" v-model="personality">
                    </div>
                </div>
                <div class="full-width-container" v-if="section == 3">


                    <p class="large-text f500">What did {{ name }} Do?</p>
                    <div class="character-form-container center-container">
                        <input type="text" class="underline-input" v-model="actions">
                    </div>
                </div>
            </div>
        </template>
        <template v-slot:footer>
            <div class="story-controls">
                <div class="row space-btn">
                    <div class="container">

                        <div class="row default-gap label-indicator" v-show="section != 1">


                            <button class="circle-btn center-container" @click="previousSection">
                                <i class="fa fa-chevron-left"> </i>
                            </button>
                            <i class="fa fa-arrow-left indicator"></i>
                            <p class="fancy-label">Go Back</p>
                        </div>
                    </div>
                    <div class="row default-gap label-indicator">

                        <p class="fancy-label">Continue</p>
                        <i class="fa fa-arrow-right indicator"></i>
                        <button class="circle-btn center-container bg-primary" @click="nextSection">
                            <i class="fa fa-chevron-right"> </i>
                        </button>
                    </div>
                </div>
            </div>
        </template>
    </BaseModal>
</template>
<script>
import BaseModal from '@/components/BaseModal.vue';
import GooglyEyes from '@/components/GooglyEyes.vue';
export default {
    components: {
        BaseModal,GooglyEyes
    },
    data() {
        return {
            name: null,
            section: 1,
            personality: null,
            actions: null
        }
    },
    methods: {
        nextSection() {
            if (this.section != 3) {
                this.section++
            }
            else {
                this.$emit('create', this.name, this.personality, this.actions)
            }
        },
        previousSection() {
            if (this.section != 1) {
                this.section--
            }
        }
    }
}
</script>