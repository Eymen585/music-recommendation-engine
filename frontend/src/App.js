function getRecommendations() {
    const userId = document.getElementById('userId').value;

    fetch('/user-profile/' + userId)
        .then(response => response.json())
        .then(profile => {
            fetch('/recommendations', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(profile),
            })
                .then(response => response.json())
                .then(data => {
                    const recommendationsDiv = document.getElementById('recommendations');
                    recommendationsDiv.innerHTML = '<h2>Recommended Songs</h2>';
                    data.forEach(song => {
                        recommendationsDiv.innerHTML += `
                        <p>${song.title} by ${song.artist}</p>
                    `;
                    });
                });
        });
}
