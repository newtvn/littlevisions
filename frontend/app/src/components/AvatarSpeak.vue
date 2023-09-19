<template>
    <div class="avatar-speak">
        <img src="@/assets/images/fox.png" alt="Fox Avatar">
        <div class="avatar-speak-text avatar-chat-bubble thought">
            {{ text }}
        </div>
    </div>
</template>
<script>
export default {
    props: {
        text: {
            type: String,
            required: true

        }
    }
}
</script>