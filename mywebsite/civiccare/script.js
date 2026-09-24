// ---------------- LOGIN ----------------
function loginUser(event) {
  event.preventDefault();

  let username = document.getElementById("username").value;
  let password = document.getElementById("password").value;
  let loginMsg = document.getElementById("loginMsg");

  if (username === "admin" && password === "1234") {
    localStorage.setItem("isLoggedIn", "true");
    window.location.href = "dashboard.html";
  } else {
    loginMsg.innerText = "Invalid Username or Password!";
  }
}

function togglePassword() {
  let password = document.getElementById("password");

  if (password.type === "password") {
    password.type = "text";
  } else {
    password.type = "password";
  }
}

function logout() {
  localStorage.removeItem("isLoggedIn");
  window.location.href = "login.html";
}

// ---------------- DASHBOARD PROTECTION ----------------
if (window.location.pathname.includes("dashboard.html")) {
  if (localStorage.getItem("isLoggedIn") !== "true") {
    window.location.href = "login.html";
  }
}

// ---------------- COMPLAINT SYSTEM ----------------
let complaintForm = document.getElementById("complaintForm");
let complaintList = document.getElementById("complaintList");

let complaints = JSON.parse(localStorage.getItem("complaints")) || [];

if (complaintForm) {
  complaintForm.addEventListener("submit", function (e) {
    e.preventDefault();

    let name = document.getElementById("name").value;
    let problemType = document.getElementById("problemType").value;
    let area = document.getElementById("area").value;
    let description = document.getElementById("description").value;

    let complaint = {
      id: Date.now(),
      name,
      problemType,
      area,
      description,
      status: "Pending"
    };

    complaints.push(complaint);
    localStorage.setItem("complaints", JSON.stringify(complaints));

    complaintForm.reset();
    displayComplaints();
  });
}

function displayComplaints() {
  if (!complaintList) return;

  complaintList.innerHTML = "";

  complaints.forEach((complaint) => {
    complaintList.innerHTML += `
      <div class="complaint-card">
        <h3>${complaint.problemType}</h3>
        <p><strong>Name:</strong> ${complaint.name}</p>
        <p><strong>Area:</strong> ${complaint.area}</p>
        <p><strong>Description:</strong> ${complaint.description}</p>
        <p><strong>Status:</strong> 
          <span class="status ${complaint.status.toLowerCase()}">${complaint.status}</span>
        </p>

        <div class="complaint-actions">
          <button class="resolve-btn" onclick="markResolved(${complaint.id})">Resolve</button>
          <button class="pending-btn" onclick="markPending(${complaint.id})">Pending</button>
          <button class="delete-btn" onclick="deleteComplaint(${complaint.id})">Delete</button>
        </div>
      </div>
    `;
  });

  updateStats();
}

function markResolved(id) {
  complaints = complaints.map(c =>
    c.id === id ? { ...c, status: "Resolved" } : c
  );
  localStorage.setItem("complaints", JSON.stringify(complaints));
  displayComplaints();
}

function markPending(id) {
  complaints = complaints.map(c =>
    c.id === id ? { ...c, status: "Pending" } : c
  );
  localStorage.setItem("complaints", JSON.stringify(complaints));
  displayComplaints();
}

function deleteComplaint(id) {
  complaints = complaints.filter(c => c.id !== id);
  localStorage.setItem("complaints", JSON.stringify(complaints));
  displayComplaints();
}

function updateStats() {
  let total = complaints.length;
  let pending = complaints.filter(c => c.status === "Pending").length;
  let resolved = complaints.filter(c => c.status === "Resolved").length;

  document.getElementById("totalComplaints").innerText = total;
  document.getElementById("pendingComplaints").innerText = pending;
  document.getElementById("resolvedComplaints").innerText = resolved;
}

displayComplaints();