/** @type {import('tailwindcss').Config} */
import daisyui from "daisyui";

export default {
  content: [
    "./index.html",
    "./src/**/*.{vue,js,ts,jsx,tsx}"
  ],
  theme: {
    extend: {
      fontFamily: {
        body: ["Cairo"],
      },
      colors: {
        primary: "#354F88",
        primaryLight: "#5978B9",
        primaryHover: "#223458",
        secondary: "#f1c40f",
        danger: "#C21807",
        success: "#255F0B",
        warning: "#C4951B",
        backG: "#F8F8F8",
      },
      container: {
        center: true,
      },
      boxShadow:{
        mycard:'-2px 6px 6px gainsboro',
      }
    },
  },
  plugins: [daisyui],
};
