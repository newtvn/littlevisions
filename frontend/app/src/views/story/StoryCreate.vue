<template>
    <main id="story-create">
        <slideout @closing="onClosing" v-model="panelVisible" dock="bottom" size="500px">
            <WriteStoryPanel v-if="panelChild === 'write'" @startWrite="createStoryFromWrite" />
            <StartStoryPanel v-if="panelChild === 'start'" @startWrite="goToStoryBuild('Bz71mLOXDNUMCSjS01tU')" />
            <ExploreChoicesPanel v-if="panelChild === 'explore'" @startWrite="goToStoryBuild('Bz71mLOXDNUMCSjS01tU')" />

        </slideout>
        <div class="main-header">
            <div class="center-container">
                <div class="header-image">
                    <div class="center-container">

                        <img src="@/assets/images/giraffe.png">
                    </div>
                </div>
                <h1>Create Your Story</h1>
            </div>
        </div>

        <div class="main-body">
            <div id="create-choice-list">
                <CreateChoiceCard text="Write my own" image="pencil.png" class=" bg-primary card" @click="writeCardClick" />
                <CreateChoiceCard text="Explore Choices" image="book.png" class=" bg-secondary card"
                    @click="exploreCardClick" />
                <CreateChoiceCard text="Start Immediately" image="rocket.png" class=" bg-tertiary card"
                    @click="startCardClick" />

            </div>
        </div>
    </main>
</template>
<script>
import CreateChoiceCard from '@/components/story/CreateChoiceCard.vue';
import WriteStoryPanel from "@/components/panels/WriteStoryPanel.vue"
import StartStoryPanel from '@/components/panels/StartStoryPanel.vue';
import ExploreChoicesPanel from '@/components/panels/ExploreChoicesPanel.vue';
import api from "@/plugins/axios_utils.js"
export default {
    data() {
        return {
            panelVisible: false,
            panelChild: null
        }
    },
    components: {
        CreateChoiceCard, WriteStoryPanel, StartStoryPanel, ExploreChoicesPanel,
    },
    methods: {
        writeCardClick() {
            this.panelVisible = true;
            this.panelChild = 'write';

        },
        createStoryFromWrite(text) {
            let loader = this.$loading.show()

            api.post("story/create/prompt", {
                prompt: text
            }).then(res => {
                var data = res.data
                this.goToStoryBuild(data.story_id, data.board_id)
            }).catch(e=>{
                console.log(e)
            }).finally(()=>{
                loader.hide()
            })
        },
        startCardClick() {
            this.panelVisible = true;
            this.panelChild = 'start';
        },
        exploreCardClick() {
            this.panelVisible = true;
            this.panelChild = 'explore';
        },

        goToStoryBuild(story_id, board_id = "") {

            this.$router.push({
                name: 'build-story', params: {
                    story_id: story_id,
                    board_id: board_id

                }
            })
        }
    }
}
</script>