<template>
    <div class="storyboard-item" :class="{active:active}" @click="storyClick" :ref="getRef">
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
        },
        getRef(){
            if(this.active){
                return "activeStory"
            }
            return ""
        }
    },
    methods:{
        storyClick(){
                this.$router.replace({name:"build-story", params:{story_id:this.$route.params['story_id'], board_id:this.$props.story.id}})
                
               
                // location.reload()
        },
        scrollToActive(){
            if(this.active){
                const activeElement = this.$refs.activeStory
                console.log(activeElement)
                if(activeElement){
                    activeElement.scrollIntoView({ behavior: 'smooth', block: 'start' });
          console.log('scrolled')
                }
            }
        }
    },
    mounted(){
        this.scrollToActive()
    }
}
</script>