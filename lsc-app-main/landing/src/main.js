import "./index.css";
import "./assets/styles/main.css";
import { createApp, reactive } from "vue";
import App from "./App.vue";
// import router from "./router";
// import resourceManager from "../../doppio/libs/resourceManager";
// import call from "../../doppio/libs/controllers/call";
// import socket from "../../doppio/libs/controllers/socket";
// import Auth from "../../doppio/libs/controllers/auth";

/* import the fontawesome core */
import { library, config } from "@fortawesome/fontawesome-svg-core";
/* import font awesome icon component */
import { FontAwesomeIcon } from "@fortawesome/vue-fontawesome";
import { fas } from "@fortawesome/free-solid-svg-icons";
import { fab } from "@fortawesome/free-brands-svg-icons";
import { far } from "@fortawesome/free-regular-svg-icons";

// Import Locales
import i18n from "./i18n";

library.add(fas, fab, far);

config.familyDefault = "classic";
config.styleDefault = "solid";

const app = createApp(App);
// const auth = reactive(new Auth());

// Plugins
app.component("font-awesome-icon", FontAwesomeIcon);
// app.use(router);
app.use(i18n);
// app.use(resourceManager);

// Global Properties,
// components can inject this
// app.provide("$auth", auth);
// app.provide("$call", call);
// app.provide("$socket", socket);

app.mount("#app");
