<script>
export default {

  name: "FlipBook",
  data() {
    return {z: 1, si: 1};
  },
  props: {
    story: Array,
  },
  mounted() {
    this.turnRight();
  },
  methods: {

    sttmot(i) {
      setTimeout(function () {
        var right = document.getElementsByClassName("right");
        right[i].style.zIndex = "auto";
      }, 300);
    },
    turnRight() {

      var right = document.getElementsByClassName("right");

      if (this.si >= 1) {
        this.si--;
      } else {
        this.si = right.length - 1;


        for (var i = 0; i < right.length; i++) {
          right[i].className = "right";
          this.sttmot(i);
          this.z = 1;
        }
      }
      right[this.si].classList.add("flip");
      this.z++;
      right[this.si].style.zIndex = this.z;
    },
    turnLeft() {

      var right = document.getElementsByClassName("right");
      if (this.si < right.length) {
        this.si++;
      } else {
        this.si = 1;
        for (let i = right.length - 1; i > 0; i--) {
          right[i].classList.add("flip");
          right[i].style.zIndex = right.length + 1 - i;
        }
      }
      right[this.si - 1].className = "right";
      setTimeout(function () {
        if (right[this.si - 1] != null) {
          right[this.si - 1].style.zIndex = "auto";
        }
      }, 350);
    },
  }
}


</script>

<template>
  <div class="book-section">
    <div class="container">
      <template v-for="(item,position) in this.story" v-bind:key="item">
        <div class="right" v-if="position===0">
          <figure class="back" id="back-cover">{{ item.description }}</figure>
          <figure class="front"><img class="image-flip" :src="item.imageUrl"/></figure>
        </div>
        <div v-else-if="position===this.story.length-1" class="right">
          <figure class="back">{{ item.description }}</figure>
          <figure class="front" id="cover"><img class="image-flip" :src="item.imageUrl"/></figure>
        </div>
        <div v-else class="right">
          <figure class="back">{{ item.description }}</figure>
          <figure class="front"><img :src="item.imageUrl" class="image-flip"/></figure>
        </div>
      </template>
    </div>
    <button @click="turnLeft()">Previous</button>
    <button @click="turnRight()">Next</button>


  </div>
</template>

<style scoped lang="css">
.image-flip {
  width: 100%;
  height: 100%;
}

body {
  margin: 0;
  background-color: #ffecc6;
}

* {
  box-sizing: border-box;
}

.back {
  padding: 20px !important;
  font-family: "Poppins", sans-serif !important;

}

.book-section {
  height: 100vh;
  width: 100%;
  padding: 40px 0;
  text-align: center;
}

.book-section > .container {
  height: 75vh;
  width: 80vw;
  position: relative;
  left: 50%;
  transform: translateX(-50%);
  border-radius: 2%;
  margin-bottom: 30px;
  perspective: 1200px;
}

.container > .right {
  position: absolute;
  height: 100%;
  width: 50%;
  transition: 0.7s ease-in-out;
  transform-style: preserve-3d;
}

.book-section > .container > .right {
  right: 0;
  transform-origin: left;
  border-radius: 10px 0 0 10px;
}

.right > figure.front, .right > figure.back {
  margin: 0;
  height: 100%;
  width: 100%;
  position: absolute;
  left: 0;
  top: 0;
  background-size: 200%;
  background-repeat: no-repeat;
  backface-visibility: hidden;
  background-color: white;
  overflow: hidden;
}

.right > figure.front {
  background-position: right;
  border-radius: 0 10px 10px 0;
  box-shadow: 2px 2px 15px -2px rgba(0, 0, 0, 0.2);
}

.right > figure.back {
  background-position: left;
  border-radius: 10px 0 0 10px;
  box-shadow: -2px 2px 15px -2px rgba(0, 0, 0, 0.2);
  transform: rotateY(180deg);
}

.flip {
  transform: rotateY(-180deg);
}

.flip::before {
  content: "";
  position: absolute;
  top: 0;
  left: 0;
  z-index: 10;
  width: 100%;
  height: 100%;
  border-radius: 0 10px 10px 0;
  background-color: rgba(0, 0, 0, 0.1);
}

.book-section > button {
  border: 2px solid #ef9f00;
  background-color: transparent;
  color: #ef9f00;
  padding: 10px 20px;
  border-radius: 5px;
  cursor: pointer;
  margin: 10px;
  transition: 0.3s ease-in-out;
}

.book-section > button:focus, .book-section > button:active {
  outline: none;
}

.book-section > p {
  color: rgba(0, 0, 0, 0.7);
  font-family: calibri;
  font-size: 24px;
  margin: 15px 0;
}

.book-section > p > a {
  text-decoration: none;
  color: #ef9f00;
}

.book-section > button:hover {
  background-color: #ef9f00;
  color: #fff;
}

.front#cover, .back#back-cover {
  background-color: #ffcb63;
  font-family: calibri;
  text-align: left;
  padding: 0 0px;
}

.front#cover h1 {
  color: #fff;
}

.front#cover p {
  color: rgba(0, 0, 0, 0.8);
  font-size: 14px;

}
</style>