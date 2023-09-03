<template>
    <div class="timeline-card">
        <img :src="story.image" :class="{ active: active }" alt="">
    </div>
</template>
<script>
export default {
    props: {
        story: {
            type: Object,
            required: true
        },
        active: {
            type: Boolean,
            default: false
        }

    }
}
</script>