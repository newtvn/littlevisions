<template>
    <p class="story-text">
        {{ typetext }}
    </p>
</template>

<script>
export default {
    props: {
        text: {
            required: true,
            type: String
        },
        delay:{
            type: Number,
            default: 100
        }
    },
    data(){
        return {
            typetext: ""
        }
    },
    watch:{
        text(oldValue,newValue){
            if(oldValue!==newValue){
                this.typetext=""
                this.typeEffect()
            }
        }
        
    },
    methods: {
        typeEffect(){
            var counter =0;
            var wordsArr = this.$props.text.split("")
            var interval = setInterval(()=>{
                this.typetext += wordsArr[counter]
                counter++
                if(counter == wordsArr.length){
                    this.$emit('complete')
                    clearInterval(interval)
                }
            },this.$props.delay)
        }
    },

    mounted(){
        this.typeEffect()

    }
}
</script>