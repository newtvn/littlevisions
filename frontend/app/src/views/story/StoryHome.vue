<template>
    <main id="story-home">
        <div class="profile-greeting row default-gap">
            <VueAvvvatar value="Edwin" style="shape" :border="true" borderColor="#FFC61A" borderSize="2" size="32" />
            <p class="greeting-text">Hello Edwin</p>
        </div>

        <div class="main-section">
            <div class="card bg-primary home-card" @click="$router.push({ name: 'story-create' })">
                <div class="card-content">
                    <h2>Create A Story</h2>
                    <p class="home-card-description">
                        Use Create Story to invent your own exciting tales, putting your imagination to work and becoming a
                        storytelling master!
                    </p>
                    <button class="card-btn">Start</button>
                </div>

                <img src="@/assets/images/giraffe.png" alt="" class="home-card-image">
            </div>
            <div class="row space-btn" id="home-cards-secondary-container">
                <div class="card bg-secondary home-card" @click="$router.push({ name: 'story-mine' })">
                    <div class="card-content">
                        <h2>Your Stories</h2>
                        <p class="home-card-description">
                            Have a look at your stories, and continue writing if you want to. </p>
                        <button class="card-btn">Stories</button>
                    </div>
                    <img src="@/assets/images/bird.png" alt="" class="home-card-image">

                </div>
                <div class="card bg-tertiary home-card" @click="$router.push({ name: 'library-home' })">
                    <div class="card-content">
                        <h2>Read from Library</h2>
                        <p class="home-card-description">
                            Check out our library to see what your people have written </p>
                        <button class="card-btn">Library</button>
                    </div>
                    <img src="@/assets/images/bunny.png" alt="" class="home-card-image">

                </div>
            </div>
        </div>
    </main>
</template>

<script>

export default {

}
</script>