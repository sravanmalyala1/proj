document.addEventListener('DOMContentLoaded', function() {
    alert('JavaScript is working!');
});



document.addEventListener('DOMContentLoaded', function() {
    document.getElementById('button1').addEventListener('click', function() {
        fetch('/my-view/')
            .then(response => {
                if (!response.ok) {
                    throw new Error('Network response was not ok');
                }
                return response.json();
            })
            .then(data => {
                console.log('Data received:', data); // Debug: Check data in the console

                // Check if table1 exists in the data and is an array
                if (Array.isArray(data.table1)) {
                    // Get the table body
                    const tableBody = document.getElementById('table-body');

                    // Clear existing rows
                    tableBody.innerHTML = '';

                    // Populate the table with data from table1
                    data.table1.forEach(row => {
                        const tr = document.createElement('tr');
                        tr.innerHTML = `
                            <td>${row.id}</td>
                            <td>${row.name}</td>
                            <td>${row.value}</td>
                        `;
                        tableBody.appendChild(tr);
                    });
                } else {
                    console.error('table1 is not an array or does not exist in the data');
                }
            })
            .catch(error => console.error('Error fetching data:', error));
    });
});


