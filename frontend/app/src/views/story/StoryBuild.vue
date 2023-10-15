<template>
    <div class="story-build-screen">
        <Transition name="fade">

            <CharacterCreateModal v-if="showCharacterModal" @close="showCharacterModal=false" @create="createCharacter"/>
        </Transition>
        <slideout @closing="onClosing" v-model="panelVisible" dock="bottom" size="600px">
            <StoryProceed :probabilities="probabilities" :narrative="storyboard.narrative" @continueStory="nextBoard"
                v-if="storyboard" />
        </slideout>
        <StoryPanel @continueStory="continueStory" :storyboard="storyboard" v-if="storyboard" />

        <StoryBoardPanel />

        <CharacterPanel @createCharacter="showCharacterModal=true"/>

        <div class="extra-controls row">
            <div class="row default-gap">
                <i class="fa fa-heart"></i>
                <p class="caption">Like</p>

            </div>
            <div class="row default-gap">
                <i class="fa fa-flag"></i>
                <p class="caption">Report</p>
            </div>
        </div>





    </div>
</template>
<style lang="scss">
@import '@/styles/story-build.scss';
</style>
<script>
import CharacterPanel from '@/components/story-build/CharacterPanel.vue'
import StoryBoardPanel from '@/components/story-build/StoryBoardPanel.vue'
import StoryPanel from '@/components/story-build/StoryPanel.vue'
import { getStoryboardDoc } from "@/firebase"
import { getDoc } from 'firebase/firestore'
import StoryProceed from '@/components/story-build/StoryProceed.vue'
import CharacterCreateModal from '@/components/story/modals/CharacterCreateModal.vue'
import api from '@/plugins/axios_utils'
export default {
    components: {
        CharacterPanel, StoryPanel,
        StoryProceed, StoryBoardPanel, CharacterCreateModal
    },
    data() {
        return {
            panelVisible: false,
            selectedChoice: null,
            storyboard: null,
            probabilities: [
            ],
            showCharacterModal: false

        }
    },
    methods: {
        continueStory() {
            this.panelVisible = true;
        },
        choosePath() {
            if (this.selectedChoice != null) {

                this.panelVisible = false;
            }
        },
        nextBoard(board_id) {
            this.panelVisible = false
            var story_id = this.$route.params['story_id']

            this.$router.replace({
                name: 'build-story', params: {
                    story_id: story_id,
                    board_id: board_id
                }
            })
        },
        createCharacter(name,personality,actions){
            this.showCharacterModal = false
            var story_id = this.$route.params['story_id']
            api.post(`story/${story_id}/build/character/continue`,{
                name: name,
                personality: personality,
                actions: actions
            }).then(res=>{
                this.nextBoard(res.data.board_id)
            })
        
        },
        async getStory() {
            var story_id = this.$route.params['story_id']
            var board_id = this.$route.params["board_id"]

            getDoc(getStoryboardDoc(story_id, board_id)).then((data) => {

                this.storyboard = data.data()
                console.log(this.storyboard)
            })

        },

        async getProbabilities() {
            var story_id = this.$route.params['story_id']
            var board_id = this.$route.params["board_id"]


            api.get(`story/${story_id}/build/${board_id}/path`).then(res => {
                this.probabilities = res.data.paths
            }).catch(e => {
                console.log(e)
                this.getProbabilities()
            })
        }
    },
    mounted() {
        this.getStory()
        this.getProbabilities()
    }
}
</script>