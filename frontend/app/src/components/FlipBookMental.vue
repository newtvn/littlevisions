

<template>
  <FlipBook :story="stories" v-if="stories.length>0"/>

</template>
<script>

import FlipBook from "@/components/Flipbook.vue";
import { getStoryboard } from '@/firebase'
import { getDocs, orderBy, query } from 'firebase/firestore';
export default {
  components: {
  FlipBook
  },
  data(){
    return {
      stories: []
    }
  },

  mounted() {
    var storyId = this.$route.params['story_id']
    console.log(storyId)
    getDocs(query(getStoryboard(storyId), orderBy('datetime'))).then(e => {
      console.log(e)
      this.stories = e.docs.map(doc => ({
        ...doc.data(),
        id: doc.id,
      }))
    })
  }
}
</script>
<style scoped lang="css"></style>