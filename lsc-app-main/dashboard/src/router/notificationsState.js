import { reactive } from "vue";
import { initSocket } from "../socket";

const socket = initSocket();

export const notificationsState = reactive({
  hasNewNotifications: false,
});

const requestOptions = {
  method: "GET",
  headers: { Cookie: document.cookie },
  redirect: "follow",
};

fetch("/api/method/frappe.auth.get_logged_user", requestOptions)
  .then((response) => {
    if (!response.ok) {
      throw new Error("Network response was not ok");
    }
    return response.json();
  })
  .then((data) => {
    socket.on(data.message, (data) => {
      notificationsState.hasNewNotifications = true;
    });
  })
  .catch((error) => {
    console.error("Fetch error:", error);
  });
