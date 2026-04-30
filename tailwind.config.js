/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./index.html",
    "./src/**/*.html",
    "./*.html",
    "./*.js"
  ],
  theme: {
    extend: {
      fontFamily: {
        sans: ['Inter', 'sans-serif'],
        display: ['Outfit', 'sans-serif'],
      },
      colors: {
        primary: '#0a0a0a', 
        secondary: '#171717',
        accent: '#3b82f6', // modern blue
        accentDark: '#2563eb',
        light: '#f8fafc',
      }
    },
  },
  plugins: [],
}
