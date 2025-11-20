/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./**/*.{html,js}"],
  theme: {
    extend: {
      colors: {
        'brand-green': '#2F5C46', // Approximated from design
        'brand-light-green': '#E8F5E9',
        'brand-dark': '#1A1A1A',
        'brand-gray': '#F5F5F5',
      },
      fontFamily: {
        sans: ['Inter', 'sans-serif'],
      }
    },
  },
  plugins: [],
}
