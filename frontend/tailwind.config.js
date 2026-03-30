/** @type {import('tailwindcss').Config} */
export default {
  content: ["./index.html", "./src/**/*.{js,ts,jsx,tsx}"],
  theme: {
    extend: {
      colors: {
        harness: {
          blue: '#0278D5',
          dark: '#0B1B2B',
          teal: '#00ADE4',
          green: '#42BE65',
          orange: '#FF832B',
        }
      }
    },
  },
  plugins: [],
}
