<script>
    export let params = {}
    let question_id = params.question_id
    let question = {}

    function get_question() {
        fetch("http://127.0.0.1:8000/v1/question/detail/"+question_id).then((res) => {
            res.json().then((json) => {
                question = json
            })
        });
    }

    get_question()
</script>

<h1>{question.subject}</h1>
<div>
    {question.content}
</div>