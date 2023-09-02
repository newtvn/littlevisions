import { initializeApp } from 'firebase/app'
import { getFirestore,collection,doc } from 'firebase/firestore'
// ... other firebase imports
const firebaseConfig = {
    apiKey: "AIzaSyBy34e1q5g0MKM4rdXpdVcpim6ZqHve4Z0",
    authDomain: "littlevisions.firebaseapp.com",
    projectId: "littlevisions",
    storageBucket: "littlevisions.appspot.com",
    messagingSenderId: "936806799910",
    appId: "1:936806799910:web:5f5c0ea39d752f1016a4e7"
  };
export const firebaseApp = initializeApp(firebaseConfig)

// used for the firestore refs
export const firestore = getFirestore(firebaseApp)
// here we can export reusable database references
export const storiesCollection = collection(firestore,'stories')

export const getStoryboard = (id)=>{
  return collection(firestore,`stories/${id}/storyboard`)
}
export const getStoryboardDoc=(story_id,board_id)=>{
  return doc(firestore,`stories/${story_id}/storyboard/${board_id}`)
}