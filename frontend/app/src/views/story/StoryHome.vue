<template>
     <main id="story-home">
        <PickModal v-if="showPickModal" @close="showPickModal = false" @complete="completePick" />
        <WriteModal v-if="showWriteModal" @close="showWriteModal = false" @complete="completeWrite" />
        <section id="hero-section">
            <div class="center-container" id="hero-text-container">
                <h1>Write your own story</h1>
                <p>Start writing your own story and share it with the world</p>
            </div>
            <div class="row default-gap" id="start-story">
                <!-- <p class="button-prefix">Start a New Story</p> -->
                <button class="primary-btn padded-btn" @click="showPickModal = true">
                    <div class="row">
                        Start a New Story
                        <i class="fas fa-plus"></i>
                    </div>

                </button>
            </div>
        </section>
        <LibrarySection />
    </main>
</template>
<script>
import LibrarySection from "@/components/story/LibrarySection.vue"
import PickModal from "@/components/story/modals/PickModal.vue";
import WriteModal from "@/components/story/modals/WriteModal.vue"

export default{
    name:"StoryHome",
    components:{
        LibrarySection,PickModal,WriteModal
    },
    data(){
        return {
            showPickModal:false,
            showWriteModal:false
        }
    },
    methods:{
        createStory(prompt){
            console.log(prompt)
            this.$router.push({name:'build-story',params:{id:"12323"}})
        },
        completePick(e){
            this.showPickModal = false
            if(e.write){
                this.showWriteModal = true
            }
            else{
                this.createStory(e)
            }
            
        },

        completeWrite(e){
            this.showWriteModal = false
            this.createStory(e)
        }
    }
}
</script>