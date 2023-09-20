<template>
    <div class="avatar-speak" :class="classes">
        <img src="@/assets/images/fox.png" alt="Fox Avatar" v-if="type==='primary'">
        <img src="@/assets/images/bird.png" alt="Fox Avatar" v-if="type==='secondary'">
        <img src="@/assets/images/bunny.png" alt="Fox Avatar" v-if="type==='tertiary'">
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

        },
        type: {
            type: String,
            default: "primary"
        }
    },
    computed:{
        classes(){
            var type = this.$props.type;
            if(type==='primary'){
                return "primary-bubble"
            }
            else if(type==='secondary'){
                return "secondary-bubble"
            }
            else if(type==='tertiary'){
                return "tertiary-bubble"
            }
            return ""
        }
    }
}
</script>