<template>
    <div class="create-choice-card card scale-hover">

        <img :src="require(`../../assets/images/${image}`)" alt="">
        <h2>{{ text }}</h2>
        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1440 320">
            <path fill-opacity="1"
                d="M0,64L60,90.7C120,117,240,171,360,160C480,149,600,75,720,53.3C840,32,960,64,1080,101.3C1200,139,1320,181,1380,202.7L1440,224L1440,320L1380,320C1320,320,1200,320,1080,320C960,320,840,320,720,320C600,320,480,320,360,320C240,320,120,320,60,320L0,320Z">
            </path>
        </svg>
    </div>
</template>
<script>
export default {
    name: 'CreateChoiceCard',
    props: {
        text: {
            type: String,
            required: true
        },
        image: {
            type: String,
            required: true
        }
    }
}

</script>