<template>
    <div class="storyboard-item" :class="{active:active}" @click="storyClick">
       <img :src="story.image">
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
            if(this.$props.story){

                return this.$props.story.id===this.$route.params['board_id']
            }
            return false
        }
    },
    methods:{
        storyClick(){
                this.$router.replace({name:"build-story", params:{story_id:this.$route.params['story_id'], board_id:this.$props.story.id}})
               
                // location.reload()
            
        }
    }
}
</script>