<template>
    <div class="character-item scale-hover">
        <div class="character-image">
            <img :src="image_url" alt="">
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
            image_url: null
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