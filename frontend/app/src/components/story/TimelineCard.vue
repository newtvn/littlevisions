<template>
    <div class="timeline-card">
        <img src="https://arc-anglerfish-washpost-prod-washpost.s3.amazonaws.com/public/AGMJJNTVPMI6ZITNDQQ4C2Y4SM.jpg"
            alt="">
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