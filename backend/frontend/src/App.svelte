<script>
  let message;

  fetch("http://127.0.0.1:8000/hello/준호").then((res) => {
    res.json().then((json) => {
      message = json.message;
    });
  });
</script>

<h1>{message} ㅎ</h1>