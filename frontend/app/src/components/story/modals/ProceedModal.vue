<template>
  <Loading v-model:active="isLoading" :can-cancel="false" :is-full-page="true" />

  <BaseModal>
    <template v-slot:header>
      <p class="possibility-subtitle">How Should Your Story Proceed?</p>
    </template>


    <template v-slot:body>

      <p class="possibility-header">You can <span>choose</span> from the following possibilities:</p>
      <div class="possibility-list">

        <PossibilityListCard v-for="possibility in paths" :key="possibility.id" :possibility="possibility"
          :active="selectedPossibility === possibility" @click="selectedPossibility = possibility" />

      </div>
      <p class="possibility-text" v-if="selectedPossibility">{{ selectedPossibility.text }}</p>
      <hr class="divider">

      <p class="possibility-header">Or you can <span>create</span> your own:</p>
      <div class="form-container">
        <input type="text" class="textarea" placeholder="How would you proceed?" v-model="textData">
      </div>


      <!-- <textarea style="width: 100%;height: 15vh"-->
      <!--                placeholder="Modify a template text here or create your own, the choice is yours."-->
      <!--                v-model="textData"></textarea> -->
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
import { callOpenAIGpt, callOpenAiImage } from "../../../open_ai_api.js";
import { getStoryNarrative } from '@/firebase';
import Loading from 'vue-loading-overlay';
import 'vue-loading-overlay/dist/css/index.css';
export default {
  components: {
    BaseModal,
    PossibilityListCard,
    Loading
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
      textData: null,
      isLoading: false,
      paths: []

    }
  },

  mounted() {
    this.getPossibilityImages()
  },
  methods: {
    getKeywordsForPossibility(text) {
      return callOpenAIGpt(`Generate an image generation prompt given the following description:${text} max 10 words,keep it simple`)
    },
    getCustomExtendedNarrative(text) {
      var story_id = this.$route.params['story_id']
      return getStoryNarrative(story_id).then(narrative => {

        return callOpenAIGpt(`Extend the provided narrative in 30 words maximum: ${narrative} given the following guiding text ${text}. Return only the extended text and max words 30`)
      })
    },
    getPossibilityImages() {
      this.$props.possibilities.slice(0, 4).forEach(possibility => {
        this.getKeywordsForPossibility(`${possibility.text}.black and white concept art `).then(res => {
          var text = res.choices[0].message.content
          // possibility['image'] = "https://www.shutterstock.com/shutterstock/photos/1808543779/display_1500/stock-photo-ability-circle-word-cloud-collage-concept-background-1808543779.jpg"
          // this.paths.push(possibility)
          callOpenAiImage(text, 1).then(e => {
            console.log(e)
            var url = e[0].url;
            possibility['image'] = url;
            this.paths.push(possibility)

          })
        })
      })
    },

    buttonClick() {
      if (this.textData != null && this.textData !== "") {
        this.isLoading = true
        this.getCustomExtendedNarrative(this.textData).then((e) => {
          var text = e.choices[0].message.content
          console.log(text)
          this.getKeywordsForPossibility(`${text}.black and white concept art `).then(res => {
            var prompt = res.choices[0].message.content
            console.log(prompt)
            callOpenAiImage(prompt, 1).then(image => {
              var image_url = image[0].url
              var possibility = {
                text: text,
                image: image_url
              }
              this.$emit('proceed', possibility)
            })
          })

        }).finally(() => {
          this.isLoading = false
        })
      }
      else {

        this.$emit('proceed', this.selectedPossibility)
      }
    }


  }
}

</script>