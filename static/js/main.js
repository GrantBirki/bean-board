async function apiCall(url, method, data) {

    headers = {
        'Accept': 'application/json',
        'Content-Type': 'application/json'
    };

    if (method == 'GET') {
        rawResponse = await fetch(url, {
            method: method,
            headers: headers,
        });
    }
    else {
        rawResponse = await fetch(url, {
            method: method,
            headers: headers,
            body: JSON.stringify(data)
        });
    }
    try {
        var content = await rawResponse.json();
        var status = rawResponse.status;
        if (status !== 200) {
            console.log('apiCall Status:', status);
            return {content, status};
        }
        else {
            return {content, status};
        }
    } catch (error) {
        alert('Failed');
        console.log('API call failed:', error);
    }
}

function capitalize(string) {
    return string.charAt(0).toUpperCase() + string.slice(1);
}
