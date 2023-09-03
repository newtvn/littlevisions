import { createStore } from "vuex";

export default createStore({
  state: {
    currentStoryText: null,
  },
  getters: {},
  mutations: {
    setCurrentStoryText(state, text) {
      state.currentStoryText += text;
    },
  },
  actions: {
    setNarrative(_,text) {
      var narrative = localStorage.getItem("narrative");
  
      if (narrative) {
        var _text = (narrative += text);
        localStorage.setItem("narrative", _text);
      } else {
        localStorage.setItem("narrative", text);
      }
    },
    clearNarrative(){
      localStorage.removeItem("narrative")
    },
    
  },
  modules: {},
});
