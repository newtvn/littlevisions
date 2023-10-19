<template>
    <div class="composition-enhancement-page">

        <!-- <section id="composition-intro-section">
        <div class="composition-intro-text">
            <p class="story-text">
                You wrote an essay that requires some improvements in regards to creativity
            </p>
        </div>
    </section> -->

        <section id="composition-preview-section">
            <div class="composition-writing-container">
                <div class="composition-writing">
                    <p class="composition-text">
                        {{ composition.text }}
                    </p>
                </div>
            </div>
            <div class="composition-helpers-container">
                <div class="composition-helpers-list">
                    <CompositionHelperCard v-for="helper in helpers" :key="helper.id" :helper="helper" />

                </div>
            </div>
        </section>
    </div>
</template>
<script> 
import CompositionHelperCard from '@/components/compositions/CompositionHelperCard.vue'
export default {
    components: {
        CompositionHelperCard
    },
    data() {
        return {
            composition: {
                id: "shshs",
                text: `I went to the park today with my mom and dad. It was so much fun! We brought my kite, and I tried to make it fly really high, but the wind wasn't strong enough. My dad helped me, and we finally got it up in the sky. I felt like I was flying with it!

                        Then, we had a picnic. My mom made my favorite sandwich with peanut butter and jelly. I also had a big, juicy apple and some chocolate milk. After eating, we played on the swings, and I went so high that it felt like I could touch the clouds.
                    

                        There were lots of birds in the park, and I tried to talk to them. I think they listened because they chirped back! I also saw a cute squirrel running around. It was really fast, just like a superhero.

                        We met a friendly dog named Max. Max was so fluffy, and he licked my face. I giggled a lot! I wish we could take Max home, but we already have our dog, Buddy. Buddy is my best friend, and he's always excited to see me.

                        When it was time to leave, I didn't want to go. I told my mom and dad that the park was the best place ever. They smiled and said we could come back soon. I can't wait for our next adventure at the park!`,
                title: "Mid-term composition refining",
                comment: null,
                progress: 20,


            },
            helpers: [
                {
                    id: 1,
                    title: "Vocabulary",
                    description: "Add more descriptive words to make your writing more interesting.",
                    icon: "fas fa-language"
                },
                {
                    id: 2,
                    title: "Sentence Structure",
                    description: "Vary your sentence structure to make your writing more engaging.",
                    icon: "fas fa-code-branch"
                },
                {
                    id: 3,
                    title: "Transitions",
                    description: "Use transitional words and phrases to make your writing flow smoothly.",
                    icon: "fas fa-exchange-alt"
                },
                {
                    id: 4,
                    title: "Punctuation",
                    description: "Check your punctuation to make sure your writing is clear and easy to read.",
                    icon: "fas fa-pencil-alt"
                }
            ]
        }
    }
}
</script>
<style lang="scss">
@import "@/styles/composition-enhancement.scss";
</style>