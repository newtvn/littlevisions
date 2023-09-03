import { initializeApp } from "firebase/app";
import {
  getFirestore,
  collection,
  doc,
  addDoc,
  setDoc,
  query,
  orderBy,
  getDocs,
} from "firebase/firestore";

import { getStorage, ref, uploadBytes, getDownloadURL } from "firebase/storage";
// ... other firebase imports
const firebaseConfig = {
  apiKey: "AIzaSyBy34e1q5g0MKM4rdXpdVcpim6ZqHve4Z0",
  authDomain: "littlevisions.firebaseapp.com",
  projectId: "littlevisions",
  storageBucket: "littlevisions.appspot.com",
  messagingSenderId: "936806799910",
  appId: "1:936806799910:web:5f5c0ea39d752f1016a4e7",
};
export const firebaseApp = initializeApp(firebaseConfig);

// used for the firestore refs
export const firestore = getFirestore(firebaseApp);
export const storage = getStorage(firebaseApp);
// here we can export reusable database references
export const storiesCollection = collection(firestore, "stories");

export const getStoryboard = (id) => {
  return collection(firestore, `stories/${id}/storyboard`);
};
export const getStoryboardDoc = (story_id, board_id) => {
  return doc(firestore, `stories/${story_id}/storyboard/${board_id}`);
};
export const createStory = (e) => {
  var story_colllection = collection(firestore, "stories");
  return addDoc(story_colllection, e);
};
export const createStoryBoard = (story_id, e) => {
  var storyboard_collection = collection(
    firestore,
    `stories/${story_id}/storyboard`
  );
  return addDoc(storyboard_collection, e);
};

export async function getStoryNarrative(story_id) {
  var q = query(getStoryboard(story_id), orderBy("datetime"));
  var docs = await getDocs(q);
  var narrative = "";
  docs.docs.map((data) => {
    narrative += data.data().text;
  });
  console.log(narrative);
  return narrative;
}

export async function pushSoundToFirebase(story_id, board_id, blob) {
  const soundRef = ref(storage, `speech/${board_id}`);
  uploadBytes(soundRef, blob).then((snapshot) => {
    getDownloadURL(snapshot.ref).then(downloadUrl=>{

      var storyboard_doc = getStoryboardDoc(story_id, board_id);
      setDoc(storyboard_doc, { audio_url: downloadUrl },{ merge: true });
    }).catch(e=>{
        console.log(e)
    })
  });
}
export async function pushImageToFirebase(board_id,blob){
  const imageRef = ref(storage, `image/${board_id}`);
  return uploadBytes(imageRef,blob).then(snapshot=>getDownloadURL(snapshot.ref))
}
