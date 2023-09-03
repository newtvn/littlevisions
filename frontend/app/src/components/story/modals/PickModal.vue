<template>
    <BaseModal id="pick-modal">
        <template v-slot:header>

            <p class="modal-title">Will you write your own or pick from our choices</p>
        </template>
        <template v-slot:body>
            <div class="column" id="pick-modal-buttons">
                <button class="padded-btn" :class="{ 'outline-btn': !writeSelected, 'tertiary-btn': writeSelected }"
                    @click="writeSelect()">
                    <div class="row">
                        Write your own
                        <i class="fas fa-pencil"></i>
                    </div>
                </button>

            </div>
            <hr class="divider">
            <div class="template-choices">
                <ChoiceCard v-for="choice in choices" :key="choice.name" :choice="choice" @click="choiceSelect(choice.text)"
                    :selected="selectedChoice === choice.name"  />
            </div>
        </template>

        <template v-slot:footer>
            <div class="row default-gap button-row">

                <p class="button-prefix" v-if="writeSelected">Write my Story</p>
                <p class="button-prefix" v-else>Write About {{ selectedChoice }}</p>
                <button class="primary-btn circle-btn" @click="buttonClick">
                    <i class="fas fa-arrow-right"></i>
                </button>
            </div>
        </template>

    </BaseModal>
</template>
<script>
import BaseModal from "@/components/BaseModal.vue"
import ChoiceCard from "../ChoiceCard.vue";
export default {
    name: "PickModal",
    components: {
        BaseModal, ChoiceCard
    },
    data() {
        return {
            selectedChoice: null,
            writeSelected: true,
            choices: [
                {
                    name: "Dragons",
                    image: "https://images.unsplash.com/photo-1515263487990-61b07816b324?ixid=MnwxMjA3fDB8MHxzZWFyY2h8Mnx8ZHJhZ29uc3xlbnwwfHwwfHw%3D&ixlib=rb-4.0.3&auto=format&fit=crop&w=500&q=60",
                    text: "A dragon got stuck in a cave"
                },
                {
                    name: "Princess",
                    image: "https://media.istockphoto.com/id/528631226/photo/little-princess-girl-pointing-her-magic-wand-towards-camera.jpg?s=612x612&w=0&k=20&c=E1zXn7OYETch7B388zXvxRSVArBkNyDri4jk8IdzkIE=",
                    text: "A princess with a tiara"
                }
            ]
        }
    },
    methods: {
        writeSelect() {
            this.selectedChoice = null;
            this.writeSelected = true
        },
        choiceSelect(name) {
            this.writeSelected = false
            this, this.selectedChoice = name
        },
        buttonClick() {
            this.$emit('complete',{
                write: this.writeSelected,
                choice: this.selectedChoice
            })

        }
    }
}
</script>