<template>
    <div class="template-choice-card" :class="{ selected: selected }">
        <img :src="choice.image" alt="" class="choice-image tiny-image">
        <p class="choice-name">{{ choice.name }}</p>
    </div>
</template>
<script>
export default {
    name: 'ChoiceCard',
    props: {
        choice: {
            type: Object,
            default: () => {
                return {
                    name: "Dragons",
                    image: "https://img.freepik.com/free-photo/eye-mythological-dragon-fire-generative-ai_188544-12557.jpg?w=2000"
                }
            }
        },
        selected: {
            type: Boolean,
            default: false
        }
    }
}
</script>