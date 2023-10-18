import { createRouter, createWebHistory } from "vue-router";
// import HomeView from "../views/HomeView.vue";
import StoryView from "../views/StoryView.vue";
import StoryBuild from "../views/story/StoryBuild.vue";
import StoryHome from "../views/story/StoryHome.vue";
import StoryPlay from "../views/story/StoryPlay.vue";
import StoryCreate from "../views/story/StoryCreate.vue";
import StoryMine from "../views/story/StoryMine.vue";
import LibraryView from "../views/LibraryView.vue";
import FlipBookMental from "@/components/FlipBookMental.vue";
import CharacterView from "@/views/story/CharacterView.vue";
import HomeView from "@/views/HomeView.vue";
const routes = [
  {
    path: "/",
    name: "UseSelect",
    component: HomeView,
  },
  {
    path: "/stories",
    name: "story",
    component: StoryView,
    children: [
      {
        path: "",
        name: "story-home",
        component: StoryHome,
      },

      {
        path: "create/",
        name: "story-create",
        component: StoryCreate,
      },
      {
        path: "mine/",
        name: "story-mine",
        component: StoryMine,
      },
      {
        path: "library/",
        name: "library-home",
        component: LibraryView,
      },
      {
        path: "play/:story_id/",
        name: "play-story",
        component: StoryPlay,
      },
      {
        path: "/character/:id",
        name: "character-page",
        component: CharacterView,
      },
    ],
  },

  {
    path: "/stories/:story_id/build/:board_id?/",
    name: "build-story",
    component: StoryBuild,
    meta: {
      watchParam: "board_id",
    },
  },
  {
    path: "/flipbook/:story_id",
    name: "flipbook",
    component: FlipBookMental,
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;
