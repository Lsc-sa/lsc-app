import "./index.css";
import "./assets/styles/main.css";
import { createApp, reactive } from "vue";
import App from "./App.vue";
import VueDatePicker from "@vuepic/vue-datepicker";
import "@vuepic/vue-datepicker/dist/main.css";
import router from "./router/index.js";
import resourceManager from "../../libs/resourceManager";
import i18n from "./i18n";
import { VueQueryPlugin } from "@tanstack/vue-query";
import { initSocket } from "./socket";
/* import the fontawesome core */
import StarRating from "vue-star-rating";

import { library, config } from "@fortawesome/fontawesome-svg-core";

/* import font awesome icon component */
import { FontAwesomeIcon } from "@fortawesome/vue-fontawesome";
import { fas } from "@fortawesome/free-solid-svg-icons";
import { fab } from "@fortawesome/free-brands-svg-icons";
import { far } from "@fortawesome/free-regular-svg-icons";

library.add(fas, fab, far);

config.familyDefault = "classic";
config.styleDefault = "solid";

const app = createApp(App);
// const auth = reactive(new Auth());

// Plugins
app.component("font-awesome-icon", FontAwesomeIcon);
app.use(i18n);
app.use(router);
app.use(resourceManager);
app.use(VueQueryPlugin);
// Global Properties,
// components can inject this
// app.provide("$auth", auth);
// app.provide("$call", call);
app.component("VueDatePicker", VueDatePicker);
app.component("StarRating", StarRating);

let socket;
socket = initSocket();
// app.config.globalProperties.$socket = socket;
app.provide("$socket", socket);
app.mount("#app");
