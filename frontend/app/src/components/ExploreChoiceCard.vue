<template>
    <div class="explore-choice-card" :class="{ selected: selected }">
        <div class="selected-bar-indicator">

        </div>
        <p class="explore-choice-card-title">
            {{ choice.title }}
        </p>

        <div class="explore-choice-card-mood-container">
            <p class="explore-choice-card-mood">
                {{ moodEmoji }}
            </p>
        </div>
    </div>
</template>

<script>
export default {
    props: {
        choice: {
            type: Object,
            required: true
        },
        selected: {
            type: Boolean,
            default: false
        }
    },

    computed: {
        moodEmoji() {
            var mood = this.$props.choice.mood;
            if (mood === 'sad') {
                return "😭"
            }
            else if (mood === 'scary') {
                return "😨"
            }
            else if (mood === 'happy') {
                return "😃"
            }
            else if (mood === 'funny') {
                return "😂"
            }

            return "🙂"
        }
    }

}
</script>