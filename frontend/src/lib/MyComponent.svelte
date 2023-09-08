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

<h1>This is an instance of MyComponent</h1>
<h2>The value of foo is {foo}</h2>
<button on:click={something}> Make a REST call </button>
