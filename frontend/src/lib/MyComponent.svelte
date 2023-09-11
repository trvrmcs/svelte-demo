<script lang="ts">
    export let foo: string = "xxx";

    const something = () => {
        fetch("/test")
            .then((response) => {
                response.json().then((data) => {
                    foo = data.foo;
                });
            })
            .catch((err) => {
                foo = "something went wrong";
                console.warn("Something went wrong.", err);
            });
    };
</script>

<h3>This is an instance of MyComponent</h3>

<button on:click={something}>
    Retrieve a value from the Python backend via REST</button
>
<pre>{foo}</pre>
