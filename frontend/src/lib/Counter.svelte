<script lang="ts">
  let count: number = 0;
  const increment = () => {
    count += 1;
  };
</script>

<button class="button is-primary" on:click={increment}>
  This button has been clicked {count} times
</button>
