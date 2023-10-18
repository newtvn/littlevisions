<template>
  <main id="">
    <div class="row">
      <div class="feature-navigation-card">
        <div class="feature-navigation-card-content">
          <h2>Stories</h2>
          <p class="feature-navigation-card-description">
            Use Create Story to invent your own exciting tales, putting your imagination to work and becoming a
            storytelling master!
          </p>
          <button class="feature-navigation-card-btn" @click="$router.push({ name: 'story-create' })">Start</button>
        </div>

        <img src="@/assets/images/giraffe.png" alt="" class="feature-navigation-card-image">
      </div>
      <div class="feature-navigation-card">
        <div class="feature-navigation-card-content">
          <h2>Assignments</h2>
          <p class="feature-navigation-card-description">
            Improve on your already written assignments done by your parents
          </p>
          <button class="feature-navigation-card-btn" @click="$router.push({ name: 'story-create' })">Start</button>
        </div>

        <img src="@/assets/images/giraffe.png" alt="" class="feature-navigation-card-image">
      </div>
    </div>

  </main>
</template>

<script>
// @ is an alias to /src

export default {
  name: 'HomeView',
  components: {
  }
}
</script>
