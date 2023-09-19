<template>
    <main id="story-create">
        <slideout @closing="onClosing" v-model="panelVisible" dock="bottom" size="500px">
            <WriteStoryPanel />
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
                <CreateChoiceCard text="Write my own" image="pencil.png" class=" bg-primary card"
                    @click="panelVisible = true" />
                <CreateChoiceCard text="Explore Choices" image="book.png" class=" bg-secondary card" />
                <CreateChoiceCard text="Start Immediately" image="rocket.png" class=" bg-tertiary card" />

            </div>
        </div>
    </main>
</template>
<script>
import CreateChoiceCard from '@/components/story/CreateChoiceCard.vue';
import WriteStoryPanel from "@/components/panels/WriteStoryPanel.vue"
export default {
    data() {
        return {
            panelVisible: false
        }
    },
    components: {
        CreateChoiceCard, WriteStoryPanel
    }
}
</script>