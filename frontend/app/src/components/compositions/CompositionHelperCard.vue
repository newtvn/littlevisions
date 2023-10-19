<template>
    <div class="composition-helper-card">
        <div class="composition-helper-title">

            <p>{{ helper.title }}</p>
        </div>
        <div class="composition-helper-description">

            <p>{{ helper.description }}</p>
        </div>
        .
        <button>Learn</button>
    </div>
</template>
<script>
export default {
    props:{
        helper:{
            type:Object,
            required: true
        }
    }

}
</script>