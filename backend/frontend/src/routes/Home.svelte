<script>
    import { link } from 'svelte-spa-router'

    let question_list = []

    function get_question_list() {
        fetch("http://127.0.0.1:8000/v1/question/list").then((res) => {
            res.json().then((json) => {
                console.log(json);
                question_list = json;
            });
        });
    }
  
  get_question_list();
</script>

<ul>
    {#each question_list as question}
        <li><a use:link href="/detail/{question.id}">{question.subject}</a></li>
    {/each}
</ul>