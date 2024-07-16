const results = {
    "Kharif": {
        "Genetic": {
            "Best Profit": 46040.68,
            "Crops": {
                "Paddy": 3182.5,
                "Maize": 347.63,
                "Bajra": 84.03,
                "Arhar": 226.57,
                "Moong": 2.18,
                "Urad": 46.56,
                "Groundnut": 50.45,
                "Sesamum": 5.87,
                "Sugarcane": 41850.59
            },
            "Execution Time": 0.19991111755371094
        },
        "DifferentialEvolution": {
            "Best Profit": 46769.38,
            "Crops": {
                "Paddy": 3247.00,
                "Maize": 433.27,
                "Bajra": 289.90,
                "Arhar": 246.13,
                "Moong": 2.29,
                "Urad": 69.80,
                "Groundnut": 65.47,
                "Sesamum": 8.53,
                "Sugarcane": 42406.98
            },
            "Execution Time": 0.2916731834411621
        },
        "ParticleSwarmOptimization": {
            "Best Profit": 46401.16,
            "Crops": {
                "Paddy": 3247.01,
                "Maize": 433.27,
                "Bajra": 289.90,
                "Arhar": 246.13,
                "Moong": 2.29,
                "Urad": 69.80,
                "Groundnut": 65.48,
                "Sesamum": 8.53,
                "Sugarcane": 42406.98
            },
            "Execution Time": 0.19247984886169434
        },
        "EvolutionaryProgramming": {
            "Best Profit": 46001.75,
            "Crops": {
                "Paddy": 805.75,
                "Maize": 133.59,
                "Bajra": 55.81,
                "Arhar": 224.95,
                "Moong": 2.11,
                "Urad": 27.38,
                "Groundnut": 44.14,
                "Sesamum": 6.24,
                "Sugarcane": 42406.98
            },
            "Execution Time": 0.008893489837646484
        }
    },
    "Rabi": {
        "Genetic": {
            "Best Profit": 9910.37,
            "Crops": {
                "Wheat": 7848.49,
                "Barley": 88.05,
                "Gram": 190.75,
                "R & M": 478.26,
                "Lentil": 130.59,
                "Potato": 861.29
            },
            "Execution Time": 0.016266584396362305
        },
        "DifferentialEvolution": {
            "Best Profit": 10004.06,
            "Crops": {
                "Wheat": 7931.98,
                "Barley": 124.4,
                "Gram": 203.35,
                "R & M": 550.07,
                "Lentil": 161.0,
                "Potato": 1033.26
            },
            "Execution Time": 0.19333124160766602
        },
        "ParticleSwarmOptimization": {
            "Best Profit": 9800.71,
            "Crops": {
                "Wheat": 7931.98,
                "Barley": 0.0,
                "Gram": 203.35,
                "R & M": 550.07,
                "Lentil": 161.0,
                "Potato": 1033.26
            },
            "Execution Time": 0.13570046424865723
        },
        "EvolutionaryProgramming": {
            "Best Profit": 9387.80,
            "Crops": {
                "Wheat": 7931.98,
                "Barley": 84.97,
                "Gram": 42.29,
                "R & M": 550.07,
                "Lentil": 104.07,
                "Potato": 732.63
            },
            "Execution Time": 0.005026102066040039
        }
    }
};

document.addEventListener("DOMContentLoaded", function () {
    // Function to render chart
    function renderChart(cropData, bestProfit) {
        const chartContainer = document.getElementById("chart-container");

        // Clear previous chart if any
        if (chartContainer.chartInstance) {
            chartContainer.chartInstance.destroy();
        }

        const cropNames = Object.keys(cropData);
        const profitData = cropNames.map(crop => cropData[crop]);

        // Log data for debugging
        console.log("Crops: ", cropNames);
        console.log("Best Profit Data: ", profitData);

        // Create a bar chart using Chart.js
        const ctx = chartContainer.getContext("2d");
        chartContainer.chartInstance = new Chart(ctx, {
            type: "bar",
            data: {
                labels: cropNames,
                datasets: [{
                    label: "Best Profit",
                    backgroundColor: "rgba(54, 162, 235, 0.5)",
                    data: profitData,
                    yAxisID: 'y-axis-profit',
                }]
            },
            options: {
                layout: {
                    padding: {
                        left: 200,
                        right: 200,
                        top: 10,
                        bottom: 300
                    }
                },
                scales: {
                    'y-axis-profit': {
                        type: 'linear',
                        position: 'left',
                        beginAtZero: true,
                        ticks: {
                            callback: function (value) { return value.toLocaleString(); }, // format y-axis values as locale strings
                            fontSize: 8 // decrease font size
                        },
                        title: {
                            display: true,
                            text: 'Best Profit',
                            fontSize: 10 // decrease font size
                        }
                    }
                },
                legend: {
                    display: false
                }
            }
        });
    }

    // Event listener for showing result button
    const showResultBtn = document.getElementById("show-result-btn");
    showResultBtn.addEventListener("click", function () {
        const selectedSeason = document.getElementById("season-select").value;
        const selectedAlgorithm = document.getElementById("algorithm-select").value;

        // Log selections for debugging
        console.log("Selected Season: ", selectedSeason);
        console.log("Selected Algorithm: ", selectedAlgorithm);

        // Adjust the algorithm key to match the data structure
        const algorithmKey = selectedAlgorithm.replace(/\s+/g, '');

        // Pass selected season and algorithm to render chart function
        const seasonData = results[selectedSeason];
        const algorithmData = seasonData[algorithmKey];
        renderChart(algorithmData.Crops, algorithmData["Best Profit"]);
    });
});
