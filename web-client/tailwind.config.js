/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        primary:{
          DEFAULT: "#059669",
          light: "#10B981",
          dark: "#047857",
        },
        background: "F9FAFB",
        card: "#FFFFFF",
      },
    },
  },
  plugins: [],
}

