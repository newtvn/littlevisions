<template>
    <div class="story-build-sidebar">
        <div class="storyboard-header">
            <div class="center-container">

                <h4>Your Storyboard</h4>
            </div>
        </div>
        <div class="storyboard-body">
            <div class="storyboard-list">
                <StoryBoardItem/>
                <StoryBoardItem />
            </div>
        </div>
    </div>
</template>
<script>
import StoryBoardItem from './StoryBoardItem.vue';
export default{
components:{
    StoryBoardItem
}
}

</script>