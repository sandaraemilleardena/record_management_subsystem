document.addEventListener("DOMContentLoaded", loadRecords);

function loadRecords() {
    fetch("/records")
        .then(response => response.json())
        .then(data => {
            const table = document.getElementById("recordTable");
            table.innerHTML = "";

            data.forEach((record, index) => {
                table.innerHTML += `
                    <tr>
                        <td>${index + 1}</td>
                        <td>${record.name}</td>
                        <td>
                            <button class="edit" onclick="editRecord('${record.name}')">Edit</button>
                            <button class="delete" onclick="deleteRecord('${record.name}')">Delete</button>
                        </td>
                    </tr>
                `;
            });
        });
}

function addRecord() {
    const name = document.getElementById("nameInput").value;

    fetch("/add", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ name: name })
    }).then(() => {
        document.getElementById("nameInput").value = "";
        loadRecords();
    });
}

function deleteRecord(name) {
    fetch(`/delete/${name}`, {
        method: "DELETE"
    }).then(() => loadRecords());
}

function editRecord(oldName) {
    const newName = prompt("Enter new name:");
    if (!newName) return;

    fetch("/edit", {
        method: "PUT",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
            old_name: oldName,
            new_name: newName
        })
    }).then(() => loadRecords());
}