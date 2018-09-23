// Set new default font family and font color to mimic Bootstrap's default styling
Chart.defaults.global.defaultFontFamily = '-apple-system,system-ui,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif';
Chart.defaults.global.defaultFontColor = '#292b2c';

// Area Chart Example
var ctx = document.getElementById("myAreaChart");
var myLineChart = new Chart(ctx, {
  type: 'line',
  data: {
    labels: ["12:00:00PM", "12:01:00PM", "12:02:00PM", "12:03:00PM", "12:04:00PM", "12:05:00PM", "12:06:00PM"],
    datasets: [{
      label: "Timestamp",
      lineTension: 0.3,
      backgroundColor: "rgba(2,117,216,0.2)",
      borderColor: "rgba(2,117,216,1)",
      pointRadius: 5,
      pointBackgroundColor: "rgba(63, 63, 191, 1)",
      pointBorderColor: "rgba(255,255,255,0.8)",
      pointHoverRadius: 5,
      pointHoverBackgroundColor: "rgba(2,117,216,1)",
      pointHitRadius: 50,
      pointBorderWidth: 2,
      data: [0.01, 0.02, 0.005, 0.001, 0.125, 0.04],
    },{
    label: "Timestamp",
      lineTension: 0.3,
      backgroundColor: "rgba(2,193,66,66,0.2)",
      borderColor: "rgba(2,193,66,1)",
      pointRadius: 5,
      pointBackgroundColor: "rgba(63, 191, 63, 1)",
      pointBorderColor: "rgba(255,255,255,0.8)",
      pointHoverRadius: 5,
      pointHoverBackgroundColor: "rgba(2,193,66,1)",
      pointHitRadius: 50,
      pointBorderWidth: 2,
      data: [0.04, 0.03, 0.106, 0.211, 0.125, 0.08],
     },{
    label: "Timestamp",
      lineTension: 0.3,
      backgroundColor: "rgba(2,191,63,191,0.2)",
      borderColor: "rgba(2,191,63,1)",
      pointRadius: 5,
      pointBackgroundColor: "rgba(127, 63, 191, 1)",
      pointBorderColor: "rgba(255,255,255,0.8)",
      pointHoverRadius: 5,
      pointHoverBackgroundColor: "rgba(2,191,63,1)",
      pointHitRadius: 50,
      pointBorderWidth: 2,
      data: [0.04, 0.06, 0.206, 0.311, 0.190, 0.18],
     }],
  },
  options: {
    scales: {
      xAxes: [{
        time: {
          unit: 'date'
        },
        gridLines: {
          display: false
        },
        ticks: {
          maxTicksLimit: 7
        }
      }],
      yAxes: [{
        ticks: {
          min: 0.0,
          max: 0.5,
          maxTicksLimit: 5
        },
        gridLines: {
          color: "rgba(0, 0, 0, .125)",
        }
      }],
    },
    legend: {
      display: false
    }
  }
});
