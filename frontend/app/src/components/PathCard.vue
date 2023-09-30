<template>
    <div class="card-container path-card" @click="flipCard">
      <div class="card" :class="{ 'flipped': selected }">
        <div class="card-front">
          <slot name="front"></slot>
        </div>
        <div class="card-back">
          <slot name="back"></slot>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    props:{
        selected:{
            type: Boolean
        }
    },
    data() {
      return {
        isFlipped: false,
      };
    },
    methods: {
      flipCard() {
        this.$emit('flip')
      },
    },
  };
  </script>
  
  <style scoped>
  /* Styles for the card container */
  .card-container {
    perspective: 1000px;
   
    position: relative;
    /* margin: 50px auto; */
  }
  
  /* Styles for the card */
  .card {
    width: 100%;
    height: 100%;
    transform-style: preserve-3d;
    transition: transform 0.5s;
  }
  
  /* Styles for the front and back of the card */
  .card-front,
  .card-back {
    position: absolute;
    width: 100%;
    height: 100%;
    backface-visibility: hidden;
    display: flex;
    justify-content: center;
    align-items: center;
    font-size: 24px;
    font-weight: bold;
  }
  
  /* Style the front of the card */
  .card-front {
    background-color: #ffb347;
    color: white;
  }
  
  /* Style the back of the card */
  .card-back {
    background-color: #87CEEB;
    color: #333;
    transform: rotateY(180deg);
  }
  
  /* Style the card when flipped */
  .card.flipped {
    transform: rotateY(180deg);
  }
  
  /* Add some fun decorations */
  
  
  /* Add a flip animation */
  @keyframes flip {
    0%,
    100% {
      transform: rotateY(0);
    }
    50% {
      transform: rotateY(180deg);
    }
  }
  </style>
  