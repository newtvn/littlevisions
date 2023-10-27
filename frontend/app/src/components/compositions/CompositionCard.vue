<template>
    <div class="card card--secondary card--reverse composition-card">
        <div class="card__top">
            <span class="card__tag">
                {{ progress }}% complete
            </span>
        </div>
        <div class="card__bottom">
            <h2 class="card__title">
                {{ title }}
            </h2>
            <div class="row default-gap">
                <img src="https://images.unsplash.com/photo-1438761681033-6461ffad8d80?" alt="" class="profile-image">
                <p class="card__text" v-if="comment">
                    {{ comment }}
                </p>
            </div>
        </div>
    </div>
</template>

<script>

export default{
    props:{
        title: {
            type: String,
            required: true,
            default: "Assignment"
        
        },
        comment: {
            type: String,
            required: false
        },
        progress: {
            type: Number,
            required: true,
            default: 0
        
        }
    }
}
</script>

<style lang="scss" scoped>
$spacer-xs: 10px;
$spacer-s: 20px;
$spacer-m: 35px;
$spacer-l: 60px;
$spacer-xl: 100px;

:root {
    --accent: #c7ecee;
    --accentComplimentary: #7ed6df;
}




.card {
    border-radius: $spacer-m;
    overflow: hidden;
    height: 100%;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    min-height: 300px;
    max-width: 300px;

    &__top {
        position: relative;
        background-color: var(--accentComplimentary);
        padding: $spacer-m $spacer-m 2*$spacer-m $spacer-m;
        z-index: 0;
        display: flex;
        align-items: flex-start;

        &:has(.card__figure) {
            aspect-ratio: 3/2;
        }
    }

    &__bottom {
        position: relative;
        margin-top: -$spacer-m;
        background-color: var(--accent);
        padding: $spacer-m;
        border-radius: $spacer-m;
        display: flex;
        gap: $spacer-l;
        flex-direction: column;
        justify-content: space-between;
        flex-grow: 1;
        z-index: 1;
    }

    &__figure {
        position: absolute;
        inset: 0;
        mix-blend-mode: lighten;
        opacity: .5;
    }

    &__image {
        width: 100%;
        height: 100%;
        object-fit: cover;
    }

    &__tag {
        padding: $spacer-xs $spacer-s;
        border: 1px solid currentColor;
        border-radius: 2em;
        position: relative;
        z-index: 1;
        // box-shadow: 0 0 2em rgba(255,255,255,0.35);
        // background-color: rgba(255,255,255,0.15);
    }

    &__title {
        font-size: 2rem;
        font-weight: 600;
    }

    &__text {
        font-size: 1.1rem;

    }
}

.card--reverse {
    flex-direction: column-reverse;

    .card {
        &__bottom {
            margin-top: 0;
            margin-bottom: -$spacer-m;
        }

        &__top {
            position: relative;
            padding: 2*$spacer-m $spacer-m $spacer-m $spacer-m;
            align-items: flex-end;
        }
    }
}

.card--primary {
    --accent: #ffbe76;
    --accentComplimentary: #706fd3;
}

.card--secondary {
    --accent: #63cdda;
    --accentComplimentary: #f5cd79;
}

.card--tertiary {
    --accent: #888df1;
    --accentComplimentary: #ff9ff3;
}
</style>