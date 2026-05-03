const chartjs = document.getElementById('chart');

new Chart(chartjs, {
  type: 'bar',
  data: {
    labels: ["Walmart", "NVIDIA", "Amazon", "Apple", "Alphabet (GOOG)","Meta Platforms"],
    datasets: [{
      label: "Company Shares price",
      data: [131, 198, 268, 280,383,608]
    }]
  }
});