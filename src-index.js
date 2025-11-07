export default {
  async fetch(request) {
    const url = new URL(request.url)
    url.hostname = "khleez-bot.choreo.dev" // Replace with your Choreo or Render bot URL
    return fetch(url.toString(), request)
  }
}
