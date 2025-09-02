let votes = JSON.parse(localStorage.getItem("votes")) || [];

function vote(category, candidate) {
  // For single-choice categories, replace old vote
  if (category !== "Prefects") {
    votes = votes.filter(v => v.category !== category);
  }

  votes.push({ category, candidate });
  localStorage.setItem("votes", JSON.stringify(votes));

  alert(`✅ Vote casted for ${candidate} in ${category}`);
}

function downloadCSV() {
  if (votes.length === 0) {
    alert("⚠️ No votes recorded yet.");
    return;
  }

  let csv = "Category,Candidate\n";
  votes.forEach(v => {
    csv += `${v.category},${v.candidate}\n`;
  });

  const blob = new Blob([csv], { type: "text/csv" });
  const url = window.URL.createObjectURL(blob);
  const a = document.createElement("a");
  a.setAttribute("href", url);
  a.setAttribute("download", "votes.csv");
  a.click();
}