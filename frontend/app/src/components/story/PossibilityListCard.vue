<template>
    <div class="possibility-list-card" :class="{ active: active }">
        <img :src="possibility.image">
    </div>
</template>
<script>
export default {
    name: "PossibilityListCard",
    props: {
        possibility: {
            type: Object,
            required: true
        },
        finish: {
            type: Boolean,
            default: false
        },
        active: {
            type: Boolean,
            default: false
        }
    },

}
</script>