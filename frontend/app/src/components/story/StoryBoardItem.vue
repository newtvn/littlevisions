<template>
    <div class="storyboard-item" :class="{active:active}">
        StoryItemHere
    </div>
</template>
<script>

export default {
    name: "StoryBoardItem",
    props:{
        story:{
            type:Object,
            required:false,
        }
    },
    computed:{
        active(){
            // if(this.props.story){

            //     return this.$props.story.id===this.$route.params['id']
            // }
            return false
        }
    }
}
</script>