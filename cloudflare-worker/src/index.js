export default {
  async fetch(request) {
    const url = new URL(request.url)
    url.hostname = "khleez-bot.choreo.dev" // Replace with your actual backend URL
    return fetch(url.toString(), request)
  }
}
