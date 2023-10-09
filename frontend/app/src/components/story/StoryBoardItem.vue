<template>
    <div class="storyboard-item" @click="itemClick" :class="{ active: $route.params['board_id'] === item.id }">
        <img :src="image_url" alt="">
    </div>
</template>
<script>
import api from '@/plugins/axios_utils';



export default {
    name: "StoryBoardItem",
    props: {
        item: {
            type: Object,
            required: false,
        }
    },
    data() {
        return {
            image_url: null
        }
    },
    methods: {
        itemClick() {
            this.$router.replace({ name: "build-story", params: { story_id: this.$route.params['story_id'], board_id: this.$props.item.id } })
        },
        getImageUrl() {
            var story_id = this.$route.params['story_id']
            var board_id = this.$props.item.id
            if (!("image_url" in this.$props.item)) {
                api.get(`story/${story_id}/image/generate/${board_id}`).then(res => {
                    this.image_url = res.data.image_url
                })
            }
        }

    },
    mounted() {
        if ("image_url" in this.$props.item) {
            this.image_url = this.$props.item.image_url
        }
        else {
            this.getImageUrl()
        }
    }
}
</script>