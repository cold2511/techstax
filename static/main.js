function loadEvents() {
  fetch("/events")
    .then(res => res.json())
    .then(data => {
      const list = document.getElementById("events");
      list.innerHTML = "";

      data.forEach(event => {
        let text = "";

        if (event.action === "PUSH") {
          text = `${event.author} pushed to ${event.to_branch}`;
        }
        else if (event.action === "PULL_REQUEST") {
          text = `${event.author} submitted a pull request from ${event.from_branch} to ${event.to_branch}`;
        }
        else if (event.action === "MERGE") {
          text = `${event.author} merged branch ${event.from_branch} to ${event.to_branch}`;
        }

        const li = document.createElement("li");
        li.innerText = text;
        list.appendChild(li);
      });
    });
}

loadEvents();
setInterval(loadEvents, 15000);
