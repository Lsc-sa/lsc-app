import { io } from "socket.io-client";
const URL = `${window.location.origin}/mosandah.frappe.cloud`;
// const URL = `${window.location.origin}/${window.location.host}`;

export function initSocket() {
  let socket = io(URL, {
    withCredentials: true,
    reconnectionAttempts: 5,
  });
  return socket;
}

// import { reactive } from "vue";
// import { io } from "socket.io-client";

// export const state = reactive({
//   connected: false,
//   fooEvents: [],
//   barEvents: [],
// });

// // "undefined" means the URL will be computed from the `window.location` object
// // const URL = process.env.NODE_ENV === "production" ? undefined : "http://localhost:3000";
// // const URL = window.location.origin;

// export const socket = io(URL, {
//   withCredentials: true,
// });

// socket = io(window.location.origin, {
//     extraHeaders: { Authorization: 'token 89e26fc28371597:0ab3b73068612ac' }
//   });

// socket.on("send_notification_data", (...args) => {
//   console.log("send_notification_data", args);
//   state.fooEvents.push(args);
// });

// socket.on("connect", () => {
//   console.log("socket connected? " + socket.connected);
//   state.connected = true;
// });

// socket.on("disconnect", () => {
//   console.log("disconnect");
//   state.connected = false;
// });

// socket.on("foo", (...args) => {
//   console.log("foo", args);
//   state.fooEvents.push(args);
// });

// socket.on("bar", (...args) => {
//   console.log("bar", args);
//   state.barEvents.push(args);
// });
