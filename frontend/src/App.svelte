<script lang="ts">
  import svelteLogo from "./assets/svelte.svg";
  import fastAPILogo from "./assets/fastapi.svg";
  import bulmaLogo from "./assets/bulma.svg";

  import Counter from "./lib/Counter.svelte";
  import RestDemo from "./lib/RestDemo.svelte";
  import MyCounter from "./lib/MyCounter.svelte";
  import Hero from "./lib/Hero.svelte";
  import { onMount } from "svelte";
  let i: number = 0;
  onMount(() => {
    console.log("onMount");
    const protocol = { "http:": "ws", "https:": "wss" }[location.protocol];
    const url = `${protocol}://${location.host}/ws`;
    const ws = new WebSocket(url);

    ws.onmessage = (event) => {
      let data = JSON.parse(event.data);

      i = data.i;
    };
  });
</script>

<Hero />

<section class="section">
  <h1 class="title">Basic Svelte bindings</h1>

  <Counter />
</section>

<section class="section">
  <h1 class="title">REST example</h1>
  <RestDemo />
</section>

<section class="section">
  <h1 class="title">Websocket Integration</h1>

  <MyCounter {i} />
</section>

<section class="section">
  <h1 class="title">Built With</h1>

  <article class="media">
    <figure class="media-left">
      <p class="image is-64x64">
        <img src={fastAPILogo} alt="fastAPI logo" />
      </p>
    </figure>
    <div class="media-content">
      <div class="content">
        <h3 class="title is-3">FastAPI</h3>
      </div>
    </div>
  </article>
  <article class="media">
    <figure class="media-left">
      <p class="image is-64x64">
        <img src={bulmaLogo} alt="bulma logo" />
      </p>
    </figure>
    <div class="media-content">
      <div class="content">
        <h3 class="title is-3">Bulma</h3>
      </div>
    </div>
  </article>

  <article class="media">
    <figure class="media-left">
      <p class="image is-64x64">
        <img src={svelteLogo} alt="svelte logo" />
      </p>
    </figure>
    <div class="media-content">
      <div class="content">
        <h3 class="title is-3">Svelte</h3>
      </div>
    </div>
  </article>
</section>

<style>
</style>
