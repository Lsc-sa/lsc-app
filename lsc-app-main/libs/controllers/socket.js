import io from "socket.io-client";

let host = window.location.hostname;
let port = "/lsc.psc-s.com";
let protocol = window.location.protocol === "https:" ? "https" : "http";
let url = `${protocol}://${host}${port}`;

let socket = io(url, {
  withCredentials: true,
  reconnectionAttempts: 3,
});

console.log(url, socket);
export default socket;
