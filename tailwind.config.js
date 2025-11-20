/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./*.html", "./src/**/*.{js,ts,jsx,tsx}"],
  theme: {
    extend: {
      colors: {
        'brand-sage': '#9CB79E', // Main background green
        'brand-sage-light': '#C8DBC9', // Lighter accent
        'brand-dark': '#1B3123', // Dark text
        'brand-white': '#FDFDFD',
        'brand-gray': '#F5F5F5',
      },
      fontFamily: {
        sans: ['Inter', 'sans-serif'],
      }
    },
  },
  plugins: [],
}
