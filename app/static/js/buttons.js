const enable = document.getElementById('enable');
enable.addEventListener('click', async _ => {
  resp = await apiCall('/api/button', 'POST', {enabled: true});
  updateStatus(resp.content.state, resp.status);
});

const disable = document.getElementById('disable');
disable.addEventListener('click', async _ => {
  resp = await apiCall('/api/button', 'POST', {enabled: false});
  updateStatus(resp.content.state, resp.status);
});

function updateStatus(state, status) {

  console.log(state);
  console.log(status);

  if (status != 200) {
    alert('Error: ' + status);
    return;
  }

  if (state === 'enabled') {
    css_state = 'ok-lower';
  } else {
    css_state = 'error-lower';
  }

  document.getElementById("main-status").textContent=capitalize(state);
  document.getElementById("main-status").className = css_state + " info-lower info-upper";
}