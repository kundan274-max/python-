function showMessage(event, message) {
  event.preventDefault();
  alert(message);
}

function findDonor() {
  let bloodGroup = document.getElementById("bloodGroup").value;
  let result = document.getElementById("donorResult");

  let donors = {
    "A+": [
      "Ravi Kumar - A+ - 9876543210 - Jamshedpur",
      "Sneha Singh - A+ - 9876543201 - Mango"
    ],
    "A-": [
      "Ankit Raj - A- - 9876543202 - Sakchi"
    ],
    "B+": [
      "Aman Verma - B+ - 9876543212 - Mango",
      "Pooja Kumari - B+ - 9876543203 - Adityapur"
    ],
    "B-": [
      "Rahul Das - B- - 9876543204 - Bistupur"
    ],
    "O+": [
      "Neha Sharma - O+ - 9876543205 - Jugsalai"
    ],
    "O-": [
      "Anjali Singh - O- - 9876543211 - Sakchi"
    ],
    "AB+": [
      "Priya Kumari - AB+ - 9876543213 - Adityapur"
    ],
    "AB-": [
      "Sanjay Kumar - AB- - 9876543206 - Telco"
    ]
  };

  let donorList = donors[bloodGroup];

  if (donorList && donorList.length > 0) {
    let output = "<strong>Available Donors:</strong><br><br>";
    donorList.forEach(function(donor) {
      output += "🩸 " + donor + "<br><br>";
    });
    result.innerHTML = output;
  } else {
    result.innerHTML = "❌ No donor found for this blood group.";
  }
}