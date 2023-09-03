<template>
  <BaseModal>
    <template v-slot:header>
      <p class="subtitle">How Should Your Story Proceed?</p>
    </template>


    <template v-slot:body>

      <div class="possibility-list">
        <PossibilityListCard v-for="possibility in paths" :key="possibility.id" :possibility="possibility"
          :active="selectedPossibility === possibility" @click="selectedPossibility = possibility" />

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

      </div>
    </template>
  </BaseModal>
</template>
<script>
import BaseModal from '@/components/BaseModal.vue';
import PossibilityListCard from '../PossibilityListCard.vue';
import {  callOpenAIGpt } from "../../../open_ai_api.js";

export default {
  components: {
    BaseModal,
    PossibilityListCard
  },
  props: {
    possibilities: {
      type: Array,
      required: true
    }
  },
  data() {
    return {
      selectedPossibility: null,
      imagePrompt: "",
      textData: "",
      paths: []

    }
  },

  mounted(){
    this.getPossibilityImages()
  },
  methods: {
    getKeywordsForPossibility(text) {
      return callOpenAIGpt(`Generate an image generation prompt given the following description:${text} max 10 words,keep it simple`)
    },
    getPossibilityImages() {
      this.$props.possibilities.slice(0,4).forEach(possibility => {
        this.getKeywordsForPossibility(`${possibility.text}.black and white concept art `).then(res => {
          console.log(res)
          // var text = res.choices[0].message.content
          possibility['image'] = "https://www.shutterstock.com/shutterstock/photos/1808543779/display_1500/stock-photo-ability-circle-word-cloud-collage-concept-background-1808543779.jpg"
          this.paths.push(possibility)
          // callOpenAiImage(text, 1).then(e => {
          //   console.log(e)
          //   var url = e[0].url;
          //   possibility['image'] = url;
          //   this.paths.push(possibility)

          // })
        })
      })
    },

  buttonClick(){
    this.$emit('proceed',this.selectedPossibility)
  }

    // buttonClick() {
    //   console.log("Build next part here")
    //   this.$emit("proceed", this.selectedPossibility.id)
    //   //            this.$emit('close');
    // },

    // changeTextToSomeAI() {
    //   callOpenAIGpt("Hello there who am I speaking to").then(text => {
    //     console.log(text);
    //     this.textData = text.choices[0].message.content
    //   });
    // },
    // callImage() {
    //   for (let i = 0; i < this.possibilities.length; i++) {
    //     console.log(this.possibilities[i].imagePrompt)

    //     callOpenAiImage(this.possibilities[i].imagePrompt).then(image => {
    //       console.log(image);
    //       this.possibilities[i].image = image[0].url;
    //     })
    //   }
    // },
    // callImageWithSinglePrompt(Text, number) {

    //   callOpenAiImage(Text, number)
    //       .then(image => {
    //         console.log(image);
    //         for (let i = 0; i < this.possibilities.length; i++) {
    //           this.possibilities[i].image = image[i].url;
    //         }
    //       })

    //   this.callTextWithMultiplePrompt();
    // },
    // callTextWithMultiplePrompt() {

    //   for (let i = 0; i < this.possibilities.length; i++) {
    //     console.log(this.possibilities[i].imagePrompt)

    //     callOpenAIGpt("Can you extend this story that begins by  " + this.possibilities[i].text + " max of 20 words").then(text => {
    //       console.log(text);
    //       this.possibilities[i].text = text.choices[0].message.content
    //     })
    //   }
    // }
  }
}

</script>