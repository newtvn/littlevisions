<script setup>

import FlipBook from "@/components/Flipbook.vue";
</script>

<template>
  <FlipBook
      :story="[{description:'Hello world i am a boy',imageUrl:'https://images.unsplash.com/photo-1663344010224-a89a22f14bb7?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxlZGl0b3JpYWwtZmVlZHw1fHx8ZW58MHx8fHx8&auto=format&fit=crop&w=500&q=60'}
      ,{description:'How was your day',imageUrl:'https://images.unsplash.com/photo-1663344010224-a89a22f14bb7?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxlZGl0b3JpYWwtZmVlZHw1fHx8ZW58MHx8fHx8&auto=format&fit=crop&w=500&q=60'},
       {description:'Hinderance',imageUrl:'https://images.unsplash.com/photo-1663344010224-a89a22f14bb7?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxlZGl0b3JpYWwtZmVlZHw1fHx8ZW58MHx8fHx8&auto=format&fit=crop&w=500&q=60'}]"></FlipBook>
</template>

<style scoped lang="css">

</style>