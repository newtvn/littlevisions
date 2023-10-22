<template>
    <div class="character-container">

        <div class="character-detail-container" v-show="show_detail" :style="backgroundColor">
            <div class="character-image row default-gap">
                <img :src="image_url" alt="" :id="image_url">
                <span class="character-name">

                    {{ character.name }}
                </span>
            </div>
            <div class="character-description row default-gap">
                <p>{{ character.description }}</p>
            </div>
        </div>
        <div class="character-item scale-hover" @click="show_detail = !show_detail">
            <div class="character-image row default-gap">
                <img :src="image_url" alt="" @load="getPalette">
                {{ character.name }}
            </div>
        </div>
    </div>
</template>

<script>
import api from '@/plugins/axios_utils'

export default {

    props: {
        character: {
            type: Object,
            required: true
        }
    },
    data() {
        return {
            image_url: null,
            show_detail: false,
            image_palette: null
        }
    },
    computed:{
        backgroundColor(){
            var color = "white"
            if(this.image_palette){
                color =  this.image_palette["Vibrant"]
            }
            return {"background-color":color}
        }
    },
    methods: {
        getImageUrl() {
            var story_id = this.$route.params['story_id']
            var character_id = this.$props.character.id
            if (!("image_url" in this.$props.character)) {
                api.get(`story/${story_id}/character/${character_id}/image/generate/`).then(res => {
                    this.image_url = res.data.image_url
                }).catch(e => {
                    console.log(e)
                })
            }
        },
        getPalette(){
            // const img = document.getElementById(this.image_url)
            
            // const vibrant = Vibrant(img)
            // vibrant.getPalette().then(e=>{
            //     this.image_palette = e
            // })
        }
    },
    mounted() {
        if ("image_url" in this.$props.character) {
            this.image_url = this.$props.character.image_url
        }
        else {
            this.getImageUrl()
        }
    }
}
</script>