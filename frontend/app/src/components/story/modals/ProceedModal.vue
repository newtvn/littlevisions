<template>
  <BaseModal>
    <template v-slot:header>
      <p class="subtitle">How Should Your Story Proceed?</p>
    </template>


    <template v-slot:body>
      <input style="width: 90%" type="text" v-model="imagePrompt" id="image-placeholder"
             placeholder="Enter image prompt that describes your next scene">

      <button style="width: 10%;" @click="callImageWithSinglePrompt(this.imagePrompt,this.possibilities.length)">
        Send
      </button>

      <div class="possibility-list">
        <PossibilityListCard v-for="possibility in possibilities" :key="possibility.id" :possibility="possibility"
                             :final="possibility.final" :active="selectedPossibility===possibility"
                             @click="()=>{selectedPossibility=possibility; textData = selectedPossibility.text}"/>

      </div>
      <p class="possibility-text" v-if="selectedPossibility">{{ selectedPossibility.text }}</p>

      <!--      <textarea style="width: 100%;height: 15vh"-->
      <!--                placeholder="Modify a template text here or create your own, the choice is yours."-->
      <!--                v-model="textData"></textarea>-->
    </template>

    <template v-slot:footer>

      <div class="fitted-container row left-auto default-gap">
        <p class="button-prefix">
          Continue My Story
        </p>
        <button class="primary-btn circle-btn" @click="buttonClick">
          <i class="fas fa-chevron-right"></i>
        </button>

        <button class="primary-btn circle-btn" @click="callImage">
          <i class="fas fa-chevron-left"></i>
        </button>

      </div>
    </template>
  </BaseModal>
</template>
<script>
import BaseModal from '@/components/BaseModal.vue';
import PossibilityListCard from '../PossibilityListCard.vue';
import {callOpenAiImage, callOpenAIGpt} from "../../../open_ai_api.js";

export default {
  components: {
    BaseModal,
    PossibilityListCard
  },
  data() {
    return {
      selectedPossibility: null,
      imagePrompt: "",
      textData: "",

      possibilities: [
        {
          id: 1,
          text: "A cat walked into the room",
          image: "",
          final: false,
          imagePrompt: "A space image"
        },
        {
          id: 2,
          text: "A dog with a god complex stood on the podium",
          image: "",
          final: false,
          imagePrompt: "An image of a cat"

        },
        {
          id: 3,
          text: "A bird flew from outside",
          image: "",
          final: false,
          imagePrompt: "An image of a dog"

        },
        {
          id: 4,
          text: "A dog fell down",
          image: "",
          final: true,
          imagePrompt: "An image of a man thinking"
        }
      ]
    }
  },
  methods: {
    buttonClick() {
      console.log("Build next part here")
      this.$emit("proceed", this.selectedPossibility.id)
      //            this.$emit('close');
    },
    changeTextToSomeAI() {
      callOpenAIGpt("Hello there who am I speaking to").then(text => {
        console.log(text);
        this.textData = text.choices[0].message.content
      });
    },
    callImage() {
      for (let i = 0; i < this.possibilities.length; i++) {
        console.log(this.possibilities[i].imagePrompt)

        callOpenAiImage(this.possibilities[i].imagePrompt).then(image => {
          console.log(image);
          this.possibilities[i].image = image[0].url;
        })
      }
    },
    callImageWithSinglePrompt(Text, number) {

      callOpenAiImage(Text, number)
          .then(image => {
            console.log(image);
            for (let i = 0; i < this.possibilities.length; i++) {
              this.possibilities[i].image = image[i].url;
            }
          })

      this.callTextWithMultiplePrompt();
    },
    callTextWithMultiplePrompt() {

      for (let i = 0; i < this.possibilities.length; i++) {
        console.log(this.possibilities[i].imagePrompt)

        callOpenAIGpt("Can you extend this story that begins by  " + this.possibilities[i].text + " max of 20 words").then(text => {
          console.log(text);
          this.possibilities[i].text = text.choices[0].message.content
        })
      }
    }
  }
}

</script>