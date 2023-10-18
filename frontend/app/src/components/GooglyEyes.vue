<template>
    <div class="googly-eyes">

        <div class="outer-eye">
            <div class="inner-eye"></div>
        </div>
        <div class="outer-eye outer-eye-2">
            <div class="inner-eye"></div>
        </div>
    </div>
</template>
<style scoped>
.outer-eye {
    /*Positioning*/
    position: relative;
    display: inline-block;
    /*Styling*/
    background: white;
    border-radius: 50%;
    /*Size*/
    width: 100px;
    height: 100px;
}

.outer-eye-2 {
    left: 50px;
}

.inner-eye {
    /*Positioning*/
    position: absolute;
    top: 50px;
    left: 45px;
    /*Styling*/
    background: #4056f4;
    border-radius: 50%;
    /*Size*/
    width: 35px;
    height: 35px;
    /*Assigns animation*/
    animation: shifty 3s infinite;
}

/*Begin animation details*/
@keyframes shifty {
    50% {
        /*Moves pupils to left, change number to see what happens*/
        transform: translateX(-25px);
    }

    75% {
        /*Moves pupils right and up, change numbers to see what happens*/
        transform: translateY(-30px) translateX(-10px);
    }
}
</style>