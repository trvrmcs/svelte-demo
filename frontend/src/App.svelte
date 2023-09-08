<script lang="ts">
  import svelteLogo from "./assets/svelte.svg";
  import viteLogo from "/vite.svg";
  import Counter from "./lib/Counter.svelte";
  import MyComponent from "./lib/MyComponent.svelte";
  import MyCounter from "./lib/MyCounter.svelte";

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

<main>
  <div>
    <a href="https://vitejs.dev" target="_blank" rel="noreferrer">
      <img src={viteLogo} class="logo" alt="Vite Logo" />
    </a>
    <a href="https://svelte.dev" target="_blank" rel="noreferrer">
      <img src={svelteLogo} class="logo svelte" alt="Svelte Logo" />
    </a>
  </div>
  <h1>Vite, Svelte, Typescript, FastAPI</h1>

  <div class="card">
    <Counter />
  </div>
  <div class="card">
    <MyComponent />
  </div>
  <div class="card">
    <MyCounter {i} />
  </div>
</main>

<style>
  .logo {
    height: 6em;
    padding: 1.5em;
    will-change: filter;
    transition: filter 300ms;
  }
  .logo:hover {
    filter: drop-shadow(0 0 2em #646cffaa);
  }
  .logo.svelte:hover {
    filter: drop-shadow(0 0 2em #ff3e00aa);
  }
</style>
