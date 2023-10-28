<template>
  <NavBar />
  <main id="">

    <div class="row feature-navigation-cards">
      <RouterLink :to="{ name: 'story-home' }">
        <div class="feature-navigation-card  scale-hover bg-primary">
          <div class="feature-navigation-card-content">
            <h2>Stories</h2>
            <p class="feature-navigation-card-description">
              Get ready to craft amazing adventures with LittleVisions' Stories feature, where you can create, explore,
              and
              share imaginative tales with your friends!
            </p>
            <!-- <button class="feature-navigation-card-btn" @click="$router.push({ name: 'story-create' })">Start</button> -->
          </div>

          <img src="@/assets/images/spongebob.png" alt="" class="feature-navigation-card-image">
        </div>
      </RouterLink>
      <RouterLink :to="{ name: 'compositions-list' }">

        <div class="feature-navigation-card scale-hover  bg-secondary">
          <div class="feature-navigation-card-content">
            <h2>Assignments</h2>

            <p class="feature-navigation-card-description">
              Get ready for creative challenges! Your parents have exciting assignments to boost your imagination with
              LittleVisions.
            </p>
            <!-- <button class="feature-navigation-card-btn" @click="$router.push({ name: 'story-create' })">Start</button> -->
          </div>

          <img src="@/assets/images/stitch.png" alt="" class="feature-navigation-card-image">
        </div>
      </RouterLink>
    </div>

  </main>
</template>

<script>
import NavBar from '@/components/navigation/NavBar.vue';
// @ is an alias to /src

export default {
  name: 'HomeView',
  components: {
    NavBar
  },
  methods:{
  
  }
}
</script>
<style lang="scss">
@import "@/styles/use-select.scss";
</style>
