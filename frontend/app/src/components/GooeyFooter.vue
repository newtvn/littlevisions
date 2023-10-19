<template lang="pug">
div.footer
    div.bubbles
        - for (var i = 0; i < 128; i++) //Small numbers looks nice too
            div.bubble(style=`--size:${2+Math.random()*4}rem; --distance:${6+Math.random()*4}rem; --position:${-5+Math.random()*110}%; --time:${2+Math.random()*2}s; --delay:${-1*(2+Math.random()*2)}s;`)
            div.content

        div
            a.image(href="https://codepen.io/z-" target="_blank" style="background-image: url(\"https://s3-us-west-2.amazonaws.com/s.cdpn.io/199011/happy.svg\")")
            p ©2019 Not Really
svg(style="position:fixed; top:100vh")
    defs
        filter#blob
            feGaussianBlur(in="SourceGraphic" stdDeviation="10" result="blur")
            feColorMatrix(in="blur" mode="matrix" values="1 0 0 0 0  0 1 0 0 0  0 0 1 0 0  0 0 0 19 -9" result="blob")
            //feComposite(in="SourceGraphic" in2="blob" operator="atop") //After reviewing this after years I can't remember why I added this but it isn't necessary for the blob effect

</template>
<style lang="scss" scoped>
@import '../styles/variables.scss';
.footer {
    z-index: 1;
    --footer-background: #ED5565;
    display: grid;
    position: relative;
    grid-area: footer;
    max-height: 200px;

    .bubbles {
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        height: 1rem;
        background: var(--footer-background);
        filter: url("#blob");

        .bubble {
            position: absolute;
            left: var(--position, 50%);
            background: var(--footer-background);
            border-radius: 100%;
            animation: bubble-size var(--time, 4s) ease-in infinite var(--delay, 0s),
                bubble-move var(--time, 4s) ease-in infinite var(--delay, 0s);
            transform: translate(-50%, 100%);
        }
    }

//     .content {
//         z-index: 2;
//         display: grid;
//         grid-template-columns: 1fr auto;
//         grid-gap: 4rem;
//         padding: 2rem;
//         background: var(--footer-background);

//         a,
//         p {
//             color: #F5F7FA;
//             text-decoration: none;
//         }

//         b {
//             color: white;
//         }

//         p {
//             margin: 0;
//             font-size: .75rem;
//         }

//         div {
//             display: flex;
//             flex-direction: column;
//             justify-content: center;

//             >div {
//                 margin: 0.25rem 0;

//                 >* {
//                     margin-right: .5rem;
//                 }
//             }

//             .image {
//                 align-self: center;
//                 width: 4rem;
//                 height: 4rem;
//                 margin: 0.25rem 0;
//                 background-size: cover;
//                 background-position: center;
//             }
//         }
//     }
}


@keyframes bubble-size {

    0%,
    75% {
        width: var(--size, 4rem);
        height: var(--size, 4rem);
    }

    100% {
        width: 0rem;
        height: 0rem;
    }
}

@keyframes bubble-move {
    0% {
        bottom: -4rem;
    }

    100% {
        bottom: var(--distance, 10rem);
    }
}
</style>