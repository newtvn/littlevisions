<template>
    <main id="story-create">
        <slideout @closing="onClosing" v-model="panelVisible" dock="bottom" size="500px">
            <WriteStoryPanel v-if="panelChild === 'write'" @startWrite="goToStoryBuild('Bz71mLOXDNUMCSjS01tU')"/>
            <StartStoryPanel v-if="panelChild === 'start'" @startWrite="goToStoryBuild('Bz71mLOXDNUMCSjS01tU')"/>
            <ExploreChoicesPanel v-if="panelChild === 'explore'" @startWrite="goToStoryBuild('Bz71mLOXDNUMCSjS01tU')"/>

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
        startCardClick() {
            this.panelVisible = true;
            this.panelChild = 'start';
        },
        exploreCardClick() {
            this.panelVisible = true;
            this.panelChild = 'explore';
        },

        goToStoryBuild(id){
            this.$router.push({name: 'build-story',params:{
                story_id:id
            
            }})
        }
    }
}
</script>